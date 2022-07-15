

# Send a WhatsApp Message to a Contact at 1:30 PM
#pywhatkit.sendwhatmsg("+989149236907", "Hi", 15, 1)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
#pywhatkit.sendwhats_image("+989933518768", "C:\\Users\\admin\\Desktop\\main.py\\pic\\image1.jpg", "Hello")

# Send an Image to a Contact with the no Caption
#ywhatkit.sendwhats_image("+989149236907", "C:\\Users\\admin\\Desktop\\main.py\\pic\\image1.jpg",'ii')
import datetime
m=datetime.datetime.now()
print(m.minute)