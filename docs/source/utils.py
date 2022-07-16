# coding=utf-8

import glob
import os
import re
import shutil


RES_DIR = r"C:\chenchang\study\boc-resources\morgan-optimizing-compiler"
DOC_DIR = r"C:\chenchang\study\boc-chinese-text\docs\source"


def main():
    n = 1
    for f in glob.glob("img-*.png"):
        if f == "img-234.png":
            new_name = "figure-13.func.png"
            pass
        else:
            new_name = "figure-13.%d.png" % n
            n += 1
        print(f, new_name)
        shutil.copyfile(f, new_name)#, True)
    pass


def add_figures():
    with open(r"C:\chenchang\study\boc-chinese-text\docs\source\chapter13.rst", encoding="utf-8") as input_file, \
        open(r"C:\chenchang\study\boc-chinese-text\docs\source\chapter13_2.rst", "w", encoding="utf-8") as output_file:
        for ln in input_file:

#<Figure 13.5 Building Stack of Temporaries to Allocate>
#.. figure:: chapter03/figure-3.1.png
            m = re.search("<(Figure 13\.(\d{1,2}) .+)>", ln)
            #m = re.search("^.(.)", ln)
            if m:
                print(m.group(0), m.group(1), m.group(2))
                output_file.write(".. figure:: chapter13/figure-13.%s.png\n\n    " % m.group(2))
                output_file.write("%s\n" % m.group(1))
            else:
                output_file.write(ln)


def copy_figures_ch11():
    start_no = 176
    end_no = 201
    n = 1
    for no in range(start_no, end_no+1):
        if no in (0, ):
            pass
        else:
            old_name = os.path.join(RES_DIR, "img-%d.png" % no)

            if n in (11, 13, 18):
                # figure 11.11 is missing
                # figure 11.13 is missing
                # figure 11.18 is missing
                n += 1

            new_name = os.path.join(DOC_DIR, "chapter11", "figure-11.%d.png" % n)

            n += 1

            print(old_name, new_name)
            shutil.copyfile(old_name, new_name)


def add_figures_ch11():
    with open(os.path.join(DOC_DIR, "chapter11.rst"), encoding="utf-8") as input_file:
        rs = input_file.readlines()

    with open(os.path.join(DOC_DIR, "chapter11.rst"), "w", encoding="utf-8") as output_file:
        for ln in rs:
            m = re.search("<(Figure 11\.(\d{1,2}) .+)>", ln)
            #m = re.search("^.(.)", ln)
            if m:
                print(m.group(0), m.group(1), m.group(2))
                if m.group(2) not in ("11", "13", "18"):
                    output_file.write(".. figure:: chapter11/figure-11.%s.png\n\n    " % m.group(2))
                    output_file.write("%s\n" % m.group(1))
                else:
                    output_file.write(ln)
            else:
                output_file.write(ln)


def add_zero_prefix_to_figure_file_names():
    for f in glob.glob(os.path.join(RES_DIR, "img-*.png")):
        m = re.match("^(.+?)(\d+)(\.png)$", f)
        assert m
        #print(f, m.group(2))
        new_file_name = m.group(1) + "{:03}".format(int(m.group(2))) + m.group(3)
        #new_file_name = m.group(1) + "{:03}".format(m.group(2)) + m.group(3)
        print(new_file_name.replace("compiler", "compiler2"))
        shutil.copyfile(f, new_file_name.replace("compiler", "compiler2"))
        pass


def copy_figures_ch01():
    start_no = 1
    end_no = 4
    n = 1
    for no in range(start_no, end_no+1):
        if no in (0, ):
            pass
        else:
            old_name = os.path.join(RES_DIR, "img-%d.png" % no)

            if n in (11, 13, 18):
                # figure 11.11 is missing
                # figure 11.13 is missing
                # figure 11.18 is missing
                n += 1

            new_name = os.path.join(DOC_DIR, "chapter01", "figure-1.%d.png" % n)

            n += 1

            print(old_name, new_name)
            shutil.copyfile(old_name, new_name)


def add_figures_ch01():
    with open(os.path.join(DOC_DIR, "chapter01.rst"), encoding="utf-8") as input_file:
        rs = input_file.readlines()

    with open(os.path.join(DOC_DIR, "chapter01.rst"), "w", encoding="utf-8") as output_file:
        for ln in rs:
            m = re.search("<(1\.(\d{1,2}) .+)>", ln)
            #m = re.search("^.(.)", ln)
            if m:
                print(m.group(0), m.group(1), m.group(2))
                if m.group(2) not in ("11", "13", "18"):
                    output_file.write(".. figure:: chapter01/figure-1.%s.png\n\n    " % m.group(2))
                    output_file.write("Figure %s\n\n" % m.group(1))
                else:
                    output_file.write(ln)
            else:
                output_file.write(ln)


