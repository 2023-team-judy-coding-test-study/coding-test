import java.util.*;


class Solution {
    public String[] solution(String[] orders, int[] courses) {
        List<String> result = new ArrayList<>();
        
        for (int course : courses) {
            Map<String, Integer> countMap = new HashMap<>();
            int maxCount = 0;

            for (String order : orders) {
                if (order.length() < course) continue;
                
                List<String> combinations = new ArrayList<>();
                combination(order, 0, "", course, combinations);

                for (String combo : combinations) {
                    countMap.put(combo, countMap.getOrDefault(combo, 0) + 1);
                    maxCount = Math.max(maxCount, countMap.get(combo));
                }
            }

            for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
                if (entry.getValue() == maxCount && maxCount > 1) {
                    result.add(entry.getKey());
                }
            }
        }
        
        Collections.sort(result);
        return result.toArray(new String[0]);
    }

    private void combination(String order, int start, String current, int course, List<String> combinations) {
        if (current.length() == course) {
            char[] chars = current.toCharArray();
            Arrays.sort(chars);
            combinations.add(new String(chars));
            return;
        }

        for (int i = start; i < order.length(); i++) {
            combination(order, i + 1, current + order.charAt(i), course, combinations);
        }
    }
}
