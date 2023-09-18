# Created by pyp2rpm-3.3.10
%global pypi_name Jinja2
%global pypi_version 3.0.3

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A very fast and expressive template engine

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/jinja/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(babel) >= 2.7
BuildRequires:  python3dist(markupsafe) >= 2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Jinja is a fast, expressive, extensible templating engine. Special placeholders
in the template allow writing code similar to Python syntax. Then the template
is passed data to render the final document.It includes:- Template inheritance
and inclusion. - Define and import macros within templates. - HTML templates
can use autoescaping to prevent XSS from untrusted user input. - A sandboxed...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(babel) >= 2.7
Requires:       python3dist(markupsafe) >= 2
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Jinja is a fast, expressive, extensible templating engine. Special placeholders
in the template allow writing code similar to Python syntax. Then the template
is passed data to render the final document.It includes:- Template inheritance
and inclusion. - Define and import macros within templates. - HTML templates
can use autoescaping to prevent XSS from untrusted user input. - A sandboxed...

%package -n python-%{pypi_name}-doc
Summary:        Jinja2 documentation
%description -n python-%{pypi_name}-doc
Documentation for Jinja2

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
%{python3_sitelib}/jinja2
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.rst docs/license.rst

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 3.0.3-1
- Initial package.

