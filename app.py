from resources.query_service import QueryService
from flask_restful import Api, Resource, reqparse
from flask import Flask, render_template
import pandas as pd
import requests
from flask import request


app = Flask(__name__)
# api = Api(app)
# api.add_resource(QueryService, '/news_urls')


@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index1.html")

    else:
        data = pd.read_csv (r'testing/db_dell.csv', delimiter=",")
        user_ID = int(request.form['data'])
        print(type(user_ID))
        print(user_ID)

        arr=["Emp ID","Emp_name"]

        # input_string = input("Enter array separated by commas: ")   #must include emp_ID
        # arr  = input_string.split(",")

        df = pd.DataFrame(data, columns = arr)
        df.set_index("Emp ID", inplace = True)
        result = df.loc[user_ID]
        print(result)
        print("\n")

        return render_template("index1.html")


if __name__ == '__main__':
    try:
        app.run('localhost', port = 5000, debug = True, use_reloader = False)
    except Exception as e:
        print (e)
