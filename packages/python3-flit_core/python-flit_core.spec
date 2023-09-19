# Created by pyp2rpm-3.3.10
%global pypi_name flit_core
%global pypi_version 3.9.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Distribution-building parts of Flit. See flit package for more information

License:        BSD
URL:            https://pypi.org/project/flit-core/
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip

%description
%{summary}

%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 0.971-1
- Initial package.