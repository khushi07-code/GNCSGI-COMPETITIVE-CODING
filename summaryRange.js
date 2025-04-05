/**
 * @param {number[]} nums
 * @return {string[]}
 */

// Input: nums = [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: The ranges are:
// [0,2] --> "0->2"
// [4,5] --> "4->5"
// [7,7] --> "7"

var summaryRanges = function(nums) {
    if(nums.length==0){
        return [];
    }
    let a;
    let b;
    let ans=[]
    let previous=null;
    nums.forEach((i)=>{
        if(previous==null){
            previous=i;
            a=i;
            b=i;
        }else{
            if(previous!=i-1){
                ans.push((a!=b) ?`${a}->${b}`:`${a}`);
                a=i;
            }
            b=i;
            previous=i;
        }
    })
    ans.push((a!=b) ?`${a}->${b}`:`${a}`);
    return ans;
};
