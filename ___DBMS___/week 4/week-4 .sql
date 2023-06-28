***********************************************************************WEEK-4:*******************************************

Q.NO-1.1:

Find the maximum and average capacity of buildings in the university.

SQL> select building, max(capacity) as max_capacity,avg(capacity) as average_capacity
  2  from classroom
    group by building;

BULIDING                       MAX_CAPACITY    AVERAGE
------------------------------ ------------ ----------
packard                                 500        500
painter                                  10         10
taylor                                   70         70
watson                                   50         40

Q.NO-1.2:

Display the least budget of the departments.

SQL>  select min(budget) as Least_budget
  2  from department;

LEAST_BUDGET
------------
       50000

Q.NO-1.3:

Find the total number of courses and credits offered by Biology
department.

SQL>  select count(dept_name) as Count,sum(credits) as Sum_of_credits
  2  from course
  3  where dept_name='Biology';

     COUNT SUM_OF_CREDITS
---------- --------------
         3             11

Q.NO-1.4:

Find the average salary of instructors in the Computer Science department.

SQL> select avg(salary) as avg_salary
  2  from instructor
  3  where dept_name='Comp. Sci.';

AVG_SALARY
----------
77333.3333

Q.NO-1.5:

Find the total number of instructors who teach a course in the Spring 2010
semester.

SQL>  select count(distinct ID) as count
  2  from teaches
  3  where semester='Spring' and year=2010;

     COUNT
----------
         6

Q.NO-1.6:

Find the average salary in each department

SQL> select avg(salary) as Average,dept_name
  2   from instructor
  3   group by dept_name;

   AVERAGE DEPT_NAME
---------- --------------------
     72000 Biology
77333.3333 Comp. Sci.
     80000 Elec. Eng.
     85000 Finance
     61000 History
     40000 Music
     91000 Physics

7 rows selected.

Q.NO-1.7:

Find the number of instructors in each department who teach a course in the Spring 2010 semester.

SQL> select count(distinct i.ID),dept_name
  2  from instructor i,teaches t
  3  where semester='Spring' and year=2010
  4  and i.ID=t.ID
  5  group by dept_name;

COUNT(DISTINCTI.ID) DEPT_NAME
------------------- --------------------
                  3 Comp. Sci.
                  1 Finance
                  1 History
                  1 Music

Q.NO-1.8:

Find the department name and average salary of the department for only those departments where the average salary of the instructors is more than
$42,000.

SQL> select dept_name,avg(salary) as avg_salary
  2  from instructor
  3  where salary>42000
  4  group by dept_name;

DEPT_NAME            AVG_SALARY
-------------------- ----------
Biology                   72000
Comp. Sci.           77333.3333
Elec. Eng.                80000
Finance                   85000
History                   61000
Physics                   91000

6 rows selected.

Q.NO-1.9:

For each course section offered in 2009, find the average total credits (tot_cred) of all students enrolled in the section, if the section had at least 2
students

SQL> select t.sec_id as sec_id , avg (tot_cred) as average_credits
  2  from takes t,student st
  3  where t.ID=st.ID
  4  and year=2009
  5  group by sec_id
  6  having count(t.sec_id)>1;

SEC_ID   AVERAGE_CREDITS
-------- ---------------
1             69.0909091
2                     43

Q.NO-1.10:

For each department, find the maximum salary of instructors in that department. You may assume that every department has at least one
instructor.

SQL> select max(salary) as Max_salary,dept_name
  2  from instructor i,teaches t
  3  where i.ID=t.ID
  4  group by dept_name;

MAX_SALARY DEPT_NAME
---------- --------------------
     72000 Biology
     92000 Comp. Sci.
     80000 Elec. Eng.
     90000 Finance
     60000 History
     40000 Music
     95000 Physics

7 rows selected.

Q.NO-1.11:

For the student with ID 12345 (or any other value), show the total number of credits scored for all courses (taken by that student). Don't display the tot_creds value from the student table, you should use SQL aggregation on courses taken by the student.

SQL> select sum(credits)
  2  from student st,course c,takes t
  3  where st.ID=t.ID and c.course_id=t.course_id
  4  group by t.ID
  5  having t.ID=12345;

SUM(CREDITS)
------------
          14
