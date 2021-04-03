from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session, url_for
import os
import mysql.connector

# 連結 local 資料庫
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yaomysql86",
    database="website"
)

mycursor = mydb.cursor() # 啟動 cursor

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

@app.route("/signup", methods=["POST"]) #建立註冊帳號程序
def signup():
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]
    sql = "select username from user where username='%s'"%(account)
    mycursor.execute(sql)
    result = mycursor.fetchall()
    #檢查帳號是否存在，不存在 result 會是 empty list
    if len(result)==0: 
        sql = "insert into user (name, username, password) values (%s, %s, %s)"
        val = (name, account, password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("signup success "+str(account))
        session["name"] = name
        session["username"] = account #有可能之後要改，彭彭這邊沒有要檢查
        return redirect("/member")
    else:
        print("signup fail")
        return redirect(url_for(".errorPage", message="帳號已被註冊"))

@app.route("/signin", methods=["POST"]) #建立登入帳號程序
def verify():
    account = request.form["account"]
    password = request.form["password"]
    sql="select exists (select * from user where username='%s' and password='%s')"%(account, password) #檢查帳號密碼是否存在
    mycursor.execute(sql)
    result = mycursor.fetchall()
    verify_result = result[0][0] #帳號密碼存在回傳 1，否則回傳 0
    if verify_result==1:
        mycursor.execute("select name from user where username='%s'"%(account))
        result = mycursor.fetchall()
        name = result[0][0]
        session["name"] = name #記錄使用者名稱進 session
        session["username"] = account #記錄登入 session
        print("User (login) "+str(account)) #列印使用者登入
        return redirect("/member")
    else:
        return redirect("/error")

@app.route("/signout", methods=["GET"]) #建立登出帳號程序。使用者登出導回首頁
def logout():
    session.pop("username", None) # 把使用者紀錄去除
    print("User (logout) ") # 列印使用者登出
    return redirect("/")

@app.route("/member") #登入後的會員頁網址
def memberPage():
    if "username" in session:
        return render_template("member.html", data=session["name"]) #樣本頁面加入使用者名稱
    return redirect("/") #如果 username 沒有在 session 裡面直接導回首頁

@app.route("/error/") #登入失敗頁網址
def errorPage():
    message=request.args.get("message", "帳號或密碼輸入錯誤")
    return render_template("error.html", data=message)

app.run(port=3000)

if __name__ == "__main__":
    app.run(debug=True)
