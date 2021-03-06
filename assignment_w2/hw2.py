def avg(data):
    sum = 0
    for n in range(data["count"]):
        sum += data["employee"][n]["salary"]
    avg_salary = round(sum/(data["count"])) #四捨五入至整數
    return avg_salary

   
data = {"count":3, "employee":[
    {"name":"John", "salary":30000},
    {"name":"Bob", "salary":60000},
    {"name":"Jenny", "salary":50000}]}


print(avg(data)) #四捨五入 46667


