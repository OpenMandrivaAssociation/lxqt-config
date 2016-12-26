%define git 0
Name: lxqt-config
Version: 0.11.0
%if %git
Release: 1.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 3
Source0: https://github.com/lxde/%{name}/archive/%{name}-%{version}.tar.xz
%endif
Source100: %{name}.rpmlintrc
Summary: Config panel for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
Patch0: lxqt-config-0.11.0-use-lxqt-build-tools.patch
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
BuildRequires: zlib-devel
Requires: lxqt-l10n
%rename lxqt-config-randr

%description
Config panel for the LXQt desktop.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%apply_patches
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

%files
%{_sysconfdir}/xdg/qt5/menus/lxqt-config.menu
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
