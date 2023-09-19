# Created by pyp2rpm-3.3.10
%global pypi_name pydantic
%global pypi_version 1.9.2

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Data validation and settings management using python type hints

License:        MIT
URL:            https://github.com/samuelcolvin/pydantic
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-dataclasses >= 0.6
BuildRequires:  python%{python3_pkgversion}-email-validator >= 1.0.3
BuildRequires:  python%{python3_pkgversion}-python-dotenv >= 0.10.4
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-typing-extensions >= 3.7.4.3

%description
 pydantic[![CI]( [![Coverage]( [![pypi]( [![CondaForge]( [![downloads](

Requires:       python%{python3_pkgversion}-dataclasses >= 0.6
Requires:       python%{python3_pkgversion}-email-validator >= 1.0.3
Requires:       python%{python3_pkgversion}-python-dotenv >= 0.10.4
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.7.4.3

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

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.9.2-1
- Initial package.

