import java.util.*;

class B_Light_It_Up {
    public static void main(String[] args) throws java.lang.Exception {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt();
        int[] a = new int[k];
        for (int i = 0; i < k; i++) a[i] = in.nextInt();
        int[][] p = new int[n][2];
        for (int i = 0; i < n; i++) {
            p[i][0] = in.nextInt();
            p[i][1] = in.nextInt();
        }
        double min = 0;
        for (int i = 0; i < n; i++) {
            double d = dist(p[i], p[a[0] - 1]);
            for (int j = 1; j < k; j++) {
                d = Math.min(d, dist(p[i], p[a[j] - 1]));
            }
            min = Math.max(min, d);
        }
        System.out.println(min);
    }
    public static double dist(int[] p1, int[] p2) {
        double x = p1[0] - p2[0], y = p1[1] - p2[1];
        return Math.sqrt(x * x + y * y);
    }
}