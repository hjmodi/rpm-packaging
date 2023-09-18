# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-exporter-otlp-proto-grpc
%global pypi_version 1.12.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        OpenTelemetry Collector Protobuf over gRPC Exporter

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-grpc
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(backoff) >= 1.10 with python3dist(backoff) < 2~~)
BuildRequires:  (python3dist(backoff) >= 1.10 with python3dist(backoff) < 3~~)
BuildRequires:  (python3dist(googleapis-common-protos) >= 1.52 with python3dist(googleapis-common-protos) < 2)
BuildRequires:  (python3dist(grpcio) >= 1 with python3dist(grpcio) < 2~~)
BuildRequires:  (python3dist(opentelemetry-api) >= 1.3 with python3dist(opentelemetry-api) < 2)
BuildRequires:  python3dist(opentelemetry-proto) = 1.12
BuildRequires:  (python3dist(opentelemetry-sdk) >= 1.11 with python3dist(opentelemetry-sdk) < 2)
BuildRequires:  python3dist(pytest-grpc)
BuildRequires:  python3dist(setuptools)

%description
OpenTelemetry Collector Protobuf over gRPC Exporter |pypi|.. |pyp This library
allows to export data to the OpenTelemetry Collector using the OpenTelemetry
Protocol using Protobuf over gRPC.Installation :: pip install opentelemetry-
exporter-otlp-proto-grpc References -* OpenTelemetry Collector Exporter < *
OpenTelemetry Collector <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(backoff) >= 1.10 with python3dist(backoff) < 2~~)
Requires:       (python3dist(backoff) >= 1.10 with python3dist(backoff) < 3~~)
Requires:       (python3dist(googleapis-common-protos) >= 1.52 with python3dist(googleapis-common-protos) < 2)
Requires:       (python3dist(grpcio) >= 1 with python3dist(grpcio) < 2~~)
Requires:       (python3dist(opentelemetry-api) >= 1.3 with python3dist(opentelemetry-api) < 2)
Requires:       python3dist(opentelemetry-proto) = 1.12
Requires:       (python3dist(opentelemetry-sdk) >= 1.11 with python3dist(opentelemetry-sdk) < 2)
Requires:       python3dist(pytest-grpc)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
OpenTelemetry Collector Protobuf over gRPC Exporter |pypi|.. |pyp This library
allows to export data to the OpenTelemetry Collector using the OpenTelemetry
Protocol using Protobuf over gRPC.Installation :: pip install opentelemetry-
exporter-otlp-proto-grpc References -* OpenTelemetry Collector Exporter < *
OpenTelemetry Collector <


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
%{python3_sitelib}/opentelemetry_exporter_otlp_proto_grpc-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.12.0-1
- Initial package.