# Created by pyp2rpm-3.3.10
%global pypi_name importlib-metadata
%global pypi_version 4.8.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Read metadata from Python packages

License:        None
URL:            https://github.com/python/importlib_metadata
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/importlib_metadata-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flufl.flake8)
BuildRequires:  python3dist(importlib-resources) >= 1.3
BuildRequires:  python3dist(ipython)
BuildRequires:  python3dist(jaraco.packaging) >= 8.2
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pep517)
BuildRequires:  python3dist(pyfakefs)
BuildRequires:  python3dist(pytest) >= 6
BuildRequires:  python3dist(pytest-black) >= 0.3.7
BuildRequires:  python3dist(pytest-checkdocs) >= 2.4
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-enabler) >= 1.0.1
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(pytest-mypy)
BuildRequires:  python3dist(pytest-perf) >= 0.9.2
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(typing-extensions) >= 3.6.4
BuildRequires:  python3dist(zipp) >= 0.5
BuildRequires:  python3dist(sphinx)

%description
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flufl.flake8)
Requires:       python3dist(importlib-resources) >= 1.3
Requires:       python3dist(ipython)
Requires:       python3dist(jaraco.packaging) >= 8.2
Requires:       python3dist(packaging)
Requires:       python3dist(pep517)
Requires:       python3dist(pyfakefs)
Requires:       python3dist(pytest) >= 6
Requires:       python3dist(pytest-black) >= 0.3.7
Requires:       python3dist(pytest-checkdocs) >= 2.4
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-enabler) >= 1.0.1
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(pytest-mypy)
Requires:       python3dist(pytest-perf) >= 0.9.2
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(sphinx)
Requires:       python3dist(typing-extensions) >= 3.6.4
Requires:       python3dist(zipp) >= 0.5
%description -n python3-%{pypi_name}
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: .. image::

%package -n python-%{pypi_name}-doc
Summary:        importlib-metadata documentation
%description -n python-%{pypi_name}-doc
Documentation for importlib-metadata

%prep
%autosetup -n importlib_metadata-%{pypi_version}
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
%{python3_sitelib}/importlib_metadata
%{python3_sitelib}/importlib_metadata-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 4.8.3-1
- Initial package.

