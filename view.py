class View:
    def kuva_elemendid(self, elemendid):
        print("Kõik elemendid: ")
        print("{:<10} | {:>10} | {:>10}".format('nimetus', 'hind', 'kogus'))
        print("------------------------------------")
        for element in elemendid:
            print("{:<10} | {:>10.2f} | {:>10}".format(element['nimetus'], element['hind'], element['kogus']))
            print("")

    def kuva_element(self, nimetus, element):
        if element:
            print("Kuvame elemendi {} andmed:".format(nimetus))
            print("{:<10} | {:>10} | {:>10}".format('nimetus', 'hind', 'kogus'))
            print("------------------------------------")
            print("{:<10} | {:>10.2f} | {:>10}".format(element['nimetus'], element['hind'], element['kogus']))
        else:
            print("Elementi {} ei eksisteeri.".format(nimetus))
        print("")

    def lisa_element(self, nimetus, hind, kogus):
        print("Elemendi lisamine")
        print("Lisatud {} hinnaga {}EUR koguses {}".format(nimetus, hind, kogus))

    def uuenda_element(self, nimetus, vana_hind, vana_kogus, uus_hind, uus_kogus):
        print("Elemendi {} uuendamine".format(nimetus))
        if(vana_hind != uus_hind):
            print("Muudetud hind: {} -> {}".format(vana_hind, uus_hind))
        if(vana_kogus != uus_kogus):
            print("Muudetud kogus: {} -> {}".format(vana_kogus, uus_kogus))
# Elemendide kustutamise sõnumid
    def kustuta_element(self, nimetus):
        print("Elemendi {} kustutamine".format(nimetus))
        print("Element {} on kustutatud elementide nimekirjast".format(nimetus))

    def kustuta_elemendid(self):
        print("Elemendid kustutati".format())
        print("Elemendid on kustutatud elementide nimekirjast".format())