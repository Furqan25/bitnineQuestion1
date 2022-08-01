import keyboard
import os
import re


def main():
    print("Please enter numbers to add or subtract:")
    try:
        keyboard.add_hotkey('esc', lambda: os._exit(0))
        while True:
            x = input()
            x = x.replace(" ", "")
            ui_beforestrip = re.split(r'(-+|\++|[(]|[)])', x)
            ui = [i for i in ui_beforestrip if i.strip()]

            for i, stuff in enumerate(ui):
                if stuff.isdigit() and int(stuff) > 100000000 or i == 0 and (stuff == "+"):
                    raise ValueError()
                elif stuff.isdigit():
                    ui[i] = int(stuff)
                elif stuff != "+" and stuff != "-" and stuff != "(" and stuff != ")":
                    raise ValueError()
            final = ''.join(str(x) for x in ui)
            print(eval(final))
    except ValueError:
        print("Number exceeded 100,000,000 or\nyou used symbols aside from + , - , (, )")


if __name__ == "__main__":
    main()
