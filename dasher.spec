Summary:	Predictive text entry application
Summary(pl.UTF-8):	Przewidująca aplikacja do wprowadzania tekstu
Name:		dasher
Version:	4.10.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/gnome/sources/dasher/4.10/%{name}-%{version}.tar.bz2
# Source0-md5:	83e556690ac54c4bb8c49c050510259e
URL:		http://www.inference.phy.cam.ac.uk/dasher/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	ORBit2-devel >= 1:2.14.7
BuildRequires:	at-spi-devel >= 1.20.0
BuildRequires:	atk-devel >= 1.20.0
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.8
BuildRequires:	docbook-dtd412-xml
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-speech-devel >= 0.4.10
BuildRequires:	gnome-vfs2-devel >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libbonobo-devel >= 2.20.0
BuildRequires:	libglade2-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXtst-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%description -l pl.UTF-8
Dasher to wydajny interfejs do wprowadzania tekstu sterowany przez
naturalne ciągłe gesty urządzenia wskazującego. Dasher jest
konkurencyjnym systemem wprowadzania tekstu wszędzie tam, gdzie nie
można użyć pełnowymiarowej klawiatury - na przykład w palmtopach czy
komputerach przenośnych, komputerach sterowanych przez jednorękich, za
pomocą joysticka, ekranu dotykowego, trackballa lub myszy albo bez
użycia rąk (poprzez śledzenie ruchów głowy albo oczu). Wersja Dashera
śledząca ruchy oczu pozwala doświadczonemu użytkownikowi pisać tekst z
podobną szybkością do normalnego pisma - 25 słów na minutę; przy
użyciu myszy doświadczeni użytkownicy mogą pisać nawet 39 słów na
minutę.

%prep
%setup -q

%build
rm -r m4
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gnome \
	--enable-speech \
	--enable-a11y \
	--disable-scrollkeeper \
	--with-cairo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install dasher.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall dasher.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/dasher.schemas
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}*
%{_omf_dest_dir}/%{name}
