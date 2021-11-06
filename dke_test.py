from gpiozero import Button
from time import sleep

button = Button("GPIO17")

while True:
    if button.is_pressed:
        print("Pressed")
    sleep(0.25)