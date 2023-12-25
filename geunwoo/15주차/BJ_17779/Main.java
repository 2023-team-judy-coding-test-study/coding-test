import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] board;
    static int totalOfPeople;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {

        // 격자판 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());

        board = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                totalOfPeople += board[i][j];
            }
        }

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                for (int d1 = 0; d1 < n; d1++) {
                    for (int d2 = 0; d2 < n; d2++) {
                        if (x + d1 + d2 >= n)
                            continue;
                        if (y - d1 < 0 || y + d2 >= n)
                            continue;

                        solution(x, y, d1, d2);
                    }
                }
            }
        }

        System.out.println(answer);
    }

    static private void solution(int x, int y, int d1, int d2) {
        int[][] borders = new int[n][n];

        // 경계선
        for (int i = 0; i <= d1; i++) {
            borders[x + i][y - i] = 1;
            borders[x + d2 + i][y + d2 - i] = 1;
        }

        for (int i = 0; i <= d2; i++) {
            borders[x + i][y + i] = 1;
            borders[x + d1 + i][y - d1 + i] = 1;
        }

        int[] sumOfPeople = new int[6];

        //
        //
        //
        // 1번
        for (int r = 0; r < x + d1; r++) {
            for (int c = 0; c <= y; c++) {
                if (borders[r][c] == 1)
                    break;
                sumOfPeople[1] += board[r][c];
            }
        }

        // 2번
        for (int r = 0; r <= x + d2; r++) {
            for (int c = n - 1; c > y; c--) {
                if (borders[r][c] == 1)
                    break;
                sumOfPeople[2] += board[r][c];
            }
        }

        // 3번
        for (int r = x + d1; r < n; r++) {
            for (int c = 0; c < y - d1 + d2; c++) {
                if (borders[r][c] == 1)
                    break;
                sumOfPeople[3] += board[r][c];
            }
        }

        // 4번
        for (int r = x + d2 + 1; r < n; r++) {
            for (int c = n - 1; c >= y - d1 + d2; c--) {
                if (borders[r][c] == 1)
                    break;
                sumOfPeople[4] += board[r][c];
            }
        }

        // 5번
        sumOfPeople[5] = totalOfPeople;
        for (int i = 1; i <= 4; i++) {
            sumOfPeople[5] -= sumOfPeople[i];
        }

        Arrays.sort(sumOfPeople);

        answer = Math.min(sumOfPeople[5] - sumOfPeople[1], answer);
    }
}
