package _36_Valid_Sudoku;

import java.util.*;

class Solution {

    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Integer>> rows = new HashMap<>();
        Map<Integer, Set<Integer>> cols = new HashMap<>();
        Map<Integer, Set<String>> points = new HashMap<>();
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    continue;
                }

                int c = board[i][j] - '0';

                Set<Integer> rs = rows.getOrDefault(c, new HashSet<>());
                if (rs.contains(i)) {
                    return false;
                }
                rows.put(c, rs);

                Set<Integer> cs = cols.getOrDefault(c, new HashSet<>());
                if (cs.contains(j)) {
                    return false;
                }
                cols.put(c, cs);

                Set<String> ps = points.getOrDefault(c, new HashSet<>());
                String inbox = "" + (i/3) + (j / 3);
                if (ps.contains(inbox)) {
                    return false;
                }
                points.put(c, ps);

                rs.add(i);
                cs.add(j);
                ps.add(inbox);
            }
        }
        return true;
    }
}