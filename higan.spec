Name: higan
Version: 106
Release: 2%{?dist}

License: GPLv3
Summary: Emulator
URL:     http://byuu.org/emulation/higan
Source:  https://gitlab.com/higan/higan/repository/v%{version}/archive.tar.bz2
Patch0:  use_sharedpath.patch

BuildRequires: gcc-c++
BuildRequires: gtk2-devel
BuildRequires: gtksourceview2-devel
BuildRequires: libao-devel
BuildRequires: libX11-devel
BuildRequires: libXv-devel
BuildRequires: openal-soft-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL-devel
BuildRequires: systemd-devel


%description
Higan is an emulator.


%prep
%autosetup -n higan-v%{version}-b55783c322a0158d9c192e0e14348fe9b5f76f7e -p1

sed -i \
        -e "/handle/s#/usr/local/lib#/usr/%{_libdir}#" \
        nall/dl.hpp || die "fixing libdir failed!"

# fix so that it doesn't build march=native
sed -i \
	    -e 's/march=native/march=x86-64/g' \
        -e 's/^\(flags.*\)/\1 -g/' \
        higan/GNUmakefile icarus/GNUmakefile


%build
pushd icarus
make %{?_smp_mflags} compiler="$(which g++)" phoenix="gtk" platform="linux"
popd

pushd higan
make %{?_smp_mflags} compiler="$(which g++)" phoenix="gtk" platform="linux" profile="profile_accuracy"
popd


%install
install -d %{buildroot}/%{_datadir}/applications

pushd higan
%make_install prefix=%{buildroot}/%{_prefix}
popd
pushd icarus
%make_install prefix=%{buildroot}/%{_prefix}
popd


%files
%{_bindir}/higan
%{_bindir}/icarus
%{_datadir}/applications/higan.desktop
%{_datadir}/applications/icarus.desktop
%{_datadir}/higan
%{_datadir}/icarus
%{_datadir}/icons/higan.png
%{_datadir}/icons/icarus.png


%changelog
* Sun Mar 04 2018 Dick Marinus <dick@mrns.nl> - 106-2
- Change URL, add use_sharedpath patch from Tobias Hansen

* Thu Jan 04 2018 Dick Marinus <dick@mrns.nl> - 106-1
- Update to 106

* Fri Dec 29 2017 Dick Marinus <dick@mrns.nl> - 102-2
- Add debug symbols for find-debuginfo.sh

* Mon Feb 20 2017 Mirko Rolfes <songokussj@gmx.net> - 102
- Update to 102

* Mon Aug 22 2016 Mirko Rolfes <songokussj@gmx.net> - 101-1
- Update to 101

* Tue Aug 02 2016 Mirko Rolfes <songokussj@gmx.net> - 100-1
- Update to 100

* Tue Jun 21 2016 Randy Barlow <bowlofeggs@fedoraproject.org> - 099-1
- Initial release.
