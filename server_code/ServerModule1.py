import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import random
from . import Globals

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
# Load files from Google Drive, parse + combine original words list with new_words list
data = app_files.words.get_bytes().decode()
words = list(data.split("\n"))
words = {line.strip("\n").replace("'s", "").lower() for line in words}  # A set.
words = sorted(words)[1:]  # Ignore the empty word at the start of the list.
source_word_list = []


@anvil.server.callable
def pick_source_word():
    global source_word_list, words
    for word in words:
        if len(word) >= 8:
            source_word_list.append(word)
    random_int = random.randint(0, len(source_word_list) - 1)
    return source_word_list[random_int]
  
  
@anvil.server.callable
def calculate_time(curr_time, end_time):
  total_time = round(end_time - curr_time, 4)
  return total_time
  
  
@anvil.server.callable
def evaluate_answer(source_word, user_input_list):
  rules = {'valid_input': True, 'word_count':len(user_input_list), 'invalid_letters': [],
      'invalid_words': [], 'small_words': [],
      'duplicate_words': [], 'source_word_check': False}
  prev_words = []
  
  if rules['word_count'] != 7:
    rules['valid_input'] = False
    
  for word in user_input_list:
    temp_list = list(source_word)
    # 1. check if word made from letters in source word
    for ch in word:
        if ch in temp_list:
            temp_list.remove(ch)
        else:
            if ch not in rules['invalid_letters']:
                rules['invalid_letters'].append(ch)
            rules['valid_input'] = False
    # 2. check if word exists in dictionary
    if word not in words:
        rules['invalid_words'].append(word)
        rules['valid_input'] = False
    # 3. check if word is 4+ letters
    if len(word) < 4:
        rules['small_words'].append(word)
        rules['valid_input'] = False
    # 4. check if word is duplicate
    if word in prev_words:
        rules['duplicate_words'].append(word)
        rules['valid_input'] = False
    prev_words.append(word)
    # 5. check if word is source word
    if word == source_word:
        rules['source_word_check'] = True
        rules['valid_input'] = False
  return rules
          

@anvil.server.callable
def generate_errors(rules):
  errors = []
  if rules['word_count'] != 7:
    errors.append("Invalid number of words: {0} / 7".format(rules['word_count']))
  if rules['invalid_letters']:
    errors.append("Invalid letters: " + ", ".join(rules['invalid_letters']))
  if rules['invalid_words']:
    errors.append("Invalid words: " + ", ".join(rules['invalid_words']))
  if rules['small_words']:
    errors.append("Small words: " + ", ".join(rules['small_words']))
  if rules['duplicate_words']:
    errors.append("Duplicate words: " + ", ".join(rules['duplicate_words']))
  if rules['source_word_check']:
    errors.append("You may not use the source word!")
  
  return errors
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  