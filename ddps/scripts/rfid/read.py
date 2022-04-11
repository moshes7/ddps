import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

def read():

    reader = SimpleMFRC522()

    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()

    pass


def read_with_tries(num_tries=5, pause_time=0.5):

    reader = SimpleMFRC522()

    is_rfid = False

    for n in range(num_tries):

        try:
            id, text = reader.read()
            print(id)
            print(text)

            is_rfid = True
            break

        finally:
            GPIO.cleanup()

        time.sleep(pause_time)


if __name__ == '__main__':

    read()

    pass