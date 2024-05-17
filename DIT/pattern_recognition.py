
def brute_force(text, pattern):
    """
    Function that returns a list of indexes with a pattern match
    :param text:
    :param pattern: sequence of chars; pattern that is searched
    :return:
    """
    patt_length = len(pattern)
    match_list = []

    for i in range(len(text) - patt_length + 1):
        j = 0

        while j < patt_length:
            if text[i + j] != pat[j]:
                break
            j += 1

        if j == patt_length:
            match_list.append(j)

    return match_list


# Driver's Code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"

    # Function call
    print(brute_force(txt, pat))

# This code is contributed
# by PrinciRaj1992