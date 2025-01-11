import java.util.ArrayList;

public class task_4 {
    public static void main(String[] args) {
        System.out.println(essay(10,7, "hello my name is Bessie and this is my essay"));
        System.out.println();

        System.out.println(split("()()()"));// [(), (), ()]
        System.out.println(split("((()))")); // [((()))]
        System.out.println(split("((()))(())()()(()())")); // [((()))), (()), (), (), (()())]
        System.out.println(split("((())())(()(()()))"));// [((())()), (()(()()))]
        System.out.println();

        System.out.println(toCamelCase("hello_edabit"));// helloEdabit
        System.out.println(toSnakeCase("helloEdabit")); // hello_edabit
        System.out.println(toCamelCase("is_modal_open")); // isModalOpen
        System.out.println(toSnakeCase("getColor")); // get_color
        System.out.println();

        System.out.println(overTime(new double[] {9, 17, 30, 1.5}));// #240.00
        System.out.println(overTime(new double[] {16, 18, 30, 1.8}));// $84.00
        System.out.println(overTime(new double[] {13.25, 15, 30, 1.5})); // $52.50
        System.out.println();

        System.out.println(BMI("205 pounds", "73 inches"));// "27.0 Overweight"
        System.out.println(BMI("55 kilos", "1.65 meters"));// "20.2 Normal weight"
        System.out.println(BMI("154 pounds", "2 meters"));// "17.5 Underweight"
        System.out.println();

        System.out.println(bugger(39));// 3
        System.out.println(bugger(999));// 4
        System.out.println(bugger(4));// 0
        System.out.println();

        System.out.println(toStarShorthand("abbccc"));// ab*2c*3
        System.out.println(toStarShorthand("77777geff")); // 7*5gef*2
        System.out.println(toStarShorthand("")); // ""
        System.out.println();

        System.out.println(doesRhyme("Sam I am!", "Green eggs and ham."));// true
        System.out.println(doesRhyme("Sam I am!", "Green eggs and HAM."));// true
        System.out.println(doesRhyme("You are off to the races", "a splendid day.")); // false
        System.out.println();

        System.out.println(trouble(451999277, 1177722899)); // true
        System.out.println(trouble(1222345, 12345));// false
        System.out.println(trouble(666789, 12345667));// true
        System.out.println(trouble(33789, 12345337));// false
        System.out.println();

        System.out.println(countUniqueBooks("AZYWABBCATTTA", 'A'));// 4
        System.out.println(countUniqueBooks("$AA$BBCATT$C$$B$", '$')); // 3
        System.out.println(countUniqueBooks("ZZABCDEF", 'Z'));// 0
    }
    public static String essay(int n, int k, String text) {
        StringBuilder res = new StringBuilder();
        int i = 0;
        for(String str : text.split(" ")) {
            if(str.length() > k)
                return "Some word is too long";
            else if(i != 0 && i + str.length() <= k) {
                res.append(" ");
                i += str.length();
            }
            else {
                if(i != 0)
                    res.append("\n");
                i = str.length();
            }
            res.append(str);
        }
        return res.toString();
    }

