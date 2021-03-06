# Query a count of the number of cities in CITY having a Population larger than 100,000.
select count(name) from city where population>100000;

# Query the total population of all cities in CITY where District is California.
select sum(population)
from city
where district = "California";

# Query the average population of all cities in CITY where District is California.
select avg(population)
from city
where district = "California";

# Query the average population for all cities in CITY, rounded down to the nearest integer.
select round(avg(population))
from city;

# Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
select SUM(population)
from city
where countrycode = "JPN";

# Query the difference between the maximum and minimum populations in CITY.
select  max(population) - min(population) 
from city;

# Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her   keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeroes removed), and the actual average salary.
# Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.
select ceiling(avg(salary) - avg(replace(salary,"0",""))) 
from Employees;

# We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
select (Select max(Salary * months) from employee),
count(name)
from employee where (salary * months) = (select max(salary * months) from Employee);

# Query the following two values from the STATION table:

# The sum of all values in LAT_N rounded to a scale of  decimal places.
# The sum of all values in LONG_W rounded to a scale of  decimal places.

select round(sum(lat_n),2),
round(sum(long_w),2)
from station;

# Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.
Select round(sum(lat_n),4) 
from STATION 
where lat_n>38.7880 and lat_n<137.2345;

# Generate the following two result sets:
# Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
# Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them
# https://www.hackerrank.com/challenges/the-pads/problem
select concat(name,'(',substring(occupation,1,1),')') from occupations order by name asc;
select concat("There are a total of ",count(*),' ',lower(occupation),'s.') from occupations group by occupation order by count(*);