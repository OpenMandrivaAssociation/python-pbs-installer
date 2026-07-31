%define module pbs-installer
%define oname pbs_installer

Name:		python-pbs-installer
Version:	2026.07.28
Release:	1
Summary:	Installer for Python Build Standalone
License:	MIT
Group:		Development/Python
URL:		https://pbs-installer.readthedocs.io
# repo-url https://github.com/frostming/pbs-installer/
# Use pypi source as git repo tarball produces wrong version strings in dist-info path
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Installer for Python Build Standalone

%files
%{_bindir}/pbs-install
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
