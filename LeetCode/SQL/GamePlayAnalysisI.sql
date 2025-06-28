-- First login date

-- Solução I
SELECT player_id, first_login
FROM (
    SELECT player_id, MIN(event_date) as first_login
    FROM Activity
    GROUP BY player_id
);

-- Solução otimizada
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
