"""""
Hex Colours task CP1404
Mischa Burgess
"""""

colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "azure1": "#f0ffff", "blue1": "#0000ff",
           "BlueViolet": "#8a2be2", "chartreuse1": "#7fff00", "cyan2": "#00eeee", "DarkGreen": "#006400",
           "DarkOrchid": "#9932cc", "DarkSalmon": "#e9967a"}  # create a hex colour dictionary

colour_choice = input("Enter the name of the colour you would like: ")
while colour_choice != "":  # while colour choice isn't empty
    print("The colour code for {} is {}".format(colour_choice, colours.get(colour_choice)))  # return colour code
    colour_choice = input("Enter the name of the colour you would like: ")



