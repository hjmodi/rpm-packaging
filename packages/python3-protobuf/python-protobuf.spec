# Created by pyp2rpm-3.3.8
%global pypi_name protobuf
%global pypi_version 3.19.6

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Protocol Buffers

License:        3-Clause BSD License
URL:            https://developers.google.com/protocol-buffers/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Protocol Buffers are Google's data interchange format

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
%doc README.md
%{python3_sitelib}/google
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}-*.pth
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Thu Sep 21 2023 Harsh Modi <hmodi@redhat.com> - 3.19.6-1
- Initial package.
