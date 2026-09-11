# Write your MySQL query statement below
with temp as (select d.name as Department ,e.name as Employee ,e.Salary , dense_rank() over(partition by e.departmentId order by e.salary desc ) as rnk from  Employee e join Department d 
on e.departmentId = d.id)
select Department ,Employee , Salary from temp 
where rnk<=3;