# Write your MySQL query statement below
with temp as (select person_name , sum(weight) over(order by turn) as "rnk" from Queue )
 , temp2 as(select person_name ,rnk from temp 
where rnk <= 1000
order by rnk desc)
select person_name from temp2 
limit 1