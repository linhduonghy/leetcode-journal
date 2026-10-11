import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int[] resultsArray(int[][] queries, int k) {

        int n = queries.length;
        int[] res = new int[n];
        Arrays.fill(res, -1);
        if (n < k) {
            return res;
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        for (int i = 0; i < k; ++i) {
            pq.add(distance(queries[i]));
        }
        res[k - 1] = pq.peek();

        for (int i = k; i < n; ++i) {
            int dis = distance(queries[i]);
            int maxValue = pq.peek();
            if (dis < maxValue) {
                pq.poll();
                pq.add(dis);
                maxValue = pq.peek();
            }
            res[i] = maxValue;
        }
        return res;
    }

    static int distance(int[] query) {
        return Math.abs(query[0]) + Math.abs(query[1]);
    }

    public static void main(String[] args) {
        int[][] arr = new int[][] {{-7,9},{-7,-6},{6,7},{5,8},{1,-5}};
        new Solution().resultsArray(arr, 2);
    }

}