import random


def nahodna_cisla(pocet, minimum=0, maximum=100):
    seznam = []
    for _ in range(pocet):
        seznam.append(random.randint(minimum, maximum))
    return seznam

class StudentsGrades:
    def __init__(self, body):
        self.scores = body

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.get_by_index(index)
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, hledane_body):
        indexy = []

        for i in range(len(self.scores)):
            if self.scores[i] == hledane_body:
                indexy.append(i)

        return indexy

    def get_sorted(self):
        kopie_bodu = self.scores.copy()

        n = len(kopie_bodu)

        for i in range(n):
            for j in range(0, n - i - 1):
                if kopie_bodu[j] > kopie_bodu[j + 1]:
                    kopie_bodu[j], kopie_bodu[j + 1] = kopie_bodu[j + 1], kopie_bodu[j]

        return kopie_bodu

if __name__ == "__main__":
    vysledky = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 20, 58])

    print(f"pocet studentu: {vysledky.count()}")


    for i in range(vysledky.count()):
        body = vysledky.get_by_index(i)
        znamka = vysledky.get_grade(i)
        print(f"student {i}: {body} points - {znamka}")

    print(f"studenti se 100 body: {vysledky.find(100)}")

    print(f"serazene vysledky: {vysledky.get_sorted()}")
    print(f"puvodni seznam (kontrola): {vysledky.scores}")


    data = nahodna_cisla(20, 0, 100)
    nahodni_studenti = StudentsGrades(data)
    print(f"nahodnych studentu: {nahodni_studenti.count()}")
    print(f"serazene body nahodnych: {nahodni_studenti.get_sorted()}")