Summary:	A client for the mldonkey P2P network
Summary(pl):	Klient dla sieci P2P mldonkey
Name:		kmldonkey
Version:	0.10.1
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://savannah.nongnu.org/download/kmldonkey/%{name}-%{version}.tar.bz2
# Source0-md5:	e1932b1455c7a5cec53145b675bdd8d7
Patch0:		%{name}-desktop.patch
URL:		http://www.kmldonkey.org/
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	kdebase-devel >= 3.0
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMLDonkey is a client for the mldonkey P2P network.

%description -l pl
KMLDonkey to klient dla sieci P2P mldonkey.

%package devel
Summary:	KMLDonkey header files
Summary(pl):	Pliki nag³ówkowe KMLDonkey
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
KMLDonkey header files.

%description devel -l pl
Pliki nag³ówkowe KMLDonkey.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kdelnkdir=%{_desktopdir} \
	kcmdonkeydir=%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_desktopdir}/{ed2k,magnet,sig2dat}.protocol $RPM_BUILD_ROOT%{_datadir}/services/

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so*
%{_libdir}/kde3/*.la
%{_datadir}/apps/kmldonkey
%{_datadir}/apps/mldonkeyapplet
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_iconsdir}/*/*/*/*
%{_desktopdir}/*.desktop
%{_desktopdir}/kde/*.desktop
%{_datadir}/services/*.protocol
%{_datadir}/services/kded/kmldonkeyd.desktop
%{_datadir}/services/kmldonkey_debugpage.desktop
%{_datadir}/servicetypes/kmldonkey_plugin.desktop
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/kmldonkey
