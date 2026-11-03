import random

while True:
    print()
    print("=========================================================")
    print("1. Soal mengecek kelipatan 3")
    print("2. Soal mengecek kelipatan 3 tapi bukan kelipatan 4")
    print("3. Soal mengeluarkan angka dalam bentuk string (0-9)")
    print("4. Soal mengeluarkan angka dalam bentuk string (0-99)")
    print("5. Soal mencari bilangan terkecil dari 4 bilangan")
    print("6. Soal Matrix")
    print("7. Keluar Program")
    print("=========================================================")
    print()
    opsi=int(input("Masukan no yg mau dimasukan: "))

    if(opsi==1):
        # Soal 1
        x = int(input("Masukan angka yg akan dicek apakah kelipatan 3: "))

        if x%3==0:
            print(f"{x} adalah kelipatan 3")
        else:
            print(f"{x} bukan kelipatan 3")

    elif(opsi==2):
        # Soal 2
        x = int(input("Masukan angka yg akan dicek apakah kelipatan 3 tetapi bukan kelipatan 4: "))

        if x%3==0:
            if x%4==0:
                print(f"{x} kelipatan 3 dan kelipatan 4")
            else:
                print(f"{x} kelipatan 3 dan bukan kelipatan 4")
        else:
            print(f"{x} bukan kelipatan 3")

    elif(opsi==3):
        # Soal 3
        angka=["nol","satu","dua","tiga","empat","lima,","enam","tujuh","delapan","sembilan"]

        x=int(input("Masukan nilai(int): "))

        if (x>=0 and x<=9):
            print(angka[x])
        else:
            print(f"Angka tidak dalam range")
    elif(opsi==4):
        # Soal 4
        angka = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan']
        x = int(input("masukan angka(0-99): "))
        if x >= 0 and x <= 9:
            print(angka[x])
        elif x == 10:
            print("sepuluh")
        elif x == 11:
            print("sebelas")
        elif x >= 12 and x <= 19:
            sisa = x % 10
            print(angka[sisa] + " belas")
        elif x >= 20 and x <= 99:
            puluhan = x // 10
            sisa = x % 10
            if sisa == 0:
                print(angka[puluhan] + " puluh")
            else:
                print(angka[puluhan] + " puluh " + angka[sisa])
        else:
            print("angka tidak dalam range")
    elif(opsi==5):
        # Soal 5
        data =[]
        for i in range(4):
            x= int(input(f"Masukan nilai ke {i+1}: "))
            data.append(x)

        data.sort()
        terkecil=data[0]
        print(f"Nilai terkecil dari {data} adalah {terkecil}")
    elif(opsi==6):
        # Soal no 6
        baris=3
        kolom=4
        matrix=[]
        for i in range(baris):
            row=[]
            for j in range(kolom):
                x=random.randint(1,10)
                row.append(x)
            matrix.append(row)
        print("==========Matrix Awal===============")
        for baris_matriks in matrix:
            print(baris_matriks)
        # A
        if(matrix[0][1]%2==0):
            print()
            print("=====================================================================================")
            print(f"Elemen ke (0,1) adalah {matrix[0][1]} bilangan genap ,ditambah 1 maka {matrix[0][1]+1}")
            print("=====================================================================================")
            matrix[0][1]+=1
            for baris_matriks in matrix:
                print(baris_matriks)
        # B
        if(matrix[1][2]%2==1):
            print("=====================================================================================")
            print(f"Elemen ke (1,2) adalah {matrix[1][2]} bilangan ganjil ,ditambah selisih elemen ke (1,2)dengan elemen ke(1,3)={abs(matrix[1][2]-matrix[1][3])}")
            print("=====================================================================================")
            matrix[1][2]+=abs(matrix[1][2]-matrix[1][3])
            for baris_matriks in matrix:
                print(baris_matriks)
        else:
            print("=====================================================================================")
            print(f"Elemen ke (1,2) adalah {matrix[1][2]} bilangan genap ,dikurangi selisih elemen ke (1,2)dengan elemen ke(1,1)={abs(matrix[1][2]-matrix[1][1])}")
            print("=====================================================================================")
            matrix[1][2]-=abs(matrix[1][2]-matrix[1][1])
            for baris_matriks in matrix:
                print(baris_matriks)
        # C
        if(matrix[0][0]<matrix[2][2]):
            print("=====================================================================================")
            print(f"elemen ke(0,0)={matrix[0][0]}<elemen ke(2,2)={matrix[2][2]}")
            print("=====================================================================================")
            matrix[0][0],matrix[2][2]=matrix[2][2],matrix[0][0]
            for baris_matriks in matrix:
                print(baris_matriks)+        
        elif(matrix[0][0]>matrix[2][2]):
            print("=====================================================================================")
            print(f"elemen ke(0,0)={matrix[0][0]}>elemen ke(2,2)={matrix[2][2]}")
            print("=====================================================================================")
            matrix[0][0],matrix[2][2]=matrix[2][2],matrix[0][0]
            for baris_matriks in matrix:
                print(baris_matriks)
            print()
        
        
        
    elif(opsi==7):
        print("Selesai!!!")
        break
    else:
        print("salah soal cuy")