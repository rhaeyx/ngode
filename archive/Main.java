import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String s = input.next();

        int k = -1;
        int l = -1;
        int obstacles = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'K') {
                k = i;
            }

            if (s.charAt(i) == 'L') {
                l = i;
            }
        }

        if ((l < k) || (l < 0) || (k < 0)) {
            System.out.println("NOT FOUND");
        } else {
            System.out.println(l - k - 1);
        }
    }
}