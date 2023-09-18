# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-instrumentation-requests
%global pypi_version 0.33b0

Name:           python-%{pypi_name}
Version:        0.33~b0
Release:        1%{?dist}
Summary:        OpenTelemetry requests instrumentation

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation/opentelemetry-instrumentation-requests
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(httpretty) >= 1 with python3dist(httpretty) < 2)
BuildRequires:  (python3dist(opentelemetry-api) >= 1.12 with python3dist(opentelemetry-api) < 2)
BuildRequires:  python3dist(opentelemetry-instrumentation) = 0.33~b0
BuildRequires:  python3dist(opentelemetry-semantic-conventions) = 0.33~b0
BuildRequires:  python3dist(opentelemetry-test-utils) = 0.33~b0
BuildRequires:  python3dist(opentelemetry-util-http) = 0.33~b0
BuildRequires:  (python3dist(requests) >= 2 with python3dist(requests) < 3)
BuildRequires:  (python3dist(requests) >= 2 with python3dist(requests) < 3)
BuildRequires:  python3dist(setuptools)

%description
OpenTelemetry Requests Instrumentation |pypi|.. |pyp This library allows
tracing HTTP requests made by the requests < library.Installation :: pip
install opentelemetry-instrumentation-requestsConfiguration -Exclude lists
************* To exclude certain URLs from being tracked, set the environment
variable OTEL_PYTHON_REQUESTS_EXCLUDED_URLS (or OTEL_PYTHON_EXCLUDED_URLS as
fallback) with comma...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(httpretty) >= 1 with python3dist(httpretty) < 2)
Requires:       (python3dist(opentelemetry-api) >= 1.12 with python3dist(opentelemetry-api) < 2)
Requires:       python3dist(opentelemetry-instrumentation) = 0.33~b0
Requires:       python3dist(opentelemetry-semantic-conventions) = 0.33~b0
Requires:       python3dist(opentelemetry-test-utils) = 0.33~b0
Requires:       python3dist(opentelemetry-util-http) = 0.33~b0
Requires:       (python3dist(requests) >= 2 with python3dist(requests) < 3)
Requires:       (python3dist(requests) >= 2 with python3dist(requests) < 3)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
OpenTelemetry Requests Instrumentation |pypi|.. |pyp This library allows
tracing HTTP requests made by the requests < library.Installation :: pip
install opentelemetry-instrumentation-requestsConfiguration -Exclude lists
************* To exclude certain URLs from being tracked, set the environment
variable OTEL_PYTHON_REQUESTS_EXCLUDED_URLS (or OTEL_PYTHON_EXCLUDED_URLS as
fallback) with comma...


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
%{python3_sitelib}/opentelemetry
%{python3_sitelib}/opentelemetry_instrumentation_requests-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.33~b0-1
- Initial package.