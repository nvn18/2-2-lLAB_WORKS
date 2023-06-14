Q.NO-2.1:

Find the details of all students.

SQL> select * from student;

ID    NAME                 DEPT_NAME              TOT_CRED
----- -------------------- -------------------- ----------
00128 Zhang                Comp. Sci.                  102
12345 Shankar              Comp. Sci.                   32
19991 Brandt               History                      80
23121 Chavez               Finance                     110
44553 Peltier              Physics                      56
45678 Levy                 Physics                      46
54321 Williams             Comp. Sci.                   54
55739 Sanchez              Music                        38
70557 Snow                 Physics                       0
76543 Brown                Comp. Sci.                   58
76653 Aoi                  Elec. Eng.                   60

ID    NAME                 DEPT_NAME              TOT_CRED
----- -------------------- -------------------- ----------
98765 Bourikas             Elec. Eng.                   98
98988 Tanaka               Biology                     120

13 rows selected.

Q.NO-2.2:

Find the department names of instructors.


SQL> select dept_name from instructor;

DEPT_NAME
--------------------
Comp. Sci.
Finance
Music
Physics
History
Physics
Comp. Sci.
History
Finance
Biology
Comp. Sci.

DEPT_NAME
--------------------
Elec. Eng.

12 rows selected.

Q.NO-2.3:

Find the names of all the instructors from Biology department.


SQL> select name from instructor where dept_name='Biology';

NAME
--------------------
Crick

Q.NO-2.4:

Find the names of all instructors in the Computer Science department who have salaries greater than $70,000.


SQL> select name from instructor where dept_name='Comp. Sci.' and salary>70000;

NAME
--------------------
Katz
Brandt

Q.NO-2.5:

Find the names of courses in Computer science department which have 3 credits.


SQL> select title from course where dept_name='Comp. Sci.' and credits=3;

TITLE
--------------------------------------------------
Robotics
Image Processing
Database System Concepts

Q.NO-2.6:

Find the names of the instructors, their present salaries and the resulting salaries if they were given a 10% raise.


SQL> select name,salary,salary*1.1 as Raised_Salary from instructor;

NAME                     SALARY RAISED_SALARY
-------------------- ---------- -------------
Srinivasan                65000         71500
Wu                        90000         99000
Mozart                    40000         44000
Einstein                  95000        104500
El Said                   60000         66000
Gold                      87000         95700
Katz                      75000         82500
Califieri                 62000         68200
Singh                     80000         88000
Crick                     72000         79200
Brandt                    92000        101200

NAME                     SALARY RAISED_SALARY
-------------------- ---------- -------------
Kim                       80000         88000

12 rows selected.

Q.NO-2.7:

Find the names of instructors with salary amounts between $90,000 and $100,000.


SQL> 
SQL>  select name
  2   from instructor
  3   where salary between 90000 and 100000;

NAME
--------------------
Wu
Einstein
Brandt

Q.NO-2.8:

Find all instructors whose salary is unknown.

SQL> select name
  2  from instructor
  3  where salary is null;

no rows selected

Q.NO-2.9:

Find the names of all departments whose building name includes the substring ‘Watson’.


SQL> select dept_name
  2  from department
  3  where lower(building) like '%watson%';

DEPT_NAME
--------------------
Biology
Physics

Q.NO-2.10:

Find departments whose names contain the string “sci” as a substring, regardless of the case.

SQL> select dept_name
  2  from department
  3  where lower(dept_name) like '%sci%';

DEPT_NAME
--------------------
Comp. Sci.

Q.NO-2.11:

List the names of all instructors in the Physics department in alphabetic order.


SQL>  select name
  2   from instructor
  3   where dept_name='Physics'
  4   order by name;

NAME
--------------------
Einstein
Gold

Q.NO-2.12:

List the entire instructor relation in descending order of salary. If several instructors have the same salary, order them in ascending order by name.

SQL> select name 
  2  from instructor
  3  order by salary desc,
  4  name;

NAME
--------------------
Einstein
Brandt
Wu
Gold
Kim
Singh
Katz
Crick
Srinivasan
Califieri
El Said

