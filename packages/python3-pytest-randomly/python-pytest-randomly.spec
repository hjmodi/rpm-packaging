# Created by pyp2rpm-3.3.10
%global pypi_name pytest-randomly
%global pypi_version 3.10.3

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Pytest plugin to randomly order tests and control random

License:        MIT
URL:            https://github.com/pytest-dev/pytest-randomly
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 pytest-randomly :target:

Requires:       python%{python3_pkgversion}-importlib-metadata >= 3.6
Requires:       python%{python3_pkgversion}-pytest
Requires:       python%{python3_pkgversion}-setuptools

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_randomly
%{python3_sitelib}/pytest_randomly-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 3.10.3-1
- Initial package.
