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

* A Python 3.5.4 or greater installation (or virtual environment) is required for
using the GUI tools (`deriva-qt`). Otherwise, Python 2.7 or greater is
sufficient, though Python 3.5.4 or greater is _recommended_.
* For MacOSX and Linux systems which include Python as a core part of the
operating system, it is _highly recommended_ to install this software
into a _virtual environment_, so that it does not interfere or conflict
with the operating system's Python installation. The native Python3
`venv` module, the `virtualenv` package from PyPi, or the
[Anaconda Distribution](https://www.anaconda.com/distribution/)
environment are all suitable.

* The most recent versions of `git`, `pip`, `setuptools`, and `wheel`
are recommended. If these components are already installed, updating them
to the latest versions available is _optional_.

    * `Windows` (7 or greater) / `MacOSX` (10.11 or greater):

        1. Download and install `git` from [here](https://git-scm.com).
        2. For non-virtual environments:
            ```sh
            pip3 install –-upgrade pip, setuptools, wheel
            ```

    * `Fedora` (28 or greater) for non-virtual environments:
        ```sh
        sudo dnf install git python3-pip python3-setuptools python3-wheel
        ```

    * `Ubuntu` (18.04 or greater) or `Debian` (9 or greater) for non-virtual environments:
        ```sh
        sudo apt-get install git python3-pip python3-setuptools python3-wheel
        ```

    *  Python3 virtual environments (any OS):
        ```sh
        pip install –-upgrade pip, setuptools, wheel
        ```

* Important note when using `pip` to install software into system Python locations.
Many newer Linux (as well as MacOSX) distributions contain both Python2
and Python3 installed alongside each other. In these environments, both
the python interpreter and `pip` are symlinked to the appropriate version,
with `python` and `pip` generally linked to the Python2 versions.
Python3 versions are commonly accessed via `python3` and `pip3`.
If you are working outside of a Python3 virtual environment and installing
either to the system Python location (not recommended) or a user-based
location (e.g. with the `pip` `--user` argument), then you _must_
substitute `pip3` for `pip` when issuing `pip` installation commands.
Also note that when installing into the system Python location via
`pip` on Linux/MacOSX, the commands must be run as root or the  `sudo`
command must be prefixed to the command line.

#### Installation sequence

Follow the installation sequence below. If the DERIVA GUI utilities
(`deriva-qt`) are not required, the PyQt5 installation step may be skipped.

##### 1. Install __PyQt5__:

For the DERIVA GUI utilities (`deriva-qt`), the PyQt5 (with WebEngine)
software package is required. For Linux 64-bit variants, Windows x86_64
variants, and MacOSX 64-bit variants, `pip`-based installation of the
PyPi wheel distribution is recommended.  Linux users who wish to install
PyQt5 into the system Python (not recommended) should use the package
manager provided by the operating system instead of `pip`.

*  Python3 virtual environments (any OS):
    ```sh
    pip install pyqtwebengine
    ```
* `Windows` (7 or greater):
    ```sh
    pip3 install pyqtwebengine
    ```
* `MacOSX` (10.11 or greater):
    ```sh
    sudo pip3 install pyqtwebengine
    ```
* `Fedora` (27 or greater) for system Python installation:
    ```sh
    sudo dnf install python3-qt5-webengine
    ```
* `Ubuntu` (18.04 or greater) or `Debian` (9 or greater) for system Python installation:
    ```sh
    sudo apt-get install python3-pyqt5.qtwebengine
    ```
* `CentOS` (7 or greater):

    For Centos7, which does not make an installation of Python3 available
    through it's package manager, it is recommended to install Python3 and
    create a virtual environment following the procedures outlined
    [here](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7).
    After a successful installation of Python3 and activation of a
    Python 3 virtual envirionment, simply follow the instructions for
    installing the PyQt5 WebEngine software into a virtual environment
    as outlined in this document.

* Other Linux 64-bit:
    Other Linux 64-bit distributions have not been tested. However, the
    software may function correctly on these systems. The recommend
    approach for these systems is to create a Python3 virtual environment
    and install the PyQt5 WebEngine software into that virtual
    environment as outlined in this document.

##### 2. Install other dependencies via `pip`:

* __bdbag__: `pip install bdbag[boto,globus]`

`NOTE`: Do not forget to substitute `pip3` for `pip` if you are __NOT__
installing to a Python3 virtual environment and using a system that
provides both Python2 and Python3.

##### 3. Install DERIVA software from GitHub source:

* __deriva-py__: `pip install git+https://github.com/informatics-isi-edu/deriva-py.git`
* __deriva-catalog-manage__: `pip install git+https://github.com/informatics-isi-edu/deriva-catalog-manage.git`
* __deriva-qt__ (requires Python3 and PyQt5 WebEngine): `pip install git+https://github.com/informatics-isi-edu/deriva-qt.git`

`NOTE`: Do not forget to substitute `pip3` for `pip` if you are __NOT__
installing to a Python3 virtual environment and using a system that
provides both Python2 and Python3.

## Creating binary distributions of DERIVA Client Tools
Self installing binary "bundles" for Windows and MacOSX can be generated
using the following procedure.

#### Building

Build environment installation prerequisites:

* A Python 3.5.4 virtualenv
* __cx_Freeze__ >= 6.0b1: `pip install git+https://github.com/anthony-tuininga/cx_Freeze.git`
* __PyQt5 WebEngine__: `pip install pyqtwebengine`
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