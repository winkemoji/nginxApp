import os
import webbrowser
import socket
import sys

try:
    # get app current directory
    abspath = os.getcwd()

    # cmd string
    cdRoot = abspath[abspath.index(':') - 1] + ':'
    cdAbs = 'cd '+abspath+'/nginx-1.16.0/'
    startNgx = 'start nginx.exe'
    quitNgx = 'nginx -s stop'
    killNgx = 'TASKKILL /F /IM nginx.exe /T'
    # start nginx
    if(bool(1-os.path.exists(abspath + '/nginx-1.16.0/'))):
        sys.exit(1)

    os.system(cdRoot + '&&' + cdAbs + '&&' + startNgx)
    # open default web browser
    webbrowser.open("http://localhost:80/")

    try:
        print('Press Ctrl + C to save quit.\n')
        print('If you forget to save quit. I recommend you press K to kill all nginx process. :)')
        while True:
            s = input()
            if s.lower() =='k':
                os.system(cdRoot + '&&' + cdAbs + '&&' + killNgx)
                sys.exit()
    except KeyboardInterrupt as identifier:
        os.system(cdRoot + '&&' + cdAbs + '&&' + quitNgx)

except Exception as ex:
    sys.exit()