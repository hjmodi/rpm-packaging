# Created by pyp2rpm-3.3.10
%global pypi_name unicodedata2
%global pypi_version 15.0.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Unicodedata backport updated to the latest Unicode version

License:        Apache License 2.0
URL:            http://github.com/fonttools/unicodedata2
Source0:        %{pypi_source}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-coverage
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-randomly
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
[![Githun CI Status]( [![PyPI]( [unicodedata] backport/updates.The versions of
this package match Unicode versions, so unicodedata213.0.0 is data from Unicode
13.0.0.Pre-compiled wheel packages are available on [PyPI] and can be installed
via pip.[unicodedata]: [PyPI]:

Requires:       python%{python3_pkgversion}-coverage
Requires:       python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-pytest-randomly
Requires:       python%{python3_pkgversion}-pytest-xdist

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 15.0.0-1
- Initial package.
