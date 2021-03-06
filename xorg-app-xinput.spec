Summary:	Configuration and testing of XInput devices
Name:		xorg-app-xinput
Version:	1.6.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/archive/individual/app/xinput-%{version}.tar.bz2
# Source0-md5:	305980ac78a6954e306a14d80a54c441
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXinerama-devel
BuildRequires:	xorg-libXrandr-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to configure and test XInput devices.

%prep
%setup -q -n xinput-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xinput
%{_mandir}/man1/xinput.1x*

