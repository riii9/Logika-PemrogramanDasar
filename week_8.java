import java.util.Random;
import java.util.Scanner; 


public class week_8{
    public static void main(String[] args) {

        Random random = new Random();
        Scanner input = new Scanner(System.in);

        // Soal no 1===========================================================
        // A
        System.out.println("Soal no 1");
        System.out.println("");
        System.out.println("======A. int dan int ===========");
        int a = random.nextInt(10) + 1;
        int b = random.nextInt(10) + 1;

        System.out.println("nilai a = "+ a + " dan nilai b = " + b);
        System.out.println("================================");
        System.out.println("nilai a + b = "+(a+b));
        System.out.println("nilai a - b = "+(a-b));
        System.out.println("nilai a x b = "+(a*b));
        System.out.println("nilai a / b = "+(a/b));

        // B
        System.out.println("");
        System.out.println("======B. int dan float ===========");
        a = random.nextInt(10) + 1;
        float c = random.nextFloat()*10 + 1;

        System.out.println("nilai a = "+ a + " dan nilai c = " + c);
        System.out.println("================================");
        System.out.println("nilai a + c = "+(a+c));
        System.out.println("nilai a - c = "+(a-c));
        System.out.println("nilai a x c = "+(a*c));
        System.out.println("nilai a / c = "+(a/c));


         // C
        System.out.println("");
        System.out.println("======C. int dan double ===========");
        a = random.nextInt(10) + 1;
        double d = random.nextDouble()*10+1;

        System.out.println("nilai a = "+ a + " dan nilai d = " + d);
        System.out.println("================================");
        System.out.println("nilai a + d = "+(a+d));
        System.out.println("nilai a - d = "+(a-d));
        System.out.println("nilai a x d = "+(a*d));
        System.out.println("nilai a / d = "+(a/d));

         // d
        System.out.println("");
        System.out.println("======D. float dan double ===========");
        c = random.nextFloat()*10 + 1;
        d = random.nextDouble()*10 +1;

        System.out.println("nilai c = "+ c + " dan nilai d = " + d);
        System.out.println("================================");
        System.out.println("nilai c + d = "+(c+d));
        System.out.println("nilai c - d = "+(c-d));
        System.out.println("nilai c x d = "+(c*d));
        System.out.println("nilai c / d = "+(c/d));


        // e
        System.out.println("");
        System.out.println("======E. Numerik dan String ===========");
        a = random.nextInt(10);
        String s = "hallo";

        System.out.println("nilai a = "+ a + " dan string s = " + s);
        System.out.println("================================");
        System.out.println("nilai a + s = "+(a+s));
        System.out.println("operator -, x, / tidak bisa dalam operasi ini");

        // f
        System.out.println("");
        System.out.println("======F. String dan String ===========");
        String k = "hello,";
        s = "dunia";

        System.out.println("nilai k = "+ k + " dan string s = " + s);
        System.out.println("================================");
        System.out.println("nilai k + s = "+(k+s));
        System.out.println("operator -, x, / tidak bisa dalam operasi ini");
        System.out.println("");

        // Soal no 2
        System.out.println("================================");
        System.out.println("Soal no 2");
        System.out.println("================================");
        System.out.println("");
        System.out.println("masukan jam");
        int jam = input.nextInt();
        System.out.println("masukan menit");
        int menit = input.nextInt();
        System.out.println("masukan detik");
        int detik = input.nextInt();

        System.out.printf("Waktu tercatat: %02d:%02d:%02d\n", jam, menit, detik);
        System.out.println("================================");
        System.out.println("Waktu dalam detik: "+(jam*3600+menit+60+detik));
    }
}