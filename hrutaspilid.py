'''
Mikael og Hrólfur
4/23/2018

Lokaverkefni - Hrútaspilið
'''

import random
global spil_a_bordi

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
            input("> Ýttu á enter til þess að halda áfram:")

        print("Talvan er með", self.tolva_keppa, "og þú ert með", self.spilari_keppa)
        input("> Ýttu á enter til þess að halda áfram:")
        
        if self.tolva_keppa > self.spilari_keppa:
            print("* Þú tapaðir\n")
            talva.append(self.spil_s)
            spilari.pop(spilari.index(self.spil_s))
            talva.append(talva.pop(talva.index(self.spil_t)))

            if len(jafntefli) > 0:
                print("og talvan fær spilin sem voru undir")
                input("> Ýttu á enter til þess að halda áfram:")
                talva.extend(jafntefli)
                del jafntefli[:]
            return "T"

        elif self.tolva_keppa < self.spilari_keppa:
            print("* Þú vannst\n")
            spilari.append(self.spil_t)
            talva.pop(talva.index(self.spil_t))
            spilari.append(spilari.pop(spilari.index(self.spil_s)))

            if len(jafntefli) > 0:
                print("og þú færð spilin sem voru undir")
                input("> Ýttu á enter til þess að halda áfram:")
                spilari.extend(jafntefli)
                del jafntefli[:]
            return "S"

        elif self.spilari_keppa == self.tolva_keppa:
            jafntefli.append(self.spil_s)
            jafntefli.append(self.spil_t)
            spilari.pop(spilari.index(self.spil_s))
            talva.pop(talva.index(self.spil_t))
            print("* Jafntefli\n")
            print("Splin voru lögð undir")
            return "J"

        else:
            print("ERROR, Class: Keppa, Fall: Keppni")

spil = []
skra = open("hrutar.txt", "r")
for lina in skra:
    spil.append(lina)       
skra.close()

temp = []
spilastokkur = []

for stak in spil:
    temp = stak.split(",")
    spilastokkur.append(Hrutar(temp[0], float(temp[1]), float(temp[2]), float(temp[3]), float(temp[4]), float(temp[5]), float(temp[6]), float(temp[7]), float(temp[8])))

spilari = []
talva = []
jafntefli = []

random.shuffle(spilastokkur)
for x in range(26):
    spilari.append(spilastokkur[x])
for x in range(26, 52):
    talva.append(spilastokkur[x])

umferdir = 1

val = 0
while val != 3:

    print("1. Spilareglur\n2. Spila\n3. Hætta")
    val = int(input("Sláðu inn tölu: "))

    print("=======================================") #Bil

    #Liður 1
    if val == 1:
        print("Spilareglunar\n=======================================") #Titill og Bil
        print("1) Í hverri umferð er spilað með efsta spili stokksins.")
        print("2) Þegar maður á leik, skal maður velja flokk til að keppa í.")
        print("3) Sá sem er með hæstu tölu flokks vinnur og fær að gera aftur.")
        print("4) Spilað er þangað til að maður er kominn með öll spilin.")

    #Liður 2
    elif val == 2:
        spilariSpilar = random.choice([True, False])
        leiklokid = False
        
        while leiklokid != True:
            input("> Ýttu á enter til að fara í næstu umferð:")
            print("Umferð", umferdir, "\n=======================================") #Titill og Bil

            s_spil = spilari[0]
            t_spil = talva[0]

            #Spilarinn á umferð núna
            svar = 0
            if spilariSpilar == True:
                #Valmynd til að velja flokk
                print("Hverju viltu keppa í?\n\nNafn:", s_spil.nafn,"\n\n1. Þyngd\t",s_spil.thyngd,"\n2. Mjólk\t",s_spil.mjolk,"\n3. Ull\t\t",s_spil.ull,"\n4. Fj Afkvæma\t",s_spil.fjAfkvaema,"\n5. Læri\t\t",s_spil.laeri,"\n6. Frjósemi\t",s_spil.frjosemi,"\n7. Þykki Baks\t",s_spil.thykkiBaks,"\n8. Malir\t",s_spil.malir)
                svar = int(input("Sláðu inn tölu: "))

                print("=======================================")
                
                if svar == 1:
                    h1 = Keppa(s_spil,t_spil,t_spil.thyngd,s_spil.thyngd)
                    Sigurvegari = h1.keppni()

                elif svar == 2:
                    h1 = Keppa(s_spil,t_spil,t_spil.mjolk,s_spil.mjolk)
                    Sigurvegari = h1.keppni()
                    
                elif svar == 3:
                    h1 = Keppa(s_spil,t_spil,t_spil.ull,s_spil.ull)
                    Sigurvegari = h1.keppni()

                elif svar == 4:
                    h1 = Keppa(s_spil,t_spil,t_spil.fjAfkvaema,s_spil.fjAfkvaema)
                    Sigurvegari = h1.keppni()

                elif svar == 5:
                    h1 = Keppa(s_spil,t_spil,t_spil.laeri,s_spil.laeri)
                    Sigurvegari = h1.keppni()

                elif svar == 6:
                    h1 = Keppa(s_spil,t_spil,t_spil.frjosemi,s_spil.frjosemi)
                    Sigurvegari = h1.keppni()
                    
                elif svar == 7:
                    h1 = Keppa(s_spil,t_spil,t_spil.thykkiBaks,s_spil.thykkiBaks)
                    Sigurvegari = h1.keppni()
                    

                elif svar == 8:
                    h1 = Keppa(s_spil,t_spil,t_spil.malir,s_spil.malir)
                    Sigurvegari = h1.keppni()

            #Talvan á umferð núna           
            elif spilariSpilar == False:

                print("> Talvan á leik")
                tel = random.randint(1,8)

                if tel == 1:
                    print("Talvan valdi flokkin: Þyngd")
                    h1 = Keppa(s_spil, t_spil, t_spil.thyngd, s_spil.thyngd)
                    Sigurvegari = h1.keppni()

                elif tel == 2:
                    print("Talvan valdi flokkin: Mjólk")
                    h1 = Keppa(s_spil, t_spil, t_spil.mjolk, s_spil.mjolk)
                    Sigurvegari = h1.keppni()
                    
                elif tel == 3:
                    print("Talvan valdi flokkin: Ull")
                    h1 = Keppa(s_spil, t_spil, t_spil.ull, s_spil.ull)
                    Sigurvegari = h1.keppni()

                elif tel == 4:
                    print("Talvan valdi flokkin: Fjöldi afkvæma")
                    h1 = Keppa(s_spil,t_spil,t_spil.fjAfkvaema,s_spil.fjAfkvaema)
                    Sigurvegari = h1.keppni()

                elif tel == 5:
                    print("Talvan valdi flokkin: Læri")
                    h1 = Keppa(s_spil,t_spil,t_spil.laeri,s_spil.laeri)
                    Sigurvegari = h1.keppni()

                elif tel == 6:
                    print("Talvan valdi flokkin: Frjósemi")
                    h1 = Keppa(s_spil,t_spil,t_spil.frjosemi,s_spil.frjosemi)
                    Sigurvegari = h1.keppni()
                    
                elif tel == 7:
                    print("Talvan valdi flokkin: Þykki baks")
                    h1 = Keppa(s_spil,t_spil,t_spil.thykkiBaks,s_spil.thykkiBaks)
                    Sigurvegari = h1.keppni()
                    
                elif tel == 8:
                    print("Talvan valdi flokkin: Malir")
                    h1 = Keppa(s_spil,t_spil,t_spil.malir,s_spil.malir)
                    Sigurvegari = h1.keppni()
            
            if Sigurvegari == "T":
                spilariSpilar = False
                Sigurvegari = ""
            elif Sigurvegari == "S":
                spilariSpilar = True
                Sigurvegari = ""

            print("Tölvan er með",len(talva),"spil og þú ert með",len(spilari),"spil\n")

            #Ef spilastokkur spilarans er búinn, þá endar leikurinn
            if len(spilari) == 0:
                leiklokid = True
            #Ef spilastokkur tölvunar er búinn, þá endar leikurinn
            elif len(talva) == 0:
                leiklokid = True

            #Þegar leikurinn er búinn, þá endar það forritið og segir hver vann
            if leiklokid == True:
                val = 3   #Endar forritið
                print("=======================================\nLeiklok !") #Bil og Titill
                if len(spilari) == 0:
                    print("Þú tapaðir og talvan vann!") #Spilari tapaði
                elif len(talva) == 0:
                    print("Þú vannst og talvan tapaði!")#Spilari vann
            else:
                umferdir+=1

    #Ef notandinn vill hætta eða sló inn ranga tölu
    else:
        if val == 3:
            print("Þú hættir")
        else:
            print("Rangur innsláttur")

    print("=======================================") #Bil
