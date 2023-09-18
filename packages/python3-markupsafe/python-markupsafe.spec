# Created by pyp2rpm-3.3.10
%global pypi_name MarkupSafe
%global pypi_version 2.0.1

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MarkupSafe MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are replaced
so that they display as the actual characters. This mitigates injection
attacks, meaning untrusted user input can safely be displayed on a page.
Installing -Install and update using pip_:.. code-block:: text pip install -U
MarkupSafe.....

%package -n python-%{pypi_name}-doc
Summary:        MarkupSafe documentation
%description -n python-%{pypi_name}-doc
Documentation for MarkupSafe

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
%license LICENSE.rst docs/license.rst
%doc README.rst
%{python3_sitearch}/markupsafe
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst docs/license.rst

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 2.0.1-1
- Initial package.
