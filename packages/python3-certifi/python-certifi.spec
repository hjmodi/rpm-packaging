# Created by pyp2rpm-3.3.10
%global pypi_name certifi
%global pypi_version 2023.7.22

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Certifi: Python SSL Certificates Certifi provides Mozilla's carefully curated
collection of Root Certificates for validating the trustworthiness of SSL
certificates while verifying the identity of TLS hosts. It has been extracted
from the Requests_ project.Installation certifi is available on PyPI. Simply
install it with pip:: $ pip install certifiUsage To reference the installed
certificate...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Certifi: Python SSL Certificates Certifi provides Mozilla's carefully curated
collection of Root Certificates for validating the trustworthiness of SSL
certificates while verifying the identity of TLS hosts. It has been extracted
from the Requests_ project.Installation certifi is available on PyPI. Simply
install it with pip:: $ pip install certifiUsage To reference the installed
certificate...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 2023.7.22-1
- Initial package.

