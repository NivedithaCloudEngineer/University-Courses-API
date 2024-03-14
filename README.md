# University-Courses-API

University Courses API
This project is an API for managing university courses. It allows users to create students, create courses, and associate students with courses.
Project name- CodelityProject
The below are the Resources which I’ve created to make 4 API requests out of which 2 are POST and 2 are GET. 
Resources Created:
Main.Py(Source Code which Serves API requests on local host exposed at the port 5000)
Test.Py (Which perform unit tests against the source code)
DockerFile(To create the image to run the python the application)
Docker-Compse.yml (To containerize the image to expose the application and to attach the volume) 
How to make the application live
Use this command docker -compose up –build from the root of the folder where all the files including docker file reside. 
API end point for the students will be accessed at http://localhost:5000/students- 
API end point for the students have not taken will be accessed at http://localhost:5000/students- 
For creating a student, which includes first and last name:
The /students endpoint with the POST method allows for the creation of a new student. It accepts JSON data containing the first and last names of the student.
For creating courses, including the course name, course code, and description:
The /courses endpoint with the POST method allows for the creation of a new course. It accepts JSON data containing the course name, code, and description.
For all students and which courses the students have taken:
The /students endpoint with the GET method retrieves all students along with the courses they have taken. 
For all students and which courses the students have not taken:
The /students/not taken endpoint with the GET method retrieves students who have not taken any courses. 

Endpoints
The following endpoints are available in the API:
•	POST /students: Create a new student.
•	POST /courses: Create a new course.
•	GET /students: Retrieve all students along with their associated courses.
•	GET /students/not_taken: Retrieve students who have not taken any courses.
For detailed information on each endpoint and their usage, refer to the API documentation.
Data Validation
The API performs data validation to ensure the integrity of the data. Validation rules are enforced for creating students, creating courses, and other operations to maintain data consistency.
Testing
Unit tests are included to ensure the functionality of the API. To run the tests, use the following command:

