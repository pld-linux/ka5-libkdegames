#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		qtver		5.15.2
%define		kaname		libkdegames
Summary:	Libkdegames
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	61de93d0acc98ad868c85b5d11ac9526
URL:		http://www.kde.org/
BuildRequires:	OpenAL-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdnssd-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	libsndfile-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Base library common to many KDE games.

%description -l pl.UTF-8
Bazowa biblioteka wspólna dla wielu gier KDE.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libKF5KDEGames.so.7
%attr(755,root,root) %{_libdir}/libKF5KDEGames.so.*.*.*
%ghost %{_libdir}/libKF5KDEGamesPrivate.so.7
%attr(755,root,root) %{_libdir}/libKF5KDEGamesPrivate.so.*.*.*
%{_libdir}/qt5/qml/org/kde/games/core/KgItem.qml
%dir %{_libdir}/qt5/qml/org/kde/games
%dir %{_libdir}/qt5/qml/org/kde/games/core
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/games/core/libcorebindingsplugin.so
%{_libdir}/qt5/qml/org/kde/games/core/qmldir
%{_datadir}/carddecks
%{_datadir}/kconf_update/kgthemeprovider-migration.upd
%{_datadir}/qlogging-categories5/libkdegames.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KDEGames
%{_libdir}/cmake/KF5KDEGames
%{_libdir}/libKF5KDEGames.so
%{_libdir}/libKF5KDEGamesPrivate.so
