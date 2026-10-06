# Write your MySQL query statement below
with temp as(
    select requester_id, count(*) as "total" from RequestAccepted
    group by requester_id
    union all
    select accepter_id as "requester_id", count(*)  as "total" from RequestAccepted 
    group by accepter_id
)
select requester_id as"id" ,sum(total) as "num" from temp
group by requester_id 
order by num desc limit 1