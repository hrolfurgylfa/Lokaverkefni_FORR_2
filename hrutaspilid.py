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

hrutar = open("hrutar.txt", "r")

for lina in hrutar:
    lina =  line.split(";")



val = ""

while val != 3:

    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print("\n")#Þetta er til þess að gera tvö enter

    print("1. Stillingar")
    print("2. Spila")
    print("3. Hætta")
    valmynd = input("-------------------->>> ")#Hérna velur notandinn hvaða lið hann ætlar að fara í

    print()#Þetta er til þess að gera enter
    for tel in range(50):#Þessi for lúppa gerir línu sem er auðvelt að stjórna stærðinni á
        print("-",end="")
    print()#Þetta er til þess að gera enter

    if valmynd == "1":#Liður 1
        print("Það eru ekki komnar neinar stillingar")

    elif valmynd == "2":#Liður 2
        print("Sláðu inn hversu margir spilarar eiga að vera")
        spilarar = input("-------------------->>> ")
        print("\nSláðu inn hversu margar tölvur eiga að vera")
        tolvur = input("-------------------->>> ")

    elif valmynd == "3":#Þetta er til þess að það komi ekki "ERROR Sláðu inn tölu á milli 1 og 3" þegar maður er að hætta í forritinu
        pass

    else:
        print("ERROR\tSláðu inn tölu á milli 1 og 3")