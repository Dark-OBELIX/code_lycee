class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse
    
    def liste_octet(self):
        return[int(i) for i in self.adresse.split(".")]
    
    def est_reserve(self):
        return True if self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255' else False 

    def adresse_suivante(self):
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + f'{octet_nouveau}')
        else:
            return False

adresse1 = AdresseIP('192.168.0.0')
print(adresse1.adresse_suivante().adresse)
