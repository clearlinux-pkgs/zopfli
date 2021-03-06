#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zopfli
Version  : 1.0.3
Release  : 8
URL      : https://github.com/google/zopfli/archive/zopfli-1.0.3/zopfli-1.0.3.tar.gz
Source0  : https://github.com/google/zopfli/archive/zopfli-1.0.3/zopfli-1.0.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: zopfli-bin = %{version}-%{release}
Requires: zopfli-lib = %{version}-%{release}
Requires: zopfli-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
Zopfli Compression Algorithm is a compression library programmed in C to perform
very good, but slow, deflate or zlib compression.

%package bin
Summary: bin components for the zopfli package.
Group: Binaries
Requires: zopfli-license = %{version}-%{release}

%description bin
bin components for the zopfli package.


%package dev
Summary: dev components for the zopfli package.
Group: Development
Requires: zopfli-lib = %{version}-%{release}
Requires: zopfli-bin = %{version}-%{release}
Provides: zopfli-devel = %{version}-%{release}
Requires: zopfli = %{version}-%{release}

%description dev
dev components for the zopfli package.


%package lib
Summary: lib components for the zopfli package.
Group: Libraries
Requires: zopfli-license = %{version}-%{release}

%description lib
lib components for the zopfli package.


%package license
Summary: license components for the zopfli package.
Group: Default

%description license
license components for the zopfli package.


%prep
%setup -q -n zopfli-zopfli-1.0.3
cd %{_builddir}/zopfli-zopfli-1.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619063557
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  libzopfli DEFAULTFLAGS="$CFLAGS"
popd

%install
export SOURCE_DATE_EPOCH=1619063557
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zopfli
cp %{_builddir}/zopfli-zopfli-1.0.3/COPYING %{buildroot}/usr/share/package-licenses/zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/zopfli
/usr/bin/zopflipng

%files dev
%defattr(-,root,root,-)
/usr/include/zopfli.h
/usr/include/zopflipng_lib.h
/usr/lib64/cmake/Zopfli/ZopfliConfig-relwithdebinfo.cmake
/usr/lib64/cmake/Zopfli/ZopfliConfig.cmake
/usr/lib64/cmake/Zopfli/ZopfliConfigVersion.cmake
/usr/lib64/libzopfli.so
/usr/lib64/libzopflipng.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libzopfli.so.1
/usr/lib64/libzopfli.so.1.0.3
/usr/lib64/libzopflipng.so.1
/usr/lib64/libzopflipng.so.1.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zopfli/6d182cfd7e2a6c633140f7cdb0c4a46fc4a23589
