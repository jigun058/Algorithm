import java.io.*;
import java.util.*;

public class Main {
  static int N, M;
  static char[][] map;
  static int[][] dp;
  static List<Integer> validMasks;

  static boolean isValid(int r, int mask) {
    for (int i = 0; i < M; i++) {
      if ((mask & (1 << i)) != 0) {
        if (map[r][i] == 'x')
          return false;

        if (i > 0 && (mask & (1 << (i-1))) != 0)
          return false;

        if (i < M - 1 && (mask & (1 << (i+1))) != 0)
          return false;
      }
    }
    
    return true;
  }

  static boolean canSit(int cur, int prev) {
    for (int i = 0; i < M; i++) {
      if ((cur & (1 << i)) != 0) {
        if (i > 0 && (prev & (1 << (i - 1))) != 0)
          return false;

        if (i < M - 1 && (prev & (1 << (i + 1))) != 0)
          return false;
      }
    }

    return true;
  }

  static int solve() {
    for (int mask = 0; mask < (1 << M); mask++) {
      if (isValid(0, mask)) {
        dp[0][mask] = Integer.bitCount(mask);
      }
    }

    for (int r = 1; r < N; r++) {
      for (int curMask = 0; curMask < (1 << M); curMask++) {
        if (!isValid(r, curMask)) continue;

        for (int prevMask = 0; prevMask < (1 << M); prevMask++) {
          if (dp[r-1][prevMask] == -1) continue;

          if (canSit(curMask, prevMask)) {
            dp[r][curMask] = Math.max(dp[r][curMask], dp[r-1][prevMask] + Integer.bitCount(curMask));
          }
        }
      }
    }

    int maxStudents = 0;
    for (int mask = 0; mask < (1 << M); mask++) {
      maxStudents = Math.max(maxStudents, dp[N-1][mask]);
    }

    return maxStudents;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());

    while (T-- > 0) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      N = Integer.parseInt(st.nextToken());
      M = Integer.parseInt(st.nextToken());

      map = new char[N][M];
      for (int i = 0; i < N; i++) {
        map[i] = br.readLine().toCharArray();
      }

      dp = new int[N][1 << M];
      for (int i = 0; i < N; i++) {
        Arrays.fill(dp[i], -1);
      }

      System.out.println(solve());
    }
  }
}