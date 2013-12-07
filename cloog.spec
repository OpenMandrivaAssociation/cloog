%define major 4
%define libname %mklibname %{name}-isl %{major}
%define devname %mklibname -d %{name}-isl

Summary:	The Chunky Loop Generator
Name:		cloog
Version:	0.18.0
Release:	6
Group:		System/Libraries
License:	GPLv2+
Url:		http://www.cloog.org
Source0:	http://www.bastoul.net/cloog/pages/download/%{name}-%{version}.tar.gz
Patch0:		cloog-0.18.0-automake-1.13.patch
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
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--with-isl=system \
	--with-bits=gmp

%make

%install
%makeinstall_std

%files
%{_bindir}/cloog

%files -n %{libname}
%{_libdir}/libcloog-isl.so.%{major}*

%files -n %{devname}
%{_includedir}/cloog
%{_libdir}/libcloog-isl.so
%{_libdir}/pkgconfig/cloog-isl.pc

