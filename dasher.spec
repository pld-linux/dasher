Summary:	Predictive text entry application
Summary(pl.UTF-8):	Przewidująca aplikacja do wprowadzania tekstu
Name:		dasher
Version:	4.11
Release:	3
License:	GPL v2
Group:		X11/Applications/Accessibility
Source0:	http://ftp.gnome.org/pub/GNOME/sources/dasher/4.11/%{name}-%{version}.tar.bz2
# Source0-md5:	55695cacecb9fa9e3259e0f2ef82ae9e
URL:		http://www.inference.phy.cam.ac.uk/dasher/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	ORBit2-devel >= 1:2.14.7
BuildRequires:	at-spi-devel >= 1.20.0
BuildRequires:	atk-devel >= 1.20.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	docbook-dtd412-xml
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-speech-devel >= 0.4.10
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	intltool >= 0.40.1
BuildRequires:	libbonobo-devel >= 2.20.0
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXtst-devel
Requires(post,postun):	gtk-update-icon-cache
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
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
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

%find_lang %{name} --with-gnome --with-omf --all-name

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
