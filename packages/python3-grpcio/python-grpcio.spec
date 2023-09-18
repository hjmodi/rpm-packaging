# Created by pyp2rpm-3.3.10
%global pypi_name grpcio
%global pypi_version 1.48.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        HTTP/2-based RPC framework

License:        Apache License 2.0
URL:            https://grpc.io
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(enum34) >= 1.0.4
BuildRequires:  python3dist(futures) >= 2.2
BuildRequires:  python3dist(grpcio-tools) >= 1.48.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.5.2

%description
gRPC Python |compat_check_pypi|Package for gRPC Python... |compat_check_pyp
Supported Python Versions - Python > 3.6Installation gRPC Python is available
for Linux, macOS, and Windows.Installing From PyPI If you are installing
locally...:: $ pip install grpcioElse system wide (on Ubuntu)...:: $ sudo pip
install grpcioIf you're on Windows make sure that you installed the
:code:pip.exe component

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(enum34) >= 1.0.4
Requires:       python3dist(futures) >= 2.2
Requires:       python3dist(grpcio-tools) >= 1.48.2
Requires:       python3dist(six) >= 1.5.2
%description -n python3-%{pypi_name}
gRPC Python |compat_check_pypi|Package for gRPC Python... |compat_check_pyp
Supported Python Versions - Python > 3.6Installation gRPC Python is available
for Linux, macOS, and Windows.Installing From PyPI If you are installing
locally...:: $ pip install grpcioElse system wide (on Ubuntu)...:: $ sudo pip
install grpcioIf you're on Windows make sure that you installed the
:code:pip.exe component


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
%doc src/core/lib/transport/README.md src/core/lib/README.md src/core/lib/gprpp/README.md src/core/lib/iomgr/README.md src/core/lib/surface/README.md src/core/lib/gpr/README.md src/core/lib/channel/README.md src/core/tsi/README.md src/core/README.md src/core/ext/transport/README.md src/core/ext/transport/chttp2/transport/README.md src/core/ext/transport/chttp2/README.md src/core/ext/transport/binder/README.md src/core/ext/README.md src/core/ext/filters/client_channel/README.md src/core/ext/filters/client_channel/resolver/README.md src/core/ext/filters/client_channel/resolver/dns/native/README.md src/core/ext/filters/client_channel/resolver/binder/README.md src/core/ext/filters/client_channel/resolver/sockaddr/README.md src/python/grpcio/README.rst README.md include/grpc/event_engine/README.md include/grpc/impl/codegen/README.md
%{python3_sitearch}/grpc
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.48.2-1
- Initial package.
