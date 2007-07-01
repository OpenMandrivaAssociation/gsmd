%define	name	gsmd
%define	version	0
%define	svnrel	20070701
%define	release %mkrel 0.%{svnrel}.1

%define major 0
%define libname %mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}

Summary: 	GSM daemon for OpenMoko
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		System/Servers
License: 	GPL
URL: 		http://www.openmoko.org/
Source0:	%{name}-%{svnrel}.tar.lzma
BuildRequires:	lzma glib-gettextize

%description
GSM daemon for OpenMoko.

%package -n	%{libname}
Summary:	GSM libraries for OpenMoko
Group:		System/Libraries
License:	LGPL
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
GSM libraries for OpenMoko.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
License:	LGPL
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Development files for %{name}.

%prep
%setup -q -n gsm

%build
autoreconf -v --install
glib-gettextize --force --copy
%configure --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_libdir}/{,gsmd/}*.la

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%{_bindir}/libgsmd-tool
%{_sbindir}/gsmd

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%dir %{_libdir}/gsmd
%{_libdir}/gsmd/*.so.*

%files -n %{devname}
%defattr(-,root,root)
%dir %{_includedir}/libgsmd
%{_includedir}/libgsmd/*.h
%dir %{_includedir}/gsmd
%{_includedir}/gsmd/*.h
%{_libdir}/*.so
%{_libdir}/gsmd/*.so
%{_libdir}/pkgconfig/*.pc
