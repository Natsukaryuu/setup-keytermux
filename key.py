import os
import sys
import time
from os import system as execall

print ("Memeriksa...")
time.sleep(2)
if os.path.isdir("/data/data/com.termux/files/home/.termux"):
    if os.path.isfile("/data/data/com.termux/files/home/.termux/termux.properties"):
        pass
    else:
        execall("touch /data/data/com.termux/files/home/.termux/termux.properties")
        if os.path.isfile("/data/data/com.termux/files/home/.termux/termux-properties"):
            pass
        else:
            print ("Silahkan jalankan ulang script ini!")
            sys.exit(1)
else:
    execall("mkdir /data/data/com.termux/files/home/.termux")
    if os.path.isdir("/data/data/com.termux/files/home/.termux"):
        pass
    else:
        print ("Silahkan jalankan ulang script ini!")
        sys.exit(1)
print ("Memeriksa berhasil!")
time.sleep(2)
os.system("clear")

print ("-" * 25)
def info(git, name, fp):
    print ("author: " + name)
    print ("github: " + git)
    print ("fanpage: " + fp)
info("nskrin", "https://github.com/nskrin/", "https://facebook.com/nskrin/")
print ("-" * 25)
print ("Membuat key...")
time.sleep(2)
if os.path.isdir("/data/data/com.termux/files/home/.termux"):
    execall("""
echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" > /data/data/com.termux/files/home/.termux/termux.properties
echo "use-black-ui = true" >> /data/data/com.termux/files/home/.termux/termux.properties
echo "fullscreen = true" >> /data/data/com.termux/files/home/.termux/termux.properties
echo "use-fullscreen-workaround = true" >> /data/data/com.termux/files/home/.termux/termux.properties
""")
print ("berhasil")
print ("tutup aplikasi termuxnya dan buka lagi atau buka new session")
