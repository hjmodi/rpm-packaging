# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-instrumentation
%global pypi_version 0.33b0

Name:           python-%{pypi_name}
Version:        0.33~b0
Release:        1%{?dist}
Summary:        Instrumentation Tools & Auto Instrumentation for OpenTelemetry Python

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-instrumentation
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(opentelemetry-api) >= 1.4 with python3dist(opentelemetry-api) < 2)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 16
BuildRequires:  (python3dist(wrapt) >= 1 with python3dist(wrapt) < 2~~)

%description
OpenTelemetry Instrumentation |pypi|.. |pyp Installation :: pip install
opentelemetry-instrumentation This package provides a couple of commands that
help automatically instruments a program:.. note:: You need to install a distro
package to get auto instrumentation working. The opentelemetry-distro package
contains the default distro and automatically configures some of the common
options for...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(opentelemetry-api) >= 1.4 with python3dist(opentelemetry-api) < 2)
Requires:       python3dist(setuptools)
Requires:       python3dist(setuptools) >= 16
Requires:       (python3dist(wrapt) >= 1 with python3dist(wrapt) < 2~~)
%description -n python3-%{pypi_name}
OpenTelemetry Instrumentation |pypi|.. |pyp Installation :: pip install
opentelemetry-instrumentation This package provides a couple of commands that
help automatically instruments a program:.. note:: You need to install a distro
package to get auto instrumentation working. The opentelemetry-distro package
contains the default distro and automatically configures some of the common
options for...


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
%{_bindir}/opentelemetry-bootstrap
%{_bindir}/opentelemetry-instrument
%{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry_instrumentation-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.33~b0-1
- Initial package.
