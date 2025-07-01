WITH students_courses as (
    SELECT class, COUNT(courses.student) as qtd_students
    FROM Courses
    GROUP BY class
    ORDER BY COUNT(student)
)

SELECT class
FROM students_courses
WHERE qtd_students >= 5;

-- Forma alternativa e mais simples
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(students) >= 5;