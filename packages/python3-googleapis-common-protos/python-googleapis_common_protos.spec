# Created by pyp2rpm-3.3.10
%global pypi_name googleapis-common-protos
%global pypi_version 1.56.3

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Common protobufs used in Google APIs

License:        Apache-2.0
URL:            https://github.com/googleapis/python-api-common-protos
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-grpcio
BuildRequires:  python%{python3_pkgversion}-protobuf
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 Google APIs common protos[![pypi]( googleapis-common-protos contains the
python classes generated from the common protos in the [googleapis/api-common-
protos]( repository.

Requires:       python%{python3_pkgversion}-grpcio
Requires:       python%{python3_pkgversion}-protobuf

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
%{python3_sitelib}/google
%{python3_sitelib}/googleapis_common_protos-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.56.3-1
- Initial package.

