import java.util.*;

class Solution {
    static String[][] g_relation;
    static int g_m;
    static int g_n;
    static ArrayList<String> colsList;
    static ArrayList<String> candidateKeyList = new ArrayList<>();
    static HashSet<ArrayList<Character>> keySet = new HashSet<>();
    static int result = 0;

    public int solution(String[][] relation) {
        // init
        g_relation = relation;
        g_m = relation.length;
        g_n = relation[0].length;
        int rowLen = relation[0].length;

        // 후보키 갯수 선정
        for (int i = 1; i <= rowLen; i++) {
            int[] selected = new int[rowLen];
            colsList = new ArrayList<>();

            dfs(0, 0, i, selected);

            // System.out.println();
        }

        // 희소성 판단
        int answer = 0;
        return result;
    }

    public void dfs(int idx, int cnt, int max, int[] selected) {
        // 종료 조건
        if (cnt >= max) {
            String cols = "";
            for (int i = 0; i < selected.length; i++) {
                if (selected[i] == 1)
                    cols += i;
            }

            // 이미 수행한 속성 집합인지 확인
            for (String c : colsList) {
                if (c.equals(cols))
                    return;
            }
            colsList.add(cols);

            findKey(cols);

            return;
        }

        // 가지 치기
        for (int i = 0; i < selected.length; i++) {
            if (selected[i] == 1)
                continue;
            selected[i] = 1;
            dfs(i + 1, cnt + 1, max, selected);
            selected[i] = 0;
        }
    }

    private void findKey(String cols) {
        // System.out.println("keySet: " + keySet);
        // System.out.println(cols + " is key");
        char[] colArr = cols.toCharArray();
        ArrayList<Character> colList = new ArrayList<Character>();
        for (char c : colArr) {
            colList.add(c);
        }
        HashSet<String> set = new HashSet<>();

        // 최소성 검증
        // if (keySet.containsAll(cols)) return;
        for (ArrayList<Character> key : keySet) {
            if (colList.containsAll(key)) {
                return;
            }
        }

        for (int i = 0; i < g_m; i++) {
            String row = "";
            for (char c : colArr) {
                String col = String.valueOf(c);

                int colIdx = Integer.valueOf(col);
                row += g_relation[i][colIdx];
                row += "|";
            }

            if (set.contains(row))
                return;
            set.add(row);
        }
        // System.out.println(cols + " is key");
        keySet.add(colList);
        result++;
    }
}