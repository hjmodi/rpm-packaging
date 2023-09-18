# Created by pyp2rpm-3.3.10
%global pypi_name googleapis-common-protos
%global pypi_version 1.56.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(grpcio) >= 1 with python3dist(grpcio) < 2~~dev0)
BuildRequires:  (python3dist(protobuf) >= 3.15 with python3dist(protobuf) < 5~~dev0)
BuildRequires:  python3dist(setuptools)

%description
 Google APIs common protos[![pypi]( googleapis-common-protos contains the
python classes generated from the common protos in the [googleapis/api-common-
protos]( repository.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(grpcio) >= 1 with python3dist(grpcio) < 2~~dev0)
Requires:       (python3dist(protobuf) >= 3.15 with python3dist(protobuf) < 5~~dev0)
%description -n python3-%{pypi_name}
 Google APIs common protos[![pypi]( googleapis-common-protos contains the
python classes generated from the common protos in the [googleapis/api-common-
protos]( repository.


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
%{python3_sitelib}/google
%{python3_sitelib}/googleapis_common_protos-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.56.3-1
- Initial package.

