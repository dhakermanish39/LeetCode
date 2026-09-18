# Write your MySQL query statement below
with temp as (select reports_to as "employee_id" , count(*) as "reports_count" ,round(avg(age)) as "average_age" from Employees 
where reports_to is not null
group by 1) 
select t.employee_id , e.name , t.reports_count , t.average_age from Employees e
join temp t on e.employee_id=t.employee_id
order by t.employee_id