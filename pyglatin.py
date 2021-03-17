#Nathan Li - Python Pig Latin Translator - 1/28/2021

pyg = "ay"

original = input("Enter a word:") #raw_input was renamed to input starting with python 3 :/

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print("empty")