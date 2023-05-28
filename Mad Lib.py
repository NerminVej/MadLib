import pyinputplus as pyip
from pathlib import Path

"""
This is a Mad Libs program
It reads in text files and lets the user add their own text anywhere the word DJECTIVE, NOUN, ADVERB, or VERB appears.

Step 1: Use Path to open a txt file that has the Mad Lib text inside it.
Step 2: Do the inputs with pyinputplus for all 4 words
Step 3: Use .replace() to replace the 4 words in the madLibsText string
Step 4: Use open with the write mode to write to a new txt file
"""
# Step 1: Use Path to open a txt file that has the Mad Lib text inside it.
p = Path("madlib.txt")
madLibText = p.read_text()

# Step 2: Do the inputs with pyinputplus for all 4 words
adjective = pyip.inputStr("Enter an adjective:")
noun = pyip.inputStr("Enter an noun: ")
verb = pyip.inputStr("Enter an verb: ")
adverb = pyip.inputStr("Enter an adverb: ")

# Step 3: Use .replace() to replace the 4 words in the madLibsText string

madLibText = madLibText.replace("ADJECTIVE", adjective)
madLibText = madLibText.replace("NOUN", noun)
madLibText = madLibText.replace("ADVERB", adverb)
madLibText = madLibText.replace("VERB", verb)

#Step 4: Use open with the write mode to write to a new txt file

userMadLib = open("usermadlib.txt", "w")
userMadLib.write(madLibText)


print(madLibText)

