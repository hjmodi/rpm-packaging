# Created by pyp2rpm-3.3.10
%global pypi_name wrapt
%global pypi_version 1.15.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Module for decorators, wrappers and monkey patching

License:        BSD
URL:            https://github.com/GrahamDumpleton/wrapt
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 38.3

%description
|Actions| |PyPI|The aim of the **wrapt** module is to provide a transparent
object proxy for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.The **wrapt** module focuses very
much on correctness. It therefore goes way beyond existing mechanisms such as
functools.wraps() to ensure that decorators preserve introspectability,
signatures,...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
|Actions| |PyPI|The aim of the **wrapt** module is to provide a transparent
object proxy for Python, which can be used as the basis for the construction of
function wrappers and decorator functions.The **wrapt** module focuses very
much on correctness. It therefore goes way beyond existing mechanisms such as
functools.wraps() to ensure that decorators preserve introspectability,
signatures,...


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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 1.15.0-1
- Initial package.

