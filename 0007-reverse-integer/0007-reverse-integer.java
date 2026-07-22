class Solution {
    public int reverse(int num) {
        if(num==0)
         return num;
        if(num<0){
             int rev=0;
        num=-num;
        while (num>0){
            
             if (rev  > (Integer.MAX_VALUE/10)){
                rev=rev*0;
                break;
            }
            rev=rev*10+(num%10);
            num=num/10;
        }
        return -rev;
        }
        else{
             int rev=0;
        
        while (num>0){
            if (rev  > (Integer.MAX_VALUE/10)){
                rev=rev*0;
                break;
            }
            rev=rev*10+(num%10);
             
            num=num/10;
        }
        return rev;
        }
       
    }
}