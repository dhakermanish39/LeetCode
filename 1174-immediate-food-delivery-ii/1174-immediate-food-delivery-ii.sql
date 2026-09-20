# Write your MySQL query statement below
with temp as (select case when min(order_date )=min(customer_pref_delivery_date) then 1 else 0 end as "num"
from Delivery group by customer_id )
select round((sum(num)/count(num))*100,2) as "immediate_percentage" from temp