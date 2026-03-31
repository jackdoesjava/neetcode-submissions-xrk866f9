class KthLargest {
    private final int k;
    private final PriorityQueue<Integer> pq;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>();
        for (int n : nums){
            add(n);
        }
    }
    
    public int add(int val) {
        pq.add(val);
        if (pq.size() > k){
            pq.poll();
        }
        return pq.peek();
    }
}
