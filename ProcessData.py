#ProcessData.py
#Name: Tessa Horn
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
     
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    student_id = makeID(first, last, idNum)
    output = last + "," + first + "," + student_id + "\n"
    outFile.write(output)

  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  idLen = len(idNum)
  while len(last) < 5:
    last = last + "x"
  id = first[0] + last + idNum[idLen -3: ]
  return id 


  print(id)
 
  #Process each line of the input file and output to the CSV file

  #Close files in the end to save and ensure they are not damaged.
 

if __name__ == '__main__':
  main()
