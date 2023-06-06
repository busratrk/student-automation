adList=[]
soyadList=[]
numList=[]
vizeList=[]
finalList=[]

def OgrenciEkle():
    print("��renci Kayd� Ekleme ��lemi")
    ad=input("AD:")
    soyad=input("SOYAD:")
    numara=int(input("��RENC� NO:"))
    vize=int(input("V�ZE NOTU:"))
    final=int(input("F�NAL NOTU:"))
    adList.append(ad)
    soyadList.append(soyad)
    numList.append(numara)
    vizeList.append(vize)
    finalList.append(final)
    print("Kay�t ba�ar�l� bir �ekilde eklendi")
def OgrenciSil():
    print("��renci Kayd� Silme ��lemi")
    numara=int(input("Silinecek ��rencinin  ��renci numaras�n� giriniz:"))
    if numara in numList:
        kayitSil=numList.index(numara)
        adList.pop(kayitSil)
        soyadList.pop(kayitSil)
        numList.pop(kayitSil)
        vizeList.pop(kayitSil)
        finalList.pop(kayitSil)
        print("Kay�t silme i�lemi ba�ar�l�")
    else:
        print("silmek istedi�iniz ��renci kay�tl� de�il")

def KayitListesi():
    print("Kay�tl� ��renci Listesi")
    print(f"{'NO'} {'AD':10} {'SOYAD':15} {'V�ZE':10} {'F�NAL':10} {'ORTALAMA':5} {'DURUM':5}")
    for sn in range(len(adList)):
        ortalama=vizeList[sn]*0.4 + finalList[sn]*0.6

        durum="KALDI"
        if ortalama>=50:
            durum="GE�T�"
        print(f"{numList[sn]} {adList[sn]:10} {soyadList[sn]:10} {vizeList[sn]:10} {finalList[sn]:10} {ortalama:10} {durum:10}")
def Guncelleme():
    print("Kay�t G�ncelleme ��lemi")
    numara=int(input("G�ncelleme i�lemi yapmak istedi�iniz ��rencinin ��renci numaras�n� giriniz: "))
    if numara in numList:
        aranan_no=numList.index(numara)
        print(f"{'NO'}{'AD':10}{'SOYAD':15}{'V�ZE':10}{'F�NAL':10}{'ORTALAMA':5}{'DURUM':5}")
        ortalama=vizeList[aranan_no]*0.4 + finalList[aranan_no]*0.6
        durum="KALDI"
        if ortalama>=50:
            durum="GE�T�"
        print(
            f"{numList[aranan_no]} {adList[aranan_no]:5} {soyadList[aranan_no]:5} {vizeList[aranan_no]:5} {finalList[aranan_no]:5} {ortalama:5} {durum:5}")

        Yeni_ad=input("Yeni ad� giriniz:")
        Yeni_soyad=input("yeni soyad� giriniz:")
        Yeni_no=int(input("yeni �grenci numaras�n� giriniz:"))
        Yeni_vize=int(input("yeni vize notunu giriniz:"))
        Yeni_final=int(input("yeni final notunu giriniz:"))
        adList[aranan_no]=Yeni_ad
        soyadList[aranan_no]=Yeni_soyad
        numList[aranan_no]=Yeni_no
        vizeList[aranan_no]=Yeni_vize
        finalList[aranan_no]=Yeni_final
        print("G�ncelleme i�lemi ba�ar�l�")



fonksiyonListesi=[OgrenciEkle,OgrenciSil,KayitListesi,Guncelleme]

def menu():

 while True:
    print("1-��renci Kay�t")
    print("2-��renci Kay�t Sil")
    print("3-��renci Kay�t Listesi")
    print("4-��renci Kay�t G�ncelleme")
    print("0-��k��")
    seciminiz=int(input("L�tfen yapmak istedi�iniz i�lemi se�iniz(0-4):"))
    print("\n"*20)
    if seciminiz<=5 and seciminiz>=1:
     fonksiyonListesi[seciminiz-1]()

    elif seciminiz==0:
        print("Programdan ��k�� yap�l�yor")
        break
    else:
        print("L�tfen ge�erli bir i�lem i�in 0 ile 4 aras� bir rakam se�iniz!")


menu()


    