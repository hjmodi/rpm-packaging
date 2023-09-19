# Created by pyp2rpm-3.3.10
%global pypi_name pre-commit
%global pypi_version 2.17.0

Name:           python%{python3_pkgversion}-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        A framework for managing and maintaining multi-language pre-commit hooks

License:        MIT
URL:            https://github.com/pre-commit/pre-commit
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pre_commit-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
[![Build Status]( [![Azure DevOps coverage]( [![pre-commit.ci status]( pre-
commitA framework for managing and maintaining multi-language pre-commit hooks.

Requires:       python%{python3_pkgversion}-cfgv >= 2
Requires:       python%{python3_pkgversion}-identify >= 1
Requires:       python%{python3_pkgversion}-importlib-metadata
Requires:       python%{python3_pkgversion}-importlib-resources < 5.3~~
Requires:       python%{python3_pkgversion}-nodeenv >= 0.11.1
Requires:       python%{python3_pkgversion}-pyyaml >= 5.1
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-toml
Requires:       python%{python3_pkgversion}-virtualenv >= 20.0.8

%prep
%autosetup -n pre_commit-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%license LICENSE pre_commit/resources/empty_template_LICENSE.renv
%doc README.md
%{_bindir}/pre-commit
%{_bindir}/pre-commit-validate-config
%{_bindir}/pre-commit-validate-manifest
%{python3_sitelib}/pre_commit
%{python3_sitelib}/pre_commit-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Sep 19 2023 Harsh Modi <hmodi@redhat.com> - 2.17.0-1
- Initial package.

