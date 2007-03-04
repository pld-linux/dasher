Summary:	Predictive text entry application
Summary(pl.UTF-8):	Przewidująca aplikacja do wprowadzania tekstu
Name:		dasher
Version:	4.2.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/dasher/4.2/%{name}-%{version}.tar.bz2
# Source0-md5:	bb231a7afb424ad97264da67e5d24620
Patch0:		%{name}-ac.patch
Patch1:		%{name}-as-needed.patch
Patch2:		%{name}-iconv.patch
URL:		http://www.inference.phy.cam.ac.uk/dasher/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	ORBit2-devel >= 2.14.3
BuildRequires:	at-spi-devel >= 1.7.12
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1:1.8
BuildRequires:	expat-devel
BuildRequires:	gnome-speech-devel >= 0.4.5
BuildRequires:	gnome-vfs2-devel >= 2.16.1
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35
BuildRequires:	libbonobo-devel >= 2.16.0
BuildRequires:	libglade2-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	xorg-lib-libXtst-devel
Requires(post,postun):	scrollkeeper
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
komputerach przenośnych, komputerach sterowanych przez jednorękich,
za pomocą joysticka, ekranu dotykowego, trackballa lub myszy albo bez
użycia rąk (poprzez śledzenie ruchów głowy albo oczu). Wersja Dashera
śledząca ruchy oczu pozwala doświadczonemu użytkownikowi pisać tekst
z podobną szybkością do normalnego pisma - 25 słów na minutę; przy
użyciu myszy doświadczeni użytkownicy mogą pisać nawet 39 słów na
minutę.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS README Doc/Colourschemes
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}*
%{_omf_dest_dir}/%{name}
