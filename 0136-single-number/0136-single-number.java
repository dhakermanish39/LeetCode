class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        int num = nums[0];
        int count =0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==num){
                count++;
            }
            else{
                if(count==1)
                return nums[i-1];
                else{
                    count =1;
                    num=nums[i];
                }
            }
        }
        return nums[nums.length-1];
    }
}