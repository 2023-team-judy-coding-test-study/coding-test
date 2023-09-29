import java.io.*;
import java.util.*;

public class Main {

    public static int n;
    public static int m;

    public static StringBuilder sb = new StringBuilder();

    public static int[] answer;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        answer = new int[m];

        backtracking(0);

        System.out.print(sb.toString());
    }

    public static void backtracking(int level) {
        // 종료 조건
        if (level == m) {
            for (int i = 0; i < m; i++) {
                sb.append(answer[i]).append(" ");
            }
            sb.append("\n");

            return;
        }

        // 가지 처기
        for (int i = 1; i <= n; i++) {
            answer[level] = i;
            backtracking(level + 1);
        }
    }
}
