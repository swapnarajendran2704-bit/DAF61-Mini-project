
CREATE DATABASE IF NOT EXISTS employee;

USE employee;
CREATE TABLE IF NOT EXISTS departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    gender CHAR(1),
    age INT,
    hire_date DATE,
    designation VARCHAR(100),
    department_id INT,
    location_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (location_id) REFERENCES location(location_id)
);
USE employee;
CREATE TABLE IF NOT EXISTS location (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(50)
);SHOW TABLES;
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    gender CHAR(1),
    age INT,
    hire_date DATE,
    designation VARCHAR(100),
    department_id INT,
    location_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id),
    FOREIGN KEY (location_id)
        REFERENCES location(location_id)
);
USE employee;
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Software Development'),
(2, 'Marketing'),
(3, 'Data Science'),
(4, 'Human Resources'),
(5, 'Product Management'),
(6, 'Content Creation'),
(7, 'Finance'),
(8, 'Design'),
(9, 'Research and Development'),
(10, 'Customer Support'),
(11, 'Business Development'),
(12, 'IT'),
(13, 'Operations');

SHOW TABLES;
INSERT INTO location (location) VALUES
('Chennai'),
('Bangalore'),
('Hyderabad'),
('Pune');
SELECT * FROM departments;
SELECT * FROM location;
SELECT * FROM employees;
-- Retrieve distinct salaries from the employees table.
SELECT DISTINCT salary
FROM employees;
-- Rename column headings
SELECT
    age AS Employee_Age,
    salary AS Employee_Salary
FROM employees;
-- Find employees with salary greater than ₹50,000 and hired before 2016-01-01
SELECT *
FROM employees
WHERE salary > 50000
  AND hire_date < '2016-01-01';
  
-- Find the employee whose designation is missing and fill it with Data Scientist

UPDATE employees
SET designation = 'Data Scientist'
WHERE employee_id = 5004;
SELECT employee_id, employee_name, designation
FROM employees
WHERE employee_id = 5004;

-- ORDER BY
SELECT *
FROM employees
ORDER BY department_id ASC, salary DESC;

-- LIMIT
SELECT *
FROM employees
WHERE hire_date >= '2018-01-01'
  AND hire_date < '2019-01-01'
ORDER BY hire_date ASC
LIMIT 5;
-- Calculate the sum of all salaries in the Finance department
SELECT SUM(e.salary) AS Total_Finance_Salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
WHERE d.department_name = 'Finance';
-- Find the minimum age among all employees
SELECT MIN(age) AS Minimum_Age
FROM employees;
-- Find the maximum salary for each location
SELECT
    l.location,
    MAX(e.salary) AS Maximum_Salary
FROM employees e
JOIN location l
    ON e.location_id = l.location_id
GROUP BY l.location;
-- Calculate the average salary for each designation containing the word 'Analyst'
SELECT
    designation,
    AVG(salary) AS Average_Salary
FROM employees
WHERE designation LIKE '%Analyst%'
GROUP BY designation;
-- Find departments with fewer than 3 employees

-- Find locations with female employees whose average age is below 30
SELECT
    l.location,
    AVG(e.age) AS Average_Age
FROM location l
JOIN employees e
    ON l.location_id = e.location_id
WHERE e.gender = 'F'
GROUP BY l.location_id, l.location
HAVING AVG(e.age) < 30;
-- INNER JOIN
SELECT
    e.employee_name,
    e.designation,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;
    -- LEFT JOIN
    SELECT
    d.department_name,
    COUNT(e.employee_id) AS Total_Employees
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY d.department_id;
-- RIGHT JOIN
SELECT
    l.location,
    e.employee_name
FROM employees e
RIGHT JOIN location l
    ON e.location_id = l.location_id
ORDER BY l.location_id;

