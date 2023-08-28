#!/usr/bin/env python3

class MyString:
  
  def __init__(self):
    self.value = ""
    
  def value(self):
    self._value = self.value
    
  def is_sentence(self):
    if self.value == '.':
      return True
    else:
      return False
    
  def is_question(self):
    if self.value == '?':
      return True
    else:
      return False
  
  def is_exclamation(self):
    if self.value == '!':
      return True
    else:
      return False
    
  def count_sentences(self):
    sentences = re.split(r'[.!?]', self.value)
    sentence_count = len([sentence for sentence in sentences if sentence.strip()])
    return sentence_count

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
sentence_count = string.count_sentences()
print(sentence_count)
#Output: 3'