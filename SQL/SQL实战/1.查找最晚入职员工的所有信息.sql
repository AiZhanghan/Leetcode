SELECT
    *
FROM
    employees
ORDER BY
    hire_date DESC
LIMIT 1


-- SELECT
--     *
-- FROM
--     employees
-- WHERE
--     hire_date = (
--         SELECT
--             MAX(hire_date)
--         FROM
--             employees
--                 );