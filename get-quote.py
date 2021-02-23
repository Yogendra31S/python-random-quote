import random   
def main():
  #print("Keep it logically awesome.")   

  f = open("quotes.txt")
  quotes = f.readlines()
  last = len(quotes)- 1 
  f.close()

     
  rnd = random.randint(0, last) 
  print(quotes[rnd])

if __name__== "__main__":
  main()

