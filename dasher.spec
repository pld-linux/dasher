Summary:	Predictive text entry application
Summary(pl):	Przewiduj�ca aplikacja do wprowadzania tekstu
Name:		dasher
Version:	3.2.15
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/dasher/3.2/%{name}-%{version}.tar.bz2
# Source0-md5:	a3fa85e32c94c69476e12ecba7d257e7
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.inference.phy.cam.ac.uk/dasher/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	at-spi-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	gnome-speech-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	intltool >= 0.33
BuildRequires:	libbonobo-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
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

%description -l pl
Dasher to wydajny interfejs do wprowadzania tekstu sterowany przez
naturalne ci�g�e gesty urz�dzenia wskazuj�cego. Dasher jest
konkurencyjnym systemem wprowadzania tekstu wsz�dzie tam, gdzie nie
mo�na u�y� pe�nowymiarowej klawiatury - na przyk�ad w palmtopach czy
komputerach przeno�nych, komputerach sterowanych przez jednor�kich,
za pomoc� joysticka, ekranu dotykowego, trackballa lub myszy albo bez
u�ycia r�k (poprzez �ledzenie ruch�w g�owy albo oczu). Wersja Dashera
�ledz�ca ruchy oczu pozwala do�wiadczonemu u�ytkownikowi pisa� tekst
z podobn� szybko�ci� do normalnego pisma - 25 s��w na minut�; przy
u�yciu myszy do�wiadczeni u�ytkownicy mog� pisa� nawet 39 s��w na
minut�.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f po/no.po

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

%post
/usr/bin/scrollkeeper-update -q

%postun
if [ $1 = 0 ]; then
	/usr/bin/scrollkeeper-update -q
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS README Doc/Colourschemes
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/%{name}.png
%{_mandir}/man1/%{name}*
%{_omf_dest_dir}/%{name}
