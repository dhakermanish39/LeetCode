CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from (select * ,dense_rank() over(order by salary desc) as rnk from Employee ) as new_table
      where rnk=N

  );
END