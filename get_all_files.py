from os import listdir as scan_dir
from os.path import isdir as is_dir
from os import getcwd as get_path
from os import system as cmd_run
from os import makedirs as make_dir


types=['html', 'css', 'js']
files=[]
ignore=[]
output_dir='output'

def scan(dirrr):
    make_dir(output_dir, exist_ok=True)
    for i in scan_dir(str(dirrr)):
        if is_dir(i):
            if not i in ignore:
                temp_dirs.append(i)
                scan(i)
        else:
            if types==[] or i.split('.')[-1] in types:
                j=''
                if not dirrr=='.':
                    j=dirrr+'\\'
                if not str(str(j)+str(i)) in ignore:
                    files.append(str(j)+str(i))
    make_dir(output_dir+'\\'+dirrr, exist_ok=True)