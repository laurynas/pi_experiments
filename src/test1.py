#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

prev_input = 0

while True:
  input = GPIO.input(17)

  if (input != prev_input):
    prev_input = input

    GPIO.output(22, input)

    if input:
      print("Button pressed")

  time.sleep(0.05)

