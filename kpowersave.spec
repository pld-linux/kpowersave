#
# TODO:
# - finish the descriptive part
# - make an i18n subpackage
# - include translation into the kde-i18n package
# - make a static subpackage
# - make a devel build
# - investigate the strange Make.common file
# - find a way to make it run in priviladged mode without sudo
#   (maby some group of permissions for people who are allowed to change
#   the cpufreq and so on)
# - investigate the BR and R
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	Systray KDE powersave icon	
Summary(pl):	cokolwiek
Name:		kpowersave
Version:	0.5.7
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
#Vendor:		-
Group:		Applications
#Icon:		-
Source0:	http://dl.sourceforge.net/powersave/%{name}-%{version}.tar.bz2
# Source0-md5:	119c42dc5ef1aac07f9be436e845db92
URL:		http://powersave.sourceforge.net
#BuildRequires:	autoconf
#BuildRequires:	automake
#BuildRequires:	libtool
#BuildRequires:	-
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
#BuildArch:	noarch
#ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whatever

%description -l pl
Cokolwiek

#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-

#%description subpackage

#%description subpackage -l pl

#%if 0
#%package devel
#Summary:	Development libraries and header files for termcap library
#Group:		Development/Libraries

#%description devel
#This is the package containing the development libaries and header
#files for ...

#%package static
#Summary:	Static ... library
#Group:		Development/Libraries
#Requires:	%{name}-devel = %{version}

#%description static
#Static ... library.
#%endif

%prep
%setup -q -n %{name}-%{version}
#%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
#%post	-p /sbin/ldconfig

%preun

%postun
#%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_libdir}/*
%{_datadir}/*

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

#%attr(755,root,root) %{_bindir}/*

#%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
