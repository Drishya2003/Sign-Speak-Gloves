import subprocess
import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from mpu6050 import mpu6050

# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create instances for two ADS1115 devices
ads1 = ADS.ADS1115(i2c, address=0x48)  # Address for the first ADS1115 (0x48)
ads2 = ADS.ADS1115(i2c, address=0x49)  # Address for the second ADS1115 (0x49)

# Create an MPU6050 object
mpu = mpu6050(0x68)

# Define analog input channels for all eight inputs
channels = [
    AnalogIn(ads1, ADS.P0),
    AnalogIn(ads1, ADS.P1),
    AnalogIn(ads1, ADS.P2),
    AnalogIn(ads1, ADS.P3),
    AnalogIn(ads2, ADS.P0),
    AnalogIn(ads2, ADS.P1),
    AnalogIn(ads2, ADS.P2),
    AnalogIn(ads2, ADS.P3),
]

# Initialize variables to store data for each channel and MPU6050
c1, c2, c3, c4, c5, c6, c7, c8, gyrox, gyroy, gyroz = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
mpu_data = {}

# Loop to read the analog inputs and MPU6050 data continuously
while True:
    # Read data from MPU6050
    temp = mpu.get_temp()
    accel_data = mpu.get_accel_data()
    accx, accy, accz = accel_data['x'], accel_data['y'], accel_data['z']
    gyro_data = mpu.get_gyro_data()
    gyrox, gyroy, gyroz = gyro_data['x'], gyro_data['y'], gyro_data['z']
    time.sleep(2)

    # Store MPU6050 data in a dictionary
    mpu_data = {
        'temp': temp,
        'accx': accx,
        'accy': accy,
        'accz': accz,
        'gyrox': gyrox,
        'gyroy': gyroy,
        'gyroz': gyroz
    }

    # Read data from ADS1115 channels
    for i, channel in enumerate(channels):
        if i == 0:
            c1 = channel.value
        elif i == 1:
            c2 = channel.value
        elif i == 2:
            c3 = channel.value
        elif i == 3:
            c4 = channel.value
        elif i == 4:
            c5 = channel.value
        elif i == 5:
            c6 = channel.value
        elif i == 6:
            c7 = channel.value
        elif i == 7:
            c8 = channel.value

    # Print values for debugging
    print(c3)
    print(c1)
    print(gyrox)
    print(gyroy)
    print(gyroz)

    # Check conditions and use espeak to pronounce letters
    if c1 > 1500000 and c1 < 15900 and c2 > 15000 and c2 < 16000 and c3 > 15000 and c3 < 16000 and c4 > 15000 and c4 < 16000 and c5 > 15000 and c5 < 16000:
        alphabet = "a"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 17000 and c2 > 16000 and c2 < 23000 and c3 > 18000 and c3 < 25000 and c4 > 15000 and c4 < 27000 and c5 > 17500 and c5 < 26500:
        alphabet = "b"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15600 and c1 < 25000 and c2 > 17500 and c2 < 29000 and c3 > 17000 and c3 < 30000 and c4 > 15500 and c4 < 23000 and c5 > 19500 and c5 < 25000:
        alphabet = "c"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 17500 and c1 < 25000 and c2 > 17500 and c2 < 22000 and c3 > 19000 and c3 < 23000 and c4 > 17500 and c4 < 26000 and c5 > 17800 and c5 < 22000:
        alphabet = "d"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 17000 and c1 < 25000 and c2 > 16000 and c2 < 22000 and c3 > 17000 and c3 < 26000 and c4 > 17500 and c4 < 26000 and c5 > 15000 and c5 < 25000:
        alphabet = "e"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 17000 and c1 < 23000 and c2 > 18000 and c2 < 26000 and c3 > 15500 and c3 < 27000 and c4 > 18500 and c4 < 23000 and c5 > 17500 and c5 < 23000:
        alphabet = "f"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 17500 and c1 < 23000 and c2 > 17500 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "g"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 30000 and c2 > 15000 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "h"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 30000 and c2 > 15000 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "i"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 30000 and c2 > 15000 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "j"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 30000 and c2 > 15000 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "k"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 30000 and c2 > 15000 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "l"
        for letter in alphabet:
            subprocess.run(["espeak", letter])
    elif c1 > 15000 and c1 < 30000 and c2 > 15000 and c2 < 30000 and c3 > 15000 and c3 < 30000 and c4 > 15000 and c4 < 30000 and c5 > 15000 and c5 < 30000:
        alphabet = "m"
        for letter in alphabet:
            subprocess.run(["espeak", letter])

    time.sleep(2)
