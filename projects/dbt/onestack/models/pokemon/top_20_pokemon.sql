SELECT name, (attack + speed + defense + hp + "special-attack" + "special-defense")/6 AS total_score
FROM {{ ref('pokemon')}}
ORDER BY total_score DESC
LIMIT 20
