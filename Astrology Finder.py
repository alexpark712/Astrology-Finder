# Alex Park
# May 2021
# Astrology Calculator 

from datetime import datetime
import webbrowser

# Finds the user's birthday through prompts and turns it into a list
def birthday():
    valid_year = False
    valid_month = False
    valid_day = False
    while not valid_year:
        current_year = datetime.now().year
        year = int(input("\nWhat year were you born? "))   
        if year > current_year:
            print("\nThe year must be in the past. Please try again")
        else:
            valid_year = True
    while not valid_month:
        month = int(input("\nWhat month were you born? [1-12] "))
        if month < 1 or month > 12:
            print("\nThe month must be between 1 and 12. Please try again")
        else:
            valid_month = True
    while not valid_day:
        day = int(input("\nWhat day were you born? [1-31] "))
        if day < 1 or day > 31:
            print("\nThe day must be between 1 and 31. Please try again")
        else: 
            valid_day = True
    
    year = str(year)
    month = str(month)
    day = str(day)

    date = [month, day, year]
    return date

# Calculates the user's zodiac sign based on their birthday 
def zodiac_calculate():
    date = birthday()
    zodiac_sign = ""
    if date[0] == "1":
        if int(date[1]) <= 19:
            zodiac_sign = "capricorn"  
        else:
            zodiac_sign = "aquarius"
    elif date[0] == "2":
        if int(date[1]) <= 18:
            zodiac_sign = "aquarius"  
        else:
            zodiac_sign = "pisces"
    elif date[0] == "3":
        if int(date[1]) <= 20:
            zodiac_sign = "pisces"  
        else:
            zodiac_sign = "aries"
    elif date[0] == "4":
        if int(date[1]) <= 19:
            zodiac_sign = "aries"  
        else:
            zodiac_sign = "taurus"
    elif date[0] == "5":
        if int(date[1]) <= 20:
            zodiac_sign = "taurus"  
        else:
            zodiac_sign = "gemini"
    elif date[0] == "6":
        if int(date[1]) <= 20:
            zodiac_sign = "gemini"  
        else:
            zodiac_sign = "cancer"
    elif date[0] == "7":
        if int(date[1]) <= 22:
            zodiac_sign = "cancer"  
        else:
            zodiac_sign = "leo"
    elif date[0] == "8":
        if int(date[1]) <= 22:
            zodiac_sign = "leo"  
        else:
            zodiac_sign = "virgo"
    elif date[0] == "9":
        if int(date[1]) <= 22:
            zodiac_sign = "virgo"  
        else:
            zodiac_sign = "libra"
    elif date[0] == "10":
        if int(date[1]) <= 22:
            zodiac_sign = "libra"  
        else:
            zodiac_sign = "scorpio"
    elif date[0] == "11":
        if int(date[1]) <= 21:
            zodiac_sign = "scorpio"  
        else:
            zodiac_sign = "sagittarius"
    elif date[0] == "12":
        if int(date[1]) <= 21:
            zodiac_sign = "sagittarius"  
        else:
            zodiac_sign = "capricorn"

    return zodiac_sign

# A) Finds information about the user's zodiac sign characteristics from an online website
def characteristics():
    zodiac = zodiac_calculate() 

    vowels = ["a", "e", "i", "o", "u"]
    
    for each in vowels:
        if zodiac[0] == each:
            print("\nYou are an " + zodiac.capitalize() + "!\n")
        else:
            print("\nYou are a " + zodiac.capitalize() + "!\n")

    url = "https://www.astrology-zodiac-signs.com/zodiac-signs/" + zodiac + "/"
    webbrowser.open(url)

#B) Finds information about the user's Chinese zodiac sign from an online website
def chinese_zodiac():
    date = birthday()
    year = int(date[2])
    zodiac = ""
    if year % 12 == 0:
        zodiac = "monkey"
    elif year % 12 == 1:
        zodiac = "rooster"
    elif year % 12 == 2:
        zodiac = "dog"
    elif year % 12 == 3:
        zodiac = "pig"
    elif year % 12 == 4:
        zodiac = "rat"
    elif year % 12 == 5:
        zodiac = "ox"
    elif year % 12 == 6:
        zodiac = "tiger"
    elif year % 12 == 7:
        zodiac = "rabbit"
    elif year % 12 == 8:
        zodiac = "dragon"
    elif year % 12 == 9:
        zodiac = "snake"
    elif year % 12 == 10:
        zodiac = "horse"
    elif year % 12 == 11:
        zodiac = "sheep"

    vowels = ["a", "e", "i", "o", "u"]
    
    for each in vowels:
        if zodiac[0] == each:
            print("\nYou are an " + zodiac.capitalize() + "!\n")
        else:
            print("\nYou are a " + zodiac.capitalize() + "!\n")
  
    url = "https://chinesenewyear.net/zodiac/" + zodiac + "/"
    webbrowser.open(url)

#C) Finds information about the user's zodiac sign element from an online website
def element():
    zodiac = zodiac_calculate()
    element = ""
    if zodiac == "aries" or zodiac == "leo" or zodiac == "sagittarius":
        element = "fire"
    elif zodiac == "taurus" or zodiac == "virgo" or zodiac == "capricorn":
        element = "earth"
    elif zodiac == "gemini" or zodiac == "libra" or zodiac == "aquarius":
        element = "air"
    elif zodiac == "cancer" or zodiac == "scorpio" or zodiac == "pisces":
        element = "water"

    vowels = ["a", "e", "i", "o", "u"]

    for each in vowels:
        if zodiac[0] == each:
            print("\nYour zodiac is an " + element.capitalize() + "element!\n")
        else:
            print("\nYou zodiac is a " + element.capitalize() + "element!\n")

    url = "https://www.astrology.com/elements/" + element

    webbrowser.open(url)

#D) Finds information about the user's ephemeris based on their birth year from an online website
def ephemeris():
    date = birthday()
    year = date[2]

    print("\nEphemeris for " + year + "!\n")

    url = "https://www.astro.com/swisseph/ae/" + str(year[:2]) + "00" + "/ae_" + year + ".pdf"

    webbrowser.open(url)

# Main method that implements all the functions and shows a menu where a user selects what they want
def main():
    valid_input = False
    while not valid_input:
        print("\n-----------------------------------------------------------")
        print("A) Learn about my zodiac sign characteristics")
        print("B) Learn about my Chinese zodiac sign")
        print("C) Learn about my astrology element")
        print("D) Learn about my Ephemeris")
        print("E) Exit Program")
        select = input("\nSelect an option to learn more about your astrological sign: ")
        if select == "A":
            characteristics()
        elif select == "B":
            chinese_zodiac()
        elif select == "C":
            element()
        elif select == "D":
            ephemeris()
        elif select == "E":
            valid_input = True
            print("\nEnd of program.\n")

main()
    


