Summary:	Intrusive Red-Black Tree Collection
Name:		c-rbtree
Version:	3.2.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-rbtree/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b4caf4891956670708d81cad3f07b7dc
URL:		https://c-util.github.io/c-rbtree/
BuildRequires:	c-stdaux-devel >= 1.5.0
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-rbtree project implements an intrusive collection based on
red-black trees in ISO-C11. Its API guarantees the user full control
over its data-structures, and rather limits itself to just the
tree-specific rebalancing and coloring operations.

%package devel
Summary:	Header files for c-rbtree library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for c-rbtree library.

%package static
Summary:	Static c-rbtree library
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static c-rbtree library.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_libdir}/libcrbtree-3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcrbtree-3.so
%{_includedir}/c-rbtree.h
%{_pkgconfigdir}/libcrbtree-3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcrbtree-3.a
