"""
    HW12 flask

    Auther@Xiaoran Ma, 11/23/2017
"""

import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/student_courses')
def student_courses():
    sqlite_file = '/Users/xiaoranma/Desktop/ssw810/HW/810_startup.db'
    query = """SELECT i.cwid, i.name, i.Dept as department, g.course, count(g.Student_CWID) as students
            FROM Grades as g JOIN Instructors as i on g.Instructor_CWID=i.CWID
            GROUP BY g.Course
            ORDER BY i.CWID
            """

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(query)
    results = c.fetchall()

    # convert the query results into a list of dictionaries to pass to the template
    data = [{'cwid': cwid, 'name': name, 'department': department, 'courses': courses, 'students': students}
            for cwid, name, department, courses, students in results]

    conn.close()  # close the connection to close the database

    return render_template('student_courses.html',
                           title='Stevens Repository',
                           table_title="Number of Students by Course and Instructor",
                           instructors=data)

app.run(debug=True)









