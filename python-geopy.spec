# Conditional build:
%bcond_with	doc		# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	geopy
Summary:	A Geocoding Toolbox for Python
Name:		python-%{module}
Version:	1.3.0
Release:	4
License:	MIT
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/g/geopy/geopy-%{version}.tar.gz
# Source0-md5:	bc11aeb285b8c21522275e79fd98d547
URL:		https://pypi.python.org/pypi/geopy

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
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif


%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
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

