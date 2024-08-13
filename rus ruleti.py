
import random
import time
kolay_rulet = [1,0,0,0,0,0]
orta_rulet = [0,1,0,0,0,1]
zor_rulet = [1,0,1,0,1,0]
print("rus ruleti oyununa hoş geldiniz lütfen zorluk seçin: ")
a = 1
for i in ["kolay (1/6 keybetme şansınız var)" , "orta (2/6 kaybetme şansınız var)" , "zor(3/6 kaybetme şansınız var)"]:
    print("{}. {}".format(a,i))
    a += 1
def zorlukseçimi():
    while True :
        seçim = input("zorluk: ")
        if seçim == "kolay" :
            oyun_ruleti = kolay_rulet
            print("kolay zorluk seçildi")
            break
        elif seçim == "orta" :
            oyun_ruleti = orta_rulet
            print("orta zorluk seçildi")
            break
        elif seçim == "zor":
            oyun_ruleti = zor_rulet
            print("zor zorluk seçildi")
            break
        else : print("yanlış tuşladınız lütfen tekrar deneyin")
    print("oyun başlıyor")
    
    geri_sayım = [*range(1,4)]
    for a in  geri_sayım[::-1]:
        time.sleep(1)
        print("{}".format(a))
    return oyun_ruleti

def oyun(rulet):

    bs = random.choice(rulet)
    if bs == 1 :
        print("mermi denk gldi")
        print("oyunu kaybettiniz")
    else : print("boş kovan denk geldi\noyunu kazandınız")



rull = zorlukseçimi()

oyun(rull)



















