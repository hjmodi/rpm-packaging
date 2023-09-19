# Created by pyp2rpm-3.3.10
%global pypi_name contextvars
%global pypi_version 2.4

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        PEP 567 Backport

License:        Apache License, Version 2.0
URL:            http://github.com/MagicStack/contextvars
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-immutables >= 0.9
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
 PEP 567 Backport This package implements a backport of Python 3.7 contextvars
module (see PEP 567) for Python 3.6.**Important:** at this moment this package
does not provide an asyncio event loop with PEP 567 support yet. Stay tuned for
updates. Original "contextvars" Package This package replaces the old
"contextvars" PyPI package which repository is available here < Documentation
Read the...

Requires:       python%{python3_pkgversion}-immutables >= 0.9


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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 2.4-1
- Initial package.

