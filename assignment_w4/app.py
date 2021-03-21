from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
import os

# 建立 app 物件
app = Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/static"  #所有在 static 資料夾下的檔案，都對應到網路網址 /static/檔案名稱
) 

app.secret_key = str(os.urandom(14)) #secret key for session

@app.route("/")  #建立連線首頁的回應方式
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"]) #驗證使用者帳號密碼是否正確
def verify():
    account = request.form["account"]
    password = request.form["password"]
    if account=="test" and password=="test":
        session["username"] = account #記錄登入 session
        print("User (login)") #列印使用者登入
        return redirect("/member")
    else:
        return redirect("/error")

@app.route("/signout", methods=["GET"]) #使用者登出導回首頁
def logout():
    session.pop("username", None)
    print("User (logout)") # 列印使用者登出
    return redirect("/")

@app.route("/member") #登入後的會員頁
def memberPage():
    if "username" in session:
        return render_template("member.html")
    return redirect("/") #如果 username 沒有在 session 裡面直接導回首頁

@app.route("/error") #帳號密碼失敗的頁面
def errorPage():
    return render_template("error.html")

app.run(port=3000)

