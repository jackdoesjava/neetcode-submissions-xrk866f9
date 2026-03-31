class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0){
            return 0;
        }

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++){
            int price = prices[i];

            maxProfit = Math.max(maxProfit, price - minPrice);
            minPrice = Math.min(minPrice, price);
        }
        return maxProfit;
    }
}
