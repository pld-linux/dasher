Name:		dasher
Summary:	Predictive text entry application
Version:	3.2.3
Release:	0.9
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.2/%{name}-%{version}.tar.bz2
# Source0-md5:	6f846c5ee98d006c2545367f7ee96bd9
URL:		http://www.inference.phy.cam.ac.uk/dasher/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	at-spi-devel
BuildRequires:	GConf2-devel
BuildRequires:	libgnome-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	gnome-speech-devel
BuildRequires:	bonobo-activation-devel
BuildRequires:	libbonobo-devel
BuildRequires:	ORBit2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dasher is an information-efficient text-entry interface, driven by
natural continuous pointing gestures. Dasher is a competitive
text-entry system wherever a full-size keyboard cannot be used - for
example, on a palmtop computer; on a wearable computer; when operating
a computer one-handed, by joystick, touchscreen, trackball, or mouse;
when operating a computer with zero hands (i.e., by head-mouse or by
eyetracker). The eyetracking version of Dasher allows an experienced
user to write text as fast as normal handwriting - 25 words per
minute; using a mouse, experienced users can write at 39 words per
minute.

%prep
%setup -q

%build
%configure \
	--with-gnome \
	--with-speech \
	--with-a11y
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_mandir}/man1/%{name}*
