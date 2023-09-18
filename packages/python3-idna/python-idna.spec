# Created by pyp2rpm-3.3.10
%global pypi_name idna
%global pypi_version 3.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        None
URL:            None
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the Internationalized Domain Names in
Applications (IDNA) protocol as specified in `RFC 5891
<https://tools.ietf.org/html/rfc5891>`_. This is the latest version of
the protocol and is sometimes referred to as “IDNA 2008”.

This library also provides support for Unicode...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the Internationalized Domain Names in
Applications (IDNA) protocol as specified in `RFC 5891
<https://tools.ietf.org/html/rfc5891>`_. This is the latest version of
the protocol and is sometimes referred to as “IDNA 2008”.

This library also provides support for Unicode...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 3.4-1
- Initial package.
