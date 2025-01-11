public class Primes{
    public static void main(String[] args){
        for (int n = 3; n < 100; n++){
            if(isPrime(n)){ //проверка на простое число
                System.out.println(n);
            }
        }
    }
    public static boolean isPrime(int n){ //проверка на простое число
        boolean check = true;
        //for(int j = 7; j < n; j++) {
        if(n % 7 != 0){
            check = false;
                //break;
            }
        //}
        return check;
    }
}
