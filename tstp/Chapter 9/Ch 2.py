import csv

x = input("What is your favorite color?")
y = input("What color is ylour car?")

xy = open("xy.csv", "a", newline='')
w=csv.writer(xy, delimiter=",")
w.writerow(x)
w.writerow(y)
xy.close()    
