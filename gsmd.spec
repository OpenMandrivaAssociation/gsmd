%define	name	gsmd
%define	version	0
%define	svnrel	20070701
%define	release %mkrel 0.%{svnrel}.3

%define major 0
%define libname %mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}

Summary: 	GSM daemon for OpenMoko
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: 	GPL
URL: 		https://www.openmoko.org/
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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0-0.20070701.3mdv2011.0
+ Revision: 619261
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0-0.20070701.2mdv2010.0
+ Revision: 429330
- rebuild

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 0-0.20070701.1mdv2009.0
+ Revision: 217186
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Sun Jul 01 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0-0.20070701.1mdv2008.0
+ Revision: 46861
- fix buildrequires
- Import gsmd

