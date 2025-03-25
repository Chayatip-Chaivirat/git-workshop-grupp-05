def main():
   like()

def ask_user_input(text):
   ask = input(text)

def like():
   """Nåt är fel här"""
   ask_user_input("Skriv nåt: ")
   like_or_dislike = ask_user_input("Gillar du vad du har skrivit? ja/nej ")
   if like_or_dislike == "ja":
         print("Bra!")
   elif like_or_dislike == "nej":
      print("Oj då, skriv nåt nytt!")
   else:
      print("Välj ett giltig val!")

main()