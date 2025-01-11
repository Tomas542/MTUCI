public class Palindrom{
    public static void main(String[] args){
        for(int i = 0; i < args.length; i++){
            String s = args[i].toLowerCase();
            System.out.println(isPalindrome(s));
        }
    }

    public static String reverseString(String s){//создание обратного слова для проверки на палиндром
        String rev = "";
        int length = s.length();
        for (int i = length-1; i >= 0; i--){
            rev += s.charAt(i);
        }
        return rev;
    }

    public static boolean isPalindrome(String s){ //проверка на палиндром
        boolean check = true;
        if (!s.equals(reverseString(s))){
            check = false;
            System.out.println(s + " is NOT palindrome");
        }
        else if (s.equals(reverseString(s))){
            System.out.println(s + " is palindrome");
        }
        return check;
    }
}
