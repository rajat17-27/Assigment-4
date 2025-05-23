
try:

  file1 = open('sample.txt','r')

  read_file1 = file1.read()
  print(read_file1)
  file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


