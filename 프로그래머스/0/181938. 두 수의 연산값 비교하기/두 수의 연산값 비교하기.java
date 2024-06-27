class Solution {
    public int solution(int a, int b) {
        
        String abstr = Integer.toString(a) + Integer.toString(b);
        int ab = Integer.valueOf(abstr);
        
        if(ab >= 2*a*b){
            return ab;
        }else{
            return 2*a*b;
        }
    }
}