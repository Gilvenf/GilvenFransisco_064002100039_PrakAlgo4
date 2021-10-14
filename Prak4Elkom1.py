print ("----------PROGRAM KONVERSI BILANGAN---------")
print ("1. Desimal Ke Biner")
print ("2. Biner Ke Desimal")
print ("3. Exit")
pilih =input('pilih:')
def decimalToBinner():
    print("decimalToBinner")
    decimal =input("Masukkan angka Decimal : ")
    decimal = bin(int(decimal)).replace("0b", "")
    print(decimal)
def binnerToDecimal(): 
    print("binnerToDecimal")
    binner =input("Masukkan angka Binner : ")
    binner =int(binner,2)
    print(binner)
if int(pilih) == 1 :
    decimalToBinner()
elif int(pilih) == 2:
    binnerToDecimal()
else:
    print("Terima kasih telah menggunkan aplikasi ini :)")
    exit()


