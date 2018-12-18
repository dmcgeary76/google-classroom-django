# google-classroom-django
The purpose of this project is to create a web interface for Google Classroom content.  The entire project will ultimately allow teachers or students to login through a google account, see a list of all course activities with prompts for graded items, items that need to be graded, or prompts to begin an exercise, and a simple mechanism to automating the delivery of email progress reports to students.

This implementation uses content from the Google Classroom Progress Report code set to sync data into tables in a dedicated MySQL db.  The database tables are built as follows:


assignments
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(10)      | NO   | PRI | NULL    | auto_increment |
| name         | varchar(255) | YES  |     | NULL    |                |
| assignmentid | varchar(255) | YES  |     | NULL    |                | assignmentId from Google Classroom
| courseid     | int(5)       | YES  |     | NULL    |                | id from courses table
+--------------+--------------+------+-----+---------+----------------+

courses
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int(3)       | NO   | PRI | NULL    | auto_increment |
| name      | varchar(255) | YES  |     | NULL    |                |
| shortname | varchar(15)  | YES  |     | NULL    |                |
| courseid  | varchar(255) | YES  |     | NULL    |                |  courseId from Google Classroom
+-----------+--------------+------+-----+---------+----------------+

enrollments
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int(3)       | NO   | PRI | NULL    | auto_increment |
| studentid | int(5)       | YES  |     | NULL    |                | id from students table
| courseid  | int(5)       | YES  |     | NULL    |                | id from courses table
| status    | varchar(255) | YES  |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+

grades
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(10)      | NO   | PRI | NULL    | auto_increment |
| assignmentid | int(10)      | YES  |     | NULL    |                | id from assignments table
| studentid    | int(10)      | YES  |     | NULL    |                | id from students table
| submissionid | varchar(255) | YES  |     | NULL    |                | submissionId from Google Classroom
| state        | varchar(30)  | YES  |     | NULL    |                |
| link         | varchar(255) | YES  |     | NULL    |                | alternateLink from Google Classroom
+--------------+--------------+------+-----+---------+----------------+

students
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int(3)       | NO   | PRI | NULL    | auto_increment |
| name      | varchar(255) | YES  |     | NULL    |                |
| firstname | varchar(255) | YES  |     | NULL    |                |
| email     | varchar(255) | YES  |     | NULL    |                |
| studentid | varchar(255) | YES  |     | NULL    |                | studentId from Google Classroom
+-----------+--------------+------+-----+---------+----------------+