----------------------------------------------------------------------------------------------------------------------------
Q.NO-1.12:

Display the total credits for each of the students, along with the ID of the student; don't bother about the name of the student.

1  SELECT ST.ID,SUM(CREDITS)
2  FROM STUDENT ST,TAKES T,COURSE C
3  WHERE ST.ID=T.ID AND T.COURSE_ID=C.COURSE_ID
4* GROUP BY ST.ID

ID    SUM(CREDITS)
----- ------------
00128            7
12345           14
19991            3
23121            3
44553            4
45678           11
54321            8
55739            3
76543            7
76653            3
98765            7
98988            8

12 rows selected.


Q.NO-2.1:

Find the total number of (distinct) students who have taken course sections taught by the instructor with ID 110011

SQL> select count(distinct id)
  2  from takes
  3  where course_id=
  4  (select course_id 
  5  from teaches
  6  where ID='110011');

COUNT(DISTINCTID)
-----------------
                0
 Q.NO-2.2:

Find the names of all instructors whose salary is greater than at least one instructor in the Physics department.

SQL> select name
  2  from instructor
  3  where dept_name='Physics' and
  4  salary>
  5  (select min(salary) from instructor
  6  where dept_name='Physics');

NAME
--------------------
Einstein

Q.NO-2.3:

Find the departments that have the highest average salary.

SQL> select dept_name
  2  from instructor
  3  group by dept_name
  4  having avg(salary)=
  5    (select max(avg(salary))
  6    from instructor
  7   group by dept_name);

DEPT_NAME
--------------------
Physics

Q.NO-2.4:

Find all the courses taught in the both the Fall 2009 and Spring 2010 semesters.


SQL>  SELECT COURSE_ID
  2   FROM TEACHES
  3   WHERE (SEMESTER,YEAR) IN (('Fall',2009))
  4   AND COURSE_ID IN
  5   (SELECT COURSE_ID FROM TEACHES
  6  WHERE (SEMESTER,YEAR) IN (('Spring',2010)));

COURSE_I
--------
CS-101


Q.NO-2.5:

Find all the courses taught in the Fall 2009 semester but not in the Spring 2010 semester.

SQL> select title,course_id
  2  from course
  3  where course_id in
  4  (select course_id
  5  from teaches 
  6  where (semester='Fall' and year=2009) and (semester != 'Spring' and year !=2010));

TITLE                                              COURSE_I
-------------------------------------------------- --------
Intro. to Computer Science                         CS-101
Database System Concepts                           CS-347
Physical Principles                                PHY-101

Q.NO-2.6:

Find all courses taught in both the Fall 2009 semester and in the Spring 2010 semester. (Write correlated nested Query)

SQL>  SELECT COURSE_ID
  2   FROM TEACHES T
  3  WHERE (SEMESTER,YEAR) IN (('Fall',2009))
  4  AND COURSE_ID IN
  5  (SELECT COURSE_ID FROM TEACHES
  6  WHERE T.COURSE_ID=COURSE_ID
  7  AND (SEMESTER,YEAR) IN (('Spring',2010)));

COURSE_I
--------
CS-101
------------------------------------------------------------------------------------------------------
Q.NO-2.7:

Find all students who have taken all courses offered in the Biology department. (Write Correlated nested Query)

SQL> SELECT DISTINCT ID
  2  FROM TAKES T
  3  WHERE NOT EXISTS(SELECT COURSE_ID FROM
  4  COURSE WHERE UPPER(DEPT_NAME)='BIOLOGY'
  5  MINUS
  6  SELECT COURSE_ID 
  7  FROM TAKES WHERE T.ID=ID);

no rows selected
------------------------------------------------------------------------------------------------------
Q.NO-2.8:

Find all courses that were offered at most once in 2009.

SQL> SELECT DISTINCT COURSE_ID
  2  FROM TEACHES T
  3  WHERE COURSE_ID IN
  4  (SELECT DISTINCT COURSE_ID
  5  FROM TEACHES
  6  WHERE YEAR=2009
  7  GROUP BY COURSE_ID
  8  HAVING COUNT(COURSE_ID)<=1);

COURSE_I
--------
EE-181
CS-101
CS-347
BIO-101
PHY-101

