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
    includes.append((get_installed_file_path("deriva/core/schemas"), "deriva/core/schemas"))
    if sys.platform == "darwin":
        includes.append(("./resources/MacOS/DERIVA Command Line Applications.terminal",
                         "DERIVA Command Line Applications.terminal"))
    return includes


def get_bdist_mac_options():
    return {
        "iconfile": "./resources/images/deriva-star.icns",
        "custom_info_plist": "./resources/MacOS/Info.plist",
        "bundle_name": "DERIVA Client Tools",
    }


def get_bdist_msi_options():
    return {
        "all_users": False,
        "add_to_path": True,
        "upgrade_code": "{c3c21b7a-7dd4-43c0-a2b8-6f7185c174a5}",
        "target_name": "DERIVA-Client-Tools-%s" % __version__,
        "install_icon": "resources\\images\\deriva-star.ico"
    }


setup(
    name='DERIVA Client Tools',
    description='Bundled client application suite for the DERIVA Platform',
    url='https://github.com/informatics-isi-edu/deriva-client-bundle',
    maintainer='USC Information Sciences Institute, Informatics Systems Research Division',
    maintainer_email='isrd-support@isi.edu',
    version=__version__,
    python_requires='>3.7',
    options={
        "build_exe": {
            "optimize": 1,
            "packages": ["bdbag.fetch.resolvers",
                         "portalocker",
                         "boto3",
                         "fair_research_login"],
            "includes": ["atexit",
                         "idna.idnadata",
                         "html.parser",
                         "globus_sdk"],
            "include_files": get_extra_resources(),
            "excludes": ["tkinter", "numpy", "scipy", "pandas"],
        },
        "bdist_msi": get_bdist_msi_options(),
        "bdist_mac": get_bdist_mac_options()
    },
    executables=[
        # DERIVA GUI(Qt5) Applications
        Executable("./about.py",
                   target_name="about-deriva-client-tools" + get_target_extension(),
                   base=get_target_base(),
                   shortcut_name="About DERIVA Client Tools",
                   shortcut_dir="StartMenuFolder",
                   icon="./resources/images/deriva-star.ico"),
        Executable(get_installed_file_path("deriva/qt/auth_agent/__main__.py"),
                   target_name="deriva-auth" + get_target_extension(),
                   base=get_target_base(),
                   shortcut_name="DERIVA Authentication Agent",
                   shortcut_dir="StartMenuFolder",
                   icon=get_installed_file_path("deriva/qt/auth_agent/resources/images/keys.ico")),
        Executable(get_installed_file_path("deriva/qt/upload_gui/__main__.py"),
                   target_name="deriva-upload" + get_target_extension(),
                   base=get_target_base(),
                   shortcut_name="DERIVA Upload Utility",
                   shortcut_dir="StartMenuFolder",
                   icon=get_installed_file_path("deriva/qt/upload_gui/resources/images/upload.ico")),
        Executable(get_installed_file_path("deriva/workbench/__main__.py"),
                   target_name="deriva-workbench" + get_target_extension(),
                   base=get_target_base(),
                   shortcut_name="DERIVA Schema Workbench",
                   shortcut_dir="StartMenuFolder",
                   icon=get_installed_file_path("deriva/workbench/icons/workbench.ico")),

        # DERIVA CLI Applications
        Executable(get_installed_file_path("deriva/config/acl_config.py"),
                   target_name="deriva-acl-config" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/annotation_config.py"),
                   target_name="deriva-annotation-config" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/dump_catalog_annotations.py"),
                   target_name="deriva-annotation-dump" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/rollback_annotation.py"),
                   target_name="deriva-annotation-rollback" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/config/annotation_validate.py"),
                   target_name="deriva-annotation-validate" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/core/catalog_cli.py"),
                   target_name="deriva-catalog-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/core/hatrac_cli.py"),
                   target_name="deriva-hatrac-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/transfer/upload/__main__.py"),
                   target_name="deriva-upload-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/transfer/download/__main__.py"),
                   target_name="deriva-download-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/transfer/backup/__main__.py"),
                   target_name="deriva-backup-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/transfer/restore/__main__.py"),
                   target_name="deriva-restore-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/seo/sitemap_cli.py"),
                   target_name="deriva-sitemap-cli" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/core/utils/globus_auth_utils.py"),
                   target_name="deriva-globus-auth-utils" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/utils/catalog/manage/dump_catalog.py"),
                   target_name="deriva-catalog-dump" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/utils/catalog/components/deriva_catalog.py"),
                   target_name="deriva-catalog-config" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("deriva/utils/catalog/manage/deriva_csv.py"),
                   target_name="deriva-csv" + get_target_extension(),
                   base="Console"),

        # bdbag Applications
        Executable(get_installed_file_path("bdbag/bdbag_cli.py"),
                   target_name="bdbag" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("bdbag/bdbag_utils.py"),
                   target_name="bdbag-utils" + get_target_extension(),
                   base="Console"),
        Executable(get_installed_file_path("bdbag_gui/__main__.py"),
                   target_name="bdbag-gui" + get_target_extension(),
                   base=get_target_base(),
                   shortcut_name="BDBag GUI",
                   shortcut_dir="StartMenuFolder",
                   icon=get_installed_file_path("bdbag_gui/images/bag.ico")),

        # minid CLI
        Executable(get_installed_file_path("minid/commands/main.py"),
                   target_name="minid" + get_target_extension(),
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
