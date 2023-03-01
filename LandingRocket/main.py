# https://replit.com/@kreier/LandingRocket#main.py

from SpacecraftSim import SpacecraftEngine

'''
Spacecraft Engine API:

myRocket.getData(): 
inputs: none
outputs: an array with position, velocity, and acceleration as the first, second, and third elements.

myRocket.update():
inputs: none
outputs: none
purpose: Gets a new set of position, velocity, and acceleration for each loop.

myRocket.setThrust(signal):
inputs: thrust (percent of maximum) as a signal from 0 - 100
outputs: none
purpose: Sets the thrust of the engine 

myRocket.checkCrashStatus():
inputs: none
outputs: True or False indicating whether or not the rocket has crashed. This occurs if the rocket hits the ground with a velocity greater than 1.5 m/s.

myRocket.checkLandingStatus():
inputs: none
outputs: True or False indicating whether or not the rocket has landed. This occurs if the rocket's height hits Zero

myRocket.getLandingVel():
inputs: none
outputs: speed of the rocket upon landing.




'''

myRocket = SpacecraftEngine()

currentTime      = 0.0
currentThrust    = 0
accumulatedError = 0.0
SIMULATION_TIME  = 8.0 #seconds of simulation
SKIP             = 0

while(currentTime < SIMULATION_TIME):
  rocketData = myRocket.getData() #data for rocket
  print(f"{currentTime:.2f} , {rocketData[0]:.2f}, {rocketData[1]:.2f}, {rocketData[2]:.2f}")  
  myRocket.update() #Get update from rocket over radio
  currentTime += 0.1 # Don't change me

  #Your code goes here
  # myRocket.setThrust(100)
  # myRocket.setThrust(20.88)
  if (rocketData[0] < 70):
      myRocket.setThrust(100)
  if (rocketData[0] < 40 and SKIP == 0):
      myRocket.setThrust(59)
      SKIP = 1
  

#Don't change anything below this line.
if(myRocket.checkLandingStatus()):
  if(myRocket.checkCrashStatus() == True):
    print("Rocket has crashed")
    print("Landing speed was " + str(myRocket.getLandingVel()) + " m/s")
  else:
    print("Hooray - the rocket landed safely!")
    print("Landing speed was " + str(myRocket.getLandingVel()) + " m/s")
else:
  print("The rocket has not yet landed. Try extending the simulation time.")
  
