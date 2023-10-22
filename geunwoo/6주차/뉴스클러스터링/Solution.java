import java.util.*;

class Solution {
    static int set1Size = 0;
    static int set2Size = 0;

    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        HashMap<String, Integer> str1Set = makeSet(str1);
        HashMap<String, Integer> str2Set = makeSet(str2);

        set1Size = str1Set.size();
        set2Size = str2Set.size();

        HashMap<String, Integer> intersact = makeIntersaction(str1Set, str2Set);
        HashMap<String, Integer> union = makeUnion(str1Set, str2Set);

        int intersactSize = getMapSize(intersact);
        int unionSize = getMapSize(union);

        int j = 0;
        if (intersactSize == 0 && unionSize == 0) {
            j = 65536;
        } else {
            j = (int) (65536 * ((float) intersactSize / (float) unionSize));
        }

        return j;
    }

    private HashMap<String, Integer> makeSet(String s) {
        HashMap<String, Integer> set = new HashMap<>();

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) < 'a' || s.charAt(i) > 'z')
                continue;
            if (s.charAt(i + 1) < 'a' || s.charAt(i + 1) > 'z')
                continue;

            StringBuilder sb = new StringBuilder();
            String e = sb.append(s.charAt(i)).append(s.charAt(i + 1)).toString();

            if (set.getOrDefault(e, 0) == 0) {
                set.put(e, 0);
            }
            set.put(e, set.get(e) + 1);
        }

        return set;
    }

    private HashMap<String, Integer> makeIntersaction(HashMap<String, Integer> set1, HashMap<String, Integer> set2) {
        HashMap<String, Integer> intersact = new HashMap<>();

        for (String key : set1.keySet()) {
            if (set2.getOrDefault(key, 0) > 0) {
                intersact.put(key, Math.min(set1.get(key), set2.get(key)));
            }
        }

        return intersact;
    }

    private HashMap<String, Integer> makeUnion(HashMap<String, Integer> set1, HashMap<String, Integer> set2) {
        HashMap<String, Integer> union = new HashMap<>();

        for (String key : set1.keySet()) {
            union.put(key, set1.get(key));
        }

        for (String key : set2.keySet()) {
            union.put(key, Math.max(set2.get(key), set1.getOrDefault(key, 0)));
        }

        return union;
    }

    private int getMapSize(HashMap<String, Integer> map) {
        int cnt = 0;

        for (String key : map.keySet()) {
            cnt += map.get(key);
        }

        return cnt;
    }
}