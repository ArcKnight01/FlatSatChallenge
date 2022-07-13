#complete CAPITALIZED sections

#AUTHOR: 
#DATE:

#import libraries
import time
import os
import board
import busio
import adafruit_fxos8700
from git import Repo
from picamera import PiCamera

#setup imu and camera
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxos8700.FXOS8700(i2c)
camera = PiCamera()

#function for uploading image to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge')
        repo.git.add('Images/tonyzhou') #PATH TO YOUR IMAGES FOLDER, SHOULD BE LOCATED IN FlatSatChallenge/Images/YOURFOLDER
        repo.index.commit('New Photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')

    
#SET THRESHOLD
threshold = 1000 


#read acceleration
while True:
    accelX, accelY, accelZ = sensor.accelerometer
    name = "ZhouT"
    #CHECK IF READINGS ARE ABOVE THRESHOLD
        #PAUSE

    
        #TAKE/SAVE/UPLOAD A PICTURE 
        #name = "ZhouT"     #Last Name, First Initial  ex. FoxJ
    if name:
         t = time.strftime("_%H%M%S")      # current time string
         imgname = ('/home/pi/FlatSatChallenge/Images/tonyzhou/%s%s' % (name,t)) #change directory to your folder
    
            #<YOUR CODE GOES HERE>#
            
    
    #PAUSE
    
