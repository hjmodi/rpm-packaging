# Created by pyp2rpm-3.3.10
%global pypi_name immutables
%global pypi_version 0.19

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Immutable Collections

License:        Apache License, Version 2.0
URL:            https://github.com/MagicStack/immutables
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  (python3dist(flake8) >= 5.0.4 with python3dist(flake8) < 5.1)
BuildRequires:  python3dist(mypy) = 0.971
BuildRequires:  (python3dist(pycodestyle) >= 2.9.1 with python3dist(pycodestyle) < 2.10)
BuildRequires:  (python3dist(pytest) >= 6.2.4 with python3dist(pytest) < 6.3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions) >= 3.7.4.3

%description
immutables An immutable mapping type for Python.The underlying datastructure is
a Hash Array Mapped Trie (HAMT) used in Clojure, Scala, Haskell, and other
functional languages. This implementation is used in CPython 3.7 in the
contextvars module (see PEP 550 < and

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(flake8) >= 5.0.4 with python3dist(flake8) < 5.1)
Requires:       python3dist(mypy) = 0.971
Requires:       (python3dist(pycodestyle) >= 2.9.1 with python3dist(pycodestyle) < 2.10)
Requires:       (python3dist(pytest) >= 6.2.4 with python3dist(pytest) < 6.3)
Requires:       python3dist(typing-extensions) >= 3.7.4.3
%description -n python3-%{pypi_name}
immutables An immutable mapping type for Python.The underlying datastructure is
a Hash Array Mapped Trie (HAMT) used in Clojure, Scala, Haskell, and other
functional languages. This implementation is used in CPython 3.7 in the
contextvars module (see PEP 550 < and


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
%license LICENSE LICENSE-APACHE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 0.19-1
- Initial package.

