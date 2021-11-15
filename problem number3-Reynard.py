import re


def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    return sum([len(word) for word in words]) / len(words)


if __name__ == "__main__":
    print (avg_word_length('66689-0.txt'))