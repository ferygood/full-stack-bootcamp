import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yaomysql86",
    database="website"
)

mycursor = mydb.cursor() # 啟動 cursor

mycursor.execute("select id,name,username from user where username='timhesi'")
result = mycursor.fetchall()
print(result)
#print(result[0][0])
#print(result[0][1])
#print(result[0][2])