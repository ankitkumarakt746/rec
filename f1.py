def clearSrc():
    os.system('clear' if os.name == 'posix' else 'cls')


def color(value):
    winToLin = {"0": "0", "1": "4", "2": "2", "3": "6", "4": "1", "5": "5", "6": "3", "7": "7", 
                "8": "0", "9": "4", "A": "2", "B": "6", "C": "1", "D": "5", "E": "3", "F": "7"}
    if os.name == "posix":
        os.system('tput setaf ' + winToLin[value])
    else:
        os.system('color ' + value)
