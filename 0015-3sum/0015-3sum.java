import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        Arrays.sort(nums);

        int n = nums.length;
        for (int i = 0; i < n; i++){
            if (i != 0 && nums[i] == nums[i-1]) continue;
            if (nums[i] > 0) break;

            int j = i+1;
            int k = n-1;

            while (j < k){
                int sum = nums[i] + nums[j] + nums[k];
                if(sum < 0){
                    j++;
                } else if (sum > 0){
                    k--;
                } else {
                    results.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
                    while (j < k && nums[j] == nums[j-1]) j++;                }
            }
        }
        return results;
    }
}
   