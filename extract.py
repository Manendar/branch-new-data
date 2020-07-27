import os
import glob
import patoolib

# this function will extract zip files and load it to a specified path
def extract(infile='C:/Users/Admin/Downloads',out='C:/Users/Admin/Desktop/myextraction'):
    os.chdir(infile)
    req=[glob.glob(i) for i in ['*.zip','*.rar']]
    collect=req[0]
    collect1=req[1]
    collect.extend(collect1)
    if not os.path.exists(out):
        os.mkdir(out)
    folders = os.listdir(out)
    for files in collect:
        if files[:-3] not in folders:
            patoolib.extract_archive(files,outdir=out)

extract()
    
