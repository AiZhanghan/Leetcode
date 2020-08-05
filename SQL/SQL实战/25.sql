SELECT emp_sal.emp_no, man_sal.emp_no AS manager_no, 
    emp_sal.salary AS emp_salary, man_sal.salary AS manager_salary
FROM
    (
        SELECT de.emp_no, de.dept_no, s1.salary
        FROM dept_emp AS de INNER JOIN salaries AS s1
            ON de.emp_no = s1.emp_no 
        WHERE de.to_date = "9999-01-01"
            AND s1.to_date = "9999-01-01"
    ) AS emp_sal,
    (
        SELECT dm.emp_no, dm.dept_no, s2.salary
        FROM dept_manager AS dm INNER JOIN salaries AS s2
            ON dm.emp_no = s2.emp_no
        WHERE dm.to_date = "9999-01-01"
            AND s2.to_date = "9999-01-01"
    ) AS man_sal
WHERE emp_sal.dept_no = man_sal.dept_no
    AND emp_sal.salary > man_sal.salary;    