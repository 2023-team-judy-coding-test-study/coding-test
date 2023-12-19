import java.util.*;
import java.io.*;

public class Main {
    static int[][] g_board = new int[100][100];

    public static void main(String[] args) throws Exception {
        // 입력 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 3; i++) {
            String[] row = br.readLine().split(" ");

            for (int j = 0; j < row.length; j++) {
                g_board[i][j] = Integer.parseInt(row[j]);
            }
        }

        int timeCnt = 0;
        while (timeCnt <= 100) {

            // 정답 비교
            if (g_board[r - 1][c - 1] == k)
                break;

            // 정렬 (R연산, C연산)
            int rowLen = getRowLen();
            int colLen = getColLen();

            if (rowLen >= colLen) {
                // R 연산
                rowSort();
            } else {
                // C 연산
                colSort();
            }

            // for (int[]row : g_board){
            // if (row[0] == 0) break;
            // System.out.println(Arrays.toString(row));
            // }
            // System.out.println();

            timeCnt++;
        }

        int answer = timeCnt <= 100 ? timeCnt : -1;
        System.out.println(answer);
    }

    private static int getRowLen() {
        int maxLength = 0;

        for (int j = 0; j < 100; j++) {
            int length = 0;
            for (int i = 0; i < 100; i++) {
                if (g_board[i][j] == 0) {
                    maxLength = Math.max(maxLength, length);
                    break;
                }

                length++;
            }
        }

        return maxLength;
    }

    private static int getColLen() {
        int maxLength = 0;

        for (int i = 0; i < 100; i++) {
            int length = 0;
            for (int j = 0; j < 100; j++) {
                if (g_board[i][j] == 0) {
                    maxLength = Math.max(maxLength, length);
                    break;
                }

                length++;
            }
        }

        return maxLength;
    }

    private static void rowSort() {
        for (int i = 0; i < 100; i++) {
            // 숫자 크기, 숫자 갯수 저장
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int j = 0; j < 100; j++) {
                if (g_board[i][j] > 0) {
                    map.put(g_board[i][j], map.getOrDefault(g_board[i][j], 0) + 1);

                    g_board[i][j] = 0;
                }
            }

            // 숫자 갯수 asc -> 숫자 크기 asc 순으로 정렬
            ArrayList<Element> eArr = new ArrayList<>();
            for (Integer key : map.keySet()) {
                eArr.add(new Element(key, map.get(key)));
            }
            eArr.sort(Comparator.comparing(Element::getCnt).thenComparing(Element::getN));

            int idx = 0;
            for (Element e : eArr) {
                if (idx >= 100)
                    break;

                g_board[i][idx] = e.n;
                g_board[i][idx + 1] = e.cnt;
                idx += 2;
            }
        }
    }

    private static void colSort() {
        for (int j = 0; j < 100; j++) {
            // 숫자 크기, 숫자 갯수 저장
            HashMap<Integer, Integer> map = new HashMap<>();
            for (int i = 0; i < 100; i++) {
                if (g_board[i][j] > 0) {
                    map.put(g_board[i][j], map.getOrDefault(g_board[i][j], 0) + 1);

                    g_board[i][j] = 0;
                }
            }

            // 숫자 갯수 asc -> 숫자 크기 asc 순으로 정렬
            ArrayList<Element> eArr = new ArrayList<>();
            for (Integer key : map.keySet()) {
                eArr.add(new Element(key, map.get(key)));
            }
            eArr.sort(Comparator.comparing(Element::getCnt).thenComparing(Element::getN));

            int idx = 0;
            for (Element e : eArr) {
                if (idx >= 100)
                    break;

                g_board[idx][j] = e.n;
                g_board[idx + 1][j] = e.cnt;
                idx += 2;
            }
        }
    }

    static class Element {
        int n;
        int cnt;

        public Element(int n, int cnt) {
            this.n = n;
            this.cnt = cnt;
        }

        public int getN() {
            return this.n;
        }

        public int getCnt() {
            return this.cnt;
        }
    }
}
