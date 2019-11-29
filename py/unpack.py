import subprocess
import zlib
import tarfile
import io
import os

def createBackup():
    if os.path.exists('backup.ab'):
        return 0

    cmd = ['adb', 'start-server']
    subprocess.call(cmd)

    cmd = ['adb', '-d', 'get-state']
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    state = process.communicate()[0].decode()

    if state.find('device') == -1:
        print("Couldn't connect to the device, make sure ADB debugging is enabled.")
    else:
        cmd = ['adb', '-d', 'backup', '-noapk', 'com.aniplex.fategrandorder.en']

        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        for stdout_line in iter(process.stdout.readline, ''):
            if 'confirm' in stdout_line:
                print("Unlock your device and confirm backup operation, leave the password field blank.")

        process.stdout.close()
        code = process.wait()
        return code

def unpackBackup(file):
    print("Unpacking backup file...")

    f = open(file, 'rb')
    of = open('backup.tar', 'wb')

    buffer = f.read(4096)
    pos = buffer.find(b'none\n')+5
    data = buffer[pos:]
    stream = zlib.decompressobj()

    while data:
        of.write(stream.decompress(data))
        data = f.read(4096)

    f.close()
    of.close()

def extractBackup():
    files = ['authsave.dat', 'authsave2.dat', 'friendcodesave.dat', 'signupsave.dat']

    if not os.path.isdir('files/'):
        os.mkdir('files/')
    if not os.path.exists('backup.ab'):
        print("Backup file doesn't exist.")
        exit()
    if not os.path.exists('backup.tar'):
        unpackBackup('backup.ab')

    print("Extracting important files...")
    tf = tarfile.open('backup.tar')

    if tf:
        for member in tf.getmembers():
            if member.isreg():
                member.name = os.path.basename(member.name)
                if member.name in files:
                    tf.extract(member, 'files/')

if createBackup() == 0:
    extractBackup()
    print('Files successfully extracted.')
    exit()