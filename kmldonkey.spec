%define		_pre	pre3
Summary:	A client for the mldonkey P2P network
Summary(pl):	Klient dla sieci P2P mldonkey
Name:		kmldonkey
Version:	0.10
Release:	0.1%{_pre}
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/kmldonkey/%{name}-%{version}%{_pre}.tar.bz2
# Source0-md5:	580b2d2c9f9c48cf83da5c93bf1c950f
URL:		http://www.gibreel.net/projects/kmldonkey/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KMLDonkey is a client for the mldonkey P2P network.

%description -l pl
KMLDonkey to klient dla sieci P2P mldonkey.

%package devel
Summary:	KMLDonkey header files
Summary(pl):	Pliki nagłówkowe KMLDonkey
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
KMLDonkey header files.

%description devel -l pl
Pliki nagłówkowe KMLDonkey.

%prep
%setup -q -n %{name}-%{version}%{_pre}

%build
kde_appsdir="%{_desktopdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
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
echo "Categories=Qt;KDE;Network;X-Communication;" >> $RPM_BUILD_ROOT%{_desktopdir}/kmldonkey.desktop
echo "Categories=Qt;KDE;X-KDE-settings-network;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kcmdonkey.desktop
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
%{_pixmapsdir}/*/*/*/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_datadir}/services/*.protocol
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%dir %{_includedir}/kmldonkey
%{_includedir}/kmldonkey/*
#%{_includedir}/*.h
