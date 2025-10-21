class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int>answer;
        int val=rowIndex;
        long int temp=1;
        answer.push_back(temp);
        for(int i=1;i<=rowIndex;i++){
            temp=temp*val;
            temp/=i;
            answer.push_back(temp);
            val--;
        }
        return answer;
    }
};