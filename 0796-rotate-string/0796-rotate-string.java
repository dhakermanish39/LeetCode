class Solution {
    public boolean rotateString(String s, String goal) {
        String str=s+s;
        if(s.length()!=goal.length()) return false;
        return str.contains(goal);
        
    }
}