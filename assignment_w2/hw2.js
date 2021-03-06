function avg(data){
    var sum = 0;
    for (var i=0; i<data["count"]; i++){
        sum += data["employee"][i]["salary"];
    }
    avg_salary = Math.round(sum/(data["count"])); //四捨五入
    return avg_salary;
}

data = {"count":3, "employee":[
    {"name":"John", "salary":30000},
    {"name":"Bob", "salary":60000},
    {"name":"Jenny", "salary":50000}]}

console.log(avg(data)) //四捨五入 46667