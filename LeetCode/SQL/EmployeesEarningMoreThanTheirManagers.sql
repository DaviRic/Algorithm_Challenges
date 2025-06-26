SELECT e.name as Employee
FROM Employee e JOIN Employee m
     ON e.managerId = m.Id
WHERE e.salary > m.salary