-- Write your PostgreSQL query statement below
WITH exam_results AS (
    SELECT student_id, subject_name, COALESCE(COUNT(student_id),0) AS attended_exams
    FROM Examinations
    GROUP BY (student_id, subject_name)
)

SELECT student_id, student_name, Subjects.subject_name, COALESCE(attended_exams,0) as attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN exam_results using (student_id, subject_name)
ORDER BY student_id ASC

-- GROUP BY student_id, student_name, subject_name