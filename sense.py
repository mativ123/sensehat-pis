from sense_hat import SenseHat
import math
sense = SenseHat()

while True:
    acc = sense.get_accelerometer_raw()
    x = acc['x']

    x=round(x, 0)

    print(f"{x}")

