'''
Mikael og Hrólfur
4/23/2018

Lokaverkefni - Hrútaspilið
'''

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

print(hrutar)

skra.close()

#Valmynd
print("=======================================")
val = 0
while val != 3:

    print("1. Stillingar\n2. Spila\n3. Hætta")
    val = int(input("====================>>> "))

    print("=======================================")

    #Liður 1
    if val == 1:
        pass
        print("Það eru ekki komnar neinar stillingar")

    #Liður 2
    elif val == 2:
        spilarar = int(input("Sláðu inn fjölda spilara: "))
        tolvur = int(input("Sláðu inn fjölda talva: "))

    elif val == 3:
        print("Þú hættir")

    else:
        dprint("Rangur innsláttur")

    print("=======================================")
