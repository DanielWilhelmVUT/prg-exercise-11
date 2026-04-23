import random
import matplotlib.pyplot as plt


def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(seznam_cisel):
    novy_seznam_cisel = seznam_cisel.copy()
    delka = len(novy_seznam_cisel)

    for i in range(delka):
        min_index = i

        for j in range(i + 1, delka):
            if novy_seznam_cisel[j] < novy_seznam_cisel[min_index]:
                min_index = j
        novy_seznam_cisel[i], novy_seznam_cisel[min_index] = novy_seznam_cisel[min_index], novy_seznam_cisel[i]

    return novy_seznam_cisel


def bubble_sort(seznam_cisel):
    cisla = seznam_cisel.copy()
    delka = len(cisla)

    plt.ion()
    plt.show()

    for i in range(delka):
        for j in range(0, delka - i - 1):

            index_highlight1 = j
            index_highlight2 = j + 1


            colors = ["steelblue"] * len(cisla)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(cisla)), cisla, color=colors)
            plt.title("Bubble Sort - probublávání")
            plt.pause(0.05)


            if cisla[j] > cisla[j + 1]:
                cisla[j], cisla[j + 1] = cisla[j + 1], cisla[j]

    plt.ioff()
    plt.show()
    return cisla


if __name__ == "__main__":

    seznam_cisel = [5, 8, 11, 5, 14, 108, 55]
    print(f"puvodni: {seznam_cisel}")
    print(f"selection sort: {selection_sort(seznam_cisel)}")

    nahodny_seznam = random_numbers(10)
    print(f"nahodny seznam bubble Sort: {nahodny_seznam}")
    serazeny_bubble = bubble_sort(nahodny_seznam)
    print(f"bubble sort hotovy: {serazeny_bubble}")

