SELECT s1.emp_no, s2.from_date, (s2.salary - s1.salary) AS salary_growth
FROM salaries AS s1, salaries AS s2
WHERE s1.emp_no = s2.emp_no
    AND s1.to_date = s2.from_date
    AND salary_growth > 5000
ORDER BY salary_growth DESC;

