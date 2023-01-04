from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import pandas as pd
import itertools
from helpers import process, plot
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///courses_actual.db")

# Configure Dataframe for Logic processing
columns = ["Mon","Tue","Wed","Thu","Fri","Sat"]
indexs = ["0730","0830","0930","1030","1130","1230","1330","1430","1530","1630","1730","1830","1930","2030","2130","2230"]
df = pd.DataFrame(columns = columns, index = indexs)
filtered_list = []
current_index = 0

@app.route("/")
def index():
    # GET
    code = db.execute("select DISTINCT code from courses")
    list_code = []
    for each in code:
        list_code.append(each['code'])
    return render_template("index.html",list_code=list_code)

@app.route('/query', methods=['GET'])
def query():
    code = db.execute("select DISTINCT code from courses")
    list_code = []
    for each in code:
        list_code.append(each['code'])
    return jsonify({"success":list_code})

@app.route('/input_checking', methods=['GET','POST'])
def input_checking():
    if request.method == "POST":
        req_data = request.get_json()
        number_of_requests = len(req_data)
        requested = []
        for each in range(number_of_requests):
            requested.append(req_data[str(each)])
        for each in requested:
            if each == '' and (len(requested) > len(set(requested))):
                return jsonify({"status":"fail","reason":"empty and dup"})
            if each == '':
                return jsonify({"status":"fail","reason":"empty"})

        if len(requested) > len(set(requested)):
            return jsonify({"status":"fail","reason":"dup"})

        return jsonify({"status":"pass"})

@app.route('/processing', methods=['GET','POST'])
def processing():
    if request.method == "POST":
        req_data = request.get_json()
        number_of_requests = len(req_data)
        requested = []
        for each in range(number_of_requests):
            requested.append(req_data[str(each)])
        global current_index
        global filtered_list
        filtered_list = process(requested)
        current_index = 0
        df = plot(filtered_list,current_index)
        length = len(filtered_list)
        code_list = []
        name_list = []
        course_index_list = []
        comb = filtered_list[current_index]
        for each_index in comb:
            code_list.append(each_index['code'])
            name_list.append(each_index['name'])
            course_index_list.append(each_index['course_index'])

        return jsonify({"success":df.to_json(orient='values'),"length":length,"current_index":current_index,"code":code_list,"name":name_list,"course_index":course_index_list})

@app.route('/increment_decrement', methods=['GET','POST'])
def increment_decrement():
    if request.method == "POST":
        req_data = request.get_json()
        print(req_data)
        global current_index
        global filtered_list
        print("before adjustments",current_index)
        length = len(filtered_list)

        if req_data == "decrement":
            print("decrement processing")
            if current_index == 0:
                print("during adjustment",current_index)
                df = plot(filtered_list,current_index)
                code_list = []
                name_list = []
                course_index_list = []
                for each_index in filtered_list[current_index]:
                    print(each_index)
                    req = db.execute("SELECT code,name,course_index from courses WHERE course_index = ?",each_index['course_index'])
                    code_list.append(req[0]['code'])
                    name_list.append(req[0]['name'])
                    course_index_list.append(req[0]['course_index'])
                return jsonify({"success":df.to_json(orient='values'),"length":length,"current_index":current_index,"code":code_list,"name":name_list,"course_index":course_index_list})
            if current_index > 0:
                current_index -= 1
                print("during adjustment",current_index)
                df = plot(filtered_list,current_index)
                code_list = []
                name_list = []
                course_index_list = []
                for each_index in filtered_list[current_index]:
                    print(each_index)
                    req = db.execute("SELECT code,name,course_index from courses WHERE course_index = ?",each_index['course_index'])
                    code_list.append(req[0]['code'])
                    name_list.append(req[0]['name'])
                    course_index_list.append(req[0]['course_index'])
                return jsonify({"success":df.to_json(orient='values'),"length":length,"current_index":current_index,"code":code_list,"name":name_list,"course_index":course_index_list})
        if req_data == "increment":
            print("increment processing")
            if current_index == length - 1:
                print("during adjustment",current_index)
                df = plot(filtered_list,current_index)
                code_list = []
                name_list = []
                course_index_list = []
                for each_index in filtered_list[current_index]:
                    print(each_index)
                    req = db.execute("SELECT code,name,course_index from courses WHERE course_index = ?",each_index['course_index'])
                    code_list.append(req[0]['code'])
                    name_list.append(req[0]['name'])
                    course_index_list.append(req[0]['course_index'])
                return jsonify({"success":df.to_json(orient='values'),"length":length,"current_index":current_index,"code":code_list,"name":name_list,"course_index":course_index_list})
            if current_index < length - 1:
                current_index += 1
                print("during adjustment",current_index)
                df = plot(filtered_list,current_index)
                code_list = []
                name_list = []
                course_index_list = []
                for each_index in filtered_list[current_index]:
                    print(each_index)
                    req = db.execute("SELECT code,name,course_index from courses WHERE course_index = ?",each_index['course_index'])
                    code_list.append(req[0]['code'])
                    name_list.append(req[0]['name'])
                    course_index_list.append(req[0]['course_index'])
                return jsonify({"success":df.to_json(orient='values'),"length":length,"current_index":current_index,"code":code_list,"name":name_list,"course_index":course_index_list})

if __name__ == "__main__":
  app.run(debug=True)

