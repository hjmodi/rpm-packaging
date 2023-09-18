# Created by pyp2rpm-3.3.10
%global pypi_name opentelemetry-semantic-conventions
%global pypi_version 0.33b0

Name:           python-%{pypi_name}
Version:        0.33~b0
Release:        1%{?dist}
Summary:        OpenTelemetry Semantic Conventions

License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-semantic-conventions
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
OpenTelemetry Semantic Conventions |pypi|.. |pyp This library contains
generated code for the semantic conventions defined by the OpenTelemetry
specification.Installation :: pip install opentelemetry-semantic-
conventionsCode Generation These files were generated automatically from code
in semconv_. To regenerate the code, run ../scripts/semconv/generate.sh.To
build against a new release or...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
OpenTelemetry Semantic Conventions |pypi|.. |pyp This library contains
generated code for the semantic conventions defined by the OpenTelemetry
specification.Installation :: pip install opentelemetry-semantic-
conventionsCode Generation These files were generated automatically from code
in semconv_. To regenerate the code, run ../scripts/semconv/generate.sh.To
build against a new release or...


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
%{python3_sitelib}/opentelemetry_semantic_conventions-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.33~b0-1
- Initial package.