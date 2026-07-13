use mechanic;

create view high_revenue_mechanics as
select
    mec.mechanic_id as ID,
    mec.name as name,
    sum(price) as total
from services_performed
join mechanic as mec using (mechanic_id)
group by mec.mechanic_id
having total > 15000
order by total desc