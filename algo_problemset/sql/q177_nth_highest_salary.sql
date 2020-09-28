CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT MAX(Salary) FROM (
          SELECT s.DistinctSalary as Salary, ROW_NUMBER() OVER () as row_num
          FROM (
              SELECT DISTINCT Salary as DistinctSalary
              FROM Employee
              ORDER BY DistinctSalary DESC) s
      ) t
      WHERE t.row_num = N
  );
END
