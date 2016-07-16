# higan-specfile
This repository contains an RPM specfile for the
[higan](http://byuu.org/emulation/higan) emulator.


## Build instructions

Building higan on Fedora is pretty straightforward. Once you have cloned the
repository, simply cd into that directory and perform the following steps:

```
$ sudo dnf install /usr/bin/rpmbuild
$ mkdir -p ~/rpmbuild/SOURCES
# Get the source code and put it in the SOURCES folder
$ spectool -g higan.spec
$ mv v* ~/rpmbuild/SOURCES/
# Install build dependencies
$ sudo dnf builddep higan.spec
# Build the package
$ rpmbuild -ba higan.spec
```

rpmbuild will tell you the paths to the resulting RPMs at the end of the
build, which should be in ~/rpmbuild/RPMs/<arch>.
