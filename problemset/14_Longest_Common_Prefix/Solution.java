class Solution {

    public String longestCommonPrefix(String[] strs) {

        if (strs.length == 0)
            return "";

        StringBuilder result = new StringBuilder();

        int index = 0;
        while (true) {
            if (isMatch(strs, index)) {
                result.append(strs[0].charAt(index));
            } else {
                break;
            }
            ++index;
        }

        return result.toString();
    }

    // check index position of every string with same chatacter
    private boolean isMatch(String[] strs, int index) {

        try {
            char c = strs[0].charAt(index);
            for (int i = 1; i < strs.length; ++i) {
                if (strs[i].charAt(index) != c) {
                    return false;
                }
            }
        } catch (StringIndexOutOfBoundsException ex) {
            return false;
        }

        return true;
    }
}
