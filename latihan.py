Bilangan1 = int(input("Basukan Bilangan 1:"))
Bilangan2 = int(input("Masukan Bilangan 2:"))
Bilangan3 = int(input("Masukan Bilangan 3:"))

if  int(Bilangan1) and Bilangan1 > Bilangan3:
    print("Nilai Terbesarnya adalah :", Bilangan1)
    Terbesar = Bilangan1
    numBil = "Bilangan 1"
elif (Bilangan2 > Bilangan3) and (Bilangan2 > Bilangan1):
    print("Nilai terbesar adalah :", Bilangan2)
    Terbesar = bilangan2
    numBil = "Bilangan2"
else:
    Teerbesar = Bilangan3
    numBil = "Bilangan 3"

    print("Bilangan yang terbesar adlah", Bilangan1, "dengan nilai", Terbesar)