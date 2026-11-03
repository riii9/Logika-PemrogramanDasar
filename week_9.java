import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class week_9 {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner input = new Scanner(System.in);

        // soal no 1==================================================================
        List<String> dataList = new ArrayList<>(Arrays.asList("ayam", "sapi", "kodok", "bebek"));

        System.out.println("sebelum di tukar " + dataList);
        
        
        String temp = dataList.get(0);
        dataList.set(0, dataList.get(3));
        dataList.set(3, temp);

        System.out.println("setelah di tukar " + dataList);
        System.out.println();

        // ## soal No 2================================================================
        System.out.print("masukan boolean A (true/false): ");
        boolean boolA = Boolean.parseBoolean(input.nextLine().trim().toLowerCase());
        System.out.print("masukan boolean B (true/false): ");
        boolean boolB = Boolean.parseBoolean(input.nextLine().trim().toLowerCase());
        System.out.print("masukan boolean C (true/false): ");
        boolean boolC = Boolean.parseBoolean(input.nextLine().trim().toLowerCase());

        System.out.println();
        System.out.println("===================================");

        // Operator logika di Java: && (AND), || (OR), ! (NOT)
        System.out.println("A.  boolA & boolB & boolC = " + (boolA && boolB && boolC));
        System.out.println("B.  boolA & boolB OR boolC = " + (boolA && boolB || boolC));
        System.out.println("C.  boolA OR boolB OR boolC = " + (boolA || boolB || boolC));
        System.out.println("D.  boolA & boolB OR (NOT boolC)= " + (boolA && boolB || (!boolC)));
        System.out.println();

        // # soal no 3================================================================================

        int x = 2;
        int y = 3;
        int[][] dataMatriks = new int[x][y];


        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                dataMatriks[i][j] = random.nextInt(10) + 1;
            }
        }

        System.out.println("======matriks sebelum ditukar=========");
        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                System.out.print(dataMatriks[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();
        System.out.println("=======matriks setelah ditukar==========");
        System.out.println();

        int tempMatrix = dataMatriks[1][1];
        dataMatriks[1][1] = dataMatriks[0][2];
        dataMatriks[0][2] = tempMatrix;

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                System.out.print(dataMatriks[i][j] + " ");
            }
            System.out.println();
        }

        input.close();
    }
}