import java.util.Arrays;

public class task_2 {
    public static void main(String[] args){
        System.out.println("Repeat:");
        System.out.println(repeat("mice", 5)); //mmmmmiiiiiccccceeeee
        System.out.println(repeat("hello", 3)); //hhheeellllllooo
        System.out.println(repeat("stop", 1)); //stop
        System.out.println("");

        System.out.println("differenceMaxMin:");
        System.out.println(differenceMaxMin(new int[] {10, 4, 1, 4, -10, -50, 32, 21})); //82
        System.out.println(differenceMaxMin(new int[] {44, 32, 86, 19})); //67
        System.out.println("");

        System.out.println("isAvgWhole:");
        System.out.println(isAvgWhole(new int[] {1, 3})); //true
        System.out.println(isAvgWhole(new int[] {1, 2, 3, 4})); //false
        System.out.println(isAvgWhole(new int[] {1, 5, 6})); //true
        System.out.println(isAvgWhole(new int[] {1, 1, 1})); //true
        System.out.println(isAvgWhole(new int[] {9, 2, 2, 5})); //false
        System.out.println("");

        System.out.println("cumulativeSum:");
        System.out.println(Arrays.toString(cumulativeSum(new int[] {1, 2, 3}))); //[1, 3, 6]
        System.out.println(Arrays.toString(cumulativeSum(new int[] {1, -2, 3}))); //[1, -1, 2]
        System.out.println(Arrays.toString(cumulativeSum(new int[] {3, 3, -2, 408, 3, 3}))); //[3, 6, 4, 412, 415, 418]
        System.out.println("");

        System.out.println("getDecimalPlaces:");
        System.out.println(getDecimalPlaces("43.20")); //2
        System.out.println(getDecimalPlaces("400")); //0
        System.out.println(getDecimalPlaces("3.1")); //1
        System.out.println("");

        System.out.println("Fibo:");
        System.out.println(Fibo(3)); //3
        System.out.println(Fibo(7)); //21
        System.out.println(Fibo(12)); //233
        System.out.println("");

        System.out.println("isValid:");
        System.out.println(isValid("59001")); //true
        System.out.println(isValid("853a7")); //false
        System.out.println(isValid("732 32")); //false
        System.out.println(isValid("393939")); //false
        System.out.println("");

        System.out.println("isStrangePair:");
        System.out.println(isStrangePair("ratio", "orator")); //true
        System.out.println(isStrangePair("sparkling", "groups")); //true
        System.out.println(isStrangePair("bush", "hubris")); //false
        System.out.println(isStrangePair("","")); //true
        System.out.println("");

        System.out.println("isPrefix:");
        System.out.println(isPrefix("automation", "auto-")); //true
        System.out.println(isPrefix("retrospect", "sub-")); //false
        System.out.println("");

        System.out.println("isSufix:");
        System.out.println(isSufix("arachnophobia", "-phobia")); //true
        System.out.println(isSufix("vocation", "-logy")); //false
        System.out.println("");

        System.out.println("boxSeq:");
        System.out.println(boxSeq(0)); //0
        System.out.println(boxSeq(1)); //3
        System.out.println(boxSeq(2)); //2
        System.out.println("");
    }

    public static String repeat(String line, int times){
        String newLine = "";
        for(int i = 0; i < line.length(); i++){
            for(int j = 0; j < times; j++){
                newLine += line.charAt(i);
            }
        }
        return newLine;
    }

    public static int differenceMaxMin(int[] arra){
        Arrays.sort(arra);
        return arra[arra.length - 1] - arra[0];
    }

    public static boolean isAvgWhole (int[] arra){
        float sum = 0;
        for(int i = 0; i < arra.length; i++) {
            sum += arra[i];
        }
        return sum % arra.length == 0;
    }

    public static int[] cumulativeSum (int[] arra){
        int sum = 0;

        for(int i = 0; i < arra.length; i++){
            arra[i] += sum;
            sum = arra[i];
        }

        return arra;
    }

    public static int getDecimalPlaces(String number){
        if(number.contains(".")){
            String[] nNumber = number.split("\\.");
            return nNumber[1].length();
        }
        else return 0;
    }

    public static int Fibo(int index){
        int[] memo = new int[index+1];
        memo[0] = 1;
        memo [1] = 1;
        //if memo[index] !=
        if(index == 0 || index == 1){
            return 1;
        }
        return Fibo(index - 2) + Fibo(index - 1);
    }

    public static boolean isValid(String postIndex){
        return postIndex.matches("[0-9]+") && postIndex.length() == 5;
    }

    public static boolean isStrangePair(String firstLine, String secondLine){
        if (firstLine.length() == 0 && secondLine.length() == 0){
            return true;
        }
        else{
            return firstLine.charAt(0) == secondLine.charAt(secondLine.length()-1) && secondLine.charAt(0) ==
                    firstLine.charAt(firstLine.length()-1);
        }
    }

    public static boolean isPrefix(String line, String prefix){
        String[] clearPrefix = prefix.split("-");
        return line.startsWith(clearPrefix[0]);
    }

    public static boolean isSufix(String line, String sufix){
        String[] clearSufix = sufix.split("-");
        return line.endsWith(clearSufix[1]);
    }

    public static int boxSeq(int steps){
        int count = 0;

        for(int i = 1; i <= steps; i++){
            if(i % 2 == 0){
                count -= 1;
            }
            else count += 3;
        }

        return count;
    }
}
