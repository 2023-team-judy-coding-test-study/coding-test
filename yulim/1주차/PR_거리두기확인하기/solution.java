import java.util.*;

class Solution {
    class Point {
        int row, col, dist;

        Point(int row, int col, int dist) {
            this.row = row;
            this.col = col;
            this.dist = dist;
        }
    }
    int[][] D = {{1,0}, {-1,0}, {0,1}, {0,-1}};

    boolean bfs(String[] place, int row, int col) {
        boolean[][] visited = new boolean[5][5];

        Queue<Point> q = new LinkedList<>();
        visited[row][col] = true;
        q.add(new Point(row, col, 0));

        while (!q.isEmpty()) {
            Point curr = q.remove();

            if (curr.dist > 2) continue;
            if (curr.dist != 0 && place[curr.row].charAt(curr.col) == 'P') {
                return false;
            }

            for (int i = 0; i < 4; i++) {
                int newRow = curr.row + D[i][0];
                int newCol = curr.col + D[i][1];

                if (newRow < 0 || newRow > 4 || newCol < 0 || newCol > 4) continue;
                if (visited[newRow][newCol]) continue;
                if (place[newRow].charAt(newCol) == 'X') continue;
                visited[newRow][newCol] = true;
                q.add(new Point(newRow, newCol, curr.dist + 1));
            }
        }
        return true;
    }

    boolean check(String[] place) {

        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                if (place[row].charAt(col) == 'P') {
                    if (!bfs(place, row, col))
                        return false;
                }
            }
        }
        return true;
    }

    public int[] solution(String[][] places) {
        int[] answer = new int[5];

        for (int i = 0; i < 5; i++) {
            if (check(places[i])) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        return answer;
    }
}