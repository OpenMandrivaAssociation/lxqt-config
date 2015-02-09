%define git 0
Name: lxqt-config
Version: 0.9.0
%if %git
Release: 0.%git.1
Source0: %{name}-%{git}.tar.xz
%else
Release: 1
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
%endif
Source100: %{name}.rpmlintrc
Summary: Config panel for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: qt5-devel
BuildRequires: pkgconfig(xcursor)
Requires:	   system-tools-backends2

%description
Config panel for the LXQt desktop.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%cmake -DUSE_QT5:BOOL=ON

%build
%make -C build

%install
%makeinstall_std -C build

%files
%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
%dir %{_datadir}/lxqt/translations/lxqt-config-input
%dir %{_datadir}/lxqt/translations/lxqt-config-monitor
%dir %{_datadir}/lxqt/translations/lxqt-config
%{_sysconfdir}/xdg/menus/lxqt-config.menu
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-monitor
%{_libdir}/lib*.so
%{_datadir}/lxqt/applications/lxqt-config*.desktop
%{_datadir}/lxqt/translations/lxqt-config-appearance/*
%{_datadir}/lxqt/translations/lxqt-config-cursor/*
%{_datadir}/lxqt/translations/lxqt-config-file-associations/*
%{_datadir}/lxqt/translations/lxqt-config-input/*
%{_datadir}/lxqt/translations/lxqt-config-monitor/*
%{_datadir}/lxqt/translations/lxqt-config/*
