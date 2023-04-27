class Symbole:
    def __init__(self, symbol, weight):
        self.symbol = symbol
        self.weight = weight
        self.kod = ""

    def __repr__(self) -> str:
        return f"{self.symbol}, {self.kod}"


def wylicz(symbole):
    if len(symbole) > 1:
        roznica, przydzial = 1, 0
        for i in range(1, len(symbole)):
            left = symbole[:i]
            right = symbole[i:]
            lewa = sum([x.weight for x in left])
            prawa = sum([x.weight for x in right])
            if (x := abs(lewa - prawa)) < roznica:
                roznica = x
                przydzial = i
        return (
            wylicz(symbole[:przydzial]),
            wylicz(symbole[przydzial:]),
        )
    else:
        return symbole


def generuj(symbole, kod=""):
    if isinstance(symbole, tuple):
        generuj(symbole[0], kod + "0")
        generuj(symbole[1], kod + "1")
    elif isinstance(symbole, list):
        generuj(symbole[0], kod)
    else:
        symbole.kod = kod
        return


def koduj(s, p):
    symbole = [Symbole(s[i], p[i]) for i in range(len(S))]
    symbole.sort(key=lambda x: -x.weight)
    symbole = wylicz(symbole)
    generuj(symbole)
    print(symbole)


S = ["a", "i", "s", "d"]
P = [0.33, 0.27, 0.15, 0.25]
koduj(S, P)
