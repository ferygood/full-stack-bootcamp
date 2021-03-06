function twoSum(nums, target){
    var reduced = 0;
    if (target/2 == 0){
        reduced = target/2;
        console.log(reduced)
    } else{
        reduced = (target+1)/2;
    }
    var idx = [];
    for (i=0; i<reduced; i++){
        if (nums.includes(i)){
            var idx1 = nums.indexOf(i);
            var idx2 = nums.indexOf(target-i);
            if (idx1>=0 && idx2>=0){
                idx.push(idx1);
                idx.push(idx2);
            } //因為找不到會回傳 -1, 我們不要-1
        }
    }
    return idx;
}  

console.log(twoSum([2,11,7,15], 9)); // [0,2]