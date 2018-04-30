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

def spilariVann(spil_s, spil_t):
    print("Þú vannst")
    spilari.append(spil_t)
    talva.pop(talva.index(spil_t))
    spilariSpilar = 1
    talvaSpilar = 0

def talvaVann(spil_s, spil_t):
    print("Þú tapaðir")
    talva.append(spil_s)
    spilari.pop(spilari.index(spil_s))
    spilariSpilar = 0
    talvaSpilar = 1


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

            s_spil = random.choice(spilari)
            t_spil = random.choice(talva)

            print("> Hér er spilið þitt:")
            print("Nafn:\t" + spilari[0].nafn)
            print()
            print("Þyngd\tMjólk\tUll\tFjafkvæma")
            print(spilari[0].thyngd +" \t"+ spilari[0].mjolk +"\t"+ spilari[0].ull +"\t"+ spilari[0].fjAfkvaema)
            print()
            print("Læri\tFrjós\tÞykkBak\tMalir")
            print(spilari[0].laeri +"\t"+ spilari[0].frjosemi +"\t"+ spilari[0].thykkiBaks +"\t"+ spilari[0].malir)
            print("=======================================")

            svar = 0
            if spilariSpilar == 1:
                print("Hverjux viltu keppa í?\n1. Þyngd\n2. Mjólk\n3. Ull\n4. Fj Afkvæma\n5. Læri\n6. Frjósemi\n7. Þykki Baks\n8. Malir")
                svar = int(input("Sláðu inn tölu: "))

                if svar == 1:
                    if s_spil.thyngd > t_spil.thyngd:
                        spilariVann(s_spil, t_spil)
                elif svar == 2:
                    if s_spil.mjolk > t_spil.mjolk:
                        spilariVann(s_spil, t_spil)
                elif svar == 3:
                    if s_spil.ull > t_spil.ull:
                        spilariVann(s_spil, t_spil)
                elif svar == 4:
                    if s_spil.fjAfkvaema > t_spil.fjAfkvaema:
                        spilariVann(s_spil, t_spil)
                elif svar == 5:
                    if s_spil.laeri > t_spil.laeri:
                        spilariVann(s_spil, t_spil)
                elif svar == 6:
                    if s_spil.frjosemi > t_spil.frjosemi:
                        spilariVann(s_spil, t_spil)
                elif svar == 7:
                    if s_spil.thykkiBaks > t_spil.thykkiBaks:
                        spilariVann(s_spil, t_spil)
                elif svar == 8:
                    if s_spil.malir > t_spil.malir:
                        spilariVann(s_spil, t_spil)
                        
            elif talvaSpilar == 1:
                print("Hér er spilið tölvunar:", talva[0].nafn)
                
            
            print("Spilari 1 er núna með",len(spilari),"spil og talvan er núna með",len(talva),"spil")
            
            #leiklokid = True#TEST
                

    else:
        if val == 3:
            print("Leikurinn er að lokast")
        else:
            print("Rangur innsláttur")

    print("=======================================")
