import java.util.*;

class Solution {
    public String solution(String m, String[] musicinfos) {
        m = m.replace("C#", "1");
        m = m.replace("D#", "2");
        m = m.replace("F#", "3");
        m = m.replace("G#", "4");
        m = m.replace("A#", "5");
        String answer = "(None)";
        int maxPlayTime = 0;

        for (String info : musicinfos) {
            MusicInfo musicInfo = new MusicInfo(info);
            if (musicInfo.music.contains(m) && musicInfo.playTime > maxPlayTime) {
                answer = musicInfo.name;
                maxPlayTime = musicInfo.playTime;
            }
        }

        return answer;
    }
}

class MusicInfo {
    public int playTime = 0;
    public String name;
    public String music;

    public MusicInfo(String info) {
        String[] musicInfo = info.split(",");

        // 재생 시간 구하기
        String[] start = musicInfo[0].split(":");
        String[] end = musicInfo[1].split(":");

        int startAt = Integer.valueOf(start[0]) * 60 + Integer.valueOf(start[1]);
        int endAt = Integer.valueOf(end[0]) * 60 + Integer.valueOf(end[1]);
        int playTime = endAt - startAt;

        // 이름
        String name = musicInfo[2];

        // 악보 구하기
        String sheet = musicInfo[3];
        sheet = sheet.replace("C#", "1");
        sheet = sheet.replace("D#", "2");
        sheet = sheet.replace("F#", "3");
        sheet = sheet.replace("G#", "4");
        sheet = sheet.replace("A#", "5");

        String music = "";
        int musicLen = sheet.length();
        StringBuilder sb = new StringBuilder(music);
        int i = 0;
        while (i < playTime) {
            int idx = i % musicLen;
            char interval = sheet.charAt(idx);

            sb.append(interval);
            i++;
        }
        music = sb.toString();

        this.playTime = playTime;
        this.name = name;
        this.music = music;

        System.out.println(music);
    }
}