%define		kdeappsver	17.08.2
%define		qtver		5.3.2
%define		kaname		libkdegames
Summary:	Libkdegames
Name:		ka5-%{kaname}
Version:	17.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	cb227de78ac3369551933bd9f017bef0
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libkdegames.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libKF5KDEGames.so.7
%attr(755,root,root) %{_libdir}/libKF5KDEGames.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KDEGamesPrivate.so.1
%attr(755,root,root) %{_libdir}/libKF5KDEGamesPrivate.so.*.*.*
%{_libdir}/qt5/qml/org/kde/games/core/KgItem.qml
%dir %{_libdir}/qt5/qml/org/kde/games
%dir %{_libdir}/qt5/qml/org/kde/games/core
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/games/core/libcorebindingsplugin.so
%{_libdir}/qt5/qml/org/kde/games/core/qmldir
%{_datadir}/carddecks
%{_datadir}/kconf_update/kgthemeprovider-migration.upd

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KF5KDEGames
%{_libdir}/cmake/KF5KDEGames
%attr(755,root,root) %{_libdir}/libKF5KDEGames.so
%attr(755,root,root) %{_libdir}/libKF5KDEGamesPrivate.so
