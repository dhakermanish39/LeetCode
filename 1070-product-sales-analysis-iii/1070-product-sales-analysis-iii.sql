# Write your MySQL query statement below
with b as (select product_id , min(year) as first from Sales group by product_id)

select product_id , year  as first_year,quantity,price from Sales a
where year = (select min(first) from b where product_id = a.product_id )