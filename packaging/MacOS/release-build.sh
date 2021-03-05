#!/bin/bash
set -e pipefail

rm -rf ./deriva-client-bundle-release
python3 -m venv deriva-client-bundle-release
cd deriva-client-bundle-release
source ./bin/activate
python -m pip install --upgrade pip wheel setuptools
pip install "markdown==3.2.1" "cx_Freeze>=6.5.3"
pip install setuptools_scm
pip install deriva-client
pip install deriva-catalog-manage[csv]
git clone https://github.com/informatics-isi-edu/deriva-client-bundle
cd deriva-client-bundle
export DERIVA_CLIENT_BUNDLE_VERSION=`python ./version.py`
echo ${DERIVA_CLIENT_BUNDLE_VERSION} > ./deriva-client-bundle-version.txt
python setup.py bdist_mac
cp -R "./build/DERIVA Client Tools.app/Contents/MacOS/lib/PyQt5/Qt/lib/QtWebEngineCore.framework/Resources"/* "./build/DERIVA Client Tools.app/Contents/MacOS"
codesign --remove-signature "./build/DERIVA Client Tools.app/Contents/MacOS/lib/Python"
packagesbuild --verbose "./packaging/MacOS/Deriva Client Tools.pkgproj"
hdiutil create -fs HFSX -format UDZO -imagekey zlib-level=9 -srcfolder "./build/Deriva Client Tools.mpkg" -volname "DERIVA Client Tools-${DERIVA_CLIENT_BUNDLE_VERSION}" ./build/DERIVA-Client-Tools-${DERIVA_CLIENT_BUNDLE_VERSION}-osx
