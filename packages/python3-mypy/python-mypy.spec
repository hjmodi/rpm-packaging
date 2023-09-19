# Created by pyp2rpm-3.3.10
%global pypi_name mypy
%global pypi_version 0.971

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Optional static typing for Python

License:        MIT License
URL:            http://www.mypy-lang.org/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-mypy-extensions >= 0.4.3
BuildRequires:  python%{python3_pkgversion}-psutil >= 4
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-tomli >= 1.1
BuildRequires:  (python%{python3_pkgversion}-typed-ast >= 1.4 with python%{python3_pkgversion}-typed-ast < 2~~)
BuildRequires:  (python%{python3_pkgversion}-typed-ast >= 1.4 with python%{python3_pkgversion}-typed-ast < 2~~)
BuildRequires:  python%{python3_pkgversion}-typing-extensions >= 3.10
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
Mypy -- Optional Static Typing for Python Add type annotations to your Python
programs, and use mypy to type check them. Mypy is essentially a Python linter
on steroids, and it can catch many programming errors by analyzing your
program, without actually having to run it. Mypy has a powerful type system
with features such as type inference, gradual typing, generics and union

Requires:       python%{python3_pkgversion}-lxml
Requires:       python%{python3_pkgversion}-mypy-extensions >= 0.4.3
Requires:       python%{python3_pkgversion}-psutil >= 4
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-tomli >= 1.1
Requires:       (python%{python3_pkgversion}-typed-ast >= 1.4 with python%{python3_pkgversion}-typed-ast < 2~~)
Requires:       (python%{python3_pkgversion}-typed-ast >= 1.4 with python%{python3_pkgversion}-typed-ast < 2~~)
Requires:       python%{python3_pkgversion}-typing-extensions >= 3.10

%package -n python%{python3_pkgversion}-%{pypi_name}-doc
Summary:        mypy documentation
%description -n python%{python3_pkgversion}-%{pypi_name}-doc
Documentation for mypy

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

%files
%license LICENSE mypy/typeshed/LICENSE mypyc/external/googletest/LICENSE
%doc README.md docs/README.md mypyc/README.md mypyc/external/googletest/README.md test-data/packages/modulefinder/readme.txt test-data/unit/README.md
%{_bindir}/dmypy
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/stubgen
%{_bindir}/stubtest
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/mypyc
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python%{python3_pkgversion}-%{pypi_name}-doc
%doc html
%license LICENSE mypy/typeshed/LICENSE mypyc/external/googletest/LICENSE

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 0.971-1
- Initial package.