import random

class Electrocasnice:
    reducere = str(20) + '%'
    numarElectrocasnice = 0

    def __init__(self, nume, marca, model, anFabricare, pret, garantie):
        self.nume = nume
        self.marca = marca
        self.model = model
        self.anFabricare = anFabricare
        self.pret = pret
        self.garantie = garantie
        self.descriere = self.nume + " marca " + self.marca + ', model ' + self.model + ', fabricat in ' + str(self.anFabricare) + ' ,cu pretul de ' + str(self.pret) + ' lei'
        Electrocasnice.numarElectrocasnice += 1

    def obtineDescriere(self):
        return self.descriere

    @classmethod
    def schimbaReducere(cls, reducereNoua):
        cls.reducere = str(reducereNoua) + '%'

    @staticmethod
    def garantieExtra(ani):
        if ani == 1:
            return f"Taxa pentru inca {ani} ani de garantie este de 60 de lei."
        elif ani == 3:
            return f"Taxa pentru inca {ani} ani de garantie este de 100 de lei."
        elif ani == 5:
            return f"Taxa pentru inca {ani} ani de garantie este de 130 de lei."
        else:
            return "Puteti sa alege un an, trei ani sau cinci ani de garantie extra."

    def __add__(self, other):
        return self.nume + ' vs ' + other.nume

    def pretProdus(self):
        if self.pret < 2000:
            return 'Pretul produsului este ok.'
        elif self.pret == 2000:
            return 'Pretul produsului este accesibil.'
        else:
            return 'Pretul produsului este mare.'

    def areGarantie(self):
        if self.garantie != 0:
            return f'Produsul {self.descriere} este in garantie {self.garantie} ani.'
        else:
            return f'Produsul {self.descriere} nu are garantie.'

    @property
    def pretRedus(self):
        return f'Pretul cu reducerea aplicata este de {self.pret / 5 * 4} lei.'

    @pretRedus.deleter
    def pretRedus(self):
        print('Reducerea a fost stearsa!')
        print(f'Pret actual este de {self.pret} lei.')

class CombinaFrigorifica(Electrocasnice):
    def __init__(self, nume, marca, model, anFabricare, pret, garantie , clasa, codReducere=False):
        super().__init__(nume, marca, model, anFabricare, pret, garantie)
        self.clasa = clasa
        self.codReducere = codReducere

    def obtineClasa(self):
        return self.clasa

    def __repr__(self):
        return "{} {}".format(self.nume, self.clasa)

    def schimbaModelul(self, noulModel):
        self.model = noulModel

    def schimbaMarca(self, nouaMarca):
        self.marca = nouaMarca

    def schimbaAnul(self, noulAn):
        self.anFabricare = noulAn

    def adaugaCodReducere(self):
        if self.codReducere is False:
            self.codReducere = random.random()

    def verificaCodReducere(self):
        if self.codReducere is False:
            return 'Acest produs nu are cod de reducere.'
        else:
            return f'Codul de reducere al acestui produs este {self.codReducere}.'

    def __str__(self):
        return "{} este redus cu {}, iar noul pret va fi de {} lei.".format(self.descriere, self.reducere, self.pret / 5 * 4)

    def __add__(self, other):
        return f'{self.nume} {self.marca} {self.clasa}  VS  {other.nume} {other.marca} {other.clasa}'

    def __len__(self):
        return len(self.nume)

produs1 = Electrocasnice('Cuptor incorporabil', 'ELECTROLUX', 'EOB9S31WX', 2019, 4000, 3)
produs2 = Electrocasnice('Cuptor cu microunde', 'ELECTROLUX', 'EVL6E40X', 2020, 1200, 2)
produs3 = Electrocasnice('Mixer de mana', 'Philips', 'HR3740/00', 2018, 1200, 2)

combinaFrigorifica1 = CombinaFrigorifica("Combina frigorifica", "ARCTIC", "AK54305M30MT", 2018, 1399, 5, 'clasa F')
combinaFrigorifica2 = CombinaFrigorifica("Combina frigorifica", "Heinner", "HC-V270SWDE++", 2019, 1550, 5, "clasa E")
combinaFrigorifica3 = CombinaFrigorifica("Combina frigorifica", "BEKO", "RCSA406K40DXBN", 2019, 1550, 5, "clasa E")

print(combinaFrigorifica3.areGarantie())