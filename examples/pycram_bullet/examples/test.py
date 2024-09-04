#os.sys.path.insert is only needed when pycram_bullet is not installed
#but running from github repo instead
import os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print("current_dir=" + currentdir)
parentdir = os.path.join(currentdir, "../gym")
os.sys.path.insert(0, parentdir)

import pycram_bullet
import pycram_bullet_data

import time

#choose connection method: GUI, DIRECT, SHARED_MEMORY
pycram_bullet.connect(pycram_bullet.GUI)
pycram_bullet.loadURDF(os.path.join(pycram_bullet_data.getDataPath(), "plane.urdf"), 0, 0, -1)
#load URDF, given a relative or absolute file+path
obj = pycram_bullet.loadURDF(os.path.join(pycram_bullet_data.getDataPath(), "r2d2.urdf"))

posX = 0
posY = 3
posZ = 2
obj2 = pycram_bullet.loadURDF(os.path.join(pycram_bullet_data.getDataPath(), "kuka_iiwa/model.urdf"), posX,
                         posY, posZ)

#query the number of joints of the object
numJoints = pycram_bullet.getNumJoints(obj)

print(numJoints)

#set the gravity acceleration
pycram_bullet.setGravity(0, 0, -9.8)

#step the simulation for 5 seconds
t_end = time.time() + 5
while time.time() < t_end:
  pycram_bullet.stepSimulation()
  posAndOrn = pycram_bullet.getBasePositionAndOrientation(obj)
  print(posAndOrn)

print("finished")
#remove all objects
pycram_bullet.resetSimulation()

#disconnect from the physics server
pycram_bullet.disconnect()
