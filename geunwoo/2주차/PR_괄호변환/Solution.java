import java.util.*;

class Solution {
    public String solution(String p) {

        String answer = makeCorrectPair(p);
        return answer;
    }

    private String makeCorrectPair(String p) {
        int pSize = p.length();
        if (pSize == 0)
            return "";

        String u = "";
        String v = "";
        int lCnt = 0;
        int rCnt = 0;

        for (int i = 0; i < pSize; i++) {
            if (p.charAt(i) == '(')
                lCnt++;
            else
                rCnt++;

            u += p.charAt(i);

            if (lCnt == rCnt) {
                v = p.substring(i + 1);
                break;
            }
            ;
        }

        if (isCorrect(u)) {
            return u += makeCorrectPair(v);
        } else {
            String temp = "(";
            temp += makeCorrectPair(v);
            temp += ")";

            u = u.substring(1, u.length() - 1);

            for (int i = 0; i < u.length(); i++) {
                if (u.charAt(i) == '(')
                    temp += ')';
                else
                    temp += '(';
            }
            return temp;
        }
    }

    private boolean isCorrect(String s) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                st.push(s.charAt(i));
            } else {
                if (st.isEmpty() || st.peek() == ')')
                    return false;

                st.pop();
            }
        }
        return true;
    }
}