# Created by pyp2rpm-3.3.10
%global pypi_name pytest-asyncio
%global pypi_version 0.8.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Pytest support for asyncio

License:        Apache 2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
pytest-asyncio: pytest support for asyncio :alt: Supported Python versions

Requires:       python%{python3_pkgversion}-async-generator >= 1.3
Requires:       python%{python3_pkgversion}-coverage
Requires:       python%{python3_pkgversion}-pytest >= 3.0.6
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
%{python3_sitelib}/pytest_asyncio
%{python3_sitelib}/pytest_asyncio-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 0.8.0-1
- Initial package.
