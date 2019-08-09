## Creating binary distributions of DERIVA Client Tools

#### Building

Build environment installation prerequisites:

* Base environment
    * A __Python 3.5.4__ or greater _virtualenv_ or _venv_
    
* Common dependencies
    * __cx_Freeze__ >= 6.0b1: `pip install git+https://github.com/anthony-tuininga/cx_Freeze.git@9e06b761740a9e93431ee7ea8d0b10f786446a6a`
    * __markdown__: `pip install markdown`
    * __PyQt5 WebEngine__: `pip install pyqtwebengine`
        
* MacOSX Only:
    * __PyQt5 WebEngine__: `ln -s <absolute path to venv basedir>/lib/python3.5/site-packages/PyQt5/Qt/lib/* <absolute path to venv basedir>/lib/`
    * __Packages__: http://s.sudre.free.fr/Software/files/Packages.dmg

* Dependencies for `deriva-client` components: 

    Install `deriva-client` package from PyPi __or__ individual software components directly from GitHub, but not both. 

    1. PyPi releases:
        * `pip install deriva-client`
    2. GitHub source:   
        * __bdbag__: `pip install bdbag[boto,globus]`
        * __Globus Native App login__: `pip install fair-research-login`
        * __deriva-py__: `pip install git+https://github.com/informatics-isi-edu/deriva-py.git`
        * __deriva-qt__: `pip install git+https://github.com/informatics-isi-edu/deriva-qt.git`
        * __deriva-catalog-manage__: `pip install git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git`

#### Bundling
The bundling process uses [`cx_Freeze`](https://github.com/anthony-tuininga/cx_Freeze)
to "freeze" the Python environment and installed software and package everything
into a single application that can be redistributed to (and easily installed
by) end users.

Run the bundling commands from within the root of the `deriva-client-bundle` source directory.

###### Windows installer

```sh
python setup.py bdist_msi
```

###### MacOSX installer

```sh
python setup.py bdist_mac
packagesbuild --verbose "./packaging/MacOS/Deriva Client Tools.pkgproj"
hdiutil create -fs HFSX -format UDZO -imagekey zlib-level=9 -srcfolder "./build/Deriva Client Tools.mpkg" -volname "DERIVA Client Tools" "./build/DERIVA-Client-Tools-osx"
```