5 rows selected.
-------------------------------------------------------------------------------------------------------
Q.NO-2.9:

Find all courses that were offered at least twice in 2009.

SQL> SELECT DISTINCT COURSE_ID
  2  FROM TEACHES T
  3  WHERE COURSE_ID IN
  4  (SELECT DISTINCT COURSE_ID
  5  FROM TEACHES
  6  WHERE YEAR=2009
  7  GROUP BY COURSE_ID
  8  HAVING COUNT(COURSE_ID)>1);

COURSE_I
--------
CS-190
------------------------------------------------------------------------------------------------------
Q.NO-2.10:

Find the average instructors salaries of those departments where the average salary is greater than $42,000.

SQL> SELECT AVG(SALARY) AS AVG_SALARY,DEPT_NAME
  2  FROM INSTRUCTOR
  3  GROUP BY DEPT_NAME
  4  HAVING AVG(SALARY) IN
  5  (SELECT AVG(SALARY)
  6  FROM INSTRUCTOR
  7  GROUP BY DEPT_NAME
  8  HAVING AVG(SALARY)>42000);

AVG_SALARY DEPT_NAME
---------- --------------------
     80000 Elec. Eng.
     91000 Physics
77333.3333 Comp. Sci.
     85000 Finance
     72000 Biology
     61000 History

6 rows selected.
--------------------------------------------------------------------------------------------------------
Q.NO-2.11:

Find the departments with the maximum budget.

SQL> SELECT DEPT_NAME,BUDGET
  2  FROM DEPARTMENT D
  3  WHERE NOT EXISTS
  4  (SELECT DEPT_NAME
  5  FROM DEPARTMENT WHERE D.BUDGET<BUDGET);

DEPT_NAME                BUDGET
-------------------- ----------
Finance                  120000
--------------------------------------------------------------------------------------------------------
Q.NO-2.12:

Find the names of instructors who have not taught any course.

SQL> SELECT DISTINCT ID
  2  FROM INSTRUCTOR I
  3  WHERE NOT EXISTS
  4  (SELECT * 
  5  FROM TEACHES 
  6  WHERE I.ID=ID);

ID
-----
33456
58583
76543
--------------------------------------------------------------------------------------------------------
Q.NO-2.13:

Find the IDs and names of all students who have not taken any course offering before Spring 2009.

SQL> SELECT DISTINCT ID,NAME
  2  FROM STUDENT ST
  3  WHERE NOT EXISTS
  4  (SELECT * FROM TAKES
  5  WHERE ST.ID=ID)
  6  OR
  7  EXISTS(SELECT * FROM TAKES
  8  WHERE ST.ID=ID AND
  9  YEAR<=2009 AND SEMESTER='Fall');

ID         NAME
---------- --------------------
54321      Williams
44553      Peltier
98765      Bourikas
76543      Brown
00128      Zhang
12345      Shankar
70557      Snow
45678      Levy

8 rows selected.
------------------------------------------------------------------------------------------------
Q.NO-2.14:

Find the lowest, across all departments, of the per-department maximum salary computed.

SQL> SELECT DEPT_NAME,SALARY
  2  FROM (SELECT DEPT_NAME,SALARY
  3  FROM INSTRUCTOR I
  4  WHERE NOT EXISTS(SELECT * FROM 
  5  INSTRUCTOR WHERE I.DEPT_NAME=DEPT_NAME
  6  AND I.SALARY<SALARY) AND
  7  NOT EXISTS(SELECT * FROM INSTRUCTOR
  8  WHERE I.SALARY>SALARY));

DEPT_NAME                SALARY
-------------------- ----------
Music                     40000
------------------------------------------------------------------------------------------------
Q.NO-2.15:

Display the IDs and names of the instructors who have taught all Comp. Sci. courses.

SQL> SELECT NAME,ID
  2  FROM INSTRUCTOR I
  3  WHERE UPPER(DEPT_NAME)='COMP. SCI.'
  4  AND NOT EXISTS(
  5  (SELECT COURSE_ID FROM COURSE WHERE
  6  UPPER(DEPT_NAME)='COMP. SCI.')
  7  MINUS
  8  (SELECT COURSE_ID FROM
  9  TEACHES WHERE I.ID=ID));

no rows selected.
