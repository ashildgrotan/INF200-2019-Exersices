from src.ashild_grotan_ex.ex01.letter_counts import letter_freq
from math import log2


def entropy(message):
    """
    takes a string and calculates the message entropy of the string
    :param message: str
    :return: float
    """
    msg_freq = letter_freq(message)
    total = len(message)
    msg_entropy = 0
    for i in msg_freq:
        msg_entropy -= msg_freq[i] / total * log2(msg_freq[i] / total)
    return msg_entropy


if __name__ == "__main__":
    for msg in "", "aaaa", "aaba", "abcd", "This is a short text.":
        print("{:25}: {:8.3f} bits".format(msg, entropy(msg)))
