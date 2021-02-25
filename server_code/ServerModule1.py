import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import random
from . import Globals
from datetime import datetime


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:


# Load and parse words file from Google Drive.
# Then create a source_word_list from all words greater than 8 characters.
data = app_files.words.get_bytes().decode()
words = list(data.split("\n"))
words = {line.strip("\n").replace("'s", "").lower() for line in words}  # A set.
words = sorted(words)[1:]  # Ignore the empty word at the start of the list.
source_word_list = [ word for word in words if len(word) > 7 ]


@anvil.server.callable
def pick_source_word():
    """Returns a random word from the source_word_list."""
    random_int = random.randint(0, len(source_word_list) - 1)
    return source_word_list[random_int]
  
  
@anvil.server.callable
def calculate_time(curr_time, end_time):
  total_time = round(end_time - curr_time, 2)
  return total_time
  
  
@anvil.server.callable
def evaluate_answer(source_word, user_input_list):
  """Sets up a dictionary to keep track of errors made in the user's answer.
     Evaluate the user's answer based on the following rules:
       1. Only seven words are allowed.
       2. User may not reuse letters.
       3. Words must exist in the dictionary (words list).
       4. Words must 4 characters or more in length.
       5. Words must not be a duplicate of a previous word.
       6. Words must not be the source word.
  """
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
    # 2. Check if word exists in words list.
    if word not in words:
        rules['invalid_words'].append(word)
        rules['valid_input'] = False
    # 3. Check if word is 4+ letters.
    if len(word) < 4:
        rules['small_words'].append(word)
        rules['valid_input'] = False
    # 4. Check if word is duplicate.
    if word in prev_words:
        rules['duplicate_words'].append(word)
        rules['valid_input'] = False
    prev_words.append(word)
    # 5. Check if word is source word.
    if word == source_word:
        rules['source_word_check'] = True
        rules['valid_input'] = False
  return rules
          

@anvil.server.callable
def generate_errors(rules):
  """Build a list representing the errors in the user's answer."""
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
  
  
@anvil.server.callable
def log_attempt(new_rules, new_source_word, new_user_input_list, new_user_agent):
  """Record data about each attempt in the log table."""
  app_tables.log.add_row(
      won=new_rules['valid_input'],
      source_word=new_source_word,
      guesses=", ".join(new_user_input_list),
      datetime=datetime.now(),
      ip_address=anvil.server.context.client.ip,
      user_agent=new_user_agent
    )

  
@anvil.server.callable
def log_score(new_time, new_name, new_source_word, new_matches):
  """Record data about each victory and the scores table."""
  app_tables.scores.add_row(
    time=new_time,
    name=new_name,
    source_word=new_source_word,
    matches=", ".join(new_matches)
  )
  
  
@anvil.server.http_endpoint('/get-user-agent')
def get_user_agent():
  """Function to help obtain user-agent data."""
  return {'user-agent': anvil.server.request.headers['user-agent']}
  
  
@anvil.server.callable()
def get_scores():
  """Query the scores table, sorting entries by lowest-time-first.
     Return a dictionary with this data."""
  scores = []
  for row in app_tables.scores.search(tables.order_by("time", ascending=True)):
    scores.append({
      'rank': 0,
      'time': round(row['time'], 2),
      'name': row['name'],
      'source_word': row['source_word'],
      'matches': row['matches']})
  return scores
  
  
@anvil.server.callable
def get_logs():
  """Query the log table, return a dictionary of the entries."""
  logs = []
  for row in app_tables.log.search():
    logs.append({
      'won': row['won'],
      'source_word': row['source_word'],
      'guesses': row['guesses'],
      'datetime': row['datetime'],
      'ip_address': row['ip_address'],
      'user_agent': row['user_agent']
    })
  return logs
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  