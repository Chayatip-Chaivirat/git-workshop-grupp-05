from gustav import pizza
from hej_goblin2 import goblin_salute
def tres():
    nummer = int(input('skriv ett nummer')) 
    sum = 3 + nummer
    print(f'3+{nummer} ='f' {sum}')
    pizza()
    goblin_salute()
tres()
def ask_user_input(text):
   input(text)

def like_text():
   """Nåt är fel här"""
   ask_user_input("Skriv nåt: ")
   like_or_dislike = ask_user_input("Gillar du vad du har skrivit? ja/nej ")
   if like_or_dislike == "ja":
         print("Bra!")
   elif like_or_dislike == "nej":
      print("Oj då, skriv nåt nytt!")
   else:
      print("Välj ett giltig val!")

like_text()

def lol():
   print("Do you like League of Legends?")
   question = input("Answer with Yes or No: ")

   if question == "Yes":
      print("No you don't, you liar")
   elif question == "No":
      print("Good, you have a brain")
   else:
      print("The answer is no")
   
lol()

from hej_goblin import say_hi
say_hi()

