class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pair = new HashMap<>();
        pair.put(')', '(');
        pair.put(']', '[');
        pair.put('}', '{');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } 
            else if (c == ')' || c == ']' || c == '}') {
                if (stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                char expected = pair.get(c);
                if (top != expected) {
                    return false;
                }
            }
        }

        return stack.isEmpty();


    }
}
