import base64

with open ('C:\\Users\\Bismarck Afuzie\\Downloads\\Icons\\positive.png', 'rb') as image2string:
    converted_string = base64.b64encode (image2string.read ())
    print (converted_string.decode ('utf-8'))

with open ('C:\\Users\\Bismarck Afuzie\\Downloads\\Icons\\encode.txt', 'wb') as file:
    file.write (converted_string)

file = open ('C:\\Users\\Bismarck Afuzie\\Downloads\\Icons\\encode.txt', 'rb')
byte = file.read ()
file.close ()

decodeit = open ('positive2.jpg', 'wb')
decodeit.write (base64.b64encode ((byte)))
decodeit.close ()
