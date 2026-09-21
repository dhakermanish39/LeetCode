# Write your MySQL query statement below
#select category,case when count(account_id) is null then 0 else count(*) end  as accounts_count from(select account_id , case when income <20000 then 'Low Salary' when income>=20000 and income <=50000 then 'Average Salary' else 'High Salary' end as category from Accounts)t  group by category;
select 'Low Salary' as category, count(case when income<20000 then 1 end) as accounts_count
from Accounts
union all
select 'Average Salary' as category, count(case when income>=20000 and income<=50000 then 1 end) as accounts_count
from Accounts
union all
select 'High Salary' as category, count(case when income>50000 then 1 end) as accounts_count
from Accounts