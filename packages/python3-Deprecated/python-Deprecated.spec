# Created by pyp2rpm-3.3.10
%global pypi_name Deprecated
%global pypi_version 1.2.14

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python @deprecated decorator to deprecate old python classes, functions or methods

License:        MIT
URL:            https://github.com/tantale/deprecated
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bump2version) < 1~~
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx) < 2~~
BuildRequires:  python3dist(tox)
BuildRequires:  (python3dist(wrapt) >= 1.10 with python3dist(wrapt) < 2~~)
BuildRequires:  python3dist(sphinx)

%description
Deprecated Library Deprecated is Easy to Use If you need to mark a function or
a method as deprecated, you can use the @deprecated decorator:Save in a
hello.py:.. code:: python from deprecated import deprecated
@deprecated(version'1.2.1', reason"You should use another function") def
some_old_function(x, y): return x + y class SomeClass(object):
@deprecated(version'1.3.0', reason"This method is...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(wrapt) >= 1.10 with python3dist(wrapt) < 2~~)
%description -n python3-%{pypi_name}
Deprecated Library Deprecated is Easy to Use If you need to mark a function or
a method as deprecated, you can use the @deprecated decorator:Save in a
hello.py:.. code:: python from deprecated import deprecated
@deprecated(version'1.2.1', reason"You should use another function") def
some_old_function(x, y): return x + y class SomeClass(object):
@deprecated(version'1.3.0', reason"This method is...

%package -n python-%{pypi_name}-doc
Summary:        Deprecated documentation
%description -n python-%{pypi_name}-doc
Documentation for Deprecated

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.rst docs/source/license.rst
%doc README.md
%{python3_sitelib}/deprecated
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst docs/source/license.rst

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 1.2.14-1
- Initial package.

