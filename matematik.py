import time

# Get input for tank measurement (l)
fuel = int(input("Enter amount for tank measurement: "))

# Set fuel efficiency (km/l)
kml = 22

# Get input for acceleration (m/s^2)
a = int(input("Enter acceleration:"))

# Initialize speed (m/s), distance (m) and time, previous time 
v, d, t,pt = 0, 0, fuel, time.time()

while True:
    ct = time.time()
    dt = ct-pt
    pt = ct
    v += a * dt
    v_km_per_s = v / 1000
    d += v_km_per_s * dt
    fuel_consumption = v_km_per_s * dt / kml
    t -= fuel_consumption
    print("Speed: {:.2f} km/h Distance: {:.2f} km Fuel: {:.2f} L".format(v, d, t))
    if t <= 0:
        print("Fuel is empty, the journey has ended.")
        break
