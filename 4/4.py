from collections import Counter


def passphrase_no_duplicates(phrase):
    words = phrase.split()
    return len(words) == len(set(words))


def passphrase_no_anagrams(phrase):
    words = phrase.split()
    word_sets = []
    for word in words:
        w_ = Counter(word)
        if w_ not in word_sets:
            word_sets.append(w_)
        else:
            return False
    # word_sets = [set(word) for word in words]
    return True


print(passphrase_no_anagrams('oiii ioii iioi iiio'))
if __name__ == '__main__':
    p1_valid = p2_valid = 0
    with open('input.txt') as f:
        for line in f:
            if passphrase_no_duplicates(line):
                p1_valid += 1
            if passphrase_no_anagrams(line):
                p2_valid += 1
    print(p1_valid)
    print(p2_valid)
