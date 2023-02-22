# Android-Memory-Tools
Python script to edit process memory

Used files: `/proc/PID/mem`, `/proc/PID/maps`

# Usage
```
Get Process ID by package:
GetPidOf(package: str) -> int

Get .so library map information:
GetSoMap(pid: int, soname: str) -> dict

Read from memory by offset:
MemRead(pid: int, address: int, size: int) -> bytes

Write to memory by offset:
MemWrite(pid: int, address: int, value: bytes) -> bool
```

Telegram: @flowLv
