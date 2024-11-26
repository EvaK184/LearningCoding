nouns2=[]
with open("nouns.txt", "r") as nouns:
 lines = nouns.readlines()
 for l in lines:
  words=l.split("\n")
  nouns2.append(words[0])

print(nouns2)
                
