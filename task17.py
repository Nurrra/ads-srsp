def permutations(prefix, rest):
    if rest == "":
        print(prefix)
        return
    for i in range(len(rest)):
        permutations(prefix + rest[i], rest[:i] + rest[i + 1:])

permutations("", "ABC")