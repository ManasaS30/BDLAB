from flask import Flask,jsonify
app=Flask(__name__)
users=[
    {"id":1,"name":"Manasa.S","email":"ma1@gmail.com"},
    {"id":2,"name":"Man","email":"ma1@gmail.com"},
    {"id":1,"name":"Masa.S","email":"ma1@gmail.com"},
    {"id":1,"name":"Mana.S","email":"ma1@gmail.com"},
    {"id":1,"name":"Ma.S","email":"ma1@gmail.com"}
]
@app.route("/users",methods=['GET'])
def getusers():
    return jsonify({
        "status":True,
        "message":"users retrieved successfully",
        "count":len(users),
        "data":users
    }),200

@app.route("/users/<int:uid>",methods=['GET'])
def getuser(uid):
    for user in users:
        if user['id']==uid:
            return jsonify({
                    "sucess":True,
                    "message":"user retrieved successfully",
                    "data":user
                }),200

    return jsonify({
            "sucess":False,
            "message":"user not found",
        }),404

if __name__=="__main__":
    app.run(debug=True)