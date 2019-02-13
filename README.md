# DERIVA Client Tools

The DERIVA Client Tools are a set of software packages (CLI and GUI), that allow users to interact with DERIVA platform servers. These tools provide functions such as:
1. Authentication services for programmatic and non browser-based access.
2. Bulk import and export of catalog assets and (meta) data.
3. Catalog configuration and administration.

## Installing client tools from source

Build environment installation prerequisites:

* A Python 3.5.4 or greater installation (or virtualenv) is required for
using the GUI tools (`deriva-qt`). Otherwise, Python 2.7 or greater is sufficient.

#### Installation sequence

Follow the installation sequence below. If the DERIVA GUI utilities
(`deriva-qt`) are not required, the following PyQt5 installation step may be skipped.
The `pip` commands listed below use the `pip3` executable convention,
which is common on systems where both Python2 and Python3 are installed.
If this does not apply to your system, use `pip` instead. Also note that
when installing into the system Python location via `pip` on Linux/MacOSX,
the commands must be run as root or the  `sudo` command must be prefixed
to the command line..

##### 1. Install PyQt5

For the DERIVA GUI utilities (`deriva-qt`), the PyQt5 software package is required.
Windows and MacOSX users can install PyQt5 via `pip`.
Linux users should install PyQt5 from their OS distribution software
installation management system.

* Windows/MacOSX:
    ```sh
    pip3 install PyQt5==5.11.3
    ```
* Fedora 27 or greater:
    ```sh
    sudo dnf install python3-qt5 python3-qt5-webengine python3-devel
    ```
* Ubuntu (18.04 or greater) or Debian (9 or greater):
    ```sh
    sudo apt-get install -y python3-pyqt5 python3-pyqt5.qtwebengine
    ```
* CentOS (7 or greater), others:

    For Centos7 (and other distros) that do not provide a package manager
    based distribution of Python3 PyQt5 bindings, and is therefore not
    officially supported. It is possible to install the `manylinux1_x86_64`
    wheel via `pip`, but it has not been thoroughly tested.
    ```sh
    pip3 install PyQt5==5.11.3
    ```

##### 2. Install other dependencies via `pip`

* bdbag: `pip3 install bdbag[boto,globus]`

##### 3. Install DERIVA software from GitHub source

* deriva-py: `pip3 install --upgrade git+https://github.com/informatics-isi-edu/deriva-py.git`
* deriva-catalog-manage: `pip3 install --upgrade git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git`
* deriva-qt (requires Python3 and PyQt5): `pip3 install --upgrade git+https://github.com/informatics-isi-edu/deriva-qt.git`

## Creating binary distributions of DERIVA Client Tools

#### Building

Build environment installation prerequisites:

* A Python 3.5.4 virtualenv
* cx_Freeze >= 6.0b1: `pip install git+https://github.com/anthony-tuininga/cx_Freeze.git`
* PyQT5: `pip install PyQt5==5.11.3`
    * MacOSX Only: `ln -s <absolute path to venv basedir>/lib/python3.6/site-packages/PyQt5/Qt/lib/* <absolute path to venv basedir>/lib/`
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