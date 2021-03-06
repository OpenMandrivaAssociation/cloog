%define major 4
%define libname %mklibname %{name}-isl %{major}
%define devname %mklibname -d %{name}-isl
%define debug_package %{nil}
%define _disable_rebuild_configure 1

Summary:	The Chunky Loop Generator
Name:		cloog
Version:	0.20.0
Release:	3
Group:		System/Libraries
License:	GPLv2+
Url:		http://www.cloog.org
Source0:	https://github.com/periscop/cloog/releases/download/cloog-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(isl)

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package -n %{libname}
Summary:	Integer Set Library backend (isl) based version of the CLooG binaries
Group:		Development/C
Obsoletes:	%{_lib}cloog4 < 0.18.0-2

%description -n %{libname}
The dynamic shared libraries of the Chunky Loop Generator.

%package -n %{devname}
Summary:	Development tools for the isl based version of Chunky Loop Generator
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}cloog-devel < 0.18.0-2
Obsoletes:	%{_lib}cloog-static-devel < 0.18.0-2

%description -n %{devname}
The header files and .so link of the Chunky Loop Generator.

%prep
%autosetup -p1
# FIXME ugly hack: We make sure configure won't find
# texi2dvi because the docs don't build (and not
# having texi2dvi is the only way to tell it not
# to build docs)
sed -i -e 's,texi2dvi,broken-texi2dvi,g' configure.ac configure

%build
%configure \
	--with-isl=system \
	--with-bits=gmp \
	--enable-portable-binary

%make_build

%install
%make_install

%files
%{_bindir}/cloog

%files -n %{libname}
%{_libdir}/libcloog-isl.so.%{major}*

%files -n %{devname}
%{_includedir}/cloog
%{_libdir}/libcloog-isl.so
%{_libdir}/pkgconfig/cloog-isl.pc
%{_libdir}/isl
%{_libdir}/cloog-isl
