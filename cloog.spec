%define		major		4
%define		libname		%mklibname %name %{major}
%define		libnamedev	%mklibname -d %name
%define		staticdev	%mklibname -d -s %name

Name:		cloog
Version:	0.18.0
Release:	1
Summary:	The Chunky Loop Generator

Group:		System/Libraries
License:	GPLv2+
URL:		http://www.cloog.org
Source0:	http://www.bastoul.net/cloog/pages/download/cloog-%version.tar.gz
Patch0:		cloog-0.18.0-automake-1.13.patch
BuildRequires:	gmp-devel pkgconfig(isl)

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package -n %{libname}
Summary:	Integer Set Library backend (isl) based version of the CLooG binaries
Group:		Development/C

%description -n %{libname}
The dynamic shared libraries of the Chunky Loop Generator

%package -n %{libnamedev}
Summary:	Development tools for the isl based version of Chunky Loop Generator
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	gmp-devel pkgconfig(isl)
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
The header files and .so link of the Chunky Loop Generator.

%package -n %staticdev
Summary:	Static library for the isl based version of the Chunky Loop Generator
Group:		Development/C
Requires:	%libnamedev = %version-%release

%description -n %staticdev
Static library for the isl based version of the Chunky Loop Generator

%prep
%setup -q
%apply_patches
aclocal
automake -a
autoconf

%build
%configure --with-isl=system --with-bits=gmp
%make

%install
%makeinstall_std

%files
%{_bindir}/cloog

%files -n %{libname}
%{_libdir}/libcloog-isl.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/cloog
%{_libdir}/libcloog-isl.so
%{_libdir}/pkgconfig/cloog-isl.pc

%files -n %staticdev
%_libdir/*.a
