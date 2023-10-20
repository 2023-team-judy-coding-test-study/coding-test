import java.util.*;

class Solution {
    static char[] dy = new char[] { 0, 0, 1, 1 };
    static char[] dx = new char[] { 0, 1, 0, 1 };

    static char[][] board;
    static int[][] visited;
    static ArrayList<Node> nodes = new ArrayList<Node>();

    static int sumCnt = 0;

    public int solution(int m, int n, String[] brd) {
        initBoard(m, n, brd);
        boolean checked = true;
        while (checked == true) {
            checked = removeBlock(m, n);
            arrangeBlock(m, n);
        }

        return sumCnt;
    }

    private void initBoard(int m, int n, String[] brd) {
        board = new char[m][n];

        for (int i = 0; i < m; i++) {
            char[] rowCharList = brd[i].toCharArray();
            board[i] = rowCharList;
        }
    }

    private boolean removeBlock(int m, int n) {
        boolean check = false;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (hasBlock(m, n, i, j)) {
                    check = true;
                    checkBlock(m, n, i, j);
                }
            }
        }

        for (Node node : nodes) {
            if (board[node.y][node.x] != '*') {
                board[node.y][node.x] = '*';
                sumCnt++;
            }
        }

        nodes = new ArrayList<Node>();

        return check;
    }

    private boolean hasBlock(int m, int n, int y, int x) {
        int cnt = 0;

        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny < 0 || nx < 0 || ny >= m || nx >= n)
                continue;

            if (board[ny][nx] == '*')
                continue;

            if (board[ny][nx] == board[y][x])
                cnt++;
        }

        if (cnt == 4)
            return true;

        return false;
    }

    private void checkBlock(int m, int n, int y, int x) {
        for (int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (ny < 0 || nx < 0 || ny >= m || nx >= n)
                continue;

            if (board[ny][nx] == '*')
                continue;

            nodes.add(new Node(ny, nx));
        }
    }

    private void arrangeBlock(int m, int n) {
        // bubble sort
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m - 1; j++) {
                for (int k = 0; k < m - 1; k++) {
                    if (board[k][i] != '*' && board[k + 1][i] == '*') {
                        char temp = board[k][i];
                        board[k][i] = board[k + 1][i];
                        board[k + 1][i] = temp;
                    }
                }
            }
        }
    }
}

class Node {
    public int y;
    public int x;

    public Node(int y, int x) {
        this.y = y;
        this.x = x;
    }
}