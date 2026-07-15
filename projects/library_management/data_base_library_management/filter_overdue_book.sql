use library_management;

create or replace view overdue_book as
select
    mem.members_id as ID,
    mem.name as name,
    loa.due_date
from members mem
join loan loa using (members_id)
where return_date is null and due_date < curdate()
