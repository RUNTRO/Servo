import board
import busio
import time
from adafruit_motor import servo
import pwmio

import adafruit_tcs34725

i2c = busio.I2C(board.GP3, board.GP2)  # uses first I2C SCA/SCL pair on pico
sensor = adafruit_tcs34725.TCS34725(i2c)

# Change sensor gain to 1, 4, 16, or 60
sensor_gain = 4

sensor.gain = sensor_gain
# Change sensor integration time to values between 2.4 and 614.4 milliseconds
sensor_integration_time = 150

sensor.integration_time = sensor_integration_time

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
cs_servo = servo.Servo(pwm)
cs_servo2 = servo.Servo(pwm2)


while True:
    cs_servo.angle = 0
    cs_servo2.angle = 0
    time.sleep(.5)
    cs_servo.angle = 180
    cs_servo2.angle = 180
    time.sleep(.5)
    print("Temperature: %d" % sensor.color_temperature)
    print(
        "r: %d, g: %d, b: %d"
        % (
            sensor.color_rgb_bytes[0],
            sensor.color_rgb_bytes[1],
            sensor.color_rgb_bytes[2],
        )
    )
    print("Lux: %d" % sensor.lux)
'''
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)# Write your code here :-)
'''
