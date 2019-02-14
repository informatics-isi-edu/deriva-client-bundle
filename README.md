# DERIVA Client Tools

[![Build Status: Windows](http://buildbot.isrd.isi.edu/badges/deriva-client-bundle-Windows.svg?left_text=Build%20Status:%20Windows)](http://buildbot.isrd.isi.edu/#/)
[![Build Status: MacOSX](http://buildbot.isrd.isi.edu/badges/deriva-client-bundle-MacOS.svg?left_text=Build%20Status:%20MacOSX)](http://buildbot.isrd.isi.edu/#/)

The DERIVA Client Tools are a set of software packages (CLI and GUI), that allow users to interact with DERIVA platform servers. These tools provide functions such as:
1. Authentication services for programmatic and non browser-based access.
2. Bulk import and export of catalog assets and (meta) data.
3. Catalog configuration and administration.

## Installing DERIVA Client Tools from binaries
Binary installer packages for Windows and MacOSX are currently provided.

* Official release-stream installers can be found
[here](https://github.com/informatics-isi-edu/deriva-client-bundle/releases).

* Automatically generated installer builds, driven by commits to master branch of
[`deriva-py`](https://github.com/informatics-isi-edu/deriva-py),
[`deriva-qt`](https://github.com/informatics-isi-edu/deriva-qt),
[`deriva-catalog-manage`](https://github.com/informatics-isi-edu/deriva-catalog-manage)
and this repository can be found [here](http://buildbot.isrd.isi.edu/~buildbot/deriva-client-bundle/).

## Installing DERIVA Client Tools from source

Build environment installation prerequisites:

* A Python 3.5.4 or greater installation (or virtualenv) is required for
using the GUI tools (`deriva-qt`). Otherwise, Python 2.7 or greater is sufficient.
* The most recent versions of pip, setuptools, and wheel installed.
    ```sh
    pip3 install –-upgrade pip, setuptools, wheel
    ```

#### Installation sequence

Follow the installation sequence below. If the DERIVA GUI utilities
(`deriva-qt`) are not required, the PyQt5 installation step may be skipped.
The `pip` commands listed below use the `pip3` executable name, which is
generally present on systems where both Python2 and Python3 are installed.
If this does not apply to your system, use `pip` instead. Also note that
when installing into the system Python location via `pip` on Linux/MacOSX,
the commands must be run as root or the  `sudo` command must be prefixed
to the command line.

##### 1. Install __PyQt5__:

For the DERIVA GUI utilities (`deriva-qt`), the PyQt5 software package is required.
Windows and MacOSX users can install PyQt5 via `pip`.
Linux users should install PyQt5 from their OS distribution's software
package management system.

* `Windows` (7 or greater) / `MacOSX` (10.11 or greater):
    ```sh
    pip3 install PyQt5==5.11.3
    ```
* `Fedora` (27 or greater):
    ```sh
    sudo dnf install python3-qt5 python3-qt5-webengine python3-devel
    ```
* `Ubuntu` (18.04 or greater) or `Debian` (9 or greater):
    ```sh
    sudo apt-get install -y python3-pyqt5 python3-pyqt5.qtwebengine
    ```
* `CentOS` (7 or greater), others:

    For Centos7 (and other distros) that do not provide a package manager
    based distribution of the Python3 PyQt5 bindings, the DERIVA GUI components are
    not officially supported. NOTE: It is possible to install the PyQt5
    `manylinux1_x86_64` wheel via `pip`, and while the GUI software
    components may function properly with this package, they have not
    been thoroughly tested.
    ```sh
    pip3 install PyQt5==5.11.3
    ```

##### 2. Install other dependencies via `pip`:

* __bdbag__: `pip3 install bdbag[boto,globus]`

##### 3. Install DERIVA software from GitHub source:

* __deriva-py__: `pip3 install --upgrade git+https://github.com/informatics-isi-edu/deriva-py.git`
* __deriva-catalog-manage__: `pip3 install --upgrade git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git`
* __deriva-qt__ (requires Python3 and PyQt5): `pip3 install --upgrade git+https://github.com/informatics-isi-edu/deriva-qt.git`

## Creating binary distributions of DERIVA Client Tools
Self installing binary "bundles" for Windows and MacOSX can be generated
using the following procedure.

#### Building

Build environment installation prerequisites:

* A Python 3.5.4 virtualenv
* __cx_Freeze__ >= 6.0b1: `pip install git+https://github.com/anthony-tuininga/cx_Freeze.git`
* __PyQt5__: `pip install PyQt5==5.11.3`
    * MacOSX Only: `ln -s <absolute path to venv basedir>/lib/python3.6/site-packages/PyQt5/Qt/lib/* <absolute path to venv basedir>/lib/`
* __bdbag__: `pip install bdbag[boto,globus]`
* __deriva-py__: `pip install --upgrade git+https://github.com/informatics-isi-edu/deriva-py.git`
* __deriva-qt__: `pip install --upgrade git+https://github.com/informatics-isi-edu/deriva-qt.git`
* __deriva-catalog-manage__: `pip install --upgrade git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git`
* __Packages__ (MacOSX only): http://s.sudre.free.fr/Software/files/Packages.dmg

##### Bundling
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