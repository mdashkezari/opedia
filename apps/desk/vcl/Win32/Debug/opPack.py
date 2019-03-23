import site
import os
file = open("out.txt","w")
for pack in site.getsitepackages():
  path = pack.replace("\\","/")
  path = path + "/opedia/"
  if os.path.isdir(path):
    file.write(path)
    break
file.close()
