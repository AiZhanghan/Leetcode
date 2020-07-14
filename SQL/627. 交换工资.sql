UPDATE 
    salary
SET sex = char(ascii('m') + ascii('f') - ascii(sex))
;

-- UPDATE 
--     salary
-- SET sex = (
--     CASE sex
--         WHEN 'm' THEN 'f'
--         ELSE 'm'
--     END
--     )
-- ;
