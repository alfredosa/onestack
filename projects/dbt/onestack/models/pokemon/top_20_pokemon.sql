SELECT name, (attack + speed + defense + hp + special_attack + special_defense)/6 AS total_score
FROM pokemons
ORDER BY total_score DESC
LIMIT 20;
