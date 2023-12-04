import java.io.*;
import java.util.*;

public class Main {
    public static int n;
    public static int m;
    public static int[][] g_board;
    public static int[][] g_origin_board;
    public static final ArrayList<Camera> g_cameraList = new ArrayList<>();
    public static int g_cameraListSize;
    public static int g_min = 64;

    /*
     * 재귀 완전 탐색
     */
    public static void main(String[] args) throws Exception {

        // 1. g_board 초기화 & cctv 찾기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g_origin_board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < m; j++) {
                // g_origin_board 초기화
                g_origin_board[i][j] = Integer.parseInt(st.nextToken());

                // 카메라 찾기
                if (g_origin_board[i][j] >= 1 && g_origin_board[i][j] <= 5) {
                    g_cameraList.add(new Camera(i, j, g_origin_board[i][j], 0));

                    g_cameraListSize++;
                }
            }
        }

        // board 초기화
        initBoard();

        // 사각지대 찾기
        findBlindSpot(0);

        System.out.println(g_min);
    }

    private static void initBoard() {
        g_board = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                g_board[i][j] = g_origin_board[i][j];
            }
        }
    }

    private static void findBlindSpot(int idx) {
        // 종료 조건
        if (g_min == 0)
            return;

        if (idx >= g_cameraListSize) {

            runCam();

            int cnt = countBlindSpot();

            g_min = Math.min(g_min, cnt);

            initBoard();
            return;
        }

        for (int i = 0; i < 4; i++) {
            g_cameraList.get(idx).changeDirection(i);

            findBlindSpot(idx + 1);
        }
    }

    private static void runCam() {
        for (Camera cam : g_cameraList) {
            switch (cam.num) {
                case 1:
                    switch (cam.d) {
                        case 0:
                            checkRight(cam);
                            break;
                        case 1:
                            checkBottom(cam);
                            break;
                        case 2:
                            checkLeft(cam);
                            break;
                        case 3:
                            checkUp(cam);
                            break;
                    }
                    break;
                case 2:
                    switch (cam.d) {
                        case 0:
                            checkRight(cam);
                            checkLeft(cam);
                            break;
                        case 1:
                            checkBottom(cam);
                            checkUp(cam);
                            break;
                        case 2:
                            checkLeft(cam);
                            checkRight(cam);

                            break;
                        case 3:
                            checkUp(cam);
                            checkBottom(cam);
                            break;
                    }
                    break;
                case 3:
                    switch (cam.d) {
                        case 0:
                            checkRight(cam);
                            checkBottom(cam);
                            break;
                        case 1:
                            checkBottom(cam);
                            checkLeft(cam);
                            break;
                        case 2:
                            checkLeft(cam);
                            checkUp(cam);
                            break;
                        case 3:
                            checkUp(cam);
                            checkRight(cam);
                            break;
                    }
                    break;
                case 4:
                    switch (cam.d) {
                        case 0:
                            checkUp(cam);
                            checkRight(cam);
                            checkBottom(cam);
                            break;
                        case 1:
                            checkRight(cam);
                            checkBottom(cam);
                            checkLeft(cam);
                            break;
                        case 2:
                            checkUp(cam);
                            checkLeft(cam);
                            checkBottom(cam);
                            break;
                        case 3:
                            checkLeft(cam);
                            checkUp(cam);
                            checkRight(cam);
                            break;
                    }
                    break;
                case 5:
                    checkUp(cam);
                    checkRight(cam);
                    checkBottom(cam);
                    checkLeft(cam);
                    break;

            }
        }
    }

    private static void checkLeft(Camera cam) {
        int nx = cam.x;
        while (nx >= 0) {
            if (g_board[cam.y][nx] == 6)
                break;

            if (g_board[cam.y][nx] == 0) {
                g_board[cam.y][nx] = 7;
            }

            nx--;
        }
    }

    private static void checkRight(Camera cam) {
        int nx = cam.x;
        while (nx < m) {
            if (g_board[cam.y][nx] == 6)
                break;

            if (g_board[cam.y][nx] == 0) {
                g_board[cam.y][nx] = 7;
            }

            nx++;
        }
    }

    private static void checkUp(Camera cam) {
        int ny = cam.y;
        while (ny >= 0) {
            if (g_board[ny][cam.x] == 6)
                break;

            if (g_board[ny][cam.x] == 0) {
                g_board[ny][cam.x] = 7;
            }

            ny--;
        }
    }

    private static void checkBottom(Camera cam) {
        int ny = cam.y;
        while (ny < n) {
            if (g_board[ny][cam.x] == 6)
                break;

            if (g_board[ny][cam.x] == 0) {
                g_board[ny][cam.x] = 7;
            }

            ny++;
        }
    }

    private static int countBlindSpot() {
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (g_board[i][j] == 0)
                    cnt++;
            }
        }

        return cnt;
    }

    static class Camera {
        int y;
        int x;

        int num;

        int d;

        public Camera(int y, int x, int num, int d) {
            this.y = y;
            this.x = x;
            this.num = num;
            this.d = d;
        }

        public void changeDirection(int d) {
            this.d = d;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            return sb
                    .append("{y: ").append(this.y)
                    .append(", x: ").append(this.x)
                    .append(", num: ").append(this.num)
                    .append("}")
                    .toString();
        }
    }
}
