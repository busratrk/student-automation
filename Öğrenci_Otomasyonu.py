adList=[]
soyadList=[]
numList=[]
vizeList=[]
finalList=[]

def OgrenciEkle():
    print("Öðrenci Kaydý Ekleme Ýþlemi")
    ad=input("AD:")
    soyad=input("SOYAD:")
    numara=int(input("ÖÐRENCÝ NO:"))
    vize=int(input("VÝZE NOTU:"))
    final=int(input("FÝNAL NOTU:"))
    adList.append(ad)
    soyadList.append(soyad)
    numList.append(numara)
    vizeList.append(vize)
    finalList.append(final)
    print("Kayýt baþarýlý bir þekilde eklendi")
def OgrenciSil():
    print("Öðrenci Kaydý Silme Ýþlemi")
    numara=int(input("Silinecek öðrencinin  öðrenci numarasýný giriniz:"))
    if numara in numList:
        kayitSil=numList.index(numara)
        adList.pop(kayitSil)
        soyadList.pop(kayitSil)
        numList.pop(kayitSil)
        vizeList.pop(kayitSil)
        finalList.pop(kayitSil)
        print("Kayýt silme iþlemi baþarýlý")
    else:
        print("silmek istediðiniz öðrenci kayýtlý deðil")

def KayitListesi():
    print("Kayýtlý Öðrenci Listesi")
    print(f"{'NO'} {'AD':10} {'SOYAD':15} {'VÝZE':10} {'FÝNAL':10} {'ORTALAMA':5} {'DURUM':5}")
    for sn in range(len(adList)):
        ortalama=vizeList[sn]*0.4 + finalList[sn]*0.6

        durum="KALDI"
        if ortalama>=50:
            durum="GEÇTÝ"
        print(f"{numList[sn]} {adList[sn]:10} {soyadList[sn]:10} {vizeList[sn]:10} {finalList[sn]:10} {ortalama:10} {durum:10}")
def Guncelleme():
    print("Kayýt Güncelleme Ýþlemi")
    numara=int(input("Güncelleme iþlemi yapmak istediðiniz öðrencinin öðrenci numarasýný giriniz: "))
    if numara in numList:
        aranan_no=numList.index(numara)
        print(f"{'NO'}{'AD':10}{'SOYAD':15}{'VÝZE':10}{'FÝNAL':10}{'ORTALAMA':5}{'DURUM':5}")
        ortalama=vizeList[aranan_no]*0.4 + finalList[aranan_no]*0.6
        durum="KALDI"
        if ortalama>=50:
            durum="GEÇTÝ"
        print(
            f"{numList[aranan_no]} {adList[aranan_no]:5} {soyadList[aranan_no]:5} {vizeList[aranan_no]:5} {finalList[aranan_no]:5} {ortalama:5} {durum:5}")

        Yeni_ad=input("Yeni adý giriniz:")
        Yeni_soyad=input("yeni soyadý giriniz:")
        Yeni_no=int(input("yeni ögrenci numarasýný giriniz:"))
        Yeni_vize=int(input("yeni vize notunu giriniz:"))
        Yeni_final=int(input("yeni final notunu giriniz:"))
        adList[aranan_no]=Yeni_ad
        soyadList[aranan_no]=Yeni_soyad
        numList[aranan_no]=Yeni_no
        vizeList[aranan_no]=Yeni_vize
        finalList[aranan_no]=Yeni_final
        print("Güncelleme iþlemi baþarýlý")



fonksiyonListesi=[OgrenciEkle,OgrenciSil,KayitListesi,Guncelleme]

def menu():

 while True:
    print("1-Öðrenci Kayýt")
    print("2-Öðrenci Kayýt Sil")
    print("3-Öðrenci Kayýt Listesi")
    print("4-Öðrenci Kayýt Güncelleme")
    print("0-Çýkýþ")
    seciminiz=int(input("Lütfen yapmak istediðiniz iþlemi seçiniz(0-4):"))
    print("\n"*20)
    if seciminiz<=5 and seciminiz>=1:
     fonksiyonListesi[seciminiz-1]()

    elif seciminiz==0:
        print("Programdan çýkýþ yapýlýyor")
        break
    else:
        print("Lütfen geçerli bir iþlem için 0 ile 4 arasý bir rakam seçiniz!")


menu()


    