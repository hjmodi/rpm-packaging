# Created by pyp2rpm-3.3.10
%global pypi_name zipp
%global pypi_version 3.6.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        None
URL:            https://github.com/jaraco/zipp
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(func-timeout)
BuildRequires:  python3dist(jaraco.itertools)
BuildRequires:  python3dist(jaraco.packaging) >= 8.2
BuildRequires:  python3dist(pytest) >= 4.6
BuildRequires:  python3dist(pytest-black) >= 0.3.7
BuildRequires:  python3dist(pytest-checkdocs) >= 2.4
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-enabler) >= 1.0.1
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(pytest-mypy)
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx)

%description
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: .. .. :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(func-timeout)
Requires:       python3dist(jaraco.itertools)
Requires:       python3dist(jaraco.packaging) >= 8.2
Requires:       python3dist(pytest) >= 4.6
Requires:       python3dist(pytest-black) >= 0.3.7
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-enabler) >= 1.0.1
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(pytest-mypy)
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name}
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: .. .. :target:

%package -n python-%{pypi_name}-doc
Summary:        zipp documentation
%description -n python-%{pypi_name}-doc
Documentation for zipp

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 3.6.0-1
- Initial package.
