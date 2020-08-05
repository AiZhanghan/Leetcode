SELECT d.dept_no, d.dept_name, t.title, COUNT(*) AS count
FROM departments AS d, dept_emp AS de, titles AS t
WHERE de.emp_no = t.emp_no
    AND de.dept_no = d.dept_no
    AND de.to_date = "9999-01-01"
    AND t.to_date = "9999-01-01"
GROUP BY d.dept_no, t.title;