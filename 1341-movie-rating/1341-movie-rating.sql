# Write your MySQL query statement below
(select u.name as "results"  from Users u join 
MovieRating m on u.user_id = m.user_id
group by u.user_id 
order by count(*) desc , u.name 
limit 1)
union all
(select m.title as "results" from Movies m join 
MovieRating r on m.movie_id=r.movie_id
where r.created_at >'2020-01-31' and r.created_at <'2020-03-01'
group by m.movie_id 
order by avg(rating) desc , m.title 
limit 1
)