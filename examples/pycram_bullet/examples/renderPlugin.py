import pycram_bullet as p
import pycram_bullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pycram_bullet_data.getDataPath())
plugin = p.loadPlugin("d:/develop/bullet3/bin/pycram_bullet_testplugin_vs2010_x64_debug.dll",
                      "_testPlugin")
print("plugin=", plugin)
p.loadURDF("r2d2.urdf")

while (1):
  p.getCameraImage(320, 200)
