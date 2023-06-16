select
	trim(_c0) as name,
	cast(trim(_c1) as numeric(32,16)) as order,
	cast(trim(_c2) as numeric(32,16)) as base_experience,
	cast(trim(_c3) as numeric(32,16)) as height,
	cast(trim(_c4) as numeric(32,16)) as weight,
	cast(trim(_c5) as numeric(32,16)) as defense,
	cast(trim(_c6) as numeric(32,16)) as speed,
	cast(trim(_c7) as numeric(32,16)) as special_defense,
	cast(trim(_c8) as numeric(32,16)) as attack,
	cast(trim(_c9) as numeric(32,16)) as special_attack,
	cast(trim(_c10) as numeric(32,16)) as hp
from csv.'/var/lib/onestack/stage/pokemon.csv'
