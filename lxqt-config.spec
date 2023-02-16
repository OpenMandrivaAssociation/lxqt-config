%define git 0
Name: lxqt-config
Version:	1.2.0
%if %git
Release:	0.%{git}.1
Source0: %{name}-%{git}.tar.xz
%else
Release:	3
Source0: https://github.com/lxqt/lxqt-config/releases/download/%{version}/lxqt-config-%{version}.tar.xz
%endif
Source100: %{name}.rpmlintrc
Summary: Config panel for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Source1: lxqt-config-appearance.conf
Patch0: https://github.com/lxqt/lxqt-config/pull/915.patch
# KScreen (used by lxqt-config) 5.27 needs C++ >= 17
# Might as well go to 20 while at it.
Patch1: lxqt-config-c++20.patch
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(lxqt)
BuildRequires: cmake(lxqt-build-tools)
BuildRequires: cmake(qt5xdg)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Screen) >= 5.6.0-2
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xorg-libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: zlib-devel
%rename lxqt-config-randr

%description
Config panel for the LXQt desktop.

%prep
%if %git
%autosetup -p1 -n %{name}-%{git}
%else
%autosetup -p1
%endif
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

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

mkdir -p %{buildroot}%{_datadir}/lxqt
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/lxqt/lxqt-config-appearance.conf

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%{_sysconfdir}/xdg/menus/lxqt-config.menu
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-locale
%{_bindir}/lxqt-config-monitor
%{_bindir}/lxqt-config-brightness
%{_libdir}/lxqt-config
%{_datadir}/lxqt/lxqt-config-appearance.conf
%{_datadir}/applications/lxqt-config*.desktop
%{_datadir}/desktop-directories
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/lxqt/icons/monitor.svg
%{_mandir}/man1/lxqt-config-appearance.1*
%{_mandir}/man1/lxqt-config-mouse.1*
%{_mandir}/man1/lxqt-config.1*
