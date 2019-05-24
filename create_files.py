#!/usr/bin/env python

from glob import glob

def create_files(): #{

    files = [
            '1.jpg',
            '2.jpg',
            '3.jpg',
            ]
    for afile in files: #{
        open(afile, "w").close();

def main(): #{

    print('Hello, Denis! I\'ll create for you some files!\n-----------\n')
    create_files();
    files = glob("*.jpg")

    for afile in files: #{
        print(afile)
#}

if (__name__ == "__main__"): #{
    main();
#}
