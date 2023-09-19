# Created by pyp2rpm-3.3.10
%global pypi_name pytest-xdist
%global pypi_version 3.0.2

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        py.test plugin for distributed testing and loop-on-failing modes

License:        MIT
URL:            https://github.com/pytest-dev/pytest-xdist
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-execnet
# Not available on RHEL8.  Disable the test instead
#BuildRequires:  python3-filelock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-forked
BuildRequires:  python%{python3_pkgversion}-py
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

%description
%{desc}

Requires:       python%{python3_pkgversion}-execnet
Requires:       python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-pytest-forked
Requires:       python%{python3_pkgversion}-py

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} PYTHONDONTWRITEBYTECODE=1 py.test-%{python3_version} testing -k "not TestLocking"

%files
%doc OVERVIEW.md README.rst
%license LICENSE
%{python3_sitelib}/pytest_xdist*
%{python3_sitelib}/xdist/

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 3.10.3-1
- Initial package.
