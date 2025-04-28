WITH Ordered AS (
    SELECT
        LAT_N,
        ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn
    FROM
        STATION
),
Counted AS (
    SELECT
        COUNT(*) AS total_rows
    FROM
        STATION
)
SELECT ROUND(
    CASE
        WHEN total_rows % 2 <> 0 THEN(
            SELECT LAT_N
            FROM Ordered
            WHERE rn = (total_rows+1)/2
        )
        WHEN total_rows % 2 = 0 THEN (
            SELECT AVG(LAT_N)
            FROM Ordered
            WHERE rn IN (total_rows/2, (total_rows+1)/2)
        )
    END
    , 4) AS median_lat
FROM Counted;