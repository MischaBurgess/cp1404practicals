"""CP1404 Practical - Language information."""

from programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = []
    languages = [ruby, python, visual_basic]
    print("The dynamic languages are: ")
    for element in languages:
        if element.is_dynamic():
            print(element.name)


main()
