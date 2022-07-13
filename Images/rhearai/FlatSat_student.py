#complete CAPITALIZED sections

#AUTHOR:Rhea Rai 
#DATE:7-12-2022 

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
import time

#function for uploading image to Github
def git_push():
    try:
        repo = Repo('/home/pi/FlatSatChallenge')
        repo.git.add('Images/rhearai/')

	 # repo.git.add('folder path') #PATH TO YOUR IMAGES FOLDER, SHOULD BE LOCATED IN FlatSatChallenge/Images/YOURFOLDER
        repo.index.commit('added photo')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')

    
#SET THRESHOLD
threshold = 10


#can delete this later, but num of photos so my program actually stops:
numPhotos = 0
limPhotos = 1

#read acceleration
while True and numPhotos < limPhotos:
    accelX, accelY, accelZ = sensor.accelerometer

    if (accelX>threshold or accelY>threshold or accelZ>threshold):
        time.sleep(3) #after it moves, it should wait a bit before taking photo
        #TAKE/SAVE/UPLOAD A PICTURE 
        name = "RaiR"     #Last Name, First Initial  ex. FoxJ
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            imgname = ('/home/pi/FlatSatChallenge/Images/rhearai/%s%s' % (name,t)) #change directory to your folder
            camera.start_preview()
            time.sleep(0.1)
            imgname = "rhearai_selfie" #for selfie
            camera.capture(imgname+'.jpg')
            camera.stop_preview()
            git_push()
            time.sleep(1)
            #<YOUR CODE GOES HERE>#
            numPhotos += 1
    #time.sleep(1)
    
#PAUSE
    
