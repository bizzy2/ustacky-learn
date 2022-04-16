filename = open ('file.txt', )
filename2 = filename.read ()
print (filename2)
print ('*' * 120)
print (filename.readline ())
print ('*' * 120)
# looping through lines in files
for line in filename:
    print (line)

# writing a new file
filename3 = open ('file2.txt', 'w')
filename3 = filename3.write ('Who are you.')
# appending to the file, note with the append python can still create the file if not exist
filename3 = open ('file2.txt', 'a')
filename3.write ('\nBismarck is a billionaire in a making and soon he will shine.')
filename3.write ('\nBismarck is a billionaire in a making and soon he will shine.')
filename3.write ('\nBismarck is a billionaire in a making and soon he will shine.'*20)

