Summary:	A client for the mldonkey P2P network
Summary(pl):	Klient dla sieci P2P mldonkey
Name:		kmldonkey
Version:	0.9.1
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/kmldonkey/unstable.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0ac91aba88165ae377754156087b421b
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
Summary(pl):	Pliki nag³ówkowe KMLDonkey
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
KMLDonkey header files.

%description devel -l pl
Pliki nag³ówkowe KMLDonkey.

%prep
%setup -q

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
%{_includedir}/*.h