NAME
--------------------
Mozart

12 rows selected.

Q.NO-3.1:

Find all possible combinations of instructors and the courses they teach.

SQL> select name,t.course_id,title
  2  from instructor i,teaches t,course c
  3  where i.ID=t.ID and 
  4  t.course_id=c.course_id;

NAME                 COURSE_I TITLE
-------------------- -------- --------------------------------------------------
Srinivasan           CS-101   Intro. to Computer Science
Srinivasan           CS-315   Robotics
Srinivasan           CS-347   Database System Concepts
Wu                   FIN-201  Investment Banking
Mozart               MU-199   Music Video Production
Einstein             PHY-101  Physical Principles
El Said              HIS-351  World History
Katz                 CS-101   Intro. to Computer Science
Katz                 CS-319   Image Processing
Crick                BIO-101  Intro. to Biology
Crick                BIO-301  Genetics

NAME                 COURSE_I TITLE
-------------------- -------- --------------------------------------------------
Brandt               CS-190   Game Design
Brandt               CS-190   Game Design
Brandt               CS-319   Image Processing
Kim                  EE-181   Intro. to Digital Systems

15 rows selected.

Q.NO-3.2:

Retrieve the names of all instructors, along with their department names and department building name.

SQL> select name,i.dept_name,building
  2  from instructor i,department d
  3  where i.dept_name=d.dept_name;

NAME                 DEPT_NAME            BUILDING
-------------------- -------------------- ---------------
Srinivasan           Comp. Sci.           Taylor
Wu                   Finance              Painter
Mozart               Music                Packard
Einstein             Physics              Watson
El Said              History              Painter
Gold                 Physics              Watson
Katz                 Comp. Sci.           Taylor
Califieri            History              Painter
Singh                Finance              Painter
Crick                Biology              Watson
Brandt               Comp. Sci.           Taylor

NAME                 DEPT_NAME            BUILDING
-------------------- -------------------- ---------------
Kim                  Elec. Eng.           Taylor

12 rows selected.

Q.NO-3.3:

Find the names of instructors who have taught at least one course.


SQL> select distinct i.name
  2  from instructor i,teaches t
  3  where i.ID=t.ID;

NAME
--------------------
Einstein
Crick
El Said
Srinivasan
Brandt
Wu
Kim
Mozart
Katz

9 rows selected.

Q.NO-3.4:

For the student with ID 12345 (or any other value), show all course_id and title of all courses registered for by the student.

SQL>  select st.name,st.id,t.course_id,c.title
  2  from course c,student st,takes t
  3  where t.ID=st.ID and t.course_id=c.course_id;

NAME                 ID         COURSE_I TITLE
-------------------- ---------- -------- --------------------------------------------------
Zhang                00128      CS-101   Intro. to Computer Science
Zhang                00128      CS-347   Database System Concepts
Shankar              12345      CS-101   Intro. to Computer Science
Shankar              12345      CS-190   Game Design
Shankar              12345      CS-315   Robotics
Shankar              12345      CS-347   Database System Concepts
Brandt               19991      HIS-351  World History
Chavez               23121      FIN-201  Investment Banking
Peltier              44553      PHY-101  Physical Principles
Levy                 45678      CS-101   Intro. to Computer Science
Levy                 45678      CS-101   Intro. to Computer Science

NAME                 ID         COURSE_I TITLE
-------------------- ---------- -------- --------------------------------------------------
Levy                 45678      CS-319   Image Processing
Williams             54321      CS-101   Intro. to Computer Science
Williams             54321      CS-190   Game Design
Sanchez              55739      MU-199   Music Video Production
Brown                76543      CS-101   Intro. to Computer Science
Brown                76543      CS-319   Image Processing
Aoi                  76653      EE-181   Intro. to Digital Systems
Bourikas             98765      CS-101   Intro. to Computer Science
Bourikas             98765      CS-315   Robotics
Tanaka               98988      BIO-101  Intro. to Biology
Tanaka               98988      BIO-301  Genetics

22 rows selected.

Q.NO-3.5:

Find instructor names and course identifiers for instructors in the Computer Science department.

SQL>  select name,course_id
  2   from instructor i,teaches t
  3  where i.id=t.id and dept_name='Comp. Sci.';

NAME                 COURSE_I
-------------------- --------
Srinivasan           CS-101
Srinivasan           CS-315
Srinivasan           CS-347
Katz                 CS-101
Katz                 CS-319
Brandt               CS-190
Brandt               CS-190
Brandt               CS-319

8 rows selected.

Q.NO-3.6:

For all instructors in the university who have taught some course, find their names and the course ID of all courses they taught.

SQL> select i.name,t.course_id
  2  from instructor i,teaches t
  3  where i.ID=t.Id;

NAME                 COURSE_I
-------------------- --------
Srinivasan           CS-101
Srinivasan           CS-315
Srinivasan           CS-347
Wu                   FIN-201
Mozart               MU-199
Einstein             PHY-101
El Said              HIS-351
Katz                 CS-101
Katz                 CS-319
Crick                BIO-101
Crick                BIO-301

NAME                 COURSE_I
-------------------- --------
Brandt               CS-190
Brandt               CS-190
Brandt               CS-319
Kim                  EE-181

15 rows selected.

Q.NO-3.7:

Find the names of all instructors whose salary is greater than at least one instructor in the Biology department. Or Find the names of all instructors who earn more than the lowest paid instructor in the Biology department.

SQL> select distinct i1.name
  2  from instructor i1,instructor i2
  3  where i1.dept_name=i2.dept_name and
  4  i1.dept_name='Physics' and i1.salary>i2.salary;

NAME
--------------------
Einstein

Q.NO-3.8:

Find full details of instructors who teach at least one course.

SQL> select distinct i.*
  2  from instructor i,teaches t
  3  where i.ID=t.Id;

ID    NAME                 DEPT_NAME                SALARY
----- -------------------- -------------------- ----------
10101 Srinivasan           Comp. Sci.                65000
98345 Kim                  Elec. Eng.                80000
15151 Mozart               Music                     40000
45565 Katz                 Comp. Sci.                75000
76766 Crick                Biology                   72000
32343 El Said              History                   60000
22222 Einstein             Physics                   95000
83821 Brandt               Comp. Sci.                92000
12121 Wu                   Finance                   90000

9 rows selected.

Q.NO-3.9:

Find the instructor names and the courses they taught for all instructors in the Biology department who have taught some course

SQL> select distinct i.name
  2  from instructor i,teaches t,course c
  3  where i.Id=t.Id and c.course_id=t.course_id and c.dept_name='Biology';

NAME
--------------------
Crick

Q.NO-3.10:

Find the set of all courses taught either in Fall 2009 or in Spring 2010, or both.

SQL> select title,t.course_id
  2  from teaches t,course c
  3  where t.course_id=c.course_id and
  4  (semester,year) in (('Spring',2010),('Fall',2009));

TITLE                                              COURSE_I
-------------------------------------------------- --------
Intro. to Computer Science                         CS-101
Robotics                                           CS-315
Database System Concepts                           CS-347
Investment Banking                                 FIN-201
Music Video Production                             MU-199
Physical Principles                                PHY-101
World History                                      HIS-351
Intro. to Computer Science                         CS-101
Image Processing                                   CS-319
Image Processing                                   CS-319

10 rows selected.

Q.NO-3.11:

Find the names of all students who have taken any Comp. Sci. course ever.
(there should be no duplicate names)

SQL> select distinct name
  2  from student st,takes t,course c
  3  where st.ID=t.ID and t.course_id=c.course_id
  4  and c.dept_name='Comp. Sci.';

NAME
--------------------
Zhang
Brown
Bourikas
Shankar
Levy
Williams

6 rows selected.

Q.NO-3.12:

Display the IDs of all instructors who have never taught a course. (Don’t write
nested query)

SQL> select ID
  2  from instructor
  3  minus
  4  select ID
  5  from teaches;

ID
-----
33456
58583
76543

