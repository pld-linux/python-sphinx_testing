#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Testing utility classes and functions for Sphinx extensions
Summary(pl.UTF-8):	Klasy i funkcje narzędziowe do testowania rozszerzeń Sphinksa
Name:		python-sphinx_testing
Version:	1.0.1
Release:	7
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-testing/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-testing/sphinx-testing-%{version}.tar.gz
# Source0-md5:	0f60adab66d877ac8c2c23f78dc7ed32
Patch0:		sphinx-testing-py3.patch
URL:		https://pypi.org/project/sphinx-testing/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx < 2
BuildRequires:	python-mock
BuildRequires:	python-nose
BuildRequires:	python-six
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-nose
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-testing provides testing utility classes and functions for
Sphinx extensions.

%description -l pl.UTF-8
sphinx-testing udostępnia klasy i funkcje narzędziowe do testowania
rozszerzeń Sphinksa.

%package -n python3-sphinx_testing
Summary:	Testing utility classes and functions for Sphinx extensions
Summary(pl.UTF-8):	Klasy i funkcje narzędziowe do testowania rozszerzeń Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-sphinx_testing
sphinx-testing provides testing utility classes and functions for
Sphinx extensions.

%description -n python3-sphinx_testing -l pl.UTF-8
sphinx-testing udostępnia klasy i funkcje narzędziowe do testowania
rozszerzeń Sphinksa.

%prep
%setup -q -n sphinx-testing-%{version}
%patch -P0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m nose tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m nose tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/sphinx_testing
%{py_sitescriptdir}/sphinx_testing-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-sphinx_testing
%defattr(644,root,root,755)
%doc AUTHORS CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/sphinx_testing
%{py3_sitescriptdir}/sphinx_testing-%{version}-py*.egg-info
%endif
