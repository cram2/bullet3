"""The Python implementation of the PyBullet GRPC client."""

from __future__ import print_function

import grpc

import pycram_bullet_pb2
import pycram_bullet_pb2_grpc

#todo: how to add this?
MJCF_COLORS_FROM_FILE = 512


def run():
  print("grpc.insecure_channel")
  channel = grpc.insecure_channel('localhost:6667')
  print("pycram_bullet_pb2_grpc.PyBulletAPIStub")
  stub = pycram_bullet_pb2_grpc.PyBulletAPIStub(channel)
  response = 0

  print("submit CheckVersionCommand")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(checkVersionCommand=pycram_bullet_pb2.CheckVersionCommand(
          clientVersion=123)))
  print("PyBullet client received: ", response)

  print("submit_ResetSimulationCommand")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(resetSimulationCommand=pycram_bullet_pb2.ResetSimulationCommand()))
  print("PyBullet client received: ", response)

  print("submit LoadUrdfCommand ")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(loadUrdfCommand=pycram_bullet_pb2.LoadUrdfCommand(
          fileName="door.urdf",
          initialPosition=pycram_bullet_pb2.vec3(x=0, y=0, z=0),
          useMultiBody=True,
          useFixedBase=True,
          globalScaling=2,
          flags=1)))
  print("PyBullet client received: ", response)
  bodyUniqueId = response.urdfStatus.bodyUniqueId

  print("submit LoadSdfCommand")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(loadSdfCommand=pycram_bullet_pb2.LoadSdfCommand(
          fileName="two_cubes.sdf", useMultiBody=True, globalScaling=2)))
  print("PyBullet client received: ", response)

  print("submit LoadMjcfCommand")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(loadMjcfCommand=pycram_bullet_pb2.LoadMjcfCommand(
          fileName="mjcf/humanoid.xml", flags=MJCF_COLORS_FROM_FILE)))
  print("PyBullet client received: ", response)

  print("submit ChangeDynamicsCommand ")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(changeDynamicsCommand=pycram_bullet_pb2.ChangeDynamicsCommand(
          bodyUniqueId=bodyUniqueId, linkIndex=-1, mass=10)))
  print("PyBullet client received: ", response)

  print("submit GetDynamicsCommand ")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(getDynamicsCommand=pycram_bullet_pb2.GetDynamicsCommand(
          bodyUniqueId=bodyUniqueId, linkIndex=-1)))
  print("PyBullet client received: ", response)

  print("submit InitPoseCommand")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.PyBulletCommand(initPoseCommand=pycram_bullet_pb2.InitPoseCommand(
          bodyUniqueId=bodyUniqueId, initialStateQ=[1, 2, 3], hasInitialStateQ=[1, 1, 1])))
  print("PyBullet client received: ", response)

  print("submit RequestActualStateCommand")
  response = stub.SubmitCommand(
      pycram_bullet_pb2.
      PyBulletCommand(requestActualStateCommand=pycram_bullet_pb2.RequestActualStateCommand(
          bodyUniqueId=bodyUniqueId, computeForwardKinematics=True, computeLinkVelocities=True)))
  print("PyBullet client received: ", response)

  i = 0
  while (True):
    i = i + 1
    print("submit StepSimulationCommand: ", i)
    response = stub.SubmitCommand(
        pycram_bullet_pb2.PyBulletCommand(stepSimulationCommand=pycram_bullet_pb2.StepSimulationCommand()))
    print("PyBullet client received: ", response.statusType)


#print("TerminateServerCommand")
#response = stub.SubmitCommand(pycram_bullet_pb2.PyBulletCommand(terminateServerCommand=pycram_bullet_pb2.TerminateServerCommand()))
#print("PyBullet client received: " , response.statusType)

if __name__ == '__main__':
  run()
