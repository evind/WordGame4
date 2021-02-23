import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

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

#words = list(data.split("\n"))
#words = {line.strip("\n").replace("'s", "").lower() for line in words}  # A set.
#words = sorted(words)[1:]  # Ignore the empty word at the start of the list.

@anvil.server.callable
def create_dictionary():
  print(type(data))