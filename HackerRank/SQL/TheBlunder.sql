SELECT CEILING(AVG(SALARY) - AVG(CAST(REPLACE(SALARY, '0', '') AS UNSIGNED))) FROM EMPLOYEES;
