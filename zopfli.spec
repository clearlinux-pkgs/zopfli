#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : zopfli
Version  : 64636256319063316680
Release  : 3
URL      : https://github.com/google/zopfli/archive/64c6f362fefd56dccbf31906fdb3e31f6a6faf80.tar.gz
Source0  : https://github.com/google/zopfli/archive/64c6f362fefd56dccbf31906fdb3e31f6a6faf80.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: zopfli-lib
Patch1: build.patch
Patch2: defaults.patch

%description
Zopfli Compression Algorithm is a compression library programmed in C to perform
very good, but slow, deflate or zlib compression.

%package dev
Summary: dev components for the zopfli package.
Group: Development
Requires: zopfli-lib
Provides: zopfli-devel

%description dev
dev components for the zopfli package.


%package lib
Summary: lib components for the zopfli package.
Group: Libraries

%description lib
lib components for the zopfli package.


%prep
%setup -q -n zopfli-64c6f362fefd56dccbf31906fdb3e31f6a6faf80
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508437656
make V=1  %{?_smp_mflags} libzopfli DEFAULTFLAGS="$CFLAGS"

%install
export SOURCE_DATE_EPOCH=1508437656
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libzopfli.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libzopfli.so.1
/usr/lib64/libzopfli.so.1.0.1
