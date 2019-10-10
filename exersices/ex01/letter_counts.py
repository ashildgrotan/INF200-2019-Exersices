"""
EX01 task C. Counting letters.
"""


def letter_freq(txt):
    """
    Counts letters and symbols in a given string.
    :param txt: string to analyse
    :return: dictionary, {letter/symbol: count}
    """
    txt = txt.lower()
    frq = {}
    for l in txt:
        if l in frq:
            frq[l] += 1
        if l not in frq:
            frq[l] = 1
    return frq


if __name__ == "__main__":
    text = input("Please enter text to analyse: ")

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print("{:3}{:10}".format(letter, count))