    public static String split(String str) {
        int a = 0, b = 0, start = 0;
        String res = "";
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) == '(')
                a += 1;
            if(str.charAt(i) == ')') {
                b += 1;
                if(a == b) {
                    res += (str.substring(start, i+1)) + ", ";
                    start = i+1;
                }
            }
        }
        return res.toString();
    }

    public static String toCamelCase(String text) {
        StringBuilder str = new StringBuilder();
        for(int i = 0; i < text.length(); i++) {
            if(text.charAt(i) == '_') {
                str.append(Character.toUpperCase(text.charAt(i + 1)));
                i += 1;
            }
            else
                str.append(text.charAt(i));
        }
        return str.toString();
    }

    public static String toSnakeCase(String text) {
        StringBuilder str = new StringBuilder();
        for(int i = 0; i < text.length(); i++) {
            if(Character.isUpperCase(text.charAt(i))) {
                str.append("_" + Character.toLowerCase(text.charAt(i)));
            }
            else
                str.append(text.charAt(i));
        }
        return str.toString();
    }

    public static String overTime(double[] array) {
        StringBuilder str = new StringBuilder("$");
        double pay;
        if(array[1] <= 17.0)
            pay = (array[1] - array[0]) * array[2];
        else
            pay = (17 - array[0]) * array[2] + (array[1] - 17) * array[2] * array[3];
        str.append(String.format("%.2f", pay));
        return str.toString();
    }

    public static String BMI(String weight, String height) {
        String[] weightArr = weight.split(" ");
        String[] heightArr = height.split(" ");
        double numWeight = Integer.parseInt(weightArr[0]);
        double numHeight = Double.parseDouble(heightArr[0]);
        double BMI;
        String index;
        if(weightArr[1].matches("kilos")) {
            if(heightArr[1].matches("meters"))
                BMI = numWeight / (numHeight * numHeight);
            else
                BMI = numWeight / ((numHeight / 39.37) * (numHeight / 39.37));
        }
        else {
            numWeight = numWeight / 2.205;
            if(heightArr[1].matches("meters"))
                BMI = numWeight / (numHeight * numHeight);
            else
                BMI = numWeight / ((numHeight / 39.37) * (numHeight / 39.37));
        }
        if(BMI < 18.5)
            index = "Under";
        else if(BMI >= 18.5 && BMI <= 24.9)
            index = "Normal ";
        else
            index = "Over";
        return String.format("%.1f", BMI) + " " + index + "weight";
    }

    public static int bugger(int number) {
        int count = 0, newNumber = 1;
        StringBuilder strNumber = new StringBuilder(Integer.toString(number));
        while(strNumber.length() > 1) {
            for(int i = 0; i < strNumber.length(); i++) {
                newNumber *= Character.getNumericValue(strNumber.charAt(i));
            }
            strNumber.setLength(0);
            strNumber.append(newNumber);
            newNumber = 1;
            count ++;
        }
        return count;
    }

    public static String toStarShorthand(String str) {
        if(str.length() == 0)
            return "";
        StringBuilder res = new StringBuilder();
        for(int i = 0; i < str.length(); i++) {
            int j = i, count = 1;
            while(str.length()-1 > j && str.charAt(i) == str.charAt(j+1)) {
                j++;
                count++;
            }
            i = j;
            res.append(str.charAt(i));
            if(count != 1) {
                res.append("*" + count);
            }
        }
        return res.toString();
    }

    public static boolean doesRhyme(String str1, String str2) {
        char[] vowels = new char[] {'a','e','i','o','u','y'};
        StringBuilder vowels1 = new StringBuilder();
        StringBuilder vowels2 = new StringBuilder();
        for(int i = str1.lastIndexOf(" ") + 1; i < str1.length(); i++) {
            for(int j = 0; j < vowels.length; j++) {
                if (Character.toLowerCase(str1.charAt(i)) == vowels[j])
                    vowels1.append(Character.toLowerCase(str1.charAt(i)));
            }
        }
        for(int i = str2.lastIndexOf(" ") + 1; i < str2.length(); i++) {
            for (int j = 0; j < vowels.length; j++) {
                if (Character.toLowerCase(str2.charAt(i)) == vowels[j])
                    vowels2.append(Character.toLowerCase(str2.charAt(i)));
            }
        }
        return vowels1.compareTo(vowels2) == 0;
    }

    public static boolean trouble(int num1, int num2) {
        String strNum1 = Integer.toString(num1);
        String strNum2 = Integer.toString(num2);
        for(int i = 2; i < strNum1.length(); i++) {
            if(strNum1.charAt(i) == strNum1.charAt(i-1) && strNum1.charAt(i) == strNum1.charAt(i-2)) {
                int repeatable = strNum1.charAt(i);
                for (int n = 1; n < strNum2.length(); n++) {
                    if (repeatable == strNum2.charAt(n) && repeatable == strNum2.charAt(n-1))
                        return true;
                }
            }
        }
        return false;
    }

    public static int countUniqueBooks(String stringSequence, char bookEnd) {
        ArrayList<Character> unique = new ArrayList<>();
        int count = 0;
        boolean countEnd = false;
        for(int i = 0; i < stringSequence.length(); i++) {
            if(stringSequence.charAt(i) == bookEnd) {
                countEnd = !countEnd;
            }
            if(countEnd) {
                if(!unique.contains(stringSequence.charAt(i))) {
                    unique.add(stringSequence.charAt(i));
                    count++;
                }
            }
        }
        return --count;
    }
}