from flask import Flask,jsonify,request
import re

app=Flask(__name__)

def is_valid_email(email):
    pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern,email)

@app.route("/register",methods=['POST'])
def register():
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")

    if not name or not email:
         return jsonify({
            "status":False,
            "message":"Name and email are required"
             
        }),400
    
    if not is_valid_email(email):
        return jsonify({
            "status":False,
            "message":"email is not valid"
        }),400

    return jsonify({
        "status":True,
        "message":"registered successfully",
        "student":
        {
            "name":name,
            "email":email
        }
    }),400

if __name__=="__main__":
    app.run(debug=True)
