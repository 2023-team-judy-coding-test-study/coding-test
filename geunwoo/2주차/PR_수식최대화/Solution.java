import java.util.*;

class Solution {
    static ArrayList<Long> numList = new ArrayList<>();
    static ArrayList<String> operList = new ArrayList<>();
    static int[] visited = new int[3];
    static String[] oper = new String[] { "*", "+", "-" };
    static String[] output = new String[3];
    static long answer = 0;

    public long solution(String expression) {
        String num = "";
        for (int i = 0; i < expression.length(); i++) {
            char e = expression.charAt(i);

            if (e == '+' || e == '-' || e == '*') {
                operList.add(e + "");
                numList.add(Long.parseLong(num));
                num = "";
            } else {
                num += e;
            }
        }

        // 마지막 숫자 저장
        numList.add(Long.parseLong(num));

        per(0, output.length);

        return answer;
    }

    /*
     * 연산 우선순위를 정하고 연산관련 함수를 호출하는 함수
     */
    private void per(int depth, int r) {
        // 종료시점
        if (depth == r) {
            solve();

            return;
        }

        for (int i = 0; i < output.length; i++) {
            if (visited[i] == 1)
                continue;

            visited[i] = 1;
            output[depth] = oper[i];
            per(depth + 1, r);
            visited[i] = 0;
        }
    }

    private void solve() {
        ArrayList<String> opers = new ArrayList<>();
        opers.addAll(operList);

        ArrayList<Long> nums = new ArrayList<>();
        nums.addAll(numList);

        for (int i = 0; i < output.length; i++) {
            String curOper = output[i];

            for (int j = 0; j < opers.size(); j++) {
                if (!opers.get(j).equals(curOper))
                    continue;

                long n1 = nums.get(j);
                long n2 = nums.get(j + 1);
                long result = cal(n1, n2, curOper);

                nums.remove(j + 1);
                nums.remove(j);
                opers.remove(j);

                nums.add(j, result);

                j--;
            }
        }

        answer = Math.max(answer, Math.abs(nums.get(0)));
    }

    private long cal(long n1, long n2, String oper) {
        long result = 0;

        switch (oper) {
            case "*":
                result = n1 * n2;
                break;
            case "+":
                result = n1 + n2;
                break;
            case "-":
                result = n1 - n2;
                break;
        }

        return result;
    }
}
