class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            set.add(num);
        }
        int longest = 0;

        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            if (!set.contains(num - 1)){
                int currentNumber = num;
                int streak = 1;

                while (set.contains(currentNumber + 1)){
                    currentNumber++;
                    streak++;
                }
                longest = Math.max(longest, streak);
            }
        }
        return longest;
    }
}
