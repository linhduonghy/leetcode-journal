
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {

        List<Integer> result = new ArrayList<>();
        
        if (p.length() > s.length()) {
            return result;
        }
        int[] countP = countCharacter(p);
        int[] countS = countCharacter(s.substring(0, p.length()));



        if (matchs(countS, countP)) {
            result.add(0);
        }

        for (int i = p.length(); i < s.length(); ++i) {
            countS[s.charAt(i - p.length()) - 'a'] -= 1;
            countS[s.charAt(i) - 'a'] += 1;
            if (matchs(countS, countP)) {
                result.add(i - p.length() + 1);
            }
        }
        return result;
    }

    private static int[] countCharacter(String s) {
        int[] count = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            count[s.charAt(i) - 'a'] += 1;
        }
        return count;
    }
    private boolean matchs(int[] count1, int[] count2) {
        for (int i = 0; i < 26; ++i)
            if (count1[i] != count2[i]) 
                return false;
        return true;
    }
}