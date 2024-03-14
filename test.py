import requests

# Define the base URL of your Flask application
BASE_URL = 'http://localhost:5000'

# Test creating a new student
def test_create_student():
    url = BASE_URL + '/students'
    data = {"first_name": "Jane", "last_name": "Doe"}
    response = requests.post(url, json=data)
    print(response.json())

# Test creating a new course
def test_create_course():
    url = BASE_URL + '/courses'
    data = {"name": "Advanced Mathematics", "code": "MATH300", "description": "An advanced course in mathematics."}
    response = requests.post(url, json=data)
    print(response.json())

# Test retrieving students with courses
def test_get_students_with_courses():
    url = BASE_URL + '/students'
    response = requests.get(url)
    print(response.json())

# Test retrieving students without courses
def test_get_students_without_courses():
    url = BASE_URL + '/students/not_taken'
    response = requests.get(url)
    print(response.json())

if __name__ == '__main__':
    test_create_student()
    test_create_course()
    test_get_students_with_courses()
    test_get_students_without_courses()
