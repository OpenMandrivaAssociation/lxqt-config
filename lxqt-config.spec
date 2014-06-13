Name: lxqt-config
Version: 0.7.0
Release: 2
Source0: http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: Config panel for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: cmake(lxqt)
BuildRequires: qt4-devel
BuildRequires: pkgconfig(xcursor)

%description
Config panel for the LXQt desktop

%prep
%setup -q -c %{name}-%{version}
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_sysconfdir}/xdg/menus/lxqt-config.menu
%{_bindir}/lxqt-config
%{_bindir}/lxqt-config-input
%{_bindir}/lxqt-config-appearance
%{_bindir}/lxqt-config-file-associations
%{_libdir}/lib*.so
%{_datadir}/applications/lxqt-config*.desktop
%{_datadir}/lxqt/lxqt-config
