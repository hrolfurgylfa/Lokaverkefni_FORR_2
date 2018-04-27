'''
Mikael og Hrólfur
4/23/2018

Lokaverkefni - Hrútaspilið
'''

import random

class Hrutar():

    fj_hruta = 0

    def __init__(self, nafn, thyngd, mjolk, ull, fjAfkvaema, laeri, frjosemi, thykkiBaks, malir):
        self.nafn = nafn
        self.thyngd = thyngd
        self.mjolk = mjolk
        self.ull = ull
        self.fjAfkvaema = fjAfkvaema
        self.laeri = laeri
        self.frjosemi = frjosemi
        self.thykkiBaks = thykkiBaks
        self.malir = malir


spil = []
skra = open("hrutar.txt", "r")
for lina in skra:
    spil.append(lina)       
skra.close()

temp = []
spilastokkur = []

for stak in spil:
    temp = stak.split(",")
    spilastokkur.append(Hrutar(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8]))

spilari = []
talva = []

val = 0
while val != 3:

    print("1. Stillingar\n2. Spila\n3. Hætta")
    val = int(input("Sláðu inn tölu: "))

    print("=======================================")

    #Liður 1
    if val == 1:
        stillingar_val = ""
        while stillingar_val != "3":
            print(Hrutar)#TEST
            print("Ýttu á 1 til þess að velja magn talva sem þú keppir á móti")
            print("Ýttu á 2 til þess að velja magn alvöru spilara")
            stillingar_val = input("----->")
            if stillingar_val == 1:#Stillingar fyrir fjölda tölvu keppenda
                tolvu_keppendur = input("Sláðu inn fjölda tölvu keppenda (max 3) >>> ")
            elif stillingar_val == 2:#Stillingar fyrir fjölda alvöru spilara
                alvoru_keppendur = input("Sláðu inn fjölda alvöru keppenda (max 3) >>> ")
            elif stillingar_val == 3:#Hérna fer maður ef maður er að fara út úr stillingarvalmyndinni
                pass
            else:#Hérna fer notandinn ef hann slær inn ranga tölu
                print("Rangur innsláttur")

    #Liður 2
    elif val == 2:
        random.shuffle(spilastokkur)
        for x in range(26):
            spilari.append(spilastokkur[x])
        for x in range(26, 52):
            talva.append(spilastokkur[x])

        spilariSpilar = 1
        talvaSpilar = 0
        leiklokid = False
        while leiklokid != True:
            kynd_spilara = random.randint(0,len(spilari)-1)

            if spilariSpilar == 1:
                print("> Hér er spilið þitt:")
                print("Nafn:\n" + spilari[0].nafn)
                print("Þyngd\tMjólk\tUll\tFjafkvæma")
                print(spilari[0].thyngd +"\t"+ spilari[0].mjolk +"\t"+ spilari[0].ull +"\t"+ spilari[0].fjAfkvaema)
                print("Læri\tFrjós\tÞykkBak\tMalir")
                print(spilari[0].laeri +"\t"+ spilari[0].frjosemi +"\t"+ spilari[0].thykkiBaks +"\t"+ spilari[0].malir)

                spilariSpilar = 0
                talvaSpilar = 1
            elif talvaSpilar == 1:
                print("Hér er spilið tölvunar:", talva[0].nafn)
                spilariSpilar = 1
                talvaSpilar = 0
            leiklokid = False
                

    else:
        if val == 3:
            print("Þú hættir")
        else:
            print("Rangur innsláttur")

    print("=======================================")
