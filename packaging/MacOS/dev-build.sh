#!/bin/bash
set -e pipefail

rm -rf ./deriva-client-bundle-dev
python3 -m venv deriva-client-bundle-dev
cd deriva-client-bundle-dev
source ./bin/activate
python -m pip install --upgrade pip wheel "setuptools<=57.5.0"
pip install "markdown==3.2.1" "cx_Freeze<6.11"
pip install "PyQt5==5.15.9" "PyQt5-Qt5==5.15.2" "PyQtWebEngine==5.15.4"
pip install "cryptography<39.0.0"
pip install setuptools_scm
pip install bdbag[boto]
pip install "globus_sdk<4"
pip install bdbag_gui
pip install minid
pip install fair-research-login
pip install fair-identifiers-client
pip install git+https://github.com/informatics-isi-edu/deriva-py.git
pip install git+https://github.com/informatics-isi-edu/deriva-qt.git
pip install git+https://github.com/informatics-isi-edu/deriva-workbench.git
git clone https://github.com/informatics-isi-edu/deriva-client-bundle
cd deriva-client-bundle
export DERIVA_CLIENT_BUNDLE_VERSION=`python ./version.py`
echo ${DERIVA_CLIENT_BUNDLE_VERSION} > ./deriva-client-bundle-version.txt
python setup.py bdist_mac
cp -R "./build/DERIVA Client Tools.app/Contents/MacOS/lib/PyQt5/Qt5/lib/QtWebEngineCore.framework/Resources"/* "./build/DERIVA Client Tools.app/Contents/MacOS"
codesign --remove-signature "./build/DERIVA Client Tools.app/Contents/MacOS/lib/Python"
packagesbuild --verbose "./packaging/MacOS/Deriva Client Tools.pkgproj"
hdiutil create -fs HFSX -format UDZO -imagekey zlib-level=9 -srcfolder "./build/Deriva Client Tools.mpkg" -volname "DERIVA Client Tools-${DERIVA_CLIENT_BUNDLE_VERSION}" ./build/DERIVA-Client-Tools-${DERIVA_CLIENT_BUNDLE_VERSION}-osx
