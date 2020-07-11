SELECT
    Department.Name AS `Department`,
    Employee.Name AS `Employee`,
    Employee.Salary
FROM
    Employee INNER JOIN Department
    ON Employee.DepartmentId = Department.Id
WHERE
    (Employee.DepartmentId, Salary) IN
    (SELECT
        DepartmentId, MAX(Salary)
     FROM
        Employee
     GROUP BY
        DepartmentId);