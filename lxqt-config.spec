%define git 20140803
Name: lxqt-config
Version: 0.8.0
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
BuildRequires: cmake(lxqt-qt5)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires: qt5-devel
BuildRequires: pkgconfig(xcursor)

%description
Config panel for the LXQt desktop

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q -c %{name}-%{version}
%endif
%cmake -DUSE_QT5:BOOL=ON

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
