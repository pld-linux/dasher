Name:		dasher
Summary:	Predictive text entry application
Version:	3.2.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/3.2/%{name}-%{version}.tar.bz2
# Source0-md5:	aa851fab82fd79456fa019212a496c57
Patch0:		%{name}-locale-names.patch
URL:		http://www.inference.phy.cam.ac.uk/dasher/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	at-spi-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-speech-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libbonobo-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
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
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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

%post -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS README Doc/Colourschemes
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_mandir}/man1/%{name}*
%{_omf_dest_dir}/%{name}
