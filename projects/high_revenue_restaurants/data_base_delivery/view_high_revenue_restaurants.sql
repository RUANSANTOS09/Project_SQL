use delivery;

create or replace view high_revenue_restaurants as
select
    res.restaurant_id,
    res.name as name,
    sum(ordt.price_at_order) as total,
    count(distinct order_id) as Quantidade_total
from restaurant res
join orders ordr using(restaurant_id)
join order_items ordt using(order_id)
group by res.restaurant_id, res.name
having total > 100
