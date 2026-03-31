class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++){ //loop through each int in array/stack
            // pick first number and then check
            // for the first number following the sequence which its greater than
            // then add to an array how many places along the stack it was
            // so maybe count how many pops you do for it
            // keep going for each number from left to right
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                int prev = stack.pop();
                result[prev] = i - prev;
            }
            stack.push(i);
        }
        return result;
    }
}
