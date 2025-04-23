filename = input("Enter file name:")

try:
    file = open(filename,'r')
    data = file.read()
    file.close()

except FileNotFoundError:
    print("Error: File not found.")

except IOError:
    print("Error: Unable to read file")

else:
    new_file = open("modified_" + filename,'w')
    new_file.write(data.upper())
    new_file.close()
    print("Modified file saved as 'modified_" + filename + "'")
    
finally:
    print("Complete! Have a nice day.")