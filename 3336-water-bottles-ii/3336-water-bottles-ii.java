class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int bottle=numBottles;
        int empty=numBottles;
        while(empty>=numExchange){
            empty-=numExchange;
            numExchange++;
            bottle++;
            empty++;
        }
        return bottle;
    }
}