import random
#
# soal no 1========================================================
#  A
print("                      ")
print("=====int dan int======")
a, b = random.randint(1,10), random.randint(1,10)

print(f"nilai a = {a} dan nilai b = {b}")
print(f"nilai {a} + {b} = {a+b}")
print(f"nilai {a} - {b} = {a-b}")
print(f"nilai {a} x {b} = {a*b}")
print(f"nilai {a} / {b} = {int(a/b)}")

#  B
print("                      ")
print("=====int dan float======")
a, b = random.randint(1,10),round( random.random(),7)

print(f"nilai a = {a} dan nilai b = {b}")
print(f"nilai {a} + {b} = {a+b}")
print(f"nilai {a} - {b} = {a-b}")
print(f"nilai {a} x {b} = {a*b}")
print(f"nilai {a} / {b} = {a/b}")

#  C
print("                      ")
print("=====int dan double======")
a, b = random.randint(1,10), round(random.random(),15)

print(f"nilai a = {a} dan nilai b = {b}")
print(f"nilai {a} + {b} = {a+b}")
print(f"nilai {a} - {b} = {a-b}")
print(f"nilai {a} x {b} = {a*b}")
print(f"nilai {a} / {b} = {a/b}")

#  D
print("                      ")
print("=====float dan double======")
a, b = round(random.random(),7), round(random.random(),15)

print(f"nilai a = {a} dan nilai b = {b}")
print(f"nilai {a} + {b} = {a+b}")
print(f"nilai {a} - {b} = {a-b}")
print(f"nilai {a} x {b} = {a*b}")
print(f"nilai {a} / {b} = {a/b}")

#  e
print("                      ")
print("=====numerik dan string======")
a = random.randint(1,10)
b = "halo! "

print(f"nilai a = {a} dan string b = {b}")
print(f" {a} + {b} = {str(a)+b}")
print(f" {a} x {b} = {a*b}")
print(f"operasi - dan / tidak bisa dilakukan")

#  f
print("                      ")
print("=====string dan string======")
a, b = "halo", " dunia"

print(f"string a = {a} dan sring b = {b}")
print(f" {a} + {b} = {a+b}")
print(f"operasi -, x, dan / tidak bisa dilakukan")
print("")

# soal no 2 ========================================================
print("Soal no 2")
jam = int(input("masukan jam :"))
menit = int(input("masukan menit :"))
detik = int(input("masukan detik :"))

waktu = jam*3600 + menit * 60 + detik
waktu_format = f"{waktu:,}".replace(",",".")
print("")
print(f"=====konversi jam kedalam detik=====")
print("")
print(f"waktu = {jam:02d}:{menit:02d}:{detik:02d}")
print(f"Setelah dikonversi menjadi detik adalah {waktu_format} detik")  