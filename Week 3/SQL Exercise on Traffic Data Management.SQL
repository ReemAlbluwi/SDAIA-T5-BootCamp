--  1: Create the Table 
CREATE TABLE traffic_data (
    road VARCHAR2(100),
    traffic_date DATE,
    traffic_time TIMESTAMP,
    traffic_volume INTEGER,
    weather_condition VARCHAR2(100),
    vehicle_type_breakdown VARCHAR2(255)
);


--- 2: Insert Data into the Table:

INSERT INTO traffic_data (
    road, 
    traffic_date, 
    traffic_time, 
    traffic_volume, 
    weather_condition, 
    vehicle_type_breakdown
) VALUES (
    'Highway A1', 
    TO_DATE('2024-07-11', 'YYYY-MM-DD'), 
    TO_TIMESTAMP('2024-07-11 08:00:00', 'YYYY-MM-DD HH24:MI:SS'),  
    1200,  
    'Clear', 
    '{"car": 800, "truck": 300, "motorcycle": 100}' 


--- 3: Query 
-- 3.1 : Write a query to retrieve all columns for the first recorded traffic data in the table.


SELECT *
FROM traffic_data
ORDER BY traffic_date, traffic_time
FETCH FIRST 1 ROW ONLY;


-- 3.2 : 
SELECT road, traffic_date, traffic_time, traffic_volume, weather_condition, vehicle_type_breakdown
FROM traffic_data
WHERE traffic_volume > 1000;



--4 : Update the traffic volume to 1500 vehicles for all records where the road is "Highway A1" and
---   the time is between "0800" and "1000" on "2024-07-11".

UPDATE traffic_data
SET traffic_volume = 1500
WHERE road = 'Highway A1'
  AND traffic_date = TO_DATE('2024-07-11', 'YYYY-MM-DD')
  AND traffic_time BETWEEN TO_TIMESTAMP('2024-07-11 08:00:00', 'YYYY-MM-DD HH24:MI:SS')
                       AND TO_TIMESTAMP('2024-07-11 10:00:00', 'YYYY-MM-DD HH24:MI:SS');

--5 : Update the vehicle type breakdown to '{"car": 850, "truck": 320, "motorcycle": 130}' for therecord with the highest traffic volume.

UPDATE traffic_data
SET vehicle_type_breakdown = '{"car": 850, "truck": 320, "motorcycle": 130}'
WHERE (road, traffic_date, traffic_time) IN (
    SELECT road, traffic_date, traffic_time
    FROM traffic_data
    WHERE traffic_volume = (
        SELECT MAX(traffic_volume)
        FROM traffic_data
    )
);




-- 6 : -- Delete all records where the weather condition is "Rainy"
DELETE FROM traffic_data
WHERE weather_condition = 'Rainy';

------------------------------------------------------------------

SELECT * FROM traffic_data








