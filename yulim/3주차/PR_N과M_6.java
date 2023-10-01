import java.util.*;
import java.io.*;

public class Main {

    public static int[] arr;
    public static int[] ans;
    public static boolean[] visited;
    public static int N, M;
    public static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr = new int[N];
        ans = new int[N];
        visited = new boolean[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        dfs(0, 0);
        System.out.print(sb);

    }

    public static void dfs(int start, int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++){
                sb.append(ans[i] + " ");
            }
            sb.append('\n');
            return;
        }

        for (int i = start; i < N; i++) {
            if (!visited[i]){
                visited[i] = true;
                ans[depth] = arr[i];
                dfs(i,depth + 1);
                visited[i] = false;
            }
        }
    }
}