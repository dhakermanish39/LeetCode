class Solution {
    public int minimumSwaps(int[] nums) {
        
        int swap=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                for(int j=nums.length-1;j>i;j--){
                    if(nums[j]!=0){
                        nums[i]=nums[j];
                        nums[j]=0;
                        swap=swap+1;
                        break;
                    }

                }
            }
        }
        return swap;
    }
}