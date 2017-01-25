#Skúli Guðbrandsson
svar = "ja"
while svar == "ja":
    print("")
    print("Verkefni 1 - tölur")
    print("Verkefni 2 - nafn")
    print("Verkefni 3 - texti")

    lidur = int(input("Veldu verkefni : "))

    #Liður 1
    if lidur == 1:
        tala1 = int(input("Sláðu inn tölu eitt : "))
        tala2 = int(input("Sláðu inn tölu tvö : "))
        print("Samlagning talnanna er :",tala1 + tala2)
        print("Margföldun talnana er :",tala1 * tala2)

    #Liður 2
    if lidur == 2:
        fornafn = input("Sláðu inn fornafn")
        eftirnafn = input("Sláðu inn eftirnafn")
        print("Fornafn?",fornafn)
        print("Eftirnafn:",eftirnafn)
        print("Halló",fornafn,eftirnafn)
        