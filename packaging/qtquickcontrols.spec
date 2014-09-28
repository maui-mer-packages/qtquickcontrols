Name:       qt5-qtquickcontrols
Summary:    QtQuick Controls
Version:    5.1.0
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains the QtQuick Controls library.



#### Build section

%prep
%setup -q -n %{name}-%{version}/upstream

%build
export QTDIR=/usr/share/qt5
touch .git # To make sure syncqt is used

%qmake5 CONFIG+=package
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/*
