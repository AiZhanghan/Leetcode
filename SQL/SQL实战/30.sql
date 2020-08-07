SELECT f.title, f.description
FROM film AS f
WHERE f.film_id IN (
    SELECT fc.film_id
    FROM film_category AS fc
    WHERE fc.category_id = (
        SELECT c.category_id
        FROM category AS c
        WHERE c.name = "Action"
    )
);


-- SELECT f.title, f.description
-- FROM film AS f INNER JOIN film_category AS fc
--     ON f.film_id = fc.film_id
-- WHERE fc.category_id = (
--     SELECT c.category_id 
--     FROM category AS c
--     WHERE c.name = "Action"
-- );
