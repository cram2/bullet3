import pycram_bullet as p
import pycram_bullet_data


usePort = True

if (usePort):
  id = p.connect(p.GRPC, "localhost:12345")
else:
  id = p.connect(p.GRPC, "localhost")
print("id=", id)

if (id < 0):
  print("Cannot connect to GRPC server")
  exit(0)

print("Connected to GRPC")

p.setAdditionalSearchPath(pycram_bullet_data.getDataPath())
r2d2 = p.loadURDF("r2d2.urdf")
print("numJoints = ", p.getNumJoints(r2d2))
