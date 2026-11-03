import random

# soal no 1==================================================================
data = ["ayam", "sapi", "kodok","bebek"]

print(f"sebelum di tukar {data}")
# menukar idx 1 ke 4
data[0], data[3] = data[3], data[0] 

print(f"setelah di tukar {data}")

## soal No 2================================================================
boolA = input("masukan boolean A: ").lower()=="true"
boolB = input("masukan boolean B: ").lower()=="true"
boolC = input("masukan boolean C: ").lower()=="true"

print("")
print("===================================")

print(f"A.	boolA & boolB & boolC = {boolA & boolB & boolC}")
print(f"B.	boolA & boolB OR boolC = {boolA & boolB | boolC}")
print(f"C.	boolA OR boolB OR boolC = {boolA | boolB | boolC}")
print(f"D.	boolA & boolB OR (NOT boolC)= {boolA & boolB | (not boolC)}")

# soal no 3================================================================================
data = []
x, y= 2,3
for i in range(x):
    baris=[]
    for j in range(y):
        baris.append(random.randint(1,10))
    data.append(baris)

print("")
print("======matriks sebelum ditukar=========")
for i in range(x):
    for j in range(y):
        print(f"{data[i][j]}", end=" ")
    print()

print("")
print("=======matriks setelah ditukar==========")
print("")

data[1][1],data[0][2] = data[0][2],data[1][1]

for i in range(x):
    for j in range(y):
        print(f"{data[i][j]}", end=" ")
    print()