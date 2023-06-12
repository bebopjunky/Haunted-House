import re

def words(filename):
  with open(filename) as textfile:
    items = re.split(r'\W+', textfile.read())

  return items

def lines(filename):
  with open(filename) as textfile:
    items = textfile.read().split('\n')

  return items