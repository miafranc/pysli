import codecs
import re
import subprocess
import argparse
import os

PROLOGUE = """\\documentclass[10pt,aspectratio=169]{beamer}

\\usepackage{upquote,textcomp}
\\usepackage{lmodern}
\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}

\\setbeamersize{text margin left=2em} 

\\begin{document}
"""

EPILOGUE = """\\end{document}
"""

def create_slides(filein, fileout):
    f = codecs.open(filein, 'r')
    data = f.read()
    f.close()
    
    slides = re.split("^\+\+\+$", data, flags=re.U | re.M)
    
    f = codecs.open(fileout, 'w')
    f.write(PROLOGUE)
    f.writelines(["\\begin{frame}[fragile]\n\\begin{verbatim}\n" + s.strip() + "\n\\end{verbatim}\n\\end{frame}\n\n" for s in slides])
    f.write(EPILOGUE)
    f.close()
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create verbatim PDF slides using the smallest (one-command) markup language.')
    parser.add_argument('filename', type=str, nargs=1, help='input filename')
    parser.add_argument('-d', metavar='outdir', type=str, nargs=1, required=True, help='output directory')
    args = parser.parse_args()
    
    tex = os.path.join(args.d[0], os.path.basename(args.filename[0]) + '.tex')
    
    create_slides(args.filename[0], tex)
    r = subprocess.call(['pdflatex', '-output-directory=' + args.d[0], tex])
    