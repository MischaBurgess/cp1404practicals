"""
Wiki.py CP1404 Practical
Mischa Burgess
"""

import wikipedia

search_title = input("Please enter your Wikipedia search phrase: ")
while search_title != '':
    try:
        print("Title: {}".format(search_title))
        print("Summary: {}\n".format(wikipedia.summary(search_title)))
        print("Url: {}".format(wikipedia.page.url(search_title)))
        search_title = ''
    except wikipedia.exceptions.DisambiguationError:
        search_title = input("Please enter your Wikipedia search phrase: ")
        pass

