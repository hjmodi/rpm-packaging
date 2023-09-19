# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-api
%global pypi_version 1.12.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        OpenTelemetry Python API

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-aiocontextvars
BuildRequires:  python%{python3_pkgversion}-deprecated >= 1.2.6
BuildRequires:  python%{python3_pkgversion}-setuptools >= 16

%description
OpenTelemetry Python API |pypi|.. |pyp Installation :: pip install
opentelemetry-apiReferences -* OpenTelemetry Project <

Requires:       python%{python3_pkgversion}-aiocontextvars
Requires:       python%{python3_pkgversion}-deprecated >= 1.2.6
Requires:       python%{python3_pkgversion}-setuptools >= 16

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
%{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry_api-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.12.0-1
- Initial package.
