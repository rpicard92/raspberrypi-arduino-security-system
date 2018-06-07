import os
import subprocess


# convert file
def convertH264toMP4(file):
    print 'Converting file from .h264 format to .mp4 format.'
    command = "MP4Box -add {} {}.mp4".format(file, os.path.splitext(file)[0])
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        print 'Converstion successful.'
    except subprocess.CalledProcessError as e:
        print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))    

# find the correct converter for the file.
def convertFile(file,toType):
    # get file extension
    fileExtension = file.split('.')[1]
    # .h264 to .mp4
    if (fileExtension == 'h264' and toType == 'mp4'):
        convertH264toMP4(file)
    else:
        print 'No conversion function in place for these file types. Note: Do not include "." when specifying toType.' 
            

