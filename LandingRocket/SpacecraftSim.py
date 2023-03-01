from random import gauss

class SpacecraftEngine:
  def __init__(self):
    self.__m = 10.5 #kg 
    self.__maxValue = 100.0 
    self.__minValue = 0.0
    self.__maxThrust = 500.0 #N
    self.__minThrust = 0.0
    self.__thrust = 0.0 #N
    self.__accel = 0.0
    self.__v = -10.0 #m/s
    self.__y = 300.0 #m
    self.__b = 0.1
    self.__landingVel = None
    self.__hasCrashed = False
    self.__hasLanded = False
    self.__MAX_VEL_AT_LANDING = 1.5 # m/s
    

  def setThrust(self,value):
    if(value > self.__maxValue):
      value = self.__maxValue
    elif (value < self.__minValue):
      value = self.__minValue
    if(self.__hasLanded == True):
      self.__thrust = 0
    else:
      self.__thrust = self.__mapValueToOutput(value)
  def __calc_accel(self):
    if(self.__hasLanded == True):
      return 0.0
    else:
      return (1.0/self.__m)*(self.__thrust - self.__m*9.81 - self.__b*self.__v)
  def update(self):
    dt = 0.1
    self.__accel = self.__calc_accel()
    self.__v = self.__v + self.__accel*dt
    self.__y = self.__y + self.__v*dt 
    if(self.__y <= 0 and self.__hasLanded == False):
      self.__y = 0
      self.__hasLanded = True
      self.__landingVel = abs(self.__v)
      if(self.__landingVel > self.__MAX_VEL_AT_LANDING):
        self.__hasCrashed = True
      self.__v = 0
      self.__accel = 0
    
      
    
  def __mapValueToOutput(self,value):
    k = 0
    scaledValue = (value - self.__minValue)*(self.__maxThrust - self.__minThrust)/(self.__maxValue - self.__minValue) + self.__minThrust + k
    return scaledValue
  def getData(self):
    return [self.__y,self.__v,self.__accel]
  def checkCrashStatus(self):
    return self.__hasCrashed
  def checkLandingStatus(self):
    return self.__hasLanded
  def getLandingVel(self):
    return self.__landingVel
    
  
