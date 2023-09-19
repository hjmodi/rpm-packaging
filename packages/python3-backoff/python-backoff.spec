# Created by pyp2rpm-3.3.10
%global pypi_name backoff
%global pypi_version 1.11.1

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Function decoration for backoff and retry

License:        None
URL:            https://github.com/litl/backoff
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 **Function decoration for backoff and retry**This module provides function
decorators which can be used to wrap a function such that it will be retried
until some condition is met. It is meant to be of use when accessing unreliable
resources with the potential for intermittent failures i.e. network resources
and external

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.11.1-1
- Initial package.
