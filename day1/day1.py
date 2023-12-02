def stripNumbers(sampleText: list[str]) -> list[int]:
    numbers = [parse(line) for line in sampleText]
    return numbers

def parse(line: str) -> int:
    numberChars = []
    for character in line:
        try:
            if int(character):
                numberChars.append(character)
        except:
            pass
    if len(numberChars) == 2:
        return int("".join(numberChars))
    elif len(numberChars) > 2:
        twoDigits = numberChars[0] + numberChars[-1]
        return int(twoDigits)
    elif len(numberChars) == 1:
        twoDigits = numberChars[0] + numberChars[0]
        return int(twoDigits)
    else:
        print("no digits in string")

def add(numbers: list[int]) -> int:
    return sum(numbers)

def numberReplacement(text: str) -> str:
    numberDict = {
        "one":"o1ne",
        "two":"t2wo",
        "three":"thr3ee",
        "four":"fo4ur",
        "five":"fi5ve",
        "six":"si6x",
        "seven":"sev7en",
        "eight":"ei8ht",
        "nine":"ni9ne"
    }
    
    replacedString = text

    for key in numberDict:
        # print(key)
        if key in replacedString.lower():
            replacedString = replacedString.replace(key, numberDict[key])
    return replacedString
                
def lineParser(text: list[str]) -> list[str]:
    formattedLines = []
    for line in text:
        formattedLines.append(numberReplacement(line))
    print(formattedLines)
    return formattedLines

if __name__ == "__main__":
    realText = [line.rstrip() for line in open("/Users/brennen/Documents/scripts/advent/puzzleInput.txt")]
    sampleText = [line.rstrip() for line in open("/Users/brennen/Documents/scripts/advent/day1/sampleInput.txt")]
    sampleTextPt2 = [line.rstrip() for line in open("/Users/brennen/Documents/scripts/advent/day1/sampleInputPt2.txt")]
    # numbers = stripNumbers(realText)
    # print(add(numbers))
    part2 = lineParser(realText)
    stripPart2 = stripNumbers(part2)
    print(add(stripPart2))
    