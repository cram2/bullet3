import pycram_bullet as p
import pycram_bullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pycram_bullet_data.getDataPath())
cube = p.loadURDF("cube.urdf")
frequency = 240
timeStep = 1. / frequency
p.setGravity(0, 0, -9.8)
p.changeDynamics(cube, -1, linearDamping=0, angularDamping=0)
p.setPhysicsEngineParameter(fixedTimeStep=timeStep)
for i in range(frequency):
  p.stepSimulation()
pos, orn = p.getBasePositionAndOrientation(cube)
print(pos)
