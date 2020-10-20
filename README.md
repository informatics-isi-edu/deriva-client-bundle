# DERIVA Client Tools: Installer Packages

[![Build Status: Windows](http://buildbot.isrd.isi.edu/badges/deriva-client-bundle-Windows.svg?left_text=Build%20Status:%20Windows)](http://buildbot.isrd.isi.edu/#/)
[![Build Status: MacOSX](http://buildbot.isrd.isi.edu/badges/deriva-client-bundle-MacOS.svg?left_text=Build%20Status:%20MacOSX)](http://buildbot.isrd.isi.edu/#/)
[![Github Latest Release Downloads](https://img.shields.io/github/downloads/informatics-isi-edu/deriva-client-bundle/latest/total.svg?maxAge=600)](https://github.com/informatics-isi-edu/deriva-client-bundle/releases/latest)


The _DERIVA Client Tools_ ([`deriva-client`](https://github.com/informatics-isi-edu/deriva-client)) are a set of software packages 
that allow users to interact with DERIVA platform servers. 

### What is this repository?
This repository contains support code used for generating pre-compiled 
installer packages of `deriva-client` and a hosting location for 
official releases of these installers. The `deriva-client` package is a separate (but dependent) component of this package. 

### Am I in the right place?

* If you are looking to download these installer packages, then you have 
come to the right place. See [below](#downloading-the-installer-packages).

* If you are looking for the code that actually _builds_ the installer 
packages and the relevant documentation, then you have come to the 
right place. See [below](#building-the-installer-packages).

* If you are looking for information about `deriva-client` itself 
(like what it is and how to use it), then you have come to the _wrong_ place. 
See the documentation [here](https://github.com/informatics-isi-edu/deriva-client#deriva-client).


### Downloading the Installer Packages
Installation packages of `deriva-client` for Windows and MacOSX are 
currently provided. These installer packages include a bundled Python interpreter and all 
other software dependencies and are recommended for Windows and MacOSX 
users who are looking for a more traditional "turnkey" installation. 

Two types of installer package builds are available: _release_ builds 
and _development_ builds. A _release_ build is a stable, official 
version of the installer package, while a _development_ build reflects 
the current state of each underlying software component collected in the
`deriva-client` package. If you are not sure about which one you need, 
then download the most recent _release_ build.

###### Release Builds
For release builds, please download the installers from the official
[releases](https://github.com/informatics-isi-edu/deriva-client-bundle/releases) page.

###### Development Builds
Development builds, automatically generated by commits to master branch of
[`deriva-py`](https://github.com/informatics-isi-edu/deriva-py),
[`deriva-qt`](https://github.com/informatics-isi-edu/deriva-qt),
[`deriva-catalog-manage`](https://github.com/informatics-isi-edu/deriva-catalog-manage),
and this repository can be found [here](http://buildbot.isrd.isi.edu/~buildbot/deriva-client-bundle/).

### Installing

The software can be installed as a system installation (for all users) or per-user only.
System installations will require administrative privileges on the target system, whereas
per-user installations will not. 

* On MacOSX, users must click the `"Change Installation Location..."` and then select 
`"Install for me only"` to perform a user installation. The software will be installed 
into the user's home directory in the subdirectory `Applications/DERIVA Client Tools`.

* On Windows, the installer package defaults to user-mode 
installation. There is no interactive installer prompt for a system installation, however, 
a system installation can be performed via command line by using the `msiexec /i` command 
and then the path to the installer package, followed by the flag `ALLUSERS=1`. For example:
    ```sh
    msiexec /i DERIVA-Client-Tools-1.3.0-win-amd64.msi ALLUSERS=1
    ```

### Building the Installer Packages

Documentation on how to build the installer packages on each supported 
platform can be found [here](./building.md).

### Release Procedure

Documentation outlining the release procedure for `deriva-client` and 
the corresponding installer packages can be found [here](./releasing.md).