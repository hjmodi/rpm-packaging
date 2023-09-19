# Created by pyp2rpm-3.3.10
%global pypi_name pytest-forked
%global pypi_version 1.2.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        run tests in isolated forked subprocesses

License:        MIT
URL:            https://github.com/pytest-dev/pytest-forked
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.1
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

%description
pytest-forked: run each test in a forked subprocess .. warning:: this is a
extraction of the xdist --forked module, future maintenance beyond the bare
minimum is not planned until a new maintainer is found. This plugin **does not
work on Windows** because there's no fork support. * --forked: run each test in
a forked subprocess to survive SEGFAULTS or otherwise dying
processes.|python|...

Requires:       python%{python3_pkgversion}-pytest >= 3.10
Requires:       python%{python3_pkgversion}-setuptools

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
%doc README.rst
%{python3_sitelib}/pytest_forked
%{python3_sitelib}/pytest_forked-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 1.2.0-1
- Initial package.
