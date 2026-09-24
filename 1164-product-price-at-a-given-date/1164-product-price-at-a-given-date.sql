with temp as (
    select product_id
        , max(change_date) as max_change_date
    from products 
    where change_date <= '2019-08-16'
    group by product_id
)
select distinct Products.product_id
    , case when max_change_date is null then 10 else (select new_price  from Products where product_id=temp.product_id and change_date=temp.max_change_date)  end as price 
from temp right join  Products on 
temp.product_id=Products.product_id
;