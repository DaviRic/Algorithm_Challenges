SELECT 
    MAX(salary * months) AS max_total_earnings,
    COUNT(*) 
FROM 
    Employee
WHERE 
    salary * months = (
        SELECT MAX(salary * months) FROM Employee
    );
