%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_instrumentation_requests

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        0.40b0
Release:        1%{?dist}
Summary:        This library allows tracing HTTP requests made by the requests library.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/instrumentation/opentelemetry-instrumentation-requests
Source:         https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

%description
%{summary}

Requires:  python%{python3_pkgversion}-opentelemetry_api >= 1.12
Requires:  python%{python3_pkgversion}-opentelemetry_api < 2
Requires:  python%{python3_pkgversion}-opentelemetry_instrumentation = 0.40b0
Requires:  python%{python3_pkgversion}-opentelemetry_semantic_conventions = 0.40b0
Requires:  python%{python3_pkgversion}-opentelemetry_util_http = 0.40b0

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
%{python3_sitelib}/opentelemetry/instrumentation/requests/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Oct 04 2023 Harsh Modi <hmodi@redhat.com> - 0.40b0-1
- Initial package.