

def solution(phrase):
    fin_phrase = ''
    for element in range(0, len(phrase)):
        if phrase[element].islower():
            fin_phrase += chr(ord('z') - ord(phrase[element]) + ord('a'))
        else:
            fin_phrase += phrase[element]
    return fin_phrase


def main():
    print(solution("aBc"))


if __name__ == "__main__":
    main()
