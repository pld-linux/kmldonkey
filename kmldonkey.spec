%define		_pre	pre3
Summary:	A client for the mldonkey P2P network
Summary(pl):	Klient dla sieci P2P mldonkey
Name:		kmldonkey
Version:	0.10
Release:	0.4pre3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/kmldonkey/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	580b2d2c9f9c48cf83da5c93bf1c950f
Patch0:		%{name}-desktop.patch
URL:		http://www.kmldonkey.org/
BuildRequires:	fam-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KMLDonkey is a client for the mldonkey P2P network.

%description -l pl
KMLDonkey to klient dla sieci P2P mldonkey.

%package devel
Summary:	KMLDonkey header files
Summary(pl):	Pliki nag³ówkowe KMLDonkey
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
KMLDonkey header files.

%description devel -l pl
Pliki nag³ówkowe KMLDonkey.

%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch0 -p1

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
cp /usr/share/automake/config.sub admin
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_desktopdir}/Internet/* $RPM_BUILD_ROOT%{_desktopdir}/
mv $RPM_BUILD_ROOT%{_desktopdir}/Settings/Network/* $RPM_BUILD_ROOT%{_desktopdir}/kde/

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_datadir}/apps/*
%{_iconsdir}/*/*/*/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/services/*.protocol
%{_datadir}/services/kded/mobilemule.desktop
%{_datadir}/services/kmldonkey_debugpage.desktop
%{_datadir}/servicetypes/kmldonkey_plugin.desktop
	 
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/kmldonkey
%{_includedir}/kmldonkey/*
#%{_includedir}/*.h
