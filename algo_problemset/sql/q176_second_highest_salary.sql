# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT Salary as DistinctSalary
    FROM Employee
    ORDER BY DistinctSalary DESC
    LIMIT 1
    OFFSET 1)
SecondHighestSalary;
