import java.util.ArrayList;
import java.util.Arrays;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

public class task_5 {
    public static void main(String[] args) throws NoSuchAlgorithmException {

        System.out.println(encrypt("Hello"));
        System.out.println(encrypt("Sunshine"));
        System.out.println(decrypt(new int[] {72, 33, -73, 84, -12, -3, 13, -13, -68}));
        System.out.println();

        System.out.println(canMove("Rook", "A8", "H8"));
        System.out.println(canMove("Bishop", "A7", "G1"));
        System.out.println(canMove("Queen", "C4", "D6"));
        System.out.println();

        System.out.println(canComplete("butl", "beautiful"));
        System.out.println(canComplete("butlz", "beautiful"));
        System.out.println(canComplete("tulb", "beautiful"));
        System.out.println(canComplete("bbutl", "beautiful"));
        System.out.println();

        System.out.println(sumDigProd("16, 28"));
        System.out.println(sumDigProd("0"));
        System.out.println(sumDigProd("1, 2, 3, 4, 5, 6"));
        System.out.println();

        System.out.println(sameVowelGroup(new String[] {"toe", "ocelot", "maniac"}));
        System.out.println(sameVowelGroup(new String[] {"many", "carriage", "emit", "apricot", "animal"}));
        System.out.println(sameVowelGroup(new String[] {"hoops", "chuff", "bot", "bottom"}));
        System.out.println();

        System.out.println(validateCard("1234567890123456"));
        System.out.println(validateCard("1234567890123452"));
        System.out.println();

        System.out.println(nameToEng(0));
        System.out.println(nameToEng(18));
        System.out.println(nameToEng(126));
        System.out.println(nameToEng(909));
        System.out.println();

        System.out.println(getSHA256Hash("password123"));
        System.out.println(getSHA256Hash("Fluffy@home"));
        System.out.println(getSHA256Hash("Hey dude!"));
        System.out.println();

        System.out.println(correctTitle("jOn SnoW, kINg IN thE noRth."));
        System.out.println(correctTitle("sansa stark, lady of winterfell."));
        System.out.println(correctTitle("TYRION LANNISTER, HAND OF THE QUEEN."));
        System.out.println();

        System.out.println(hexLattice(1));
        System.out.println(hexLattice(7));
        System.out.println(hexLattice(19));
        System.out.println(hexLattice(21));
    }
    public static String encrypt (String str) {
        int[] msg = new int[str.length()];
        msg[0] = str.charAt(0);
        int currentNum = str.charAt(0);
        for (int i = 1; i < str.length(); i++) {
            msg[i] = str.charAt(i) - currentNum;
            currentNum = str.charAt(i);
        }
        return Arrays.toString(msg);
    }

    public static StringBuilder decrypt (int[] n) {
        StringBuilder str = new StringBuilder();
        int currentNum = n[0];
        char letter = (char) currentNum;
        str.append(letter);
        for (int i = 1; i < n.length; i++) {
            letter = (char) (currentNum + n[i]);
            str.append(letter);
            currentNum += n[i];
        }
        return str;
    }

    public static boolean canMove (String figure, String start, String finish) {
        if (figure.equals("Pawn")) {
            if (start.charAt(0) == finish.charAt(0)) {
                if (start.charAt(1) == '2' | start.charAt(1) == '7') {
                    return Math.abs(finish.charAt(1) - start.charAt(1)) == 1 | Math.abs(finish.charAt(1) - start.charAt(1)) == 2;
                }
                else{
                    return Math.abs(finish.charAt(1) - start.charAt(1)) == 1;
                }
            }
        }
        if (figure.equals("Knight")) {
            return (Math.abs(start.charAt(0) - finish.charAt(0)) == 2 & Math.abs(start.charAt(1) - finish.charAt(1))
                    == 1) |  (Math.abs(start.charAt(0) - finish.charAt(0)) == 1 &
                    Math.abs(start.charAt(1) - finish.charAt(1)) == 2);
        }
        if (figure.equals("Rook")) {
            return start.charAt(0) == finish.charAt(0) | start.charAt(1) == finish.charAt(1);
        }
        if (figure.equals("Bishop")) {
            return Math.abs(start.charAt(0) - finish.charAt(0)) == Math.abs(start.charAt(1) - finish.charAt(1));
        }
        if (figure.equals("Queen")) {
            return start.charAt(0) == finish.charAt(0) | start.charAt(1) == finish.charAt(1) | (Math.abs(start.charAt(0) - finish.charAt(0)) == Math.abs(start.charAt(1) - finish.charAt(1)));
        }
        if (figure.equals("King")) {
            return Math.abs(start.charAt(0) - finish.charAt(0)) <= 1 & Math.abs(start.charAt(1) - finish.charAt(1)) <= 1;
        }
        return false;
    }
    public static boolean canComplete(String word, String full_word){
        int previous_index = -1;
        int counter = 0;

        for (int i = 0; i < word.length(); i++) {
            boolean is_found = false;
            for (int j = previous_index+1; j < full_word.length(); j++) {
                if ((word.charAt(i) == full_word.charAt(j)) & (!is_found)) {

                    counter += 1;

                    previous_index = j;
                    is_found = true;
                }
            }
        }

        return word.length() == counter;
    }

    public static String sumDigProd (String str) {
        String[] digits = str.split(", ");
        int sum = 0;

        for (int i = 0; i < digits.length; i++) {
            sum += Integer.parseInt(digits[i]);
        }
        str = String.valueOf(sum);

        while (str.length() != 1) {
            sum = 1;
            for (int i = 0; i < str.length(); i++) {
                sum *= str.charAt(i) - 48;
            }
            str = String.valueOf(sum);
        }
        return str;
    }
    public static StringBuilder sameVowelGroup (String[] words) {
        ArrayList<Character> firstWordsVowels = wordsVowels(words[0]);
        StringBuilder res = new StringBuilder();
        res.append(words[0]);
        res.append(", ");
        ArrayList<Character> currentWord;
        boolean check;

        for (int i = 1; i < words.length; i ++) {
            currentWord = wordsVowels(words[i]);
            check = false;
            for (int j = 0; j < currentWord.size(); j++) {
                if (!(firstWordsVowels.contains(currentWord.get(j)))) {
                    check = true;
                    break;
                }
            }
            if (!(check)) {
                res.append(words[i]);
                res.append(", ");
            }
        }
        return res;
    }

    public static ArrayList<Character> wordsVowels (String word) {
        ArrayList<Character> vowels = new ArrayList<>();
        vowels.add('e');
        vowels.add('u');
        vowels.add('i');
        vowels.add('o');
        vowels.add('a');
        vowels.add('y');

        ArrayList<Character> wordsVowels = new ArrayList<>();
        for(int i = 0; i < word.length(); i++) {
            if(vowels.contains(word.charAt(i)) & !(wordsVowels.contains(word.charAt(i)))) {
                wordsVowels.add(word.charAt(i));
            }
        }
        return wordsVowels;
    }

    public static boolean validateCard (String num) {
        int checkDig = num.charAt(num.length() - 1) - 48;
        StringBuilder str = new StringBuilder(num);
        str.deleteCharAt(str.length()-1);
        str.reverse();
        StringBuilder doubled = new StringBuilder();
        int sum = 0;
        int curNum;

        for (int i = 0; i < str.length(); i++) {
            curNum = i + 1;
            if (curNum % 2 == 1) {
                curNum *= 2;
                doubled.append(curNum);
                if (doubled.length() != 1) {
                    curNum = (doubled.charAt(0) - 48) + (doubled.charAt(1) - 48);
                }
                sum += curNum;
                doubled.setLength(0);
            }
            else {sum += str.charAt(i) - 48;}
        }
        return 10 - sum % 10 == checkDig;
    }

    public static String nameToEng (int num) {
        int units = num % 10;
        int dozens = (num % 100 - units) / 10;
        int hundreds = (num - dozens - units) / 100;
        String answer = "";
        String[] digit_words = new String[]{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] dozens_words = new String[]{"-", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                "eighty", "ninety"};
        String[] dozens_sp20 = new String[]{"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                "seventeen", "eighteen", "nineteen"};

        if (num == 0) return "zero";

        if (hundreds > 0) {
            answer += digit_words[hundreds];
            answer += " hundred ";
        }

        if (dozens > 1) {
            answer += dozens_words[dozens] + " ";
            if (units > 0) {
                answer += digit_words[units];
            }
        } else if (dozens > 0) {
            answer += dozens_sp20[units];
        } else {
            answer += digit_words[units];
        }
        return answer;
    }
    public static String getSHA256Hash(String str) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(str.getBytes(StandardCharsets.UTF_8));
        final StringBuilder hexString = new StringBuilder();
        for (int i = 0; i < hash.length; i++) {
            final String hex = Integer.toHexString(0xff & hash[i]);
            if(hex.length() == 1)
                hexString.append('0');
            hexString.append(hex);
        }
        return hexString.toString();
    }

    public static StringBuilder correctTitle(String str) {
        str = str.toLowerCase();
        String[] words = str.split(" ");
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < words.length; i++) {
            if ((!words[i].equals("and")) && (!words[i].equals("the")) && (!words[i].equals("of")) && (!words[i].equals("in"))) {
                words[i] = words[i].substring(0, 1).toUpperCase() + words[i].substring(1);
            }
        }
        for (int i = 0; i < words.length; i++) {
            answer.append(words[i]).append(" ");
        }
        return answer;
    }

    public static String hexLattice(int number) {
        if (number == 1) {
            return "o";
        }
        int i = 0;
        int value = 1;
        while (value != number) {
            value += 6 + i * 6;
            if (value > number) {
                return "Invalid";
            }
            i++;
        }
        int max = 2 * i + 3;
        int min = i + 2;
        int string_length = max * 2 - 1;
        StringBuilder answer = new StringBuilder();
        for (int j = min; j <= max; j++) {
            StringBuilder blank = new StringBuilder();
            for (int k = 1; k <= (string_length - (2 * j - 1))/2; k++) {
                blank.append(" ");
            }
            answer.append(blank);
            for (int k = 1; k <= j; k++) {
                answer.append("o ");
            }
            if (blank.length() > 1) {
                answer.append(blank.substring(0, blank.length() - 1));
            }
            answer.append("\n");
        }

        for (int j = max-1; j >= min; j--) {
            StringBuilder blank = new StringBuilder();
            for (int k = 1; k <= (string_length - (2 * j - 1))/2; k++) {
                blank.append(" ");
            }
            answer.append(blank);
            for (int k = 1; k <= j; k++) {
                answer.append("o ");
            }
            if (blank.length() > 1) {
                answer.append(blank.substring(0, blank.length() - 1));
            }
            answer.append("\n");
        }
        return answer.substring(0);
    }

}
