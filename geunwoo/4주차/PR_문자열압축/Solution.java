import java.util.*;

class Solution {
    public int solution(String s) {
        int sLength = s.length();
        Integer cnt = 0;
        int minSum = 1000;

        for (int i = 1; i <= sLength; i++) {
            StringBuilder sb = new StringBuilder();

            String stdChunk = "";
            String newChunk = "";
            String compactedChunk = "";
            cnt = 0;

            sb.append(compactedChunk);

            for (int j = 0; j <= sLength - i; j += i) {
                newChunk = s.substring(j, j + i);
                if (stdChunk.equals("")) {
                    stdChunk = newChunk;
                } else if (!stdChunk.equals(newChunk)) {
                    if (cnt > 1)
                        sb.append(cnt.toString());
                    sb.append(stdChunk);

                    stdChunk = newChunk;
                    cnt = 0;
                }
                cnt++;
            }

            if (cnt > 1)
                sb.append(cnt.toString());
            sb.append(stdChunk);

            compactedChunk = sb.toString();
            int compactedChunkLength = compactedChunk.length() + sLength % i;
            minSum = Math.min(minSum, compactedChunkLength);

        }

        return minSum;
    }
}