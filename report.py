#!/usr/bin/env python
# -*- coding: utf-8 -*-
#pyinstaller report.py --onefile
import os
import shutil
# ディレクトリ作成とipynbのコピー
date = input("date:")
while True:
    sub_num_str = input("sub number:")
    sub_num = int(sub_num_str)
    if int(sub_num)>-1:
        break
os.makedirs(date+"/figure/tikz",exist_ok=True)
os.makedirs(date+"/sub",exist_ok=True)
print("\nFolders made.")
if os.path.exists("./"+date+"figure/tikz/setup.tex"):
    print("tikz-file already exist.  They weren't copied.")
else:
    shutil.copyfile("C:/Users/akira/Documents/tex/flowchart/flowchart.tex", "./"+date+"/figure/tikz/flowchart.tex")
    shutil.copyfile("C:/Users/akira/Documents/tex/tikz/setup.tex", "./"+date+"/figure/tikz/setup.tex")
    shutil.copyfile("C:/Users/akira/Documents/tex/band/band.tex", "./"+date+"/figure/tikz/band.tex")
    shutil.copyfile("C:/Users/akira/Documents/tex/circuitikz/opamp.tex", "./"+date+"/figure/tikz/circuit.tex")
    shutil.copyfile("C:/Users/akira/Documents/tex/beamer/beamer.tex", "./"+date+"/figure/tikz/beamer.tex")
    print("tikz-file copied.")
if os.path.exists("./"+date+"figure/graph.ipynb"):
    print("ipynbs already exist.  They weren't copied.")
else:
    shutil.copyfile("C:/Users/akira/Documents/pythonpractice/template/graph.ipynb", "./"+date+"/figure/graph.ipynb")
    shutil.copyfile("C:/Users/akira/Documents/pythonpractice/template/sympy.ipynb", "./"+date+"/figure/sympy.ipynb")
    shutil.copyfile("C:/Users/akira/Documents/pythonpractice/template/excel-csv-textable.ipynb", "./"+date+"/figure/excel-csv-textable.ipynb")
    print("ipynbs copied.")
if os.path.exists("./"+date+"figure/excel-genarate.py"):
    print("excel-generate already exist.  They weren't copied.")
else:
    shutil.copyfile("C:/Users/akira/Documents/pythonpractice/excel-generate.py", "./"+date+"/figure/excel-generate.py")
# texfile作成
# luamain
pre =   r"\documentclass{ltjsarticle}" "\n"\
        r"\input{C:/Users/akira/.luamacro}" "\n" \
        r"\graphicspath{{figure/}{../figure/}}" "\n" \
        r"\begin{document}" "\n" \
        r"%目次" "\n" \
        r"\setcounter{tocdepth}{1}" "\n" \
        r"\thispagestyle{empty} %目次が複数ページある時はローマンに変える" "\n" \
        r"\tableofcontents" "\n" \
        r"\clearpage" "\n" \
        r"\setcounter{page}{1}" "\n\n" \
        r"%subfile" "\n"
if os.path.exists("./"+date+"/luamain.tex"):
    print("luamain.tex already exists.")
else:
    # luamain 作成
    with open("./"+date+"/luamain.tex", 'a',encoding='utf-8') as f:
        f.write(pre)
        for i in range(1,sub_num+1):
            f.write(r"\subfile{sub"+r"/sub"+str(i)+r"}"+"\n")
        f.write(r"\end{document}")
        print("luamain.tex made.")
    #subi 作成
    for i in range(1,sub_num+1):
        with open("./"+date+"/sub"+"/sub"+str(i)+".tex", 'a',encoding='utf-8') as f:
            presub =    r"\documentclass[../luamain]{subfiles}" "\n" \
                        r"\setcounter{section}{"+str(i-1)+r"}" "\n\n" \
                        r"\begin{document}" "\n\n" \
                        r"\section{}" "\n\n" \
                        r"\subsection{目的}" "\n\n" \
                        r"\subsection{原理}" "\n\n" \
                        r"\subsection{方法}" "\n\n" \
                        r"\subsection{結果}" "\n\n" \
                        r"\subsection{考察}" "\n\n" \
                        r"\end{document}"
            f.write(presub)
            print("sub"+str(i)+".tex made.")
