# Created by pyp2rpm-3.3.10
%global pypi_name tomli
%global pypi_version 1.2.3

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A little TOML parser for Python

License:        MIT License
URL:            https://pypi.org/project2/tomli/
Source0:        %{pypi_source}
# Upstream tomli uses flit, but we want to use setuptools on RHEL 8.
# This a downstream-only setup.py manually created from pyproject.toml metadata.
# It contains a @@VERSION@@ placeholder.
Source1:        001-tomli-setup.py

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
%{summary}

%prep
set -ex
%autosetup -p1 -n %{pypi_name}-%{version}
sed 's/@@VERSION@@/%{version}/' %{SOURCE1} > setup.py
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
set -ex
%py3_build


%install
set -ex
%py3_install

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 0.971-1
- Initial package.