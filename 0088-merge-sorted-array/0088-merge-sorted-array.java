class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int [] result = new int [m+n];
        int s1=0 , s2=0;
        for(int i= 0; i<m+n;i++){
            if(s1<m){
                if(s2<n){
                    if(nums1[s1]<nums2[s2]){
                    result[i]=nums1[s1];
                    s1=s1+1;
                    }
                
                    else{
                    result[i]=nums2[s2];
                    s2=s2+1;
                }}
                else{
                     result[i]=nums1[s1];
                    s1=s1+1;
                }
               
            }
            else{
                  result[i]=nums2[s2];
                    s2=s2+1;
            }
        }
        for(int i=0;i<m+n;i++){
            nums1[i]=result[i];
        }
    }
}