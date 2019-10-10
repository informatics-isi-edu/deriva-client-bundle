## Release Process

##### This document outlines the steps required to release `deriva-client`, its direct dependencies, and `deriva-client-bundle` along with its corresponding platform-specific installer packages.

1. Bump version, commit/push to GitHub, build dists and upload artifacts to PyPi for each of the following: `deriva-py`, `deriva-qt`, `deriva-catalog-manage`.
2. Release each component listed above on its individual GitHub page.
3. Bump version of `deriva-client` and bump versions of individual package dependencies in `deriva-client/setup.py`.
4. Test and then commit/push `deriva-client` to GitHub.
5. Build dists (`python setup.py sdist bdist_wheel`) and upload result `deriva-client` dists to PyPi.
6. Bump version of `deriva-client-bundle` and bump versions of `deriva-client` dependency in `deriva-client-bundle/setup.py`.
7. Test and commit/push bumped version of `deriva-client-bundle` to GitHub.
8. Release `deriva-client` on GitHub. This release tagging process will trigger the BuildBot release build process of `deriva-client-bundle` against the latest version of `deriva-client` on PyPi.
9. Test buildbot generated release versions of the `deriva-client` installer packages and if OK, release `deriva-client-bundle` on GitHub page and upload the corresponding Windows/MacOS release bundle installers.
