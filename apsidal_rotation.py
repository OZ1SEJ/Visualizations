#!/usr/bin/env python3
import matplotlib.pyplot as plt
from math import pi,sin

G  = 6.6743e-11
M  = 5.9722e24
J2 = 1.08262668e-3
RE = 6371000
nm = 1851.851

rp = 200000

ras  = [200,500,1000,2000,5000]
incs = range(91)

lo  = list(range(91))
los = []

for ra in ras:
    ra = ra*1000
    a  = (rp+ra+2*RE)/2
    T  = (4*pi**2*a**3/(G*M))**0.5
    n  = 86400/T*360
    c  = a-rp-RE
    e  = c/a

    for i in incs:
        omegadot = 3/4 * n * J2 * (RE/a)**2 * (4-5*sin(i/180*pi)**2)/((1-e**2)**2)
        lo[i] = omegadot
        if i==0:
            print(lo[i])
    los.append(list(lo))

fig, ax = plt.subplots()

plt.plot(incs,los[0],label='apogee 200 km')
plt.plot(incs,los[1],label='apogee 500 km')
plt.plot(incs,los[2],label='apogee 1000 km')
plt.plot(incs,los[3],label='apogee 2000 km')
plt.plot(incs,los[4],label='apogee 5000 km')

plt.xlim([0,90])
plt.ylim([-10,25])

plt.text(5,22,"Perigee altitude is 200 km")
plt.ylabel("Apsidal rotation $-$ degrees per mean solar day")
plt.xlabel("Orbital inclination $-$ degrees")

plt.xticks([15,30,45,60,75,90])

ax.annotate('63.4°', xy=(63.4, 0),  xycoords='data',
            xytext=(0.8,0.4), textcoords='axes fraction',
            arrowprops=dict(facecolor='black',width=1,headwidth=3,headlength=6),
            horizontalalignment='right', verticalalignment='top',
            )

plt.legend()
plt.grid(True)
plt.show()
