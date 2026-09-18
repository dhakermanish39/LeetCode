# Write your MySQL query statement below
select  employee_id , department_id  from Employee e
group by employee_id , department_id,primary_flag
having  primary_flag='Y' or (primary_flag='N' and (select count(*) from Employee where employee_id= e.employee_id group by employee_id )=1)