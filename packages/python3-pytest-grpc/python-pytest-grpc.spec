# Created by pyp2rpm-3.3.8
%global pypi_name pytest-grpc
%global pypi_version 0.8.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        pytest plugin for grpc

License:        MIT
URL:            https://github.com/kataev/pytest-grpc
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 pytest-grpcWrite test for gRPC with pytest. ExampleSee example dir and/or read
'usage'. UsageFor example you have some proto file with rpc declaration.syntax
"proto3";package test.v1; service EchoService { rpc handler(EchoRequest)
returns (EchoResponse) {} message EchoRequest { string name 1; message
EchoResponse { string name 1; After compile it with grpcio-tools, you get
*_pb2.py and...

Requires:       python%{python3_pkgversion}-pytest >= 3.6
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
%doc README.md
%{python3_sitelib}/pytest_grpc
%{python3_sitelib}/pytest_grpc-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 21 2023 Harsh Modi <hmodi@redhat.com> - 0.8.0-1
- Initial package.

