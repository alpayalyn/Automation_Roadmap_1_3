def validation(point):
    while True:
        if point < 0 or point > 100:
            point = int(input("Hata! Lütfen notunuzu 0-100 arası tekrar giriniz:"))
        else:
            break            
    return point

vize1 = validation(int(input("Lütfen vize1 notunuzu giriniz:")))
vize2 = validation(int(input("Lütfen vize2 notunuzu giriniz:")))
final = validation(int(input("Lütfen final notunuzu giriniz:")))

def notlama(vize1, vize2, final):
    vize1yuzde = 30
    vize2yuzde = 30
    finalyuzde = 40
    vize1etki = vize1 * vize1yuzde /100
    vize2etki = vize2 * vize2yuzde /100
    finaletki = final * finalyuzde /100

    return vize1etki + vize2etki + finaletki

totalPoint = notlama(vize1, vize2, final)

if(totalPoint >= 90):
    print("Aldığınız Harf notu AA'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 90 and totalPoint >= 85):
    print("Aldığınız Harf notu BA'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 85 and totalPoint >= 80):
    print("Aldığınız Harf notu BB'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 80 and totalPoint >= 75):
    print("Aldığınız Harf notu CB'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 75 and totalPoint >= 70):
    print("Aldığınız Harf notu CC'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 70 and totalPoint >= 65):
    print("Aldığınız Harf notu DC'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 65 and totalPoint >= 60):
    print("Aldığınız Harf notu DD'dır ve Genel puanınız:", totalPoint)

elif(totalPoint < 60 and totalPoint >= 55):
    print("Aldığınız Harf notu FD'dır ve Genel puanınız:", totalPoint)

elif(totalPoint <55):
    print("Aldığınız Harf notu FF'dır ve Genel puanınız:", totalPoint)