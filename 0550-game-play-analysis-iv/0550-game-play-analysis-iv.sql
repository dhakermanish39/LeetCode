with first_login as (
select player_id, min(event_date) as first_date  from Activity
group by player_id
)
select round(count(a.player_id)/count(f.player_id),2) as fraction
from first_login f
left join Activity a on f.player_id = a.player_id
and a.event_date = date_add(f.first_date, interval 1 day);