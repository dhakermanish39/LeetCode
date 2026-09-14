# Write your MySQL query statement below

select id ,visit_date , people from Stadium s
where people >=100 and (((select people from Stadium where id =s.id+1) >=100 and (select people from Stadium where id =s.id-1)>=100) or ((select people from Stadium where id =s.id+1) >=100 and (select people from Stadium where id =s.id+2)>=100) or ((select people from Stadium where id =s.id-1) >=100 and (select people from Stadium where id =s.id-2)>=100))