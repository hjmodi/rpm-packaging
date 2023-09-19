# Created by pyp2rpm-3.3.10
%global pypi_name idna
%global pypi_version 3.4

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
Source0:        %{pypi_source}
# This a downstream-only setup.py manually created from pyproject.toml metadata.
Source1:        001-idna-setup.py
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the Internationalized Domain Names in
Applications (IDNA) protocol as specified in `RFC 5891
<https://tools.ietf.org/html/rfc5891>`_. This is the latest version of
the protocol and is sometimes referred to as “IDNA 2008”.

This library also provides support for Unicode...

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
cat %{SOURCE1} > setup.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 3.4-1
- Initial package.
