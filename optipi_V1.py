#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# init list with pin numbers
pinList = [2,3,4,15,17,18,22,23]

# Create a dictionary holding the relay numbers and the pins

pinOne = 2
pinTwo = 3
pinThree = 4
pinFour = 15
pinFive = 17
pinSix = 18
pinSeven = 22
pinEight = 23


def mainLoop(activePins, period):
  '''
  activePins should be a list of the active pins
  period should be how long each pin should stay on for
  '''

  #Prep
  GPIO.setmode(GPIO.BCM)
  for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

  try:
    n = 0
    while n != 1:
      for i in activePins:
        print str(i) + " Current Pin"
        GPIO.output(i, GPIO.LOW)
        time.sleep(period)
        GPIO.output(i, GPIO.HIGH)
        time.sleep(6)
    GPIO.cleanup()
  except KeyboardInterrupt:
    GPIO.cleanup()

# Testing

mainLoop([2,3,15,17], 14400 )
#mainLoop([17], 10)