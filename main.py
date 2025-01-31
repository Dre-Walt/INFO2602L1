import json

from flask import Flask, jsonify, request

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    result=[]
    pref= request.args.get('pref')
    if pref:
        for student in data:
            if student['pref'] == pref:
                result.append(student)
        return jsonify(result)
    return jsonify(data)
    

@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student ['id'] == id:
            return jsonify(student)

@app.route('/stats')
def get_stats():
    statis = {
        "Chicken": 0,
        "Fish": 0,
        "Vegetable": 0,
        "Computer Science (Major)": 0,
        "Computer Science (Special)": 0,
        "Information Technology (Major)": 0
    }

    for student in data:
        if student['pref']  == 'Chicken':
            statis["Chicken"] = statis["Chicken"] + 1
            
        if student['pref']  == 'Fish':
            statis["Fish"] = statis["Fish"] + 1
            
        if student['pref'] == 'Vegetable':
            statis["Vegetable"] = statis["Vegetable"] + 1
            
        if student['programme'] == 'Computer Science (Major)':
            statis["Computer Science (Major)"] = statis["Computer Science (Major)"] + 1

        if student['programme'] == 'Computer Science (Special)':
             statis["Computer Science (Special)"] = statis["Computer Science (Special)"] + 1
            
        if student['programme'] == 'Information Technology (Major)':
            statis["Information Technology (Major)"] = statis["Information Technology (Major)"] + 1
    return jsonify(statis)



@app.route('/add/<int:a>/<int:b>')
def add_values(a,b):
    return jsonify(a+b)

@app.route('/subtract/<int:a>/<int:b>')
def sub_value(a,b):
    return jsonify(a-b)

@app.route('/multiply/<int:a>/<int:b>')
def mul_value(a,b):
    return jsonify(a*b)

@app.route('/divide/<int:a>/<int:b>')
def div_value(a,b):
    return jsonify(a/b)

app.run(host='0.0.0.0', port=8080, debug=True)
