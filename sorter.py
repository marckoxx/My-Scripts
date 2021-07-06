import os
import shutil
import time

files = os.listdir()
years = []
months = []
days = []
type = ['Audio', 'Images', 'Videos']
audio = [".mp3", ".wav", ".m4a", ".flac"]
images = [".jpeg", ".png", ".jpg", ".gif", ".psd"]
videos = [".mp4", ".mkv", ".3gp", ".avi", ".mov", ".webm", ".ts"]
type_sort = {'Audio': audio, 'Images': images, 'Videos': videos}
month_day = {'Jan': [], 'Feb': [], 'Mar': [], 'Apr': [], 'May': [], 'Jun': [], 'Jul': [], 'Aug': [], 'Sep': [], 'Oct': [], 'Nov': [], 'Dec': []}

print("\nFile Sorter 3.0 by Marcko")
print('This will sort the files by filetype, year, months, and day of modification.')
print('Please note that this script will only work on the files on the same directory with it.\n')

transfer_mode = int(input('Would you like to copy or move your files?\n1.Copy\n2.Move\n'))

print("\nChecking files...")
for f in files:
    mod_date = time.ctime(os.path.getmtime(f))
    mod_date = mod_date.split(" ")
    if mod_date[4] not in years:
        years.append(mod_date[4])
    if mod_date[1] not in months:    
        months.append(mod_date[1])
    if mod_date[2] not in month_day[mod_date[1]] and mod_date[2] != '':
        month_day[mod_date[1]].append(mod_date[2])

print("Making folders and proceeding to the file trasnfer...\n")
for f in files:
    mod_date = time.ctime(os.path.getmtime(f))
    mod_date = mod_date.split(" ")
    if f != 'File Sorter 3.py' and f not in type and f != 'Others':
        for t in type_sort:
            for s in type_sort[t]:
                if f.endswith(s):
                    if t not in os.listdir():
                        os.mkdir('./' + t)
                    for y in years:
                        if mod_date[4] == y:
                            if str(y) not in os.listdir('./' + t):
                                os.mkdir('./' + t + '/' + str(y))
                            for m in months:
                                if mod_date[1] == m:
                                    if m not in os.listdir('./' + t + '/' + y):
                                         os.mkdir('./' + t + '/' + y + '/' + m)
                                    for d in month_day[m]:
                                        if mod_date[2] == d:
                                            if str(d) not in os.listdir('./' + t + '/' + y + '/' + m):
                                                os.mkdir('./' + t + '/' + y + '/' + m + '/' + str(d))
                                            if f not in os.listdir('./' + t + '/' + y + '/' + m + '/' + str(d)):
                                                if transfer_mode == 1:
                                                    shutil.copy(f, './' + t + '/' + y + '/' + m + '/' + str(d))
                                                    print(f + ' copied!')
                                                    break
                                                if transfer_mode == 2:
                                                    shutil.move(f, './' + t + '/' + y + '/' + m + '/' + str(d))
                                                    print(f + ' moved!')
                                                    break
                                            else:
                                                if transfer_mode == 1:                                                
                                                    print('The file ' + f + ' will not be copied to avoid further duplication')
                                                if transfer_mode == 2:
                                                    print('The file ' + f + ' is already in the folder, renaming...')
                                                    g = f.replace('.', '(1).') # nice 
                                                    os.rename(f, g)
                                                    shutil.move(g, './' + t + '/' + y + '/' + m + '/' + str(d))
                                                    print(g + ' moved!')
        if f in os.listdir():
            if 'Others' not in os.listdir():
                os.mkdir('./Others')
            if transfer_mode == 1:
                name, ext = os.path.splitext('./' + f)
                if ext not in audio + videos + images:
                    print('The file ' + f + ' will not be copied to Others to avoid further duplication')
            if transfer_mode == 2:
                if f not in os.listdir('./Others'):
                    shutil.move(f, './Others')
                    print(f + " was moved to to Others")
                else:
                    print('The file ' + f + ' is already in the folder, renaming...')
                    g = f.replace('.', '(1).')
                    os.rename(f, g)
                    shutil.move(g, './Others')
                    print(g + " was moved to to Others")

if transfer_mode == 1:
    print("\nCopying has finished!\n")
if transfer_mode == 2:
    print("\nMoving has finished!\n")

os.system('pause')
