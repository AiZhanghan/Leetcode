SELECT f.film_id, f.title
FROM film AS f LEFT OUTER JOIN film_category AS fc
    ON f.film_id = fc.film_id
WHERE fc.category_id IS NULL;