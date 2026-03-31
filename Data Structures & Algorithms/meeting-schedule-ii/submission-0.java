/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public int minMeetingRooms(List<Interval> intervals) {
        if (intervals == null || intervals.size() == 0){
            return 0;
        }

        intervals.sort(Comparator.comparing(i -> i.start));
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int i = 0; i < intervals.size(); i++){
            Interval meeting = intervals.get(i);
            if (!minHeap.isEmpty() && minHeap.peek() <= meeting.start){
                minHeap.poll();
            }
            minHeap.offer(meeting.end);
        }
        return minHeap.size();
    }
}
