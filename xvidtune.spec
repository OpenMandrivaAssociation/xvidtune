Name:		xvidtune
Version:	1.0.3
Release:	6
Summary:	Video mode tuner for X.org
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: pkgconfig(xxf86vm) >= 1.0.0
BuildRequires: pkgconfig(xaw7) >= 1.0.1
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(pthread-stubs)
BuildRequires: x11-util-macros >= 1.0.1

%description
Xvidtune is a client interface to the X server video mode extension
(XFree86-VidModeExtension).

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xvidtune
%{_datadir}/X11/app-defaults/Xvidtune
%{_mandir}/man1/xvidtune.*
