import os
import re


def file_regex_cleanup():
    filelist1 = [f1 for f1 in os.listdir(os.curdir + r'\Input')]
    for f1 in filelist1:
        if f1[-4:] == '.CPY':
            with open(os.curdir + '\\Input\\' + f1, 'r') as f:
                print(f1)
                for l in f.readlines():
                    Var_rplc_cmt = re.sub("[/s$@*&?].*[$@*&?]", "", l)
                    Var_rplc_sng_cmt = re.sub("[/s$@*&?].*[\W]", "", Var_rplc_cmt)
                    Var_rplc_chr = Var_rplc_sng_cmt.replace(Var_rplc_sng_cmt[0:6], "      ")
                    if len(Var_rplc_chr.strip()) > 0 and not (Var_rplc_chr.lstrip().startswith('88')):
                        print(Var_rplc_chr)
                        f2 = open(os.curdir + '\\output\\' + f1, 'a+')
                        for line in Var_rplc_chr:
                            for i in line:
                                f2.write(i)
                        f2.close()


def read_txt_file():
    filelist1 = [f1 for f1 in os.listdir(os.curdir + r'\output')]
    for f1 in filelist1:
        if f1[-4:] == '.CPY':
            with open(os.curdir + '\\output\\' + f1, 'r') as fp:
                Lines = fp.readlines()
                for line in Lines:
                    if 'PIC X' in line and 'FILLER' not in line and 'HEADER' not in line and 'TRAILER' not in line:
                        print("{}".format(line.strip()))
                        f2 = open(os.curdir + '\\final\\' + f1, 'a+')
                        for newline in line.strip():
                            for i in newline:
                                f2.write(i)
                        f2.close()


if __name__ == '__main__':
    file_regex_cleanup()
    read_txt_file()
