from flask import Flask,jsonify,request
import sqlite3 
import os

app=Flask(__name__)

DATABASE=os.path.join(os.path.dirname(__file__),"students.db")

def get_db_connection():
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row
    return conn

@app.route("/students",methods=['POST'])
def add_students():
    data=request.get_json()
    name=data['name']
    course=data['course']
    email=data['email']

    conn=get_db_connection()
    conn.execute(
        "INSERT INTO students(name,course,email) VALUES (?,?,?)",(name,course,email)
    )
    conn.commit()
    conn.close()
    return jsonify({
        "message":"student added successfully"
    }),201

@app.route("/students",methods=['GET'])
def getstudents():
    conn=get_db_connection()
    students=conn.execute(
        "SELECT * FROM students"
    ).fetchall()
    conn.close()
    results=[]
    for student in students:
        results.append({
            "id":student["id"],
            "name":student["name"],
            "course":student["course"],
            "email":student["email"]
            })

    return jsonify(results),200

@app.route("/students/<int:id>",methods=['PUT'])
def update_student(id):
    data=request.get_json()
    name=data['name']
    course=data['course']
    email=data['email']
    
    conn=get_db_connection()
    conn.execute(
            """UPDATE students SET name=?,course=?,email=? WHERE id=?""",(name,course,email,id)
    )
    conn.commit()
    conn.close()
    return jsonify({
        "message":"student updated successfully"
    }),200

@app.route("/students/<int:id>",methods=['DELETE'])
def delete(id):
    conn=get_db_connection()
    conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )
    conn.commit()
    conn.close()
    return jsonify({
        "message":"student deleted successfully"
        }),200

if __name__=="__main__":
    app.run(debug=True)
        