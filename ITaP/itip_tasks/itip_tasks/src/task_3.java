import java.util.Arrays;
import java.util.Locale;
import java.util.HashSet;

public class task_3 {
    public static void main(String[] args) {
        System.out.println("Solutions:");
        System.out.println(solutions(1, 0, -1));//2
        System.out.println(solutions(1, 0, 0));//1
        System.out.println(solutions(1, 0, 1));//0
        System.out.println("");

        System.out.println("FindZip");
        System.out.println(findZip("all zip files are zipped"));//18
        System.out.println(findZip("all zip files are compressed"));//-1
        System.out.println("");

        System.out.println("CheckPerfect:");
        System.out.println(checkPerfect(6));//t
        System.out.println(checkPerfect(28));//t
        System.out.println(checkPerfect(496));//t
        System.out.println(checkPerfect(12));//f
        System.out.println(checkPerfect(97));//f
        System.out.println("");

        System.out.println("FlipEndChars:");
        System.out.println(flipEndChars("Cat, dog, and mouse."));//.at, dog, and mouseC
        System.out.println(flipEndChars("ada"));//Two's a pair.
        System.out.println(flipEndChars("Ada"));//adA
        System.out.println(flipEndChars("z"));//Incompatable
        System.out.println("");

        System.out.println("IsValidHexCode:");
        System.out.println(isValidHexCode("#CD5C5C"));//t
        System.out.println(isValidHexCode("#EAECEE"));//t
        System.out.println(isValidHexCode("#eaecee"));//t
        System.out.println(isValidHexCode("#CD5C58C"));//f
        System.out.println(isValidHexCode("#CD5C5Z"));//f
        System.out.println(isValidHexCode("#CD5C&C"));//f
        System.out.println(isValidHexCode("CD5C5C"));//f
        System.out.println("");

        System.out.println("Same:");
        System.out.println(same(new int[] {1,3,4,4,4}, new int[] {2,5,7})); // true
        System.out.println(same(new int[] {9,8,7,6}, new int[] {4,4,3,1})); // false
        System.out.println(same(new int[] {2}, new int[] {3,3,3,3,3}));//t
        System.out.println("");

        System.out.println("IsKaprekar:");
        System.out.println(isKaprekar(3));//f
        System.out.println(isKaprekar(5));//f
        System.out.println(isKaprekar(297));//t
        System.out.println("");

        System.out.println("longestZero:");
        System.out.println(longestZero("01100001011000"));//0000
        System.out.println(longestZero("100100100"));//00
        System.out.println(longestZero("11111"));//""
        System.out.println("");

        System.out.println("NextPrime:");
        System.out.println(nextPrime(12));//13
        System.out.println(nextPrime(24));//29
        System.out.println(nextPrime(11));//11
        System.out.println("");

        System.out.println("RightTriangle:");
        System.out.println(rightTriangle(3, 4, 5));//t
        System.out.println(rightTriangle(145, 105, 100));//t
        System.out.println(rightTriangle(70, 130, 110));//f
    }

    public static int solutions(int a, int b, int c) {
        int D = b * b - 4 * a * c;

        if (D == 0) {return 1;}

        else if(D > 0) {return 2;}

        else {return 0;}
    }

    public static int findZip(String str) {return str.indexOf("zip",str.indexOf("zip")+1);}

    public static boolean checkPerfect(int num) {
        int perf = 1;
        for (int i = 2; i < num; i++){
            if(num % i == 0) {perf += i;};
        }
        return perf == num;
    }

    public static String flipEndChars(String str) {
        char firstChar = str.charAt(0);
        char secondChar = str.charAt(str.length() - 1);

        if (str.length() < 2) {return "Incompatible.";}
        if (firstChar == secondChar) {return "Two's a pair.";}
        else{
            str = str.substring(1, str.length()-1);
            return secondChar + str + firstChar;
        }
    }

    public static boolean isValidHexCode(String str) {
        return str.matches("#[0-9A-Fa-f]{6}");
    }

    public static boolean same(int[] arr1, int[] arr2) {
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int n1 = 0;
        int n2 = 0;
        for(int i = 1; i < arr1.length; i++) {
            if(!(arr1[i] == arr1[i-1]))
                n1 += 1;
        }
        for(int i = 1; i < arr2.length; i++) {
            if(!(arr2[i] == arr2[i-1]))
                n2 += 1;
        }
        return n1 == n2;
    }

    public static boolean isKaprekar (int num) {
        int n = num * num;
        int firstHalf = 0;
        if (String.valueOf(n).length() != 1){
            firstHalf = Integer.parseInt(String.valueOf(n).substring(0, String.valueOf(n).length()/2));
        }
        int secondHalf = Integer.parseInt(String.valueOf(n).substring(String.valueOf(n).length()/2));

        return firstHalf + secondHalf == num;
    }

    public static String longestZero(String str) {
        String line = "";
        String maxLen = "";
        for(int i = 0; i < str.length(); i ++) {
            if (str.charAt(i) == '0') {
                line += '0';
            }
            else{
                if (line.length() > maxLen.length()) {
                    maxLen = line;
                }
                line = "";
            }
        }
        return maxLen;
    }

    public static int nextPrime (int n) {
        while (true) {
            boolean check = true;
            if (n % 2 == 0){
                n++;
                continue;
            }
            for (int i = 3; i < n/2; i++) {
                if (n % i == 0) {
                    check = false;
                    break;
                }
            }
            if (check) {return n;}
            n++;
        }
    }
    public static boolean rightTriangle (int a, int b, int c) {
        return a * a + b * b == c * c || a * a + c * c == b * b || b * b + c * c == a * a;
    }
}
