"""
upquote, textcomp -- for properly handling single quotes, i.e. representing them by a straight apostrophe
    in order to be able to copy from the generated PDF file and use as it is
10pt, aspectratio=169, lmodern fonts => 81 characters on a line (~ 80 as in the old days... do I remember correctly?)

Slide separator / new slide command:
+++ on a separate line, no spaces before and after, ending with a newline (\n)
    -> test it on Windows for \r\n endlines!!!

no tabs!
"""

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
    parser = argparse.ArgumentParser(description='Create PDF slides using the smallest (one-command) markup language.')
    parser.add_argument('filename', type=str, nargs=1, help='input filename')
    parser.add_argument('-d', metavar='outdir', type=str, nargs=1, required=True, help='output directory')
    args = parser.parse_args()
    
    tex = os.path.join(args.d[0], os.path.basename(args.filename[0]) + '.tex')
    
    create_slides(args.filename[0], tex)
    r = subprocess.call(['pdflatex', '-output-directory=' + args.d[0], tex])
    