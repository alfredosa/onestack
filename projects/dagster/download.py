import os
import re
from datetime import datetime, timedelta

import pandas as pd
import requests
import yfinance as yf
from dagster import job, op


def yesterday(date: str) -> str:
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, "%Y-%m-%d")


def flatten_stats(data):
    columns = set()
    flattened_data = []

    for pokemon in data:
        base_columns = ["name", "order", "base_experience", "height", "weight"]
        columns = set()
        stats = pokemon.pop("stats", [])

        for stat in stats:
            column = stat["stat"]["name"]
            value = stat["base_stat"]

            columns.add(column)
            pokemon[column] = value

        flattened_data.append(pokemon)
    final_columns = base_columns + list(columns)
    return flattened_data, final_columns


def extract() -> list:
    url = "http://pokeapi.co/api/v2/pokemon"
    params = {"limit": 200}
    response = requests.get(url=url, params=params)

    json_response = response.json()
    results = json_response["results"]

    pokemons = [requests.get(url=result["url"]).json() for result in results]
    return pokemons


def transform_and_download(pokemons: list, target_file):
    flattened_data, columns = flatten_stats(pokemons)
    df = pd.DataFrame(data=flattened_data, columns=columns)
    df = df.sort_values(["base_experience"], ascending=False).rename(
        columns={
            "special-defense": "special_defense",
            "special-attack": "special_attack",
        }
    )
    df.to_csv(target_file, index=False)
    return True


@op(
    config_schema={
        "target_file_fin": str,
        "symbols": [str],
        "start_date": str,
        "end_date": str,
    }
)
def download_yahoo_finance_files_op(context, dependent_job=None):
    target_file = context.op_config["target_file_fin"]
    symbols = context.op_config["symbols"]
    start_date = context.op_config["start_date"]
    if not re.match(start_date, "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"):
        start_date = "2000-01-01"
    end_date = context.op_config["end_date"]
    if not re.match(end_date, "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"):
        end_date = yesterday(start_date)

    if os.path.exists(target_file):
        os.remove(target_file)

    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        df = ticker.history(start=start_date, end=end_date)
        df.insert(0, "Symbol", symbol)
        df.to_csv(target_file, mode="a", header=False, index=True)

    return target_file


@op(config_schema={"target_file_pokemon": str})
def download_pokemons_pokeapi(context, dependent_job=None):
    target_file = context.op_config["target_file_pokemon"]
    pokemons = extract()
    transform_and_download(pokemons, target_file)
    return target_file


@job
def download_all_files():
    download_yahoo_finance_files_op()
    download_pokemons_pokeapi()
