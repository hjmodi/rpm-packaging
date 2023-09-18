# Created by pyp2rpm-3.3.10
%global pypi_name pydantic
%global pypi_version 1.9.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Data validation and settings management using python type hints

License:        MIT
URL:            https://github.com/samuelcolvin/pydantic
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(dataclasses) >= 0.6
BuildRequires:  python3dist(email-validator) >= 1.0.3
BuildRequires:  python3dist(python-dotenv) >= 0.10.4
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions) >= 3.7.4.3

%description
 pydantic[![CI]( [![Coverage]( [![pypi]( [![CondaForge]( [![downloads](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(dataclasses) >= 0.6
Requires:       python3dist(email-validator) >= 1.0.3
Requires:       python3dist(python-dotenv) >= 0.10.4
Requires:       python3dist(setuptools)
Requires:       python3dist(typing-extensions) >= 3.7.4.3
%description -n python3-%{pypi_name}
 pydantic[![CI]( [![Coverage]( [![pypi]( [![CondaForge]( [![downloads](


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
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.9.2-1
- Initial package.

