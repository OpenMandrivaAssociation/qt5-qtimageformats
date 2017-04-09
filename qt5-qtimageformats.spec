%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta beta

%define qtimageformats_d %mklibname qt%{major}imageformats -d

Name:		qt5-qtimageformats
Version:	5.9.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtimageformats-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtimageformats-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libmng)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(jasper)


%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%_qt5_plugindir/imageformats/*.so

#------------------------------------------------------------------------------
%package -n	%{qtimageformats_d}
Summary:	Devel files needed to build apps based on QtImageFormats
Group:		Development/KDE and Qt
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{qtimageformats_d}
Devel files needed to build apps based on QtImageFormats.

%files -n	%{qtimageformats_d}
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QMngPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake
%{_qt5_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5

#------------------------------------------------------------------------------
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
