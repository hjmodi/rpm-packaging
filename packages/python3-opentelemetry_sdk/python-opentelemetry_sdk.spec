# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-sdk
%global pypi_version 1.12.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        OpenTelemetry Python SDK

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-sdk
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(dataclasses) = 0.8
BuildRequires:  python3dist(opentelemetry-api) = 1.12
BuildRequires:  python3dist(opentelemetry-semantic-conventions) = 0.33~b0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 16
BuildRequires:  python3dist(typing-extensions) >= 3.7.4

%description
OpenTelemetry Python SDK |pypi|.. |pyp Installation :: pip install
opentelemetry-sdkReferences -* OpenTelemetry Project <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(dataclasses) = 0.8
Requires:       python3dist(opentelemetry-api) = 1.12
Requires:       python3dist(opentelemetry-semantic-conventions) = 0.33~b0
Requires:       python3dist(setuptools)
Requires:       python3dist(setuptools) >= 16
Requires:       python3dist(typing-extensions) >= 3.7.4
%description -n python3-%{pypi_name}
OpenTelemetry Python SDK |pypi|.. |pyp Installation :: pip install
opentelemetry-sdkReferences -* OpenTelemetry Project <


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
%{python3_sitelib}/opentelemetry_sdk-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.12.0-1
- Initial package.