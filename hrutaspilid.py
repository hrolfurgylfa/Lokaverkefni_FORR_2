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

class Keppa():
    def __init__(self, spil_s, spil_t, tolva_keppa, spilari_keppa):
        self.spil_t = spil_t
        self.spil_s = spil_s
        self.tolva_keppa = tolva_keppa
        self.spilari_keppa = spilari_keppa

    def keppni(self):
        if self.tolva_keppa > self.spilari_keppa:
            print("\n==============================\n")
            print("Þú tapaðir\n")
            talva.append(self.spil_s)
            spilari.pop(spilari.index(self.spil_s))
            spilariSpilar = 0
            talvaSpilar = 1
            talva.append(talva.pop(talva.index(self.spil_t)))

        elif self.tolva_keppa < self.spilari_keppa:
            print("\n==============================\n")
            print("Þú vannst\n")
            spilari.append(self.spil_t)
            talva.pop(talva.index(self.spil_t))
            spilariSpilar = 1
            talvaSpilar = 0
            spilari.append(spilari.pop(spilari.index(self.spil_s)))

        elif self.spil_t.thyngd == self.spil_s.thyngd:
            print("jafntefli")
        else:
            print("ERROR, Class: Keppa, Fall: Keppni")


def spilariVann(spil_s, spil_t):
    print("\n==============================\n")
    print("Þú vannst\n")
    spilari.append(spil_t)
    talva.pop(talva.index(spil_t))
    spilariSpilar = 1
    talvaSpilar = 0
    spilari.append(spilari.pop(spilari.index(spil_s)))

def talvaVann(spil_s, spil_t):
    print("\n==============================\n")
    print("Þú tapaðir\n")
    talva.append(spil_s)
    spilari.pop(spilari.index(spil_s))
    spilariSpilar = 0
    talvaSpilar = 1
    talva.append(talva.pop(talva.index(spil_t)))

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

random.shuffle(spilastokkur)
for x in range(26):
    spilari.append(spilastokkur[x])
for x in range(26, 52):
    talva.append(spilastokkur[x])

val = 0
while val != 3:

    print("1. Stillingar\n2. Spila\n3. Hætta")
    val = int(input("Sláðu inn tölu: "))

    print("=======================================")

    #Liður 1
    if val == 1:
        pass
        print("Það eru ekki komnar neinar stillingar")

    #Liður 2
    elif val == 2:

        spilariSpilar = 1
        talvaSpilar = 0
        leiklokid = False
        while leiklokid != True:
            kynd_spilara = random.randint(0,len(spilari)-1)

            s_spil = spilari[0]
            t_spil = talva[0]

            print("==============================")
            print("> Hér er spilið þitt:")
            print("\nNafn:\t" + s_spil.nafn)
            print()#Þetta er til þess að búa til bil svo að þetta líti betur út
            print("Þyngd\tMjólk\tUll\tFjafkvæma")
            print(s_spil.thyngd +"\t"+ s_spil.mjolk +"\t"+ s_spil.ull +"\t"+ s_spil.fjAfkvaema)
            print("Læri\tFrjós\tÞykkBak\tMalir")
            print(s_spil.laeri +"\t"+ s_spil.frjosemi +"\t"+ s_spil.thykkiBaks +"\t"+ s_spil.malir)
            print("==============================")

            #print(spilari[0].nafn, spilari[1].nafn)
            
            svar = "0"
            if spilariSpilar == 1:
                print("Hverjux viltu keppa í?\n1. Þyngd\n2. Mjólk\n3. Ull\n4. Fj Afkvæma\n5. Læri\n6. Frjósemi\n7. Þykki Baks\n8. Malir")
                svar = input("Sláðu inn tölu: ")

                if svar == "1":
                    t1 = Keppa(s_spil, t_spil, s_spil.thyngd, t_spil.thyngd)
                    t1.keppni()

                elif svar == "2":
                    if s_spil.mjolk > t_spil.mjolk:
                        spilariVann(s_spil, t_spil)
                elif svar == "3":
                    if s_spil.ull > t_spil.ull:
                        spilariVann(s_spil, t_spil)
                elif svar == "4":
                    if s_spil.fjAfkvaema > t_spil.fjAfkvaema:
                        spilariVann(s_spil, t_spil)
                elif svar == "5":
                    if s_spil.laeri > t_spil.laeri:
                        spilariVann(s_spil, t_spil)
                elif svar == "6":
                    if s_spil.frjosemi > t_spil.frjosemi:
                        spilariVann(s_spil, t_spil)
                elif svar == "7":
                    if s_spil.thykkiBaks > t_spil.thykkiBaks:
                        spilariVann(s_spil, t_spil)
                elif svar == "8":
                    if s_spil.malir > t_spil.malir:
                        spilariVann(s_spil, t_spil)
                        
            elif talvaSpilar == 1:
                #print("Hér er spilið tölvunar:", talva[0].nafn)
                print("talvan á leik núna")
                tel = random.randint(1,8)
                if tel == 1:
                    print("Talvan spilar í: Þyngd")
                    if t_spil.thyngd > s_spil.thyngd:
                        talvaVann(s_spil, t_spil)
                elif tel == 2:
                    print("Talvan spilar í: Mjólk")
                    if t_spil.mjolk > s_spil.mjolk:
                        talvaVann(s_spil, t_spil)
                elif tel == 3:
                    print("Talvan spilar í: Ull")
                    if t_spil.ull > s_spil.ull:
                        talvaVann(s_spil, t_spil)
                elif tel == 4:
                    print("Talvan spilar í: Fjöldi Afkvæma")
                    if t_spil.fjAfkvaema > s_spil.fjAfkvaema:
                        talvaVann(s_spil, t_spil)
                elif tel == 5:
                    print("Talvan spilar í: Læri")
                    if t_spil.laeri > s_spil.laeri:
                        talvaVann(s_spil, t_spil)
                elif tel == 6:
                    print("Talvan spilar í: Frjósemi")
                    if t_spil.frjosemi > s_spil.frjosemi:
                        talvaVann(s_spil, t_spil)
                elif tel == 7:
                    print("Talvan spilar í: Þykki Baks")
                    if t_spil.thykkiBaks > s_spil.thykkiBaks:
                        talvaVann(s_spil, t_spil)
                elif tel == 8:
                    print("Talvan spilar í: Malir")
                    if t_spil.malir > s_spil.malir:
                        talvaVann(s_spil, t_spil)
            
            print("Spilari 1 er núna með",len(spilari),"spil og talvan er núna með",len(talva),"spil")
            print(spilari[0].nafn, spilari[1].nafn)
            print(talva[0].nafn, talva[1].nafn)

    else:
        if val == 3:
            print("Þú hættir")
        else:
            print("Rangur innsláttur")

    print("=======================================")
