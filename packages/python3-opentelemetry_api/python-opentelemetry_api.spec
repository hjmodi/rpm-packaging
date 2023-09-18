# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-api
%global pypi_version 1.12.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        OpenTelemetry Python API

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(aiocontextvars)
BuildRequires:  python3dist(deprecated) >= 1.2.6
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 16

%description
OpenTelemetry Python API |pypi|.. |pyp Installation :: pip install
opentelemetry-apiReferences -* OpenTelemetry Project <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiocontextvars)
Requires:       python3dist(deprecated) >= 1.2.6
Requires:       python3dist(setuptools)
Requires:       python3dist(setuptools) >= 16
%description -n python3-%{pypi_name}
OpenTelemetry Python API |pypi|.. |pyp Installation :: pip install
opentelemetry-apiReferences -* OpenTelemetry Project <


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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry_api-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.12.0-1
- Initial package.