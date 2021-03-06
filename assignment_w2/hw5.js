function maxZeros(nums){
    var zero_len = [];
    var count = 0;
    nums.push(1);
    for (i=0; i<nums.length; i++){
        if (nums[i] == 0){
            count = count + 1;
        } else{
            zero_len.push(count);
            count = 0;
        }
    }
    return Math.max.apply(null,zero_len);
}

console.log(maxZeros([0,1,0,0])) //2
console.log(maxZeros([1,0,0,0,0,1,0,1,0,0])) //4
console.log(maxZeros([1,1,1,1,1])) //0