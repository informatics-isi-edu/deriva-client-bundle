#!/bin/bash
set -e pipefail

rm -rf ./deriva-client-bundle-dev
python3 -m venv deriva-client-bundle-dev
cd deriva-client-bundle-dev
source ./bin/activate
#python -m pip install --upgrade pip wheel markdown==3.2.1 setuptools cx_Freeze>=6.5.3
python -m pip install --upgrade pip wheel markdown==3.2.1 setuptools
pip install git+https://github.com/marcelotduarte/cx_Freeze.git
pip install "PyQtWebEngine>=5.15"
pip install setuptools_scm
pip install bdbag[boto,globus]
pip install bdbag_gui
pip install fair-research-login
pip install fair-identifiers-client
pip install git+https://github.com/informatics-isi-edu/deriva-py.git
pip install git+https://github.com/informatics-isi-edu/deriva-qt.git
pip install deriva-catalog-manage[csv]@git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git
git clone https://github.com/informatics-isi-edu/deriva-client-bundle
cd deriva-client-bundle
export DERIVA_CLIENT_BUNDLE_VERSION=`python ./version.py`
python setup.py bdist_mac
cp -R "./build/DERIVA Client Tools.app/Contents/MacOS/lib/PyQt5/Qt/lib/QtWebEngineCore.framework/Resources"/* "./build/DERIVA Client Tools.app/Contents/MacOS"
codesign --remove-signature "./build/DERIVA Client Tools.app/Contents/MacOS/lib/Python"
packagesbuild --verbose "./packaging/MacOS/Deriva Client Tools.pkgproj"
hdiutil create -fs HFSX -format UDZO -imagekey zlib-level=9 -srcfolder "./build/Deriva Client Tools.mpkg" -volname "DERIVA Client Tools-${DERIVA_CLIENT_BUNDLE_VERSION}" ./build/DERIVA-Client-Tools-${DERIVA_CLIENT_BUNDLE_VERSION}-osx
