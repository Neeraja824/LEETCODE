class Solution {
    public boolean isThree(int n) {
        int x=(int)Math.sqrt(n);
        if(x*x!=n){
            return false;
        }
        return isprime(x);
    }
    public boolean isprime(int val){
        if(val<2) return false;
        for(int i=2;i*i<=val;i++){
            if(val%i==0){
                return false;
            }
        }
        return true;
    }
}