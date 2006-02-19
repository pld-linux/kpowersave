#
# TODO:
# - finish the descriptive part
# - make an i18n subpackage
# - include translation into the kde-i18n package
# - make a static subpackage
# - make a devel build
# - investigate the strange Make.common file
# - find a way to make it run in privileged mode without sudo
#   (maybe some group of permissions for people who are allowed to change
#   the cpufreq and so on)
# - investigate the BR and R
# - use kdepackage-template.spec as base
#
Summary:	Systray KDE powersave icon
Summary(pl):	Ikona oszczêdzania energii dla zasobnika KDE
Name:		kpowersave
Version:	0.5.7
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://dl.sourceforge.net/powersave/%{name}-%{version}.tar.bz2
# Source0-md5:	119c42dc5ef1aac07f9be436e845db92
URL:		http://powersave.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Systray KDE powersave icon.

%description -l pl
Ikona oszczêdzania energii dla zasobnika KDE.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/*
%{_datadir}/*
