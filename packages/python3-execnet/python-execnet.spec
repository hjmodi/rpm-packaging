# Created by pyp2rpm-3.3.10
%global pypi_name execnet
%global pypi_version 1.9.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        execnet: rapid multi-Python deployment

License:        MIT
URL:            https://execnet.readthedocs.io/en/latest/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pre-commit
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
execnet: distributed Python deployment and communication Important **execnet
currently is in maintenance-only mode, mostly because it is still the backend
of the pytest-xdist plugin. Do not use in new projects.** .. image::

Requires:       python%{python3_pkgversion}-pre-commit

%package -n python%{python3_pkgversion}-%{pypi_name}-doc
Summary:        execnet documentation
%description -n python%{python3_pkgversion}-%{pypi_name}-doc
Documentation for execnet

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 1.9.0-1
- Initial package.
