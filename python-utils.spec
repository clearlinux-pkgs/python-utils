#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE81444E9CE1F695D (wolph@wol.ph)
#
Name     : python-utils
Version  : 2.3.0
Release  : 5
URL      : https://github.com/WoLpH/python-utils/releases/download/v2.3.0/python-utils-v2.3.0.tar.xz
Source0  : https://github.com/WoLpH/python-utils/releases/download/v2.3.0/python-utils-v2.3.0.tar.xz
Source99 : https://github.com/WoLpH/python-utils/releases/download/v2.3.0/python-utils-v2.3.0.tar.xz.asc
Summary  : A module with some convenient utilities not included with the standard Python install
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-utils-license = %{version}-%{release}
Requires: python-utils-python = %{version}-%{release}
Requires: python-utils-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytest-runner
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
Useful Python Utils
==============================================================================

%package license
Summary: license components for the python-utils package.
Group: Default

%description license
license components for the python-utils package.


%package python
Summary: python components for the python-utils package.
Group: Default
Requires: python-utils-python3 = %{version}-%{release}

%description python
python components for the python-utils package.


%package python3
Summary: python3 components for the python-utils package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-utils package.


%prep
%setup -q -n python-utils-v2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551027864
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-utils
cp LICENSE %{buildroot}/usr/share/package-licenses/python-utils/LICENSE
cp docs/_theme/LICENSE %{buildroot}/usr/share/package-licenses/python-utils/docs__theme_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-utils/LICENSE
/usr/share/package-licenses/python-utils/docs__theme_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
