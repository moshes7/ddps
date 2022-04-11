import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def read():

    reader = SimpleMFRC522()

    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()

    pass


if __name__ == '__main__':

    read()

    pass