#
# TODO:
# - investigate the strange Make.common file
# - find a way to make it run in privileged mode without sudo
#   (maybe some group of permissions for people who are allowed to change
#   the cpufreq and so on)
# - use kdepackage-template.spec as base
#
Summary:	Systray KDE powersave icon
Summary(pl):	Ikona oszczêdzania energii dla zasobnika KDE
Name:		kpowersave
Version:	0.5.8
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://dl.sourceforge.net/powersave/%{name}-%{version}.tar.bz2
# Source0-md5:	6cea41c922b95224f788654004db3f64
Patch0:		kde-ac260.patch
Patch1:		kde-am.patch
Patch2:		kde-ac260-lt.patch
URL:		http://powersave.sourceforge.net/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1.6.1
BuildRequires:	dbus-devel >= 0.33
BuildRequires:	hal-devel >= 0.5.4
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	pkgconfig
BuildRequires:	powersave-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Systray KDE powersave icon.

%description -l pl
Ikona oszczêdzania energii dla zasobnika KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

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
