# DERIVA Client Tools

### Create binary distributions of DERIVA Client Tools

#### Building

Build environment installation prerequisites:

* A Python 3.5 or greater virtualenv
* cx_Freeze >= 6.0b1: `pip install git+https://github.com/anthony-tuininga/cx_Freeze.git`
* PyQT5: `pip install PyQt5`
    * MacOSX Only: `ln -s <venv>/lib/python3.5/site-packages/PyQt5/Qt/lib/* <venv>/lib/`
* bdbag: `pip install bdbag[boto,globus]`
* deriva-py: `pip install --upgrade git+https://github.com/informatics-isi-edu/deriva-py.git`
* deriva-qt: `pip install --upgrade git+https://github.com/informatics-isi-edu/deriva-qt.git`
* deriva-catalog-manage: `pip install --upgrade git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git`
* Packages (MacOSX only): http://s.sudre.free.fr/Software/files/Packages.dmg

###### Windows

```sh
python setup.py bdist_msi
```

###### MacOSX

```sh
python setup.py bdist_mac
packagesbuild --verbose "packaging/MacOS/Deriva Client Tools.pkgproj"
hdiutil create -fs HFSX -format UDZO -imagekey zlib-level=9 -srcfolder "./build/Deriva Client Tools.mpkg" -volname "DERIVA Client Tools-0.1.0" "./build/DERIVA-Client-Tools-0.1.0-osx"
```