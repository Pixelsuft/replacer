import get_all_files


config={
    'src_dir': 'src',
    'types': [],
    'output_dir': 'output',
    'ignore': ['main.py', 'get_all_files.py', '__pycache__'],
    'replacer': {
        '{{ Header }}': 'head.html',
        '<!--endbody-->': 'endbody.html'
    }
}


get_all_files.output_dir=config['output_dir']
get_all_files.types=config['types']
get_all_files.ignore=config['ignore']
get_all_files.scan(config['src_dir'])

for i in get_all_files.files:
    temp_f_r=open(i, 'r')
    readed=temp_f_r.read()
    temp_f_r.close()
    for j in config['replacer']:
        if j in readed:
            temp_f_replace_r=open(config['replacer'][j], 'r')
            readed_replace=temp_f_replace_r.read()
            temp_f_replace_r.close()
            readed=readed.replace(j, readed_replace)
    temp_f_w=open(config['output_dir']+'\\'+i, 'w')
    temp_f_w.write(readed)
    temp_f_w.close()