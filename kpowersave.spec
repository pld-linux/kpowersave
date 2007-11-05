#
# TODO:
# - investigate the strange Make.common file
# - find a way to make it run in privileged mode without sudo
#   (maybe some group of permissions for people who are allowed to change
#   the cpufreq and so on)
# - use kdepackage-template.spec as base
#
Summary:	Systray KDE powersave icon
Summary(de.UTF-8):	KDE Powersave Tray Ikone
Summary(pl.UTF-8):	Ikona oszczędzania energii dla zasobnika KDE
Name:		kpowersave
Version:	0.7.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/powersave/%{name}-%{version}.tar.bz2
# Source0-md5:	061cb55774ebac15549a1e7affa87827
Patch0:		kde-ac260-lt.patch
URL:		http://powersave.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.6.1
BuildRequires:	dbus-devel >= 0.33
BuildRequires:	dbus-qt-devel >= 0.70
BuildRequires:	hal-devel >= 0.5.4
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	powersave-devel >= 0.12.7
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
Requires:	powersave >= 0.12.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Systray KDE powersave icon.

%description -l de.UTF-8
KDE Powersave Tray Ikone.

%description -l pl.UTF-8
Ikona oszczędzania energii dla zasobnika KDE.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{sl_SI,sl}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_libdir}/libkdeinit_kpowersave.so
%{_libdir}/libkdeinit_kpowersave.la
%attr(755,root,root) %{_libdir}/kde3/kpowersave.so
%{_libdir}/kde3/kpowersave.la
%{_datadir}/apps/kpowersave
%{_datadir}/autostart/kpowersave-autostart.desktop
%{_datadir}/config/kpowersaverc
%{_desktopdir}/kde/kpowersave.desktop
%{_iconsdir}/hicolor/*/apps/kpowersave.png
