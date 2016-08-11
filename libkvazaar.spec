Name:           libkvazaar
Version:        0.8.3
Release:        1%{?dist}
Summary:        An open-source HEVC encoder

License:        LGPLv2.1
URL:            http://ultravideo.cs.tut.fi#encoder
Source0:        https://github.com/ultravideo/kvazaar/archive/v%{version}.tar.gz

BuildRequires:  yasm
BuildRequires:  autoconf

%description
An open-source HEVC encoder licensed under LGPLv2.1.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n kvazaar
Summary:        Kvazaar command line encoder

%description    -n kvazaar
This package provides Kvazaar command line encoder program.


%prep
%setup -q -n kvazaar-%{version}


%build
autoreconf -fvi
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{_datadir}/doc/


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING CREDITS README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n kvazaar
%{_bindir}/*


%changelog
* Thu Aug 11 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.8.3-1
- Public release
