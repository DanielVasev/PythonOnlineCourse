# create new file and write a text

fw = open("sample.txt", "w")
fw.write("Hello this is my new file...\n")
fw.write("This is my new line in the text!")
fw.close()

fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()



#Read the new file or any text file

#close the functionality
