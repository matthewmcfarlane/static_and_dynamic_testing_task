### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # == is the correct comparison operator
      return True
    else  #needs a colon after else
      return False
   

  dif highest_card(self, card1 card2): #def not dif....comma between paramaters card1, card2

  #expected indentation of code block
  if card1.value > card2.value: 
    return card #card is not defined, should be card1
  else:
    return card2
  


def cards_total(self, cards):#expected indentation - method must be inside class
  total #variable needs to be assigned an initial value, total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total  #cannot add an int to a string, must convert to a string using str(total). return must be outside for loop
  
```
