
WITH Triplets as (
    SELECT
        Num,
        lag(Num, 1) over(Order By Id) as prev,
        lead(Num, 1) over(Order By Id) as next
    FROM Logs)
SELECT DISTINCT Num as ConsecutiveNums
FROM Triplets
WHERE
    Num = prev AND
    prev = next
