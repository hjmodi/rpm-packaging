# Created by pyp2rpm-3.3.10
%global pypi_name click
%global pypi_version 8.0.4

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Composable command line interface toolkit

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/click/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(importlib-metadata)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
\$ click\_ Click is a Python package for creating beautiful command line
interfaces in a composable way with as little code as necessary. It's the
"Command Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.It aims to make the process of writing command
line tools quick and fun while also preventing any frustration caused by the
inability to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(colorama)
Requires:       python3dist(importlib-metadata)
%description -n python3-%{pypi_name}
\$ click\_ Click is a Python package for creating beautiful command line
interfaces in a composable way with as little code as necessary. It's the
"Command Line Interface Creation Kit". It's highly configurable but comes with
sensible defaults out of the box.It aims to make the process of writing command
line tools quick and fun while also preventing any frustration caused by the
inability to...

%package -n python-%{pypi_name}-doc
Summary:        click documentation
%description -n python-%{pypi_name}-doc
Documentation for click

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
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst docs/license.rst

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 8.0.4-1
- Initial package.

