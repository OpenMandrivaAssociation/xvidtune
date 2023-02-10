Name:		xvidtune
Version:	1.0.4
Release:	1
Summary:	Video mode tuner for X.org
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xt) >= 1.0.0
BuildRequires:	pkgconfig(xxf86vm) >= 1.0.0
BuildRequires:	pkgconfig(xaw7) >= 1.0.1
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(pthread-stubs)
BuildRequires:	pkgconfig(xorg-macros)

%description
Xvidtune is a client interface to the X server video mode extension
(XFree86-VidModeExtension).

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xvidtune
%{_datadir}/X11/app-defaults/Xvidtune
%doc %{_mandir}/man1/xvidtune.*