def copy_figures_ch02():
    chapter = 2
    start_no = 5
    end_no = 31
    n = 1
    missing_list = [] # 11, 13, 18
    for no in range(start_no, end_no+1):
        if no in (0, ):
            pass
        else:
            old_name = os.path.join(RES_DIR, "img-%d.png" % no)

            while n in missing_list:
                n += 1

            figure_dir = os.path.join(DOC_DIR, "chapter0%d" % chapter)
            os.makedirs(figure_dir, exist_ok = True)
            new_name = os.path.join(figure_dir, "figure-%d.%d.png" % (chapter, n))

            n += 1

            print(old_name, new_name)
            shutil.copyfile(old_name, new_name)


def add_figures_ch02():
    chapter = 2
    missing_list = [] # 11, 13, 18
    with open(os.path.join(DOC_DIR, "chapter0%d.rst" % chapter), encoding="utf-8") as input_file:
        rs = input_file.readlines()

    with open(os.path.join(DOC_DIR, "chapter0%d.rst" % chapter), "w", encoding="utf-8") as output_file:
        for ln in rs:
            m = re.search("<(?:Figure )?({CHAP}\.(\d{LP}1,2{RP}) .+)>".format(CHAP=chapter, LP="{", RP="}"), ln)
            #m = re.search("^.(.)", ln)
            if m:
                print(m.group(0), m.group(1), m.group(2))
                if int(m.group(2)) in missing_list:
                    output_file.write(ln)
                else:
                    output_file.write(".. figure:: chapter0{CHAP}/figure-{CHAP}.{FIGURE}.png\n\n    ".format(CHAP=chapter, FIGURE=m.group(2)))
                    output_file.write("Figure %s\n\n" % m.group(1))
#                if m.group(2) not in ("11", "13", "18"):
#                    output_file.write(".. figure:: chapter02/figure-2.%s.png\n\n    " % m.group(2))
#                    output_file.write("Figure %s\n\n" % m.group(1))
#                else:
#                    output_file.write(ln)
            else:
                output_file.write(ln)


def copy_figures(chapter, start_no, end_no, skip_list = [], missing_list = []):
    n = 1
    for no in range(start_no, end_no+1):
        if no in skip_list:
            continue
        else:
            old_name = os.path.join(RES_DIR, "img-%d.png" % no)

            while n in missing_list:
                n += 1

            figure_dir = os.path.join(DOC_DIR, "chapter0%d" % chapter)
            os.makedirs(figure_dir, exist_ok = True)
            new_name = os.path.join(figure_dir, "figure-%d.%d.png" % (chapter, n))

            n += 1

            print(old_name, new_name)
            shutil.copyfile(old_name, new_name)


def add_figures(chapter, missing_list = []):
    # chapter = 2
    # missing_list = [] # 11, 13, 18
    with open(os.path.join(DOC_DIR, "chapter0%d.rst" % chapter), encoding="utf-8") as input_file:
        rs = input_file.readlines()

    with open(os.path.join(DOC_DIR, "chapter0%d.rst" % chapter), "w", encoding="utf-8") as output_file:
        for ln in rs:
            m = re.search("<(?:Figure )?({CHAP}\.(\d{LP}1,2{RP}) .+)>".format(CHAP=chapter, LP="{", RP="}"), ln)
            #m = re.search("^.(.)", ln)
            if m:
                print(m.group(0), m.group(1), m.group(2))
                if int(m.group(2)) in missing_list:
                    output_file.write(ln)
                else:
                    output_file.write(".. figure:: chapter0{CHAP}/figure-{CHAP}.{FIGURE}.png\n\n    ".format(CHAP=chapter, FIGURE=m.group(2)))
                    output_file.write("Figure %s\n\n" % m.group(1))
#                if m.group(2) not in ("11", "13", "18"):
#                    output_file.write(".. figure:: chapter02/figure-2.%s.png\n\n    " % m.group(2))
#                    output_file.write("Figure %s\n\n" % m.group(1))
#                else:
#                    output_file.write(ln)
            else:
                output_file.write(ln)


def copy_figures_ch03():
    chapter = 3
    start_no = 32
    end_no = 51
    skip_list = [35, 36]
    missing_list = []

    copy_figures(chapter, start_no, end_no, skip_list, missing_list)


def add_figures_ch03():
    add_figures(3)


if __name__ == "__main__":
    # main()
    # add_figures()
    # copy_figures_ch11()
    #add_figures_ch11()
    #add_zero_prefix_to_figure_file_names()
    #copy_figures_ch01()
    #add_figures_ch01()
    #copy_figures_ch02()
    #add_figures_ch02()
    #copy_figures_ch03()
    add_figures_ch03()
