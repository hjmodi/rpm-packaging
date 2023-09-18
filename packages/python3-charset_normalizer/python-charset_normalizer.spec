# Created by pyp2rpm-3.3.10
%global pypi_name charset-normalizer
%global pypi_version 2.0.12

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(unicodedata2)
BuildRequires:  python3dist(sphinx)

%description
<h1 align"center">Charset Detection, for Everyone 👋 <a href" src"
align"center"> <sup>The Real First Universal Charset Detector</sup><br> <a
href" <img src" /> <a href"

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
Requires:       python3dist(unicodedata2)
%description -n python3-%{pypi_name}
<h1 align"center">Charset Detection, for Everyone 👋 <a href" src"
align"center"> <sup>The Real First Universal Charset Detector</sup><br> <a
href" <img src" /> <a href"

%package -n python-%{pypi_name}-doc
Summary:        charset-normalizer documentation
%description -n python-%{pypi_name}-doc
Documentation for charset-normalizer

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
%doc README.md
%{_bindir}/normalizer
%{python3_sitelib}/charset_normalizer
%{python3_sitelib}/charset_normalizer-%{pypi_version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Sep 18 2023 Harsh Modi <hmodi@redhat.com> - 2.0.12-1
- Initial package.

