#complete CAPITALIZED sections

#AUTHOR:JessieWang
#DATE:7/12

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
        repo.git.add('/home/pi/FlatSatChallenge/Images/jessiewang/') #PATH TO YOUR IMAGES FOLDER, SHOULD BE LOCATED IN FlatSatChallenge/Images/YOURFOLDER
        repo.index.commit('scavenger hunt')
        print('made the commit')
        origin = repo.remote('origin')
        print('added remote')
        origin.push()
        print('pushed changes')
    except:
        print('Couldn\'t upload to git')


#SET THRESHOLD
threshold =14


#read acceleration
counter=0
while True and counter<1:
    accelX, accelY, accelZ = sensor.accelerometer

    #CHECK IF READINGS ARE ABOVE THRESHOLD
        #PAUSE
    if abs(accelX)>threshold  or abs(accelY)>threshold  or abs(accelZ) >threshold: 
        time.sleep(2)
        #TAKE/SAVE/UPLOAD A PICTURE
        name = "WangJ"     #Last Name, First Initial  ex. FoxJ
        if name:
            t = time.strftime("_%H%M%S")      # current time string
            imgname = ('/home/pi/FlatSatChallenge/Images/jessiewang/%s%s.jpg' % (name,t)) #change directory to your folder
            #<YOUR CODE GOES HERE>#
            camera.close()
            camera=PiCamera()
            camera.capture(imgname)
            git_push()
            counter+=1
    #PAUSE
    
