from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "courses": [1]},
    {"id": 2, "first_name": "Alice", "last_name": "Smith", "courses": []}
]

courses = [
    {"id": 1, "name": "Introduction to Computer Science",
     "code": "CS101",
     "description": "An introductory course covering fundamental concepts in computer science."},
    {"id": 2,
     "name": "Data Structures and Algorithms",
     "code": "DSA200",
     "description": "A course covering data structures and algorithms."}
]

@app.route('/students', methods=['POST'])
def create_student():
    new_student = {"id": len(students) + 1, "first_name": "Jane", "last_name": "Doe", "courses": []}
    students.append(new_student)
    return jsonify(new_student), 201

@app.route('/courses', methods=['POST'])
def create_course():
    new_course = {"id": len(courses) + 1, "name": "Advanced Mathematics", "code": "MATH300", "description": "An advanced course in mathematics."}
    courses.append(new_course)
    return jsonify(new_course), 201

@app.route('/students', methods=['GET'])
def get_students_with_courses():
    students_with_courses = []
    for student in students:
        student_courses = [course for course in courses if course['id'] in student['courses']]
        student_data = {
            "id": student["id"],
            "first_name": student['first_name'],
            "last_name": student['last_name'],
            "courses": student_courses
        }
        students_with_courses.append(student_data)
    return jsonify(students_with_courses)

@app.route('/students/not_taken', methods=['GET'])
def get_students_without_courses():
    students_without_courses = [student for student in students if not student['courses']]
    return jsonify(students_without_courses)

if __name__ == '__main__':
    app.run(debug=True)
