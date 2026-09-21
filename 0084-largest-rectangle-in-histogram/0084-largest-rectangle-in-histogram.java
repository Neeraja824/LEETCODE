class Solution {
    public int largestRectangleArea(int[] height) {
        int prev[]=new int[height.length];
        int next[]=new int[height.length];
        Stack<Integer> st=new Stack<>();
        for(int i=height.length-1;i>=0;i--){
            while(!st.isEmpty() && height[st.peek()]>=height[i]){
                st.pop();
            }
            next[i]=st.isEmpty()?height.length:st.peek();
            st.push(i);
        }
        st.clear();
        for(int i=0;i<height.length;i++){
            while(!st.isEmpty() && height[st.peek()]>=height[i]){
                st.pop();
            }
            prev[i]=st.isEmpty()?-1:st.peek();
            st.push(i);
        }
        int max_area = 0;
        for (int i = 0; i < height.length; i++) {
            int area = height[i] * (next[i] - prev[i] - 1);
            max_area = Math.max(max_area, area);
        }
        return max_area;
    }
}