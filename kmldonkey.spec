Summary:	A client for the mldonkey P2P network
Summary(pl):	Klient dla sieci mldonkey P2P
Name:		kmldonkey
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/kmldonkey/unstable.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0ac91aba88165ae377754156087b421b
URL:		http://www.gibreel.net/projects/kmldonkey/
Requires:	mldonkey
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KMLDonkey is a client for the mldonkey P2P network.

%description -l pl
KMLDonkey to klient dla sieci mldonkey P2P.

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
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/Network
mv $RPM_BUILD_ROOT%{_applnkdir}/Internet/* $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/Network/* $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/Network

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/Misc/*
%{_applnkdir}/Settings/KDE/Network/*
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
