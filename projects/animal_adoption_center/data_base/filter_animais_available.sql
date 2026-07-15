use animal_adoption_center;


create or replace view animals_available as
select
    anm.animals_id as Id,
    anm.name as Nome,
    anm.species as especie,
    case
    	when adoption_date is null then 'Disponível'
    else
       'Adotado'
    end as situation
from animals anm
left join adoptions using(animals_id)
where adoption_date is null