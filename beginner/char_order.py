# NOTE:
# Alternatively, create a graph of all chars with compatible orders wrt dict, then find topological order of that graph!


def char_order(dictionary):
    """
    Given a sorted dictionary (array of words) of an alien language, find order of characters in the language.

    https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/

    """

    assert len(dictionary) > 1

    chars = [dictionary[0][0]]

    for i in range(len(dictionary)-1):
        this_word = dictionary[i]
        next_word = dictionary[i+1]
        for i, j in zip(this_word, next_word):
            if i == j:
                continue
            else:
                bi = i in chars
                bj = j in chars
                if not bi and not bj:
                    chars.insert(0, i)
                    chars.append(j)
                elif bi and not bj:
                    chars.insert(chars.index(i)+1, j)
                elif not bi and bj:
                    chars.insert(max(0, chars.index(j)-1), i)
                else:
                    index_i = chars.index(i)
                    index_j = chars.index(j)
                    if index_i > index_j:
                        chars[index_i], chars[index_j] = j, i
                break

    return chars


if __name__ == '__main__':

    d = ["baa", "abcd", "abca", "cab", "cad"]
    # d = ["caa", "aaa", "aab"]

    print(char_order(d))
