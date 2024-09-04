import pycram_bullet as p
import time
import pycram_bullet_data

p.connect(p.SHARED_MEMORY)

p.setAdditionalSearchPath(pycram_bullet_data.getDataPath())
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = "saveWorld" + timestr + ".py"
p.saveWorld(filename)
p.disconnect()
