SELECT
    weather.id AS 'Id'
FROM
    weather INNER JOIN weather AS w
    ON DATEDIFF(weather.RecordDate, w.RecordDate) = 1
    AND weather.Temperature > w.Temperature;