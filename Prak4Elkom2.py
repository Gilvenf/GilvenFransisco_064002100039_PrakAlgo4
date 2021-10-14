Angka=input("Masukkan list angka")
Angka =Angka.split(" ")
r = 0
while r < len(Angka) :
    if int(Angka[r])%2==0 : 
        print("Ada Angka Genap Di List Angka Ini")
        exit()
    r+=1
print("Tidak Ada Angka Genap Di List Angka Ini")
