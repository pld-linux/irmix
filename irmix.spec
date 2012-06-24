#
# Conditional build:
%bcond_without  alsa            # without ALSA
#
Summary:	irmix - an audio mixer for Lirc
Summary(pl):	irmix - mikser d�wi�ku dla Lirca
Name:		irmix
Version:	0.1.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia	
Source0:	http://www.blackfiveservices.co.uk/projects/%{name}-%{version}.tar.gz
# Source0-md5:	4f1bf91bf3bd85698743875f3cf5788b
URL:		http://www.blackfiveservices.co.uk/irmix.shtml
BuildRequires:	XFree86-devel
%{?with_alsa:BuildRequires:     alsa-lib-devel}
BuildRequires:	lirc-devel
Requires:	lirc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Irmix uses the Lirc infra-red receiver system to provide an imitation
of a TV's on-screen display, and handles making audio volumes
controllable from an infra-red remote control.

%description -l pl
Irmix pozwala na zdaln� kontrol� miksera d�wi�ku przy pomocy
odbiornika podczerwieni obs�ugiwanego przez pakiet Lirc, imituj�c
dodatkowo znane z telewizor�w wy�wietlanie na ekranie, tzw. OSD.

%prep
%setup -q

%build
%configure2_13 \
	%{!?with_alsa:--disable-alsa}
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
%attr(755,root,root) %{_bindir}/*
