# This is a Mad Libs word replacement game written in Python.
# First you will be asked to input a particular word/s, and this will be added to the Mad Lib script.
# Once this is done, you will have the opportunity to read the final script with your words.
# Credit to https://www.it.iitb.ac.in/ for the Mad Libs script
# Python code written by Kishav Dayanand

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a past tense verb: ")
adverb = input("Enter an adverb: ")
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
adverb1 = input("Enter an adverb: ")
verb2 = input("Enter a past tense verb: ")
adjective3 = input("Enter an adjective: ")

madlib =  " Today I went to the zoo. I saw a(n) " + adjective + " " + noun + " jumping up and down in its tree. \n " \
          "He " + verb + " " + adverb + " through the large tunnel that led \n " \
          "to its " + adjective1 + " " + noun1 + " . I got some peanuts and passed them through the cage to a gigantic \n " \
          "gray " + noun1 + " towering above my head. Feeding that animal made me hungry. I went to get a \n " \
          + adjective2 + " scoop of ice cream. It filled my stomach. Afterwards I had to " + verb1 + " \n " \
          + adverb1 + " to catch our bus. When I got home I " + verb2 + " my \n " \
          "mom for a " + adjective3 + " day at the zoo."

print(madlib)