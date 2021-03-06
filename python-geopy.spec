# Conditional build:
%bcond_with	doc		# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	geopy
Summary:	A Geocoding Toolbox for Python
Name:		python-%{module}
Version:	1.23.0
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/g/geopy/geopy-%{version}.tar.gz
# Source0-md5:	e8b7d678665fab26ce3e8ff97f352ee8
URL:		https://pypi.python.org/pypi/geopy
BuildRequires:	rpmbuild(macros) >= 1.710

%if %{with python2}
## BuildRequires:	pylint
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
## BuildRequires:	pylint-python3
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif

BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
geopy makes it easy for developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources, such as wikis.

geopy currently includes support for six geocoders: Google Maps,
Yahoo! Maps, Windows Local Live (Virtual Earth), geocoder.us,
GeoNames, MediaWiki pages (with the GIS extension), and Semantic
MediaWiki pages.


%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
geopy makes it easy for developers to locate the coordinates of
addresses, cities, countries, and landmarks across the globe using
third-party geocoders and other data sources, such as wikis.

geopy currently includes support for six geocoders: Google Maps,
Yahoo! Maps, Windows Local Live (Virtual Earth), geocoder.us,
GeoNames, MediaWiki pages (with the GIS extension), and Semantic
MediaWiki pages.

## %description -n python3-%{module} -l pl.UTF-8

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
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

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%dir %{py_sitescriptdir}/%{module}/geocoders
%{py_sitescriptdir}/%{module}/geocoders/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
## %doc AUTHORS CHANGES LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

