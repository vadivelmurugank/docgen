===========================================
DOCUMENTATION 
===========================================

Philosophy
-------------------------------------------------------------------

WYSIWYM : WHAT YOU SEE IS WHAT YOU MEAN ( not GET)

Doc Framework to totally separate presentation and content: users can structure and write the document once, rather than repeatedly altering it for each mode of presentation. 

    * Use Document processor rather than word processed is used.
    * Write in text file and publish is any global format
    * Version control of each content


Documents and Presentations
-------------------------------------------------------------------


html
~~~~~~~

sphinx - html/pdf/latex
    sphinx-build -b html .. 

.. code-block:: 

    rst2html <file.txt> <file.html>
    rst2tex
    rst2pdf



hieroglyph
~~~~~~~~~~

generate HTML5 Presentations

.. code-block::

    sphinx hieroglyph extension
    sphinx/conf.py:

        extensions = ['sphinx.ext.mathjax','hieroglyph']

    sphinx-build -b slides /home/evadkan/scripts/docgen/template -c /home/evadkan/scripts/docgen/sphnix build/slides 


hovercraft - impress.js
~~~~~~~~~~~~~~~~~~~~~~~

Create impress.js presentation slides from restructure text

.. code-block::

    pip3 install hovercraft configparser

    # hovercraft
    hovercraft -a <sides.txt> build_dir/


rst2beamer
~~~~~~~~~~

rst2beamer - Ast file to Presentation

.. code-block::

    export TEXMFHOME="/home/evadkan/scripts/docgen/texmf/
    /home/evadkan/scripts/docgen/texmf/tex/latex/beamer/themes/theme
    beamerthemeERIC.sty  elogo.jpg*

    rst2beamer --theme=ERIC slides.txt slides.tex
    pdflatex slides.tex  


doxygen
~~~~~~~

doxygen -  Doxygen Documentation
    doxygen -f doxy.file

.. code-block::

    python3.4 -m peekextn --doxy > project.defines
    doxygen -g project.doxy
    cat doxy.config >> project.doxy
    cat project.defines >> project.doxy




Block diagrams
-------------------------------------------------------------------

blockdiag
~~~~~~~~~~

    python -m  <blockdiag>  <diag.py>

    blockdiag
    seqdiag
    actdiag
    nwdiag

    packetdiag
    rackdiag

    blockdiagrams/
        actdia
        blockdia
        nwdia
        packetdia
        seqdia

xmind
~~~~~~

xmind - Xmindmap

.. code-block:: 

    txt2xmind.py  <file.xtxt> <file.jpeg>



aafigure
~~~~~~~~

aafigure - Ascii to jpeg

.. code-block::

    sphnix extention : sphnix.aafigure

    python2 ~/scripts/docgen/aafigure/aafigure.py ~/ascii.txt -t jpg -o ~/ascii.jpg -f "#00ff87" -x "#000087" --proportional


DOCGEN FRAMEWORK
-------------------------------------------------------------------

install
~~~~~~~~~~

* sphinx
    pip3 install sphinx docutils

* slides
    pip3 install hieroglyph sphinx_rtd_theme
    pip3 install hovercraft configparser

* diagram
    pip3 install matplotlib
    pip3 install blockdiag seqdiag actdiag nwdiag
    pip3 install packetdiag rackdiag
    pip3 install aafig text2mind


docgen
~~~~~~~

Clone docgen Make framework
***************************

.. code-block::

    git clone https://github.com/vadivelmurugank/docgen.git

Make targets
************

.. code-block::

    docgen/sphinx/rules.doc

    docgen/defs.inc:

        # Defs

        DOCGEN = $(HOME)/picothing/scripts/docgen


        python = /usr/bin/python3
        python2 = /usr/bin/python2

        # SPHNIX
        DOCGEN_PATH = $(DOCGEN)/sphnix

        # XMIND
        XMINDGEN_PATH = $(DOCGEN)/xmindgen/

        # AAFIGURE
        AAFIGURE_PATH = $(DOCGEN)/aafigure

        # TEX MF PATH
        TEXMF_PATH = $(DOCGEN)/texmf


Docgen builds
**************

Makefile for doc:

    include $(HOME)/github/docgen/defs.inc
    include $(DOCGEN_PATH)/rules.doc


Make targets:

    .. code-block::
        
        make html
        make dirhtml
        make singlehtml
        make html TEXTFILE="textfile.txt"

    .. code-block::

        make slides
        make slides SLIDES="slides.txt"


    .. code-block::
        
        make latextpdf
        make pdfslides SLIDES="slides.txt"


    .. code-block::

        # Create S5html slides
        make s5slides S5SLIDES="s5slides.txt"


    .. code-block::
        
        # create  impress.js slides
        make impress IMPSLIDES="impslides.txt"

    .. code-block::

        # Create aafig
        make aafig AATEXT="asciitext.txt"


    .. code-block::

        # Create xmind map files
        make xmind XMINDTXT="xmindtxt.txt"

    .. code-block::

        # publish changes
        make publish


Publish Document to GIT gh-pages
--------------------------------------------------------------------


.. code-block::

    # create orphaned gh-pages branch
    git checkout --orphan gh-pages
    git branch

    # remove all cached files to be committed.
        git rm -rf .

.. code-block::

    # Create index.html
    echo "Hello Pages!!" > index.html
    git add index.html
    git commit -m 'initial gh-pages commit'

    # git push to gh-pages branch
        git push origin gh-pages

.. code-block::
    
    # add gh-pages as submodule
        git checkout master
        git branch

    # Create folder "publish" and add gh-pages as submodule.
    Changing the folder to "publish" will set to gh-pages branch
        git submodule add -b gh-pages https://github.com/vadivelmurugank/<< GIT >>.git publish
        git submodule init

    # Add gh-pages as submodule
    git commit -m "added gh-pages as submodule"
    git push origin master

.. code-block::

    # Push changes into gh-pages branch
        cd publish
        git add  <<file>>
        git commit -m  "file updates"
        git push -u origin gh-pages

    # Push "publish" in master branch
        cd ..
        git add publish
        git commit -m "update publish"
        git push -u origin master

.. code-block::

    # Git Clone with submodules
        git clone https://github.com/vadivelmurugank/docs.git
        cd publish
        git submodule update --init --recursive

    # Git clone with all submodules
        git clone --recursive https://github.com/vadivelmurugank/docs.git

    # Git pull with all submodules
        git pull --recurse-submodules
        git pull && git submodule init && git submodule update && git submodule status

    # git commit
        git push -u origin master
        git push -u origin gh-pages


TODO
-----------------

* mathjax template mathematics symbols and equations
* mathjax template physics, chemistry equations

* hovercraft impress.js
* hieroglyph extensions - pydot, numpy, ..

* matplotlib diagrams
    * Graphs
    * Charts

* Add web links to documentation processors



