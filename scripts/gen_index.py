"""

gen_index.py 

   
    Generate index.txt files for docgen framework

"""

topheader="""
.. docs
..  :numbered:

:tocdepth: 6
"""

tocheader="""
.. toctree::
    :maxdepth: 6
    :titlesonly:
    :glob:
    :includehidden:
    :name: masetertoc

"""

skip_dirs=[".git", "publish","build"]
index_file="index.txt"
head_file="README"

doc_files=["index.txt", "README"]


if (__name__ == "__main__"):
    import os

    topheadwrite = 0;

    #for parent, dirs, files in os.walk(os.path.abspath(os.curdir)):
    for parent, dirs, files in os.walk(os.curdir):

        #filter directories
        dirs  = list(filter(lambda d: d not in skip_dirs, dirs))
        dirlist = [d+os.path.sep+"index" for d in dirs]
        dirlist.sort()

        filename = os.path.join(parent, index_file)

        # Backup old index.txt files
        #if (os.path.isfile(filename)):
        #    oldfilename = filename+".old"
        #    # rename existing index.txt files
        #    os.rename(filename, oldfilename)

        #filter txt and directories 
        files = list(filter(lambda f: f.endswith(".txt") and f not in index_file ,files))
        filelist = [os.path.splitext(f)[0] for f in files]
        filelist.sort()

        #debug prints
        #print("parent:", parent)
        #print(dirlist)
        #print(filelist)

        # create index.txt files 
        with open(filename, 'wt') as findex:
            if topheadwrite == 0:
                findex.write(topheader)
                topheadwrite = 1
            #print("parent:", parent)
            findex.write('='*80+'\n')
            findex.write((os.path.basename(os.path.abspath(parent))).upper()+'\n')
            findex.write('='*80+'\n')
            headerfile = os.path.join(parent, head_file)
            if (os.path.isfile(headerfile)):
                with open(headerfile) as hf:
                    findex.seek(0,0)
                    for line in hf:
                        findex.write(line)
            findex.write(tocheader)
            findex.write("\n"*2)
            for f in filelist:
                findex.write(" "*4+f+"\n")
            for d in dirlist:
                findex.write(" "*4+d+"\n")
            findex.write("\n"*2)
            


