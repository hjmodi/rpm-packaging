# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-exporter-otlp
%global pypi_version 1.12.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        OpenTelemetry Collector Exporters

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(opentelemetry-exporter-otlp-proto-grpc) = 1.12
BuildRequires:  python3dist(opentelemetry-exporter-otlp-proto-http) = 1.12
BuildRequires:  python3dist(setuptools)

%description
OpenTelemetry Collector Exporters |pypi|.. |pyp This library is provided as a
convenience to install all supported OpenTelemetry Collector Exporters.
Currently it installs:* opentelemetry-exporter-otlp-proto-grpc * opentelemetry-
exporter-otlp-proto-httpIn the future, additional packages will be available: *
opentelemetry-exporter-otlp-json-httpTo avoid unnecessary dependencies, users
should...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(opentelemetry-exporter-otlp-proto-grpc) = 1.12
Requires:       python3dist(opentelemetry-exporter-otlp-proto-http) = 1.12
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
OpenTelemetry Collector Exporters |pypi|.. |pyp This library is provided as a
convenience to install all supported OpenTelemetry Collector Exporters.
Currently it installs:* opentelemetry-exporter-otlp-proto-grpc * opentelemetry-
exporter-otlp-proto-httpIn the future, additional packages will be available: *
opentelemetry-exporter-otlp-json-httpTo avoid unnecessary dependencies, users
should...


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
%{python3_sitelib}/opentelemetry_exporter_otlp-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.12.0-1
- Initial package.