from memory import *

pid = GetPidOf('com.zhiliaoapp.musically') # get id of process
libmap = GetSoMap(pid, 'libpreload.so') # get libpreload.so map
MemWrite(pid, libmap['start'] + 0x2FC5, b'\xf0\xf0\xf1\xf1') # write f0 f0 f1 f1 to 0x2FC567 in libpreload.so
print(MemRead(pid, libmap['start'] + 0x2FC5, 4)) # read 4 bytes from 0x2FC567 in libpreload.so