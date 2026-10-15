package _37_Sudoku_Solver;

import java.util.*;

public class Solution {

    private boolean tryAssignNumber(List<List<Character>> board, int x, int y, int n,
                                    Map<Integer, Set<Integer>> rows,
                                    Map<Integer, Set<Integer>> cols,
                                    Map<Integer, Set<String>> points, boolean[][] visited) {

        board.get(x).set(y, (char) (n + '0'));
        visited[x][y] = true;
        rows.get(n).add(x);
        cols.get(n).add(y);
        points.get(n).add("" + (x / 3) + (y / 3));

        boolean foundEmpty = false;
        int nextI = 0, nextJ = 0;

        outer:
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board.get(i).get(j) == '.') {
                    nextI = i;
                    nextJ = j;
                    foundEmpty = true;
                    break outer;
                }
            }
        }

        if (!foundEmpty) {
            return true;
        }

        String nextBoxId = "" + (nextI / 3) + (nextJ / 3);
        for (int num = 1; num < 10; ++num) {
            if (!rows.get(num).contains(nextI) &&
                    !cols.get(num).contains(nextJ) &&
                    !points.get(num).contains(nextBoxId)) {
                if (tryAssignNumber(board, nextI, nextJ, num, rows, cols, points, visited)) {
                    return true;
                }
            }
        }


        visited[x][y] = false;
        rows.get(n).remove(x);
        cols.get(n).remove(y);
        points.get(n).remove("" + (x / 3) + (y / 3));
        board.get(x).set(y, '.');

        return false;
    }

    public void solveSudoku(char[][] board) {
        Map<Integer, Set<Integer>> rows = new HashMap<>();
        Map<Integer, Set<Integer>> cols = new HashMap<>();
        Map<Integer, Set<String>> points = new HashMap<>();

        for (int num = 1; num < 10; ++num) {
            rows.put(num, new HashSet<>());
            cols.put(num, new HashSet<>());
            points.put(num, new HashSet<>());
        }

        int startI = -1, startJ = -1;
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') {
                    if (startI == -1) {
                        startI = i;
                        startJ = j;
                    }
                    continue;
                }
                int c = board[i][j] - '0';

                rows.get(c).add(i);
                cols.get(c).add(j);
                points.get(c).add("" + (i / 3) + (j / 3));
            }
        }

        if (startI == -1) {
            return;
        }

        boolean[][] visited = new boolean[9][9];
        List<List<Character>> boardPointer = new ArrayList<>(9);

        for (char[] row : board) {
            List<Character> innerList = new ArrayList<>(9);
            for (char c : row) {
                innerList.add(c);
            }
            boardPointer.add(innerList);
        }

        String startBoxId = "" + (startI / 3) + (startJ / 3);

        for (int num = 1; num < 10; ++num) {
            if (!rows.get(num).contains(startI) &&
                    !cols.get(num).contains(startJ) &&
                    !points.get(num).contains(startBoxId)) {

                if (tryAssignNumber(boardPointer, startI, startJ, num, rows, cols, points, visited)) {
                    for (int x = 0; x < 9; x++) {
                        for (int y = 0; y < 9; y++) {
                            board[x][y] = boardPointer.get(x).get(y);
                        }
                    }
                    return;
                }
            }
        }
    }
}