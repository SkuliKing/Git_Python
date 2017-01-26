#Skúli Guðbrandsson
svar = "ja" #Valmynd, og liðirnir til að velja
while svar == "ja":
    print("")
    print("Liður1 - tölur")
    print("Liður 2 - nafn")
    print("Liður 3 - texti")
    print("Liður 4 - Hætta")

    lidur = int(input("Veldu verkefni : ")) #notandi velur lið

    #Liður 1
    if lidur == 1: #liður valinn
        tala1 = int(input("Sláðu inn tölu eitt : ")) #biður notanda um tölu
        tala2 = int(input("Sláðu inn tölu tvö : ")) #biður notanda um tölu
        print("Samlagning talnanna er :",tala1 + tala2) #Prentar summu tolu eitt og tvö
        print("Margföldun talnana er :",tala1 * tala2) #Prentar margfeldi tölu eitt og tvö

    #Liður 2
    if lidur == 2: #liður valinn
        fornafn = input("Sláðu inn fornafn")  #biður notanda um fornafn
        eftirnafn = input("Sláðu inn eftirnafn")  #biður notanda um eftirnafn
        print("Fornafn?",fornafn) #prentar fornafnið
        print("Eftirnafn:",eftirnafn) #prentar eftirnafnið
        print("Halló",fornafn,eftirnafn) #prentar halló og fornafn,eftirnafn

    #Liður 3
    if lidur == 3:
        texti = input("Settu inn random texta")
        telhast = 0
        tellagst = 0
        telefthst = 0
        sidastur = False

        for i in range(len(texti)):

            if texti[i].isupper() and texti[i]:
                        telhast += 1
                sidastur = True
         elif texti[i].islower() and sidastur == True:
                telefthst += 1
                sidastur = True

        if texti[i].islower():
               tellagst += 1
                sidastur = False

        print("í þessum texta eru ", telhast, " hástafir", tellagst, "Lágstafir", telefthst,
              " lágstafir sem koma strax eftir hástöfum")

    #Liður4
    if lidur == 4:
        print("BÆÆ :))")#prentar BÆÆ
        break #ender while lykkjuna



