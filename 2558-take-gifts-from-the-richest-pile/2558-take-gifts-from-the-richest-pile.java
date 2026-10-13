import java.util.PriorityQueue;
import java.lang.Math;
class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int gift : gifts) {
            pq.offer(gift);
        }
        for (int i = 0; i < k; i++) {
            int maxGifts = pq.poll();
            int remainingGifts = (int) Math.floor(Math.sqrt(maxGifts));
            pq.offer(remainingGifts);
        }
        long totalGifts = 0;
        while (!pq.isEmpty()) {
            totalGifts += pq.poll();
        }
        return totalGifts;
    }
}