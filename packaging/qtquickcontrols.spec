# Package prefix
%define pkgname qt5-qtquickcontrols

Name:       qtquickcontrols
Summary:    QtQuick Controls
Version:    5.3.2
Release:    1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.io
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the QtQuick Controls library.


%package -n qt5-qtquickcontrols
Summary:    QtQuick Controls
Group:      Qt/Qt

%description -n qt5-qtquickcontrols
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.

This package contains the QtQuick Controls library.


%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git # To make sure syncqt is used

%qmake5 CONFIG+=package
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install


%post -n qt5-qtquickcontrols
/sbin/ldconfig
%postun -n qt5-qtquickcontrols
/sbin/ldconfig


%files -n qt5-qtquickcontrols
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/*
