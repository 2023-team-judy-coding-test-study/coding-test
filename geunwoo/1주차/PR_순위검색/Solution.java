import java.util.*;

class Solution {
    static HashMap<String, List<Integer>> map = new HashMap<String, List<Integer>>();

    public int[] solution(String[] infos, String[] query) {
        int[] answer = new int[query.length];

        for (String info : infos) {
            String[] p = info.split(" ");
            makeSentence(0, p, "");
        }

        for (String key : map.keySet()) {
            Collections.sort(map.get(key));
        }

        for (int i = 0; i < query.length; i++) {
            query[i] = query[i].replaceAll(" and ", "");
            String[] q = query[i].split(" "); // [조건, 점수]

            String condition = q[0];
            int score = Integer.parseInt(q[1]);

            answer[i] = map.containsKey(q[0]) ? binarySearch(condition, score) : 0;
        }

        return answer;
    }

    // 검색 가능한 모든 경우의 수를 map에 저장
    private void makeSentence(int idx, String[] p, String str) {
        // 종료조건
        if (idx >= 4) {
            if (!map.containsKey(str)) {
                List<Integer> list = new ArrayList<Integer>();
                map.put(str, list);
            }
            map.get(str).add(Integer.parseInt(p[4]));

            return;
        }

        // 가지치기
        makeSentence(idx + 1, p, str + "-");
        makeSentence(idx + 1, p, str + p[idx]);
    }

    // 이분 탐색
    private int binarySearch(String condition, int score) {
        if (!map.containsKey(condition))
            return 0;

        List<Integer> list = map.get(condition);
        System.out.println(score + " , " + list);
        int start = 0;
        int end = list.size() - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (list.get(mid) < score)
                start = mid + 1;
            else
                end = mid - 1;
        }

        return list.size() - start;
    }
}
