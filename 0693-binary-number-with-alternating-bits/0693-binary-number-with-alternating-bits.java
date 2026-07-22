class Solution {
    public boolean hasAlternatingBits(int n) {
        boolean sign=true;
        int temp=-1;
        while(n>0){
            int temp1=n%2;
          
            if((temp==temp1)){
                sign=false;
                break;
            }
              n=n/2;
            temp=temp1;
        }
        return sign;
    }
}