public class task_1 {
    public static void main(String[] args){
        System.out.println("Remainder:");
        System.out.println(remainder(1, 3)); //1
        System.out.println(remainder(3, 4)); //3
        System.out.println(remainder(-9, 45)); //-9
        System.out.println(remainder(5, 5)); //0
        System.out.println("");

        System.out.println("Area of triangle:");
        System.out.println(triArea(3, 2)); //3
        System.out.println(triArea(7, 4)); //14
        System.out.println(triArea(10, 10)); //50
        System.out.println("");

        System.out.println("Animals' legs:");
        System.out.println(animals(2, 3, 5)); //36
        System.out.println(animals(1, 2, 3)); //22
        System.out.println(animals(5, 2, 8)); //50
        System.out.println("");

        System.out.println("Profitable Game");
        System.out.println(profitableGamble(0.2, 50, 9)); //true
        System.out.println(profitableGamble(0.9, 1, 2)); //false
        System.out.println(profitableGamble(0.9, 3, 2)); //true
        System.out.println("");

        System.out.println("Operation:");
        System.out.println(operation(24, 15, 9)); //added
        System.out.println(operation(24, 26, 2)); //subtracted
        System.out.println(operation(15, 11, 11)); //none
        System.out.println("");

        System.out.println("ASCII:");
        System.out.println(ctoa('A')); //65
        System.out.println(ctoa('m')); //109
        System.out.println(ctoa('[')); //91
        System.out.println(ctoa('\\')); //92
        System.out.println("");

        System.out.println("Add up to:");
        System.out.println(addUpTo(3)); //6
        System.out.println(addUpTo(10)); //55
        System.out.println(addUpTo(7)); //28
        System.out.println("");

        System.out.println("Triangle's next edge");
        System.out.println(nextEdge(8, 10)); //17
        System.out.println(nextEdge(5, 7)); //11
        System.out.println(nextEdge(9, 2)); //10
        System.out.println("");

        System.out.println("Sum of cubes:");
        System.out.println(sumOfCubes(new int[] {1, 5, 9})); //855
        System.out.println(sumOfCubes(new int[] {3, 4, 5})); //216
        System.out.println(sumOfCubes(new int[] {2})); //8
        System.out.println(sumOfCubes(new int[] {})); //0
        System.out.println("");

        System.out.println("ABCmath:");
        System.out.println(abcmath(42, 5, 10)); //false
        System.out.println(abcmath(5, 2, 1)); //true
        System.out.println(abcmath(1, 2, 3)); //false
        System.out.println("");
    }

    public static int remainder(int a, int b){return a % b;}

    public static double triArea(int base, int height) {return (base * height) / 2.;}

    public static int animals(int chickens, int cows, int pigs) {return chickens * 2 + cows * 4 + pigs * 4;}

    public static boolean profitableGamble(double prob, int prize, int pay) {return prob * prize - pay > 0;}

    public static String operation(int result, int a, int b) {
        if(a + b == result){
            return "added";
        }
        else if(a - b == result){
            return "substracted";
        }

        else if(a * b == result){
            return "multiplied";
        }
        else if(a / b == result){
            return "devided";
        }
        else{
            return "none";
        }
    }

    public static int ctoa(char character){
        return character;
    }

    public static int addUpTo(int a){
        int result = 0;

        for (int i = 1; i <= a; i++){
            result += i;
        }

        return result;
    }

    public static int nextEdge(int firstEgde, int secondEdge){
        return firstEgde + secondEdge - 1;
    }

    public static int sumOfCubes(int[] a){
        int sum = 0;

        for (int i = 0; i < a.length; i++){
            sum += a[i] * a[i] * a[i];
        }

        return sum;
    }

    public static boolean abcmath(int a, int b, int c){
        int sum = a;

        for(int i = 1; i <= b; i++){
            sum += sum;
        }

        return remainder(sum, c) == 0;
    }
}
