#!/usr/bin/env bash

pip install markdown==3.2.1 cx_freeze>=6.5 bdbag[boto,globus]
pip install git+https://github.com/informatics-isi-edu/deriva-py.git
pip install deriva-qt[PyQt5]@git+https://github.com/informatics-isi-edu/deriva-qt.git
pip install deriva-qt[PyQt5]@git+https://github.com/informatics-isi-edu/deriva-workbench.git

