import java.util.*;

class Solution {
    public String[] solution(String[] records) {
        HashMap<String, String> userInfo = new HashMap<>();
        ArrayList<ChatHistory> historys = new ArrayList<>();

        // 유저 정보 및 채팅 로그 저장
        for (String record : records) {
            String[] info = record.split(" ");

            String status = info[0];
            String userId = info[1];
            switch (status) {
                case "Enter":
                    userInfo.put(userId, info[2]);
                    historys.add(new ChatHistory(status, userId));

                    break;
                case "Leave":
                    historys.add(new ChatHistory(status, userId));

                    break;
                case "Change":
                    userInfo.put(userId, info[2]);
                    break;
            }
        }

        // 방문 로그 메세지 생성
        ArrayList<String> logs = new ArrayList<>();
        for (ChatHistory history : historys) {
            String nickName = userInfo.getOrDefault(history.userId, "");
            String log = nickName + "님이 ";

            if (history.status.equals("Enter")) {
                log += "들어왔습니다.";
            } else if (history.status.equals("Leave")) {
                log += "나갔습니다.";
            }

            logs.add(log);
        }

        String[] result = logs.toArray(new String[0]);

        return result;
    }
}

class ChatHistory {
    String status;
    String userId;

    public ChatHistory(String status, String userId) {
        this.status = status;
        this.userId = userId;

    }
}