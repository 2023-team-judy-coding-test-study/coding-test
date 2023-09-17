class Solution {
    public int solution(int n, int k) {
        int answer = 0;

        String[] kNums = Integer.toString(n, k).split("0"); //k진법으로 변환

        Boolean isPrime = true;
        for (String kNum: kNums) {
            if(kNum.equals("") || kNum.equals("1")) continue;

            long decimalNum = Long.parseLong(kNum);

            isPrime = true;
            for (int i = 2; i <= Math.sqrt(decimalNum); i++){
                if (decimalNum % i == 0){
                    isPrime = false;
                }
            }
            if (isPrime == true) {
                answer++;
            }
        }
        return answer;
    }
}