# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-proto
%global pypi_version 1.12.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        OpenTelemetry Python Proto

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-proto
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(protobuf) >= 3.13 with python3dist(protobuf) < 4)
BuildRequires:  python3dist(setuptools)

%description
OpenTelemetry Python Proto |pypi|.. |pyp This library contains the generated
code for OpenTelemetry protobuf data model. The code in the current package was
generated using the v0.17.0 release_ of opentelemetry-proto... _release: :: pip
install opentelemetry-protoCode Generation These files were generated
automatically from code in opentelemetry-proto_. To regenerate the code, run...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(protobuf) >= 3.13 with python3dist(protobuf) < 4)
%description -n python3-%{pypi_name}
OpenTelemetry Python Proto |pypi|.. |pyp This library contains the generated
code for OpenTelemetry protobuf data model. The code in the current package was
generated using the v0.17.0 release_ of opentelemetry-proto... _release: :: pip
install opentelemetry-protoCode Generation These files were generated
automatically from code in opentelemetry-proto_. To regenerate the code, run...


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
%{python3_sitelib}/opentelemetry_proto-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.12.0-1
- Initial package.