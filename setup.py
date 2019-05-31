#
# Copyright 2019 University of Southern California
# Distributed under the GNU GPL 3.0 license. See LICENSE for more info.
#

""" Installation script for DERIVA Client Tools
"""

from setuptools import setup, find_packages
import os
import sys
import opcode
import subprocess
from distutils.sysconfig import get_python_lib
from cx_Freeze import setup, Executable

from version import __version__


def get_target_base():
    return "Win32GUI" if sys.platform == "win32" else None


def get_target_extension():
    return ".exe" if sys.platform == "win32" else ""


def get_distutils_path():
    return os.path.join(os.path.dirname(opcode.__file__), 'distutils')


def get_installed_file_path(path):
    return os.path.abspath(get_python_lib() + os.path.sep + path)


def compile_qt_resources():
    print("compiling QT resources...")
    subprocess.call(["pyrcc5" + get_target_extension(), "-o", "resources.py", "./resources.qrc"])


def get_extra_resources():
    compile_qt_resources()
    includes = list()
    includes.append((get_distutils_path(), "lib/distutils"))
    if sys.platform == "darwin":
        includes.append(("./resources/MacOS/DERIVA Command Line Applications.terminal",
                         "DERIVA Command Line Applications.terminal"))
    return includes


def get_bdist_mac_options():
    return {
        "iconfile": "./resources/images/deriva-star.icns",
        "custom_info_plist": "./resources/MacOS/Info.plist",
        "bundle_name": "DERIVA Client Tools",
        "rpath_lib_folder": sys.prefix + "/lib"
    }


def get_bdist_msi_options():
    return {
        "add_to_path": True,
        "upgrade_code": __version__,
        "target_name": "DERIVA-Client-Tools-%s-win" % __version__,
        "install_icon": "resources\\images\\deriva-star.ico"
    }


setup(
    name='DERIVA Client Tools',
    description='Bundled client application suite for the DERIVA Platform',
    url='https://github.com/informatics-isi-edu/deriva-client-bundle',
    maintainer='USC Information Sciences Institute, Informatics Systems Research Division',
    maintainer_email='isrd-support@isi.edu',
    version=__version__,
    python_requires='>3.5.2',
    options={
        "build_exe": {
            "optimize": 1,
            "namespace_packages": ["deriva", "deriva.utils", "deriva.utils.catalog"],
            "packages": ["pkg_resources._vendor",
                         "bdbag.fetch.resolvers",
                         "goodtables",
                         "boto3"],
            "includes": ["atexit",
                         "idna.idnadata",
                         "html.parser",
                         "globus_sdk"],
            "include_files": get_extra_resources(),
            "excludes": ["tkinter", "numpy", "scipy", "pandas", "distutils"],
        },
        "bdist_msi": get_bdist_msi_options(),
        "bdist_mac": get_bdist_mac_options()
    },
    executables=[
        # DERIVA GUI(Qt5) Applications
        Executable("./about.py",
                   targetName="about-deriva-client-tools" + get_target_extension(),
                   base=get_target_base(),
                   shortcutName="About DERIVA Client Tools",
                   shortcutDir="StartMenuFolder",
                   icon="./resources/images/deriva-star.ico"),
        Executable(get_installed_file_path("deriva/qt/auth_agent/__main__.py"),
                   targetName="deriva-auth" + get_target_extension(),
                   base=get_target_base(),
                   shortcutName="DERIVA Authentication Agent",
                   shortcutDir="StartMenuFolder",
                   icon=get_installed_file_path("deriva/qt/auth_agent/resources/images/keys.ico")),
        Executable(get_installed_file_path("deriva/qt/upload_gui/__main__.py"),
                   targetName="deriva-upload" + get_target_extension(),
                   base=get_target_base(),
                   shortcutName="DERIVA Upload Utility",
                   shortcutDir="StartMenuFolder",
                   icon=get_installed_file_path("deriva/qt/upload_gui/resources/images/upload.ico")),

        # DERIVA CLI Applications
        Executable(get_installed_file_path("deriva/config/acl_config.py"),
                   targetName="deriva-acl-config" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/annotation_config.py"),
                   targetName="deriva-annotation-config" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/dump_catalog_annotations.py"),
                   targetName="deriva-annotation-dump" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/rollback_annotation.py"),
                   targetName="deriva-annotation-rollback" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/core/hatrac_cli.py"),
                   targetName="deriva-hatrac-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/transfer/upload/__main__.py"),
                   targetName="deriva-upload-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/transfer/download/__main__.py"),
                   targetName="deriva-download-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/seo/sitemap_cli.py"),
                   targetName="deriva-sitemap-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/utils/catalog/manage/dump_catalog.py"),
                   targetName="deriva-catalog-dump" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/utils/catalog/components/deriva_catalog.py"),
                   targetName="deriva-catalog-config" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/utils/catalog/manage/deriva_csv.py"),
                   targetName="deriva-csv" + get_target_extension(),
                   base="Console"),

        # bdbag CLI Applications
        Executable(get_installed_file_path("bdbag/bdbag_cli.py"),
                   targetName="bdbag" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("bdbag/bdbag_utils.py"),
                   targetName="bdbag-utils" + get_target_extension(),
                   base="Console"),
    ],
    requires=[
        'cx_Freeze',
        'markdown'
    ],
    license='GNU GPL 3.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)


