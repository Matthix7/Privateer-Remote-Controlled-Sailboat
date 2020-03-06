# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:45:11 2020

@author: catam
"""
import numpy as np
from numpy import pi, cos, sin, array
import matplotlib.pyplot as plt

servo = np.linspace(-3.14/2, 3.14/2, 5000)
b = np.linspace(-3.14/2, 3.14/2, 5000)
A,B = np.meshgrid(servo,b)


S_list = [0.5]    # Largeur barre safran
M_list = [0.1, 0.4]   # Largeur barre servo-moteur
E_list = [0.6]    # Espacement entre les centres de rotation safran et servo
# D = (S-M)**2 + E**2   # constraint


for E in E_list:
	for S in S_list:
		for M in M_list:
			res = S*M*(1-cos(A-B)) - E* (M*sin(A) - S*sin(B))

			closest_index = np.argmin(abs(res), axis = 0)
			errors = np.min(abs(res), axis = 0)
			print("Max error = ", np.max(errors))
			safran = b[closest_index]


			servo_deg = 180/pi*servo
			safran_tribord = 180/pi*safran
			safran_babord = np.flip(-180/pi*safran)

			#plt.figure()
			plt.fill_between(servo_deg, safran_tribord, y2=safran_babord, label = "Safran "+str(S)+", Servo "+str(M)+", Espacement "+str(E))

plt.xlabel("(babord, traction babord) - Angle du servo - (tribord, traction tribord)")
plt.ylabel("Angle du safran")
plt.title("Relation servo/safran du Renardeau")
plt.legend(loc = "upper left")
plt.show()







