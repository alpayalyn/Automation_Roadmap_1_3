vize1= int(input("Lütfen vize1 notunuzu giriniz:"))
vize2= int(input("Lütfen vize2 notunuzu giriniz:"))
final= int(input("Lütfen final notunuzu giriniz:"))

def vize1notu(vize1):

    if ((vize1 >= 0) and (vize1 <= 100)):
        vize1yuzde = 30
        vize1etki = vize1 * vize1yuzde/100

    else:
        print("Vize1 notunuzu geçersiz girdiniz. Bu yüzden bu kısım 0 puan olarak değerlendirilecektir.")
        vize1etki = 0
    print("Vize 1 etki notu:", vize1etki)

    return vize1etki

def vize2notu(vize2):

    if ((vize2 >= 0) and (vize2 <= 100)):
        vize2yuzde = 30
        vize2etki = vize2 * vize2yuzde / 100

    else:
        print("Vize2 notunuzu geçersiz girdiniz. Bu yüzden bu kısım 0 puan olarak değerlendirilecektir.")
        vize2etki = 0
    print("Vize 2 etki notu:", vize2etki)

    return vize2etki

def finalnotu(final):

    if ((final >= 0) and (final <= 100)):
        finalyuzde = 40
        finaletki = final * finalyuzde / 100

    else:
        print("Final notunuzu geçersiz girdiniz. Bu yüzden bu kısım 0 puan olarak değerlendirilecektir.")
        finaletki = 0
    print("final etki notu:", finaletki)

    return finaletki

v1=vize1notu(vize1)
v2=vize2notu(vize2)
fi=finalnotu(final)

Genel_puan = v1 + v2 + fi

if(Genel_puan >= 90):
    print("Aldığınız Harf notu AA'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 90 and Genel_puan >= 85):
    print("Aldığınız Harf notu BA'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 85 and Genel_puan >= 80):
    print("Aldığınız Harf notu BB'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 80 and Genel_puan >= 75):
    print("Aldığınız Harf notu CB'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 75 and Genel_puan >= 70):
    print("Aldığınız Harf notu CC'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 70 and Genel_puan >= 65):
    print("Aldığınız Harf notu DC'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 65 and Genel_puan >= 60):
    print("Aldığınız Harf notu DD'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan < 60 and Genel_puan >= 55):
    print("Aldığınız Harf notu FD'dır ve Genel puanınız:", Genel_puan)

elif(Genel_puan <55):
    print("Aldığınız Harf notu FF'dır ve Genel puanınız:", Genel_puan)





