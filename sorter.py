import os,shutil

print('\nFile Sorter by Marcko Pablo')
print('\nPlease note that it will not copy or move files that are already in the category folders')
print('\n' + "The files in the current directory are:")
files = os.listdir()
separator = ", "
print(separator.join(files) + '\n') 

images=[".jpeg",".png",".jpg",".gif"]
text=[".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"]
videos=[".mp4",".mkv"]
sounds=[".mp3",".wav",".m4a"]
applications=[".exe",".lnk"]
codes = [".c",".py",".java",".cpp",".js",".html",".css",".php"]
folders = ['./Images', './Text', './Sounds', './Videos', './Applications', './Codes', './Others']
sort_mode = input('Would you like to copy or move the files?' + '\n1. Copy' + '\n2. Move\n')

for f in folders:
    f = f.replace('./', '')
    if f not in files:
        f = './' + f
        os.mkdir(f)
    else:
        pass
    
if int(sort_mode) == 1:
    print("\nSorting and copying the files...")
    for file in files:
        if not os.path.isdir(file) and file != "sorter.py":
            dest = ""
            for ex in images:
                if file.endswith(ex):
                    dest='./Images'
                    shutil.copy(file,dest)
                    break

            for ex in text:
                if file.endswith(ex):
                    dest='./Text'
                    shutil.copy(file,dest)
                    break

            for ex in sounds:
                if file.endswith(ex):
                    dest='./Sounds'
                    shutil.copy(file,dest)
                    break

            for ex in videos:
                if file.endswith(ex):
                    dest='./Videos'
                    shutil.copy(file,dest)
                    break

            for ex in applications:
                if file.endswith(ex):
                    dest='./Applications'
                    shutil.copy(file,dest)
                    break

            for ex in codes:
                if file.endswith(ex):
                    dest= './Codes'
                    shutil.copy(file,dest)
                    break

            if dest == "":
                shutil.copy(file,'./Others')

else:
    print("\nSorting and moving the files...")
    for file in files:
        if not os.path.isdir(file) and file != "sorter.py":
            dest = ""
            for ex in images:
                if file.endswith(ex):
                    dest='./Images'
                    shutil.move(file,dest)
                    break

            for ex in text:
                if file.endswith(ex):
                    dest='./Text'
                    shutil.move(file,dest)
                    break

            for ex in sounds:
                if file.endswith(ex):
                    dest='./Sounds'
                    shutil.move(file,dest)
                    break

            for ex in videos:
                if file.endswith(ex):
                    dest='./Videos'
                    shutil.move(file,dest)
                    break

            for ex in applications:
                if file.endswith(ex):
                    dest='./Applications'
                    shutil.move(file,dest)
                    break

            for ex in codes:
                if file.endswith(ex):
                    dest= './Codes'
                    shutil.move(file,dest)
                    break

            if dest == "":
                shutil.move(file,'./Others')

print("Sorting Completed!" + '\n')

os.system('pause')
