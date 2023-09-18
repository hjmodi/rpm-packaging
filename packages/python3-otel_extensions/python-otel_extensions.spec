# Created by pyp2rpm-3.3.10
%global pypi_name otel-extensions
%global pypi_version 0.2.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python extensions for OpenTelemetry

License:        Apache-2.0
URL:            https://github.com/s4v4g3/otel-extensions-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 otel-extensions-python: OpenTelemetry Extensions for Python OpenTelemetry
Extensions for Python is a collection of helper classes, functions, and
decorators to facilitate the use of the [OpenTelemetry Python API & SDK
packages]( Version SupportPython > 3.6 Installation pip installYou can install
through pip using:sh pip install otel-extensions(you may need to run pip with
root permission:...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(opentelemetry-api)
Requires:       python3dist(opentelemetry-sdk)
Requires:       (python3dist(pydantic) >= 1 with python3dist(pydantic) < 2)
%description -n python3-%{pypi_name}
 otel-extensions-python: OpenTelemetry Extensions for Python OpenTelemetry
Extensions for Python is a collection of helper classes, functions, and
decorators to facilitate the use of the [OpenTelemetry Python API & SDK
packages]( Version SupportPython > 3.6 Installation pip installYou can install
through pip using:sh pip install otel-extensions(you may need to run pip with
root permission:...


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
%doc README.md
%{python3_sitelib}/otel_extensions
%{python3_sitelib}/otel_extensions-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.2.5-1
- Initial package.

