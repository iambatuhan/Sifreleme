import time
sifre_kombinasyonu = {" ":"0","A":"M$3","B":"Z19","C":"NG9","D":"B?*","E":"V#A","F":"C!+","G":"L%P","H":"AR-","I":"K$#","J":"JT+","K":"J55","L":"SL3","M":"F4^","N":"K66","O":"G6#","P":"W7Q","Q":"Z^2","R":"C7F","S":"B+7","T":"W3+","U":"E8E","V":"W?*","W":"M'K","X":"RQ&","Y":"TQ3","Z":"P<3","Ç":"OP.","Ğ":"I?H","İ":"U5W","Ö":"Y&%","Ü":"JCX","Ş":"VA*"}
sifre_kombinasyonu2 = {}
for x,y in sifre_kombinasyonu.items():
    sifre_kombinasyonu2[y] = x
def Sifrele(metin):
    metin = metin.upper()
    sifre = ""
    metin_uzunluğu = len(metin)
    for metiniparçala in range(0,metin_uzunluğu):
        sifre += str(sifre_kombinasyonu.get(metin[metiniparçala]))
    return sifre
def SifreÇöz(sifre):
    basamak = 0
    SifreCözüldü = ""
    while basamak < len(sifre):
        if "0" in sifre[basamak:basamak+3]:
            basamak +=1
            SifreCözüldü += " "
        else:
            SifreCözüldü += str(sifre_kombinasyonu2.get(sifre[basamak:basamak+4]))
            basamak += 4
    return SifreCözüldü

secim = input("""

1. Şifre Çözme

2. Mesaj Şifrelemek

Ne Yapmak İstersiniz?:""")

if secim == "1":
    sifreGir = input("Çözmek İstediğiniz Şifreniz:")
    print("Şifre Çözülüyor...")
    time.sleep(3)
    print("İşlem Başarılı")
    print("Mesaj:" + SifreÇöz(sifreGir))
else:
    metin = input("Şifrelemek istediğiniz metin:")
    print("Mesaj Şifreleniyor")
    time.sleep(3)
    print("İşlem Başarılı!")
    print("Şifre:" + Sifrele(metin))