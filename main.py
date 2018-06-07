import serial
import converter
import camera
import smpt

# must close arduino idea for this work
ser = serial.Serial('/dev/tty.usbmodemFA131',9600, timeout=5)

previousValue = 'null'
while True:
	print ser.readline()
    line = str(ser.readline())
    line = line.strip(' \t\n\r')
    if line == 0 and previousValue != 0 and previousValue != 'null':
        file = 'video.h264'
        recordVideo(file,3)
        toType = 'mp4'
        convertFile(file,toType)
        email = ''
        password = ''
        subject = 'From Raspberry Pi!'
        body = 'Test Body'
        server = 'smtp.gmail.com'
        port = 587
        video = 'video.mp4'
        messageBuilder = EmailMessageBuilder()
        messageBuilder.buildMessage(email,email,subject,body,video)
        messageBuilder.buildSMTPServer(server,port)
        messageBuilder.sendMessage(email,password)
    previousValue = line
    