# Created by pyp2rpm-3.3.10
%global pypi_name typing-extensions
%global pypi_version 4.1.1

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Backported and Experimental Type Hints for Python 3

License:        PSF
URL:            https://github.com/python/typing_extensions
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/typing_extensions-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flip_core
BuildRequires:  python%{python3_pkgversion}-tomli
BuildRequires:  python%{python3_pkgversion}-pip

%description
%{summary}

%prep
set -ex
%autosetup -n typing_extensions-%{version}

%build
set -ex
%pyproject_wheel

%install
set -ex
%pyproject_install

%files
%{python3_sitelib}/__pycache__/typing_extensions.*
%{python3_sitelib}/typing_extensions.py
%{python3_sitelib}/typing_extensions-%{version}.dist-info/

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 4.1.1-1
- Initial package.
