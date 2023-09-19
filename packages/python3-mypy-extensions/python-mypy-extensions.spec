# Created by pyp2rpm-3.3.10
%global pypi_name mypy-extensions
%global pypi_version 1.0.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Type system extensions for programs checked with the mypy type checker

License:        MIT License
URL:            https://github.com/python/mypy_extensions
Source0:        https://files.pythonhosted.org/packages/source/m/%{pypi_name}/mypy_extensions-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Mypy Extensions The "mypy_extensions" module defines extensions to the standard
"typing" module that are supported by the mypy type checker and the mypyc
compiler.


%prep
%autosetup -n mypy_extensions-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/mypy_extensions.py
%{python3_sitelib}/mypy_extensions-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 1.0.0-1
- Initial package.
