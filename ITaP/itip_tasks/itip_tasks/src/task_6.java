import java.util.Arrays;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class task_6 {
    public static void main(String[] args) {
        System.out.println(bell(3));
        System.out.println();

        System.out.println(translateWord(""));
        System.out.println(translateSentence("Do you think it is going to rain today?"));
        System.out.println();

        System.out.println(validColor("rgba(0,0,0,0.123456789)"));
        System.out.println();

        System.out.println(stripUrlParams("https://edabit.com?a=1&b=2&a=2"));
        System.out.println();

        System.out.println(Arrays.toString(getHashTags("Why You Will Probably Pay More for Your Christmas Tree This Year")));
        System.out.println(Arrays.toString(getHashTags("Visualizing Science")));
        System.out.println();

        System.out.println(ulam(206));
        System.out.println();

        System.out.println(longestNonrepeatingSubstring("abcabcbb"));
        System.out.println();

        System.out.println(convertToRoman(16));
        System.out.println(convertToRoman(3616));
        System.out.println();

        System.out.println(formula("18 / 9 = 2"));
        System.out.println(formula("16 * 10 = 160 = 14 + 120"));
        System.out.println();

        System.out.println(palindromeDescendant(11211230));
    }

    public static int bell (int n) {
        int[] upperRow = new int[n];
        int[] lowerRow = new int[n];
        int num = 1;
        upperRow[0] = 1;
        for (int i = 1; i < n; i++) {
            lowerRow[0] = num;
            for (int j = 1; j < i + 1; j++) {
                lowerRow[j] = num + upperRow[j-1];
                num = lowerRow[j];
            }
            num = lowerRow[i];
            for (int j = 0; j < n; j++) {
                upperRow[j] = lowerRow[j];
            }
        }
        return num;
    }

    public static String translateWord(String word) {
        Pattern pattern = Pattern.compile("^[^aeiouyAEIOUY]+");
        Matcher matcher = pattern.matcher(word);
        if (matcher.find())
            return matcher.replaceFirst("") + matcher.group() + "ay";
        return word + "yay";
    }

    public static String translateSentence(String sentence) {
        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            words[i] = translateWord(words[i]);
        }
        return String.join(" ", words);
    }

    public static boolean validColor (String color) {
        String[] str = color.split("\\(");
        String[] numbers = str[1].split(",");
        numbers[numbers.length - 1] = numbers[numbers.length - 1].replaceAll("\\)","");
        if (str[0].equals("rgb")){
            if (numbers.length != 3) {return false;}
            for (int i = 0; i < numbers.length; i++) {
                try {
                    if (Integer.parseInt(numbers[i]) > 256 || Integer.parseInt(numbers[i]) < 0) {
                        return false;
                    }
                }
                catch (NumberFormatException e){
                    return false;
                }
            }
        }
        if (str[0].equals("rgba")){
            if (numbers.length != 4) {
                return false;
            }
            for (int i = 0; i < numbers.length - 1; i++) {
                try {
                    if (Integer.parseInt(numbers[i]) > 256 || Integer.parseInt(numbers[i]) < 0) {
                        System.out.println(numbers[i]);
                        return false;
                    }
                }
                catch (NumberFormatException e) {return false;}
            }
            try {
                if (Float.parseFloat(numbers[3]) > 1. || Float.parseFloat(numbers[3]) < 0.) {
                    return false;
                }
            }
            catch (NumberFormatException e){return false;}
        }
        return true;
    }

    public static String stripUrlParams(String s) {
        return stripUrlParams(s, new String[] { "" });
    }

    public static String stripUrlParams(String url, String[] arr) {
        if (url.contains("?")) {
            String newUrl = url.split("\\?")[0] + "?";
            String[] pArr = url.split("\\?")[1].split("\\&");
            Map<String, Integer> pMap = new HashMap<String, Integer>();
            for (var p : pArr) {
                String[] t = p.split("\\=");
                boolean skip = false;
                for (var sep: arr) {
                    if (t[0].equals(sep)) {
                        skip = true;
                        break;
                    }
                }
                if (skip) continue;
                pMap.put(t[0], Integer.parseInt(t[1]));
            }
            for (Map.Entry<String, Integer> item : pMap.entrySet()) {
                newUrl += item.getKey() + "=" + item.getValue() + "&";
            }
            newUrl = (newUrl.charAt(newUrl.length()-1) == '&') ? newUrl.substring(0, newUrl.length()-1) : newUrl;
            return newUrl;
        }
        else
            return url;
    }

    public static String getLongestWord(List<String> s) {
        String longest_word = "";
        for (String w: s) {
            if (w.length() > longest_word.length())
                longest_word = w;
        }
        return longest_word;
    }
    public static Object[] getHashTags(String s) {
        List<String> strArr = new ArrayList<String>(Arrays.asList(s.split(" ")));
        List<String> longestWords = new ArrayList<String>();
        String s1;
        int size = strArr.size();
        int i = 0;
        while (i < 3) {
            s1 = getLongestWord(strArr);
            longestWords.add("#" + s1.toLowerCase());
            strArr.remove(s1);
            i++;
            if (i == size) {break;}
        }
        return longestWords.toArray();
    }
    public static int ulam(int n){
        if (n < 1)
            return 0;
        switch (n){
            case 1:
                return 1;
            case 2:
                return 2;
            case 3:
                return 3;
        }
        int[] ulamSeq = new int[n];
        ulamSeq[0] = 1; ulamSeq[1] = 2; ulamSeq[2] = 3;
        int ulamSeqIdx = 3;
        int ulamNum = 4;
        while (ulamSeqIdx < n){
            int counter = 0;
            for (int i = 0; i < ulamSeqIdx; i++){
                for (int j = i + 1; j < ulamSeqIdx; j++){
                    if (ulamSeq[i] + ulamSeq[j] == ulamNum)
                        counter++;
                    if (counter > 1) break;
                }
            }
            if (counter == 1) {
                ulamSeq[ulamSeqIdx] = ulamNum;
                ulamSeqIdx++;
            }
            ulamNum++;
        }
        return ulamSeq[n - 1];
    }
    public static String longestNonrepeatingSubstring(String s) {
        String sequence = "";
        String answer = "";
        ArrayList<String> letters = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (letters.contains(s.charAt(i) + "")) {
                if (sequence.length() > answer.length()) {
                    answer = sequence;
                }
                sequence = "";
            } else {
                letters.add(s.charAt(i) + "");
                sequence += s.charAt(i) + "";
                if (sequence.length() > answer.length()) {
                    answer = sequence;
                }
            }
        }
        return answer;
    }
    public static String convertToRoman (int n){
        int units = n % 10;
        int dozens = (n % 100 - units) / 10;
        int hundreds = (n % 1000 - dozens - units) / 100;
        int thousands = (n % 10000 - hundreds - dozens - units) / 1000;
        String[] digit_words = new String[]{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        String[] dozens_words = new String[]{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] hundred_words = new String[]{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] thousand_words = new String[]{"", "M", "MM", "MMM"};
        return thousand_words[thousands] + hundred_words[hundreds] + dozens_words[dozens] + digit_words[units];
    }

    public static boolean formula (String form) {
        String[] str = form.split("=");
        int res = 0;
        int res2 = 0;
        String[] experssion = str[0].split(" ");
        switch (experssion[1]){
            case "+":
                res = Integer.parseInt(experssion[0]) + Integer.parseInt(experssion[2]);
                break;
            case "-":
                res = Integer.parseInt(experssion[0]) - Integer.parseInt(experssion[2]);
                break;
            case "/":
                if (experssion[2].equals("0"))
                    return false;
                res = Integer.parseInt(experssion[0]) / Integer.parseInt(experssion[2]);
                break;
            case "*":
                res = Integer.parseInt(experssion[0]) * Integer.parseInt(experssion[2]);
                break;
        }

        try{
            experssion = str[2].substring(1).split(" ");
            switch (experssion[1]){
                case "+":
                    res2 = Integer.parseInt(experssion[0]) + Integer.parseInt(experssion[2]);
                    break;
                case "-":
                    res2 = Integer.parseInt(experssion[0]) - Integer.parseInt(experssion[2]);
                    break;
                case "/":
                    if (experssion[2].equals("0"))
                        return false;
                    res2 = Integer.parseInt(experssion[0]) / Integer.parseInt(experssion[2]);
                    break;
                case "*":
                    res2 = Integer.parseInt(experssion[0]) * Integer.parseInt(experssion[2]);
                    break;
            }
            return res == res2 && res == Integer.parseInt(str[1].replaceAll(" ", ""));
        }
        catch (IndexOutOfBoundsException e){}
        return res == Integer.parseInt(str[1].replaceAll(" ", ""));
    }
    public static String getDescendant(String n) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < n.length()/2; i++) {
            int newInt = Character.getNumericValue(n.charAt(i * 2)) + Character.getNumericValue(n.charAt(i * 2 + 1));
            str.append(newInt);
        }
        return str.toString();
    }
    public static boolean isPalindrome(String str) {
        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static boolean palindromeDescendant(int n) {
        String str = Integer.toString(n);
        while (str.length() >= 2) {
            if (isPalindrome(str))
                return true;
            str = getDescendant(str);
        }
        return false;
    }
}
