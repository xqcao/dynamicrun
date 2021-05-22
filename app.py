from flask import Flask,render_template,request
from flask_cors import CORS
from types import FunctionType
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/save',methods=['POST'])
def do_save():
    code = request.data.decode("utf-8")
    data = runsay(code)
    print(code)
    print(data)
    return {"msg":"success to save","response":json.dumps(data)}

def runsay(cd):
    print(cd)
    say_code = compile(cd, "<string>", "exec")
    print(say_code)
    say_func = FunctionType(say_code.co_consts[0], globals(), "say")
    res_1 = say_func()
    print("res_1", res_1)
    return {"msg": "runing success", "response": res_1}

@app.route("/run")
def call_run():
    code = """def say(): return 'hi world'"""
    print("code: ",code)
    runsay(code)
    # exec(code)
    # exec(code)
    # # res_1 = exec(f'say()')
    # res_1 = say()
    # print("res_1", res_1)
    return {"msg":"world"}
@app.route("/ping")
def hello_pong():
    return "pong"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)
