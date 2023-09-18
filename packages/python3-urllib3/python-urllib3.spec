# Created by pyp2rpm-3.3.10
%global pypi_name urllib3
%global pypi_version 1.26.16

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(brotli) >= 1.0.9
BuildRequires:  python3dist(brotlicffi) >= 0.8
BuildRequires:  python3dist(brotlipy) >= 0.6
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(cryptography) >= 1.3.4
BuildRequires:  python3dist(idna) >= 2
BuildRequires:  python3dist(ipaddress)
BuildRequires:  python3dist(pyopenssl) >= 0.14
BuildRequires:  (python3dist(pysocks) >= 1.5.6 with python3dist(pysocks) < 2~~ with (python3dist(pysocks) < 1.5.7 or python3dist(pysocks) > 1.5.7))
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3-secure-extra)
BuildRequires:  python3dist(sphinx)

%description
urllib3 is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses urllib3 and you should too. urllib3 brings many
critical features that are missing from the Python standard libraries:- Thread
safety. - Connection pooling. - Client-side SSL/TLS verification. - File
uploads with multipart encoding. - Helpers for retrying requests and dealing
with HTTP...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(brotli) >= 1.0.9
Requires:       python3dist(brotlicffi) >= 0.8
Requires:       python3dist(brotlipy) >= 0.6
Requires:       python3dist(certifi)
Requires:       python3dist(cryptography) >= 1.3.4
Requires:       python3dist(idna) >= 2
Requires:       python3dist(ipaddress)
Requires:       python3dist(pyopenssl) >= 0.14
Requires:       (python3dist(pysocks) >= 1.5.6 with python3dist(pysocks) < 2~~ with (python3dist(pysocks) < 1.5.7 or python3dist(pysocks) > 1.5.7))
Requires:       python3dist(urllib3-secure-extra)
%description -n python3-%{pypi_name}
urllib3 is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses urllib3 and you should too. urllib3 brings many
critical features that are missing from the Python standard libraries:- Thread
safety. - Connection pooling. - Client-side SSL/TLS verification. - File
uploads with multipart encoding. - Helpers for retrying requests and dealing
with HTTP...

%package -n python-%{pypi_name}-doc
Summary:        urllib3 documentation
%description -n python-%{pypi_name}-doc
Documentation for urllib3

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst dummyserver/certs/README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 1.26.16-1
- Initial package.

