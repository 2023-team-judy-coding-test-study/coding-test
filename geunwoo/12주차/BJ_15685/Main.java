import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] dy = new int[] { 0, -1, 0, 1 };
    static int[] dx = new int[] { 1, 0, -1, 0 };

    static int[][] board = new int[101][101];

    /*
     * 시뮬레이션
     */
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());

            dragonCurve(x, y, d, g);
        }

        int answer = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (board[i][j] == 1 && board[i][j + 1] == 1 && board[i + 1][j] == 1 && board[i + 1][j + 1] == 1) {
                    answer++;
                }
            }
        }

        System.out.println(answer);
    }

    public static void dragonCurve(int x, int y, int d, int g) {
        ArrayList<Integer> dList = new ArrayList<>();

        dList.add(d);

        for (int i = 1; i <= g; i++) {
            for (int j = dList.size() - 1; j >= 0; j--) {
                dList.add((dList.get(j) + 1) % 4);
            }
        }

        board[y][x] = 1;
        for (int direct : dList) {
            y += dy[direct];
            x += dx[direct];

            board[y][x] = 1;
        }
    }
}
