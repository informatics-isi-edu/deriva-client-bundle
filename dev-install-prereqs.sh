#!/usr/bin/env bash

pip install markdown==3.2.1 bdbag[boto,globus] fair-research-login git+https://github.com/anthony-tuininga/cx_Freeze.git@9e06b761740a9e93431ee7ea8d0b10f786446a6a
pip install git+https://github.com/informatics-isi-edu/deriva-py.git
pip install deriva-qt[PyQt5]@git+https://github.com/informatics-isi-edu/deriva-qt.git
pip install deriva-catalog-manage[csv]@git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git
