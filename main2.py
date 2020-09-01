# Main.py

import cv2
import numpy as np
import os
import sqlite3
import DetectChars
import DetectPlates
import PossiblePlate
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import time
import wiringpi
GPIO.setmode(GPIO.BOARD)
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
delay_period = 0.07
GPIO.setup(11,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
camera = PiCamera()

while True:
    print "Waiting..."
    sleep(10)
    GPIO.output(16,0)
    GPIO.output(15,0)
    GPIO.output(11,0)
    print "Taking photo"
    sleep(3)
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Downloads/License_Plate_Recognition/LicPlateImages/image.jpg')
    camera.stop_preview()

    # module level variables ##########################################################################
    SCALAR_BLACK = (0.0, 0.0, 0.0)
    SCALAR_WHITE = (255.0, 255.0, 255.0)
    SCALAR_YELLOW = (0.0, 255.0, 255.0)
    SCALAR_GREEN = (0.0, 255.0, 0.0)
    SCALAR_RED = (0.0, 0.0, 255.0)

    showSteps = False
    print "Recognizing..."
    ###################################################################################################
    def main():

        blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()         # attempt KNN training

        if blnKNNTrainingSuccessful == False:                               # if KNN training was not successful
            print "\nerror: KNN traning was not successful\n"               # show error message
            return                                                          # and exit program
        # end if

        imgOriginalScene  = cv2.imread("/home/pi/Downloads/License_Plate_Recognition/LicPlateImages/image.jpg")               # open image

        if imgOriginalScene is None:                            # if image was not read successfully
            print "\nerror: image not read from file \n\n"      # print error message to std out
            os.system("pause")                                  # pause so user can see error message
            return                                              # and exit program
        # end if

        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           # detect plates

        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)        # detect chars in plates

   
        if len(listOfPossiblePlates) == 0:                          # if no plates were found
            print "\nno license plates were detected\n"             # inform user no plates were found
             
        else:                                                       # else
                    # if we get in here list of possible plates has at least one plate

                    # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
            listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

                    # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
            licPlate = listOfPossiblePlates[0]

        
            if len(licPlate.strChars) == 0:                     # if no chars were found in the plate
                print "\nno characters were detected\n\n"       # show message
                 
                return                                          # and exit program
            # end if
            firstpart, secondpart = licPlate.strChars[:len(licPlate.strChars)/2], licPlate.strChars[len(licPlate.strChars)/2:]

            print "\nlicense plate read from image = " + secondpart + "\n"       # write license plate text to std out
            conn=sqlite3.connect('platenumber.db')
            curs=conn.cursor()
            
            print "\nDatabase entries for the garage:\n"
            for row in curs.execute("SELECT * FROM CarAccount WHERE PlateNo=(?)",(secondpart,)):   
                print row
                if row[6] == 0:
                    GPIO.output(11,1)
                    for pulse in range(50, 115, 1):
                        wiringpi.pwmWrite(18, pulse)
                        time.sleep(delay_period)
                    sleep(10)    
                    for pulse in range(115, 50, -1):
                        wiringpi.pwmWrite(18, pulse)
                        time.sleep(delay_period)
                elif row[6] == 1:
                    GPIO.output(16,1)
                break    
            else:
                GPIO.output(15,1)
                    
        return
    # end main
    
    ###################################################################################################

    ###################################################################################################


    ###################################################################################################
    if __name__ == "__main__":
        main()


