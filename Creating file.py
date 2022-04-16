# w,x,a can be used to create new files
# ('file3.csv', 'x')
# delete a file
# Then delete file
import os

# os.remove ('file2.txt')

# Deleting when a file exists using if statement
if os.path.exists ('file2.txt') == True:
    os.remove ('file2.txt')
else:
    print ('False')
