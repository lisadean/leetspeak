def translate(input):
    output = ""
    for c in input:
        output += substitute(c)
    return output


def substitute(input):
    original = "AEGIOST"
    translation = "4361057"
    input = input.upper()
    if input in original:
        output = translation[original.index(input)]
    else:
        output = input
    return output


def main():
    input = "elite speak"
    print(translate(input))


main()
