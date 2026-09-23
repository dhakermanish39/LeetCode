with cte as (
    select product_id
        , max(change_date) as max_change_date
    from products 
    where change_date <= '2019-08-16'
    group by product_id
)
select distinct a.product_id
    , case when max_change_date is null then 10 else new_price end as price 
from products a
left join cte b
on a.product_id = b.product_id
where change_date = max_change_date
or b.product_id is null
;