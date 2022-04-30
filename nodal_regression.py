#!/usr/bin/env python3
import matplotlib.pyplot as plt
from math import pi,sin,cos

G  = 6.6743e-11
M  = 5.9722e24
J2 = 1.08262668e-3
RE = 6371000
nm = 1851.851

rp = 200000

alts  = [200,400,500,1000,2000]
incs = range(91)

lo  = list(range(91))
los = []

for alt in alts:
    alt = alt*1000
    a  = alt+RE
    T  = (4*pi**2*a**3/(G*M))**0.5
    n  = 86400/T*360
    c  = a-rp-RE
    e  = c/a

    for i in incs:
        Omegadot = -3/2 * n * J2 * (RE/a)**2 * cos(i/180*pi)/((1-e**2)**2)
        lo[i] = Omegadot
        if i==0:
            print(lo[i])
    los.append(list(lo))

fig, ax = plt.subplots()

plt.plot(incs,los[0],label='altitude 200 km')
plt.plot(incs,los[1],label='altitude 400 km')
plt.plot(incs,los[2],label='altitude 500 km')
plt.plot(incs,los[3],label='altitude 1000 km')
plt.plot(incs,los[4],label='altitude 2000 km')

plt.xlim([0,90])
plt.ylim([0,-9])

plt.text(3,-0.4,"Nodes move:\nWestward if orbit inclination\nis between 0° and 90°\n(direct orbit)\nEastward if orbit inclination\nis between 90° and 180°\n(retrograde orbit)",backgroundcolor='1.0')
#plt.title("Apsidal rotation rate as a function of inclination")
plt.ylabel("Nodal regression $-$ degrees per mean solar day")
plt.xlabel("Orbital inclination $-$ degrees")

plt.xticks([15,30,45,60,75,90])

plt.legend()
plt.grid(True)
plt.show()
