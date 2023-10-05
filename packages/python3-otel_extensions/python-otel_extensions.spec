# Created by pyp2rpm-3.3.8
%global pypi_name otel_extensions
%global pypi_version 1.0.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python extensions for OpenTelemetry

License:        Apache-2.0
URL:            https://github.com/s4v4g3/otel-extensions-python
Source0:        https://files.pythonhosted.org/packages/source/o/%{pypi_name}/otel-extensions-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-opentelemetry-api
BuildRequires:  python%{python3_pkgversion}-opentelemetry-sdk
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 otel-extensions-python: OpenTelemetry Extensions for Python OpenTelemetry
Extensions for Python is a collection of helper classes, functions, and
decorators to facilitate the use of the [OpenTelemetry Python API & SDK
packages]( Version SupportPython > 3.6 Installation pip installYou can install
through pip using:sh pip install otel-extensions(you may need to run pip with
root permission:...

Requires:       python%{python3_pkgversion}-opentelemetry-api
Requires:       python%{python3_pkgversion}-opentelemetry-sdk

%prep
%autosetup -n otel-extensions-%{pypi_version}
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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Wed Oct 04 2023 Harsh Modi <hmodi@redhat.com> - 1.0.0-1
- Initial package.
