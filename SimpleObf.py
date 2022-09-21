import marshal
import zlib
import requests
from pystyle import *
import os
import time
os.system("title Simple-OBF: simplest marshal python obfuscator out there")
print("""
  ╔═╗╦┌┬┐┌─┐┬  ┌─┐  ╔═╗┌┐ ┌─┐
  ╚═╗║│││├─┘│  ├┤───║ ║├┴┐├┤  Simplest marshal obf out there
  ╚═╝╩┴ ┴┴  ┴─┘└─┘  ╚═╝└─┘└ 
 https://github.com/syntheticc
""")
pythonfile = input("python file name that you want to obf > ")
with open(f'{pythonfile}.py') as fi:
     pro = fi.read()
     mar = marshal.dumps(pro)
     zlb = zlib.compress(mar)
     with open(f"{pythonfile}.py", 'w') as f:
         f.write(f"import marshal,zlib;exec(marshal.loads(zlib.decompress({zlb})))")
pass 

print("finished")
time.sleep(2)
exe = input("Compile to exe press enter to continue > ")
os.system(f'pyinstaller --onefile {pythonfile}.py')