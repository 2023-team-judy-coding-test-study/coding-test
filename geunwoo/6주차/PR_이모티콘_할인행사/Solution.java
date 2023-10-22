import java.util.*


class Solution {
    public static int[][] g_users;
    public static int[] g_emoticons;

    public static int g_usersLen;
    public static int g_emoticonsLen;
    public static int g_salesLen;
    public static int memberNum = 0;
    public static int saleAmount = 0;

    public int[] solution(int[][] users, int[] emoticons) {

        g_users = users;
        g_emoticons = emoticons;

        g_usersLen = users.length;
        g_emoticonsLen = emoticons.length;
        g_salesLen = emoticons.length;

        int[] sales = new int[emoticons.length];

        comb(0, sales);

        int[] answer = new int[2];
        answer[0] = memberNum;
        answer[1] = saleAmount;
        return answer;}

    private void comb(int idx, int[] sales){
        if (idx >= g_salesLen) {
            calculate(sales);
            return;}

        for (int i=10; i <= 40; i += 10){
            sales[idx] = i;
            comb(idx+1, sales);
            sales[idx] = 0;}
    }

    private void calculate(int[] sales){
        int count = 0;
        int amount = 0;

        for (int[] user: g_users){
            int discount = user[0];
            int price = user[1];
            int sum = 0;

            for (int i=0; i < g_salesLen; i++){
                if (sales[i] >= discount){
                    sum += ((g_emoticons[i]/100)*(100-sales[i])); }
            }

            if (sum >= price) count++;
            else amount += sum;}

        if (count > memberNum){
            memberNum = count;
            saleAmount = amount;}
        else if (count == memberNum){
            if (saleAmount < amount){
                saleAmount = amount;}
        }
    }
}
