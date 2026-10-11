package _30_Substring_with_Concatenation_of_All_Words;

import java.util.*;

class Solution {

    public static void main(String[] args) {
        new Solution().findSubstring("barfoothefoobarman", new String[]{"foo", "bar"});
    }
    class WordCounter {
        int pos;
        int count;

        public WordCounter(int pos, int count) {
            this.pos = pos;
            this.count = count;
        }

        @Override
        public String toString() {
            return "WordCounter{" +
                    "pos=" + pos +
                    ", count=" + count +
                    '}';
        }
    }
    public List<Integer> findSubstring(String s, String[] words) {
        if (s.length() < words[0].length()) {
            return List.of();
        }
        Map<String, WordCounter> wordCount = new LinkedHashMap<>();
        for (int i = 0; i < words.length; i++) {
            WordCounter c = wordCount.get(words[i]);
            if (c == null) {
                wordCount.put(words[i], new WordCounter(0, 1));
            } else {
                c.count += 1;
            }
        }

        int wordLen = words[0].length();
        int concatLen = words.length * wordLen;
        int M = wordCount.size();
        int N = s.length();

        words = new String[M];
        int pos = 0;
        for (Map.Entry<String, WordCounter> entry : wordCount.entrySet()) {
            words[pos] = entry.getKey();
            entry.getValue().pos = pos;
            pos += 1;
        }

        System.out.println(Arrays.toString(words));
        System.out.println("wordCount = " + wordCount);

        String[] subString = new String[N - wordLen + 1];
        subString[0] = s.substring(0, wordLen);
        for (int i = 1; i < N - wordLen + 1; ++i) {
            subString[i] = subString[i - 1].substring(1, wordLen) + s.charAt(i + wordLen - 1);
        }

        for (int i = 0; i < subString.length; i++) {
            System.out.print(subString[i] + ", ");
        }
        System.out.println();

        int[][] sCount = new int[N][M];
        for (int i = 0; i < wordLen; ++i) {
            if (wordCount.containsKey(subString[i])) {
                sCount[i][wordCount.get(subString[i]).pos] = 1;
            }
        }
        for (int i = wordLen; i < N - wordLen + 1; ++i) {
            for (int idx = 0; idx < M; ++idx) {
                sCount[i][idx] = sCount[i - wordLen][idx];
            }
            if (wordCount.containsKey(subString[i])) {
                int idx = wordCount.get(subString[i]).pos;
                sCount[i][idx] = sCount[i - wordLen][idx] + 1;
            }
        }
        for (int i = 0; i < N - wordLen + 1; ++i) {
            for (int idx = 0; idx < M; ++idx) {
                System.out.println(i + " " + words[idx] + " " + sCount[i][idx]);
            }
        }


        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < N - concatLen + 1; ++i) {
            boolean ok = true;
            for (int idx = 0; idx < M; ++idx) {
                int prevC = 0;
                if (i - wordLen >= 0) {
                    prevC = sCount[i - wordLen][idx];
                }
                if (wordCount.get(words[idx]).count != sCount[i + concatLen - wordLen][idx] - prevC) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                result.add(i);
            }
        }

        System.out.println("result = " + result);
        return result;
    }


}