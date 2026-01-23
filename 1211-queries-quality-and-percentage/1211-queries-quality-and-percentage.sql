# Write your MySQL query statement below
SELECT query_name,
ROUND(avg(cast(rating as decimal)/position),2) as quality,
ROUND(sum(case when rating < 3 then 1 else 0 end)*100/count(*),2) as poor_query_percentage
FROM queries 
GROUP BY query_name;