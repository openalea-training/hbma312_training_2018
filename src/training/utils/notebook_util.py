
def pnotebook(fname):
  from nbformat import read, NO_CONVERT
  nb = read(fname, NO_CONVERT)  
  source = ''
  for cell in nb['cells']:
    if cell['cell_type'] == 'code' and (not 'tags' in cell['metadata'] or not ('example' in cell['metadata']['tags'])):
        if not cell['source'].startswith('%%lpy'):
          source += cell['source']+'\n'
  return source

def notebook(fname):
    import os, sys
    assert(os.path.exists(fname))
    cmd =  [sys.executable,__file__, fname]
    import subprocess
    proc = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return proc.stdout.read()



if __name__ == '__main__':
    import sys
    print (pnotebook(sys.argv[1]))