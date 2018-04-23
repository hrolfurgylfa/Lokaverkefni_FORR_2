'''
Mikael og Hrólfur
4/23/2018

Lokaverkefni - Hrútaspilið
'''

import random

class Spil():

    fj_hruta = 0

    def __init__(self, thyngd, mjolk, ull, fjAfkvaema, laeri, frjosemi, thykkiBaks, malir):
        self.thyngd = thyngd
        self.mjolk = mjolk
        self.ull = ull
        self.fjAfkvæma = fjAfkvæma
        self.laeri = laeri
        self.frjosemi = frjosemi
        self.thykkiBaks = thykkiBaks
        self.malir = malir


skra = open("hrutar.txt", "r")
hrutar = []
for line in skra:
    lina =  line.split(",")        
    hrutar.append(lina)

#print(hrutar)
skra.close()


spilari = []
talva = []

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
        random.shuffle(hrutar)
        #Spil notendans
        for x in range(26):
            spilari.append(hrutar[x])
        #spil tölvunar
        for x in range(26):
            talva.append(hrutar[x + 26])
        print(spilari)
        print(talva)

        

    else:
        if val == 3:
            print("Þú hættir")
        else:
            print("Rangur innsláttur")

    print("=======================================")
