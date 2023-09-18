# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-util-http
%global pypi_version 0.33b0

Name:           python-%{pypi_name}
Version:        0.33~b0
Release:        1%{?dist}
Summary:        Web util for OpenTelemetry

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/util/opentelemetry-util-http
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
OpenTelemetry Util HTTP |pypi|.. |pyp This library provides ASGI, WSGI
middleware and other HTTP-related functionality that is common to instrumented
web frameworks (such as Django, Starlette, FastAPI, etc.) to track requests
timing through OpenTelemetry.Installation :: pip install opentelemetry-util-
http Usage (Quart) -.. code-block:: python from quart import Quart from...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
OpenTelemetry Util HTTP |pypi|.. |pyp This library provides ASGI, WSGI
middleware and other HTTP-related functionality that is common to instrumented
web frameworks (such as Django, Starlette, FastAPI, etc.) to track requests
timing through OpenTelemetry.Installation :: pip install opentelemetry-util-
http Usage (Quart) -.. code-block:: python from quart import Quart from...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry_util_http-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.33~b0-1
- Initial package.

