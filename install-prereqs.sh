#!/usr/bin/env bash

pip install urllib3==1.24.3 markdown bdbag[boto,globus] git+https://github.com/anthony-tuininga/cx_Freeze.git
pip install git+https://github.com/informatics-isi-edu/deriva-py.git
pip install git+https://github.com/informatics-isi-edu/deriva-qt.git#egg=deriva-qt[PyQt5]
pip install git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git
