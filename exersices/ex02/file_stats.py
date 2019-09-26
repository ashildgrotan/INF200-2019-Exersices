def char_counts(textfilename):
    """
    Reads the text file textfilename as a string and counts how many times each symbols appears in the file
    :param textfilename: a text file with encoding UTF-8
    :return: List where index represents the code 0-255.
    """
    word_file = open(textfilename).read()
    symbols = [0]*256
    for symbol in word_file:
        symbols[ord(symbol)] += 1
    return symbols


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
