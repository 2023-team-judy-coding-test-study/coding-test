import java.util.*;

class Solution {
    public String[] solution(String[] files) {

        ArrayList<Word> wordList = new ArrayList<>();

        for (String file : files) {
            Word word = Word.from(file);

            wordList.add(word);
        }
        wordList.sort(Comparator.comparing(Word::getHead).thenComparing(Word::getNumber));

        String[] answer = wordList.stream()
                .map(Word::getOrigin)
                .toArray(String[]::new);
        return answer;
    }
}

class Word {
    public String origin;
    public String head;
    public String number;

    public Word(String origin, String head, String number) {
        this.origin = origin;
        this.head = head.toLowerCase();
        this.number = number;
    }

    public String getHead() {
        return this.head.toLowerCase();
    }

    public int getNumber() {
        return Integer.parseInt(this.number);
    }

    public String getOrigin() {
        return this.origin;
    }

    public static Word from(String file) {
        String head = "";
        String number = "";

        int s = 0;
        int e = 0;
        int idx = 0;
        for (int i = 0; i < file.length(); i++) {
            char c = file.charAt(i);

            if (idx == 0 && !Character.isDigit(c)) {
                head += c;
            }

            if (idx == 0 && Character.isDigit(c)) {
                idx++;
            }

            if (idx == 1 && Character.isDigit(c)) {
                number += c;
            }

            if (idx == 1 && !Character.isDigit(c)) {
                break;
            }
        }

        return new Word(file, head, number);
    }
}