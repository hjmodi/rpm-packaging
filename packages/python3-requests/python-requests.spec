# Created by pyp2rpm-3.3.10
%global pypi_name requests
%global pypi_version 2.27.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python HTTP for Humans

License:        Apache 2.0
URL:            https://requests.readthedocs.io
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(certifi) >= 2017.4.17
BuildRequires:  (python3dist(chardet) >= 3.0.2 with python3dist(chardet) < 5~~)
BuildRequires:  (python3dist(chardet) >= 3.0.2 with python3dist(chardet) < 5~~)
BuildRequires:  (python3dist(charset-normalizer) >= 2 with python3dist(charset-normalizer) < 2.1)
BuildRequires:  (python3dist(idna) >= 2.5 with python3dist(idna) < 3~~)
BuildRequires:  (python3dist(idna) >= 2.5 with python3dist(idna) < 4~~)
BuildRequires:  (python3dist(pysocks) >= 1.5.6 with (python3dist(pysocks) < 1.5.7 or python3dist(pysocks) > 1.5.7))
BuildRequires:  (python3dist(pysocks) >= 1.5.6 with (python3dist(pysocks) < 1.5.7 or python3dist(pysocks) > 1.5.7))
BuildRequires:  python3dist(pytest) >= 3
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-httpbin) = 0.0.7
BuildRequires:  python3dist(pytest-mock)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)
BuildRequires:  (python3dist(urllib3) >= 1.21.1 with python3dist(urllib3) < 1.27~~)
BuildRequires:  python3dist(win-inet-pton)

%description
 Requests**Requests** is a simple, yet elegant, HTTP library.python >>> import
requests >>> r requests.get(' auth('user', 'pass')) >>> r.status_code>>>
r.headers['content-type'] 'application/json; charsetutf8' >>> r.encoding>>>
r.text '{"authenticated": true, ...' >>> r.json() {'authenticated': True, ...}
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need
to...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(certifi) >= 2017.4.17
Requires:       (python3dist(chardet) >= 3.0.2 with python3dist(chardet) < 5~~)
Requires:       (python3dist(chardet) >= 3.0.2 with python3dist(chardet) < 5~~)
Requires:       (python3dist(charset-normalizer) >= 2 with python3dist(charset-normalizer) < 2.1)
Requires:       (python3dist(idna) >= 2.5 with python3dist(idna) < 3~~)
Requires:       (python3dist(idna) >= 2.5 with python3dist(idna) < 4~~)
Requires:       (python3dist(pysocks) >= 1.5.6 with (python3dist(pysocks) < 1.5.7 or python3dist(pysocks) > 1.5.7))
Requires:       (python3dist(urllib3) >= 1.21.1 with python3dist(urllib3) < 1.27~~)
Requires:       python3dist(win-inet-pton)
%description -n python3-%{pypi_name}
 Requests**Requests** is a simple, yet elegant, HTTP library.python >>> import
requests >>> r requests.get(' auth('user', 'pass')) >>> r.status_code>>>
r.headers['content-type'] 'application/json; charsetutf8' >>> r.encoding>>>
r.text '{"authenticated": true, ...' >>> r.json() {'authenticated': True, ...}
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need
to...


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
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 2.27.1-1
- Initial package.
