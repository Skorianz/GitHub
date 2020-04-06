def isfloat(string):
    try:
        float(string)
        return True
    
    except ValueError:
        return False

def getinputs():
    print("Sie können beliebig viele Artikel angeben. (Menge, Name, Einzelpreis)")
    
    while True:
        print("-> Eingabe für Artikel", x)

        while True:
            artikel_menge = input("Artikel-Menge: ")

            if artikel_menge.isdigit():
                artikel_menge = int(artikel_menge)

            else:
                print("Bitte geben Sie die Artikel-Menge als Ganzzahl an.")
                continue

            if artikel_menge > 0:
                break

            else:
                print("Bitte geben Sie die Artikel-Menge als positive Ganzzahl an.")
                continue

        while True:
            artikel_name = input("Artikel-Name: ")
            length = len(artikel_name)

            if length == 0:
                print("Bitte lassen Sie den Artikel-Namen nicht leer.")
                continue

            elif length > 128:
                print("Der Artikel-Name darf maximal 128 Zeichen haben.")
                continue

            else:
                break
            
        while True:
            artikel_preis = input("Artikel-Einzelpreis: ").replace(',', '.')

            if artikel_preis.isdigit() or isfloat(artikel_preis):
                artikel_preis = float(artikel_preis)

            else:
                print("Bitte geben Sie den Artikel-Einzelpreis als Ganz- oder Kommazahl an.")
                continue

            if artikel_preis > 0:
                break

            else:
                print("Bitte geben Sie die Artikel-Einzelpreis als positive Ganz- oder Kommazahl an.")
                continue
            

        artikel_gesamtpreis = artikel_preis * artikel_menge

        print("-> Alles wurde KORREKT angegeben!!")
        print("-> Artikel Nr.", x, "; Menge:", artikel_menge, ";", "Name:", artikel_name, ";", "Einzelpreis:", format(artikel_preis, '.2f') + "€", ";", "Gesamtpreis:", format(artikel_gesamtpreis, '.2f') + "€")

        while True:
            next_artikel = input("Möchten Sie einen weiteren Artikel angeben? (yes, no): ").lower()

            if next_artikel == "yes" or next_artikel == "ja" or next_artikel == "y":
                next_artikel = True
                break

            elif next_artikel == "no" or next_artikel == "nein" or next_artikel == "n":
                next_artikel = False
                break
            

        if not next_artikel:
            break

def getinputs_limit():
    print("Sie können bis zu 10 Artikel angeben. (Menge, Name, Einzelpreis)")
    
    for x in range(1, 11):
        print("-> Eingabe für Artikel", x)

        while True:
            artikel_menge = input("Artikel-Menge: ")

            if artikel_menge.isdigit():
                artikel_menge = int(artikel_menge)

            else:
                print("Bitte geben Sie die Artikel-Menge als Ganzzahl an.")
                continue

            if artikel_menge > 0:
                break

            else:
                print("Bitte geben Sie die Artikel-Menge als positive Ganzzahl an.")
                continue

        while True:
            artikel_name = input("Artikel-Name: ")
            length = len(artikel_name)

            if length == 0:
                print("Bitte lassen Sie den Artikel-Namen nicht leer.")
                continue

            elif length > 128:
                print("Der Artikel-Name darf maximal 128 Zeichen haben.")
                continue

            else:
                break
            
        while True:
            artikel_preis = input("Artikel-Einzelpreis: ").replace(',', '.')

            if artikel_preis.isdigit() or isfloat(artikel_preis):
                artikel_preis = float(artikel_preis)

            else:
                print("Bitte geben Sie den Artikel-Einzelpreis als Ganz- oder Kommazahl an.")
                continue

            if artikel_preis > 0:
                break

            else:
                print("Bitte geben Sie die Artikel-Einzelpreis als positive Ganz- oder Kommazahl an.")
                continue
            

        artikel_gesamtpreis = artikel_preis * artikel_menge

        print("-> Alles wurde KORREKT angegeben!!")
        print("-> Artikel Nr.", x, "; Menge:", artikel_menge, ";", "Name:", artikel_name, ";", "Einzelpreis:", format(artikel_preis, '.2f') + "€", ";", "Gesamtpreis:", format(artikel_gesamtpreis, '.2f') + "€")

        if x < 10:
            while True:
                next_artikel = input("Möchten Sie einen weiteren Artikel angeben? (yes, no): ").lower()

                if next_artikel == "yes" or next_artikel == "ja" or next_artikel == "y":
                    next_artikel = True
                    break

                elif next_artikel == "no" or next_artikel == "nein" or next_artikel == "n":
                    next_artikel = False
                    break
            

            if not next_artikel:
                break

def main():
    #getinputs()
    getinputs_limit()


if __name__ == "__main__":
    main()
