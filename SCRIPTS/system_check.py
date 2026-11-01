import platform
import sys
import shutil

print("===== CYBERLAB SYSTEM CHECK =====")
print("Python:", sys.version.split()[0])
print("Platform:", platform.platform())
print("Architecture:", platform.machine())

for tool in ("git", "curl", "nmap"):
    print(f"{tool}: {shutil.which(tool) or 'Not installed'}")

print("===== CHECK COMPLETE =====")
