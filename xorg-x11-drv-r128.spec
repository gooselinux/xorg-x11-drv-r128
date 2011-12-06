%define tarball xf86-video-r128
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 r128 video driver
Name:      xorg-x11-drv-r128
Version:   6.8.1
Release:   2%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   http://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   r128.xinf

Patch0:	    r128-6.8.1-panel-hack.patch

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.4.99.1
BuildRequires: mesa-libGL-devel >= 6.4-4
BuildRequires: libdrm-devel >= 2.0-1
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.1.5

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.4.99.1

%description 
X.Org X11 r128 video driver.

%prep
%setup -q -n %{tarball}-%{version}
%patch0 -p1 -b .panel

%build
# aclocal ; automake -a ; autoconf
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.r128
%{driverdir}/r128_drv.so
%{_datadir}/hwdata/videoaliases/r128.xinf
%{_mandir}/man4/r128.4*

%changelog
* Fri Sep 18 2009 Adam Jackson <ajax@redhat.com> 6.8.1-2
- r128-6.8.1-panel-hack.patch: Set sync ranges based on panel size.

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 6.8.1-1
- r128 6.8.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.0-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 6.8.0-3.1
- ABI bump

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 6.8.0-2
- rebuild for new server API

* Mon Aug 04 2008 Adam Jackson <ajax@redhat.com> 6.8.0-1
- Initial build of separate r128 driver.

