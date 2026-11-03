def soal1():
    print("Soal no 1 (Kelipatan 3)")
    x = int(input("masukan bilangan: "))

    print("==========================================")
    for i in range(3, x, 3):
        print(i, end=" ")
    print("\n==========================================")

def soal2():
    total = 0
    print("Soal no 2 (Kelipatan 3 Ganjil & Totalnya)")
    x = int(input("masukan bilangan: "))
    arr=[]

    for i in range(3, x, 3):
            if (i // 2) * 2 == i - 1:
                total += i
                arr.append(str(i))
    s = "("+",".join(arr)+")"
    print("==========================================")
    print(total , s)
    print("==========================================")


def soal3():
    print("Soal no 3 (Rata-rata)")
    x = int(input("masukan banyak bilangan: "))
    total = 0

    for i in range(1, (x + 1)):
        total += int(input(f"masukan bilangan ke {i}: "))

    mean = total / x
    print("==========================================")
    print(f"rata-rata adalah {mean}")
    print("==========================================")

def soal4():
    array = []
    print("Soal no 4 (Rata-rata & Varians Array)")
    x = int(input("masukan banyak banyak elemen: "))

    total = 0
    for i in range(x):
        e = int(input(f"masukan elemen ke {i+1}: "))
        array.append(e)
        total+=e
    mean = total/x

    total1=0
    for i in array:
        total1+=pow((i-mean),2)
    
    ans = total1/x-1
    print("==========================================")
    print(array)
    print(f"Mean       : {mean}")
    print(f"variansnya : {ans}")
    print("==========================================")
        

def soal5():
    array = []
    print("Soal no 5 (Nilai Terbesar Array 1D)")
    x = int(input("masukan banyak elemen array: "))

    for i in range(x):
        array.append(int(input(f"masukan elemen ke {i+1}: ")))
    nilaiMax = max(array)

    print("==========================================")
    print(array)
    print(f"Nilai terbesar adalah {nilaiMax}")
    print("==========================================")


def soal6():
    print("Soal no 6 (Max, Min, & Selisih Array 2D)")
    baris = int(input("masukan panjang baris array: "))
    kolom = int(input("masukan panjang kolom array: "))

    array = [[0 for _ in range(kolom)] for _ in range(baris)]

    for i in range(baris):
        for j in range(kolom):
            array[i][j] = int(input(f"Masukan elemen ke [{i+1}][{j+1}] :"))

    Max = max(max(baris) for baris in array)
    Min = min(min(baris) for baris in array)
    print("==========================================")
    for baris in array:
        for elemen in baris:
            print(f"{elemen:3}",end="")
        print()
    print(f"Nilai Terbesar: {Max}")  
    print(f"Nilai Terkecil: {Min}")
    print(f"Selisih nilai terbesar dan terkecil adalah: {Max} - {Min} = {Max-Min}\n")
    print("==========================================")
while True:
    print("\nPilih Menu Soal (1-6):")
    print("1. Kelipatan 3")
    print("2. Kelipatan 3 Ganjil & Totalnya")
    print("3. Rata-rata ")
    print("4. Rata-rata & Varians Array")
    print("5. Nilai Terbesar Array 1D")
    print("6. Max, Min, & Selisih Array 2D")


    value = int(input("\nMasukkan nomor soal yang ingin dijalankan: "))

    switch = {
        1: soal1,
        2: soal2,
        3: soal3,
        4: soal4,
        5: soal5,
        6: soal6,
    }


    if value in switch:
        switch[value]()
    else:
        print("Menu tidak diketahui!")