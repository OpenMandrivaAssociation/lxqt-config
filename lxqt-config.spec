#define git 0
Name: lxqt-config
Version:	2.2.0
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-config/releases/download/%{version}/lxqt-config-%{version}.tar.xz
%endif
Release:	%{?git:0.%{git}.}2
Source100: %{name}.rpmlintrc
Summary: Config panel for the LXQt desktop
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6SvgWidgets)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: cmake(qt6xdg)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Screen)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: zlib-devel
BuildRequires: cmake(lxqt-menu-data)
Requires: lxqt-menu-data
# distro rel... is provided by task-lxqt and by list omdv-...iso builder. No need to keep it here.
# causing problems with lxqt-wayland
#Recommends: distro-release-desktop-LXQt

%description
Config panel for the LXQt desktop.

%prep
%autosetup -p1 -n %{name}-%{?git:%{git}}%{!?git:%{version}}
%cmake \
	-DPULL_TRANSLATIONS=NO \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	-G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-locale
%{_bindir}/lxqt-config-monitor
%{_bindir}/lxqt-config-brightness
%{_libdir}/lxqt-config
%{_datadir}/applications/lxqt-config*.desktop
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/lxqt/icons/monitor.svg
%{_mandir}/man1/lxqt-config-appearance.1*
%{_mandir}/man1/lxqt-config-input.1.*
%{_mandir}/man1/lxqt-config.1*
