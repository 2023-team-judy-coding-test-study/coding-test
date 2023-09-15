class Solution {
    public int solution(int n, int k) {
        int answer = 0;

        String[] kNums = Integer.toString(n, k).split("0"); //k진법으로 변환

        Boolean isPrime = true;
        for (String kNum: kNums) {
            if(kNum.equals("") || kNum.equals("1")) continue;

            long decimalNum = Long.parseLong(kNum); //10진법으로 변환
            //int decimalNum = Integer.parseInt(kNum, k); //처음에 이렇게 변환했는데 틀림

            isPrime = true;
            for (int i = 2; i <= (int)Math.sqrt(decimalNum); i++){
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