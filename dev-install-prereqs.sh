#!/usr/bin/env bash

pip install urllib3==1.24.3 markdown bdbag[boto,globus] fair-research-login git+https://github.com/anthony-tuininga/cx_Freeze.git@9e06b761740a9e93431ee7ea8d0b10f786446a6a
pip install git+https://github.com/informatics-isi-edu/deriva-py.git
pip install git+https://github.com/informatics-isi-edu/deriva-qt.git#egg=deriva-qt[PyQt5]
pip install git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git#egg=deriva-catalog-manage[csv]
