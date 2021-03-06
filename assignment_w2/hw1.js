
function calculate(min, max){
    // 建立連續整數陣列
    var arr = [];
    for (var i = min; i < max+1; i++){
        arr.push(i);
    }
    
    // 用迴圈相加
    sum = 0;
    for (var n = 0; n < arr.length; n++){
        sum += arr[n];
    }
    return sum;
}

console.log(calculate(1,3)); //6
console.log(calculate(4,8)); //30