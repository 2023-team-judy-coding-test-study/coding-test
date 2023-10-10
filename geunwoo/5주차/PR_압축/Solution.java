import java.util.*;

class Solution {
    static HashMap<String, Integer> dict = new HashMap<>();
    static String message = "";
    static int n = 0;

    public int[] solution(String msg) {
        message = msg;
        int aAsc = Integer.valueOf('A');
        int zAsc = Integer.valueOf('Z');
        n = msg.length();

        // 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화
        int dictIdx = 0;
        for (int i = aAsc; i <= zAsc; i++) {
            dictIdx++;
            String alpha = String.valueOf((char) i);

            dict.put(alpha, dictIdx);
        }

        ArrayList<Integer> result = new ArrayList<>();
        int i = 0;
        while (i <= n - 1) {
            String w = String.valueOf(message.charAt(i));
            String c = "";
            // 2. 사전에서 현재 일별과 일치하는 가장 긴 문자열 word를 찾는다.
            String word = findLongestWord(i, i, w);

            // 3. word에 해당하는 사전의 색인 번호를 출력
            result.add(dict.getOrDefault(word, 0));

            i = i + word.length();

            // 입력에서 처리되지 않은 다음 글자가 남아있다면(c),
            if (i <= n - 1) {
                // w+c에 해당하는 단어를 사전에 등록한다.
                c = String.valueOf(message.charAt(i));
                String newWord = word + c;
                dictIdx++;
                dict.put(newWord, dictIdx);
            }
        }

        int[] answer = result.stream()
                .mapToInt(Integer::intValue)
                .toArray();
        return answer;
    }

    private String findLongestWord(int s, int i, String word) {
        int idx = dict.getOrDefault(word, 0);

        // 사전에 단어가 있다면
        if (idx > 0) {
            if (i < n - 1) {
                String c = String.valueOf(message.charAt(i + 1));
                return findLongestWord(s, i + 1, word + c);
            }
            return word;
        }
        // 사전에 단어가 없다면
        return message.substring(s, i);
    }
}