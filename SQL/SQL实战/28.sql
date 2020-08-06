SELECT c.name, COUNT(fc.film_id)
FROM 
    (
        SELECT category_id, COUNT(film_id) AS category_num
        FROM film_category
        GROUP BY category_id
        HAVING category_num >= 5
    ) AS cc,
    film AS f, film_category AS fc, category AS c
WHERE f.description LIKE "%robot%"
    AND f.film_id = fc.film_id
    AND c.category_id = fc.category_id
    AND c.category_id = cc.category_id