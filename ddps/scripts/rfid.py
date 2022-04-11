import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def play1():

    reader = SimpleMFRC522()

    try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
    finally:
        GPIO.cleanup()

    pass


if __name__ == '__main__':

    play1()

    pass