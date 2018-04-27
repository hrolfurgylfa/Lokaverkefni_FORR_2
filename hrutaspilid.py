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
        self.fjAfkvæma = fjAfkvaema
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

#spilastokkurInotkun = []

val = 0
while val != 3:

    print("1. Stillingar\n2. Spila\n3. Hætta")
    val = int(input("Sláðu inn tölu: "))

    print("=======================================")

    #Liður 1
    if val == 1:
        while stillingar_val != "3":
            print("Ýttu á 1 til þess að velja magn talva sem þú keppir á móti")
            print("Ýttu á 2 til þess að velja magn alvöru spilara")
            stillingar_val = input("----->")
            if stillingar_val == 1:#Stillingar fyrir fjölda tölvu keppenda
                pass
            elif stillingar_val == 2:#Stillingar fyrir fjölda alvöru spilara
                pass
            elif stillingar_val == 3:#Hérna fer maður ef maður er að fara út úr stillingarvalmyndinni
                pass
            else:#Hérna fer notandinn ef hann slær inn ranga tölu
                print("Rangur innsláttur")

    #Liður 2
    elif val == 2:
        for x in range(52):
            pass
         

    #Hérna fer notandinn þegar hann hættir
    if val == 3:
        print("Leikurinn er að lokast")
 
    #Hérna fer notandinn ef hann slær inn ranga tölu
    else:
        print("Rangur innsláttur")
        print("=======================================")
    
