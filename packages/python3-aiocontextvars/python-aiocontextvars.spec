# Created by pyp2rpm-3.3.10
%global pypi_name aiocontextvars
%global pypi_version 0.2.2

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Asyncio support for PEP-567 contextvars backport

License:        BSD license
URL:            https://github.com/fantix/aiocontextvars
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-contextvars = 2.4
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-asyncio = 0.8
BuildRequires:  python%{python3_pkgversion}-pytest-runner
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
 aiocontextvars **IMPORTANT:** This package will be deprecated after
contextvars asyncio backport_ is fixed. Before then, this library
experimentally provides the missing asyncio support for the contextvars
backport library. Please read more in Python 3.7 contextvars documentation <
Compatibility

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python%{python3_pkgversion}-contextvars = 2.4
%description -n python3-%{pypi_name}
 aiocontextvars **IMPORTANT:** This package will be deprecated after
contextvars asyncio backport_ is fixed. Before then, this library
experimentally provides the missing asyncio support for the contextvars
backport library. Please read more in Python 3.7 contextvars documentation <
Compatibility

%package -n python%{python3_pkgversion}-%{pypi_name}-doc
Summary:        aiocontextvars documentation
%description -n python%{python3_pkgversion}-%{pypi_name}-doc
Documentation for aiocontextvars

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc docs/readme.rst README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.2.2-1
- Initial package.
