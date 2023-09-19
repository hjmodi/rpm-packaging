# Created by pyp2rpm-3.3.10
%global pypi_name dataclasses
%global pypi_version 0.8

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A backport of the dataclasses module for Python 3.6

License:        Apache
URL:            https://github.com/ericvsmith/dataclasses
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 This is an implementation of PEP 557, Data Classes. It is a backport for
Python 3.6. Because dataclasses will be included in Python 3.7, any discussion
of dataclass features should occur on the python-dev mailing list at At this
point this repo should only be used for historical purposes (it's where the
original dataclasses discussions took place) and for discussion of the actual
backport to...

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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.8-1
- Initial package.
