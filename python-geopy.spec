%define 	module	geopy
Summary:	A Geocoding Toolbox for Python
Name:		python-%{module}
Version:	0.94
Release:	2
License:	MIT
Group:		Development/Languages/Python
Source0:	http://geopy.googlecode.com/files/geopy-%{version}.tar.gz
# Source0-md5:	09c7f9e59136cec5db7d163e55d3bc68
URL:		http://code.google.com/p/geopy/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/geopy
%{py_sitescriptdir}/geopy/*.py[co]
%dir %{py_sitescriptdir}/geopy/geocoders
%{py_sitescriptdir}/geopy/geocoders/*.py[co]
%dir %{py_sitescriptdir}/geopy/parsers
%{py_sitescriptdir}/geopy/parsers/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/geopy-*.egg-info
%endif
