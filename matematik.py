import time
st=time.time()

#matematik til hastighed
pt = st
ct = st
dt = 0

a = int(input())
v = 0


vs=0

john=0

#tankmåler
tkmk=int((input("tast hvor meget")))
kml=22
ml=kml*1000
tank=5


while(True):
    pt = ct
    ct = time.time()
    dt = (ct - pt)
    v += a * dt
    if a!=0:
        vs=v

    #print(vs)
    john+=vs*dt
    #print(john)
    #tankmålerting
    
    mathias = john/ml
    #print(mathias)
    tank=tank-(mathias/1000)
    print(tank)
    #print(mathias)


