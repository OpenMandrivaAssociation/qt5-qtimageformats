%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %{nil}

%define qtimageformats_d %mklibname qt%{major}imageformats -d

# filter plugin provides
%define __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$

Name:		qt5-qtimageformats
Version:	5.15.9
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtimageformats-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtimageformats-everywhere-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
# From KDE
Patch1000:	0001-Add-some-basic-checking-against-corrupt-input.patch
Patch1001:	0002-Check-earlier-to-avoid-sanitzer-warnings.patch
Patch1002:	0003-jp2-use-correct-buffer_size-for-jas_stream_memopen.patch
Patch1003:	0004-jp2-use-new-APIs-for-jasper-3.patch
Patch1004:	0005-Reject-tiled-tiffs-with-corrupt-tile-size-early.patch
Patch1005:	0006-webp-support-sequential-input-device-if-full-file-is.patch
Patch1006:	0007-Explicitly-include-QVarLengthArray-header.patch
Patch1007:	0008-Implement-support-for-file-memory-mapping-for-tiff-r.patch
Patch1008:	0009-TGA-Plugin-Fix-reading-of-CMapDepth.patch
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qt5-qtbase-devel = %{version}
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libmng)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libwebpmux)
BuildRequires:	pkgconfig(libwebpdemux)
BuildRequires:	pkgconfig(jasper)
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

%files
%{_qt5_plugindir}/imageformats/*.so

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
%autosetup -n %(echo %qttarballdir|sed -e 's,-opensource,,') -p1

%build
%qmake_qt5

#------------------------------------------------------------------------------
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
