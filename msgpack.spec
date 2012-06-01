%global mytarget  msgpack-git49d40a4


Name:           msgpack
Version:        0.5.7
Release:        1%{?dist}
Summary:        MessagePack, a binary-based efficient data interchange format

Group:          Development/Libraries
License:        Apache License V2.0
URL:            http://sourceforge.jp/projects/msgpack/
Source0:        %{mytarget}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{mytarget}-root-%(%{__id_u} -n)

BuildRequires:  ruby, libtool, automake

%description
MessagePack, a binary-based efficient data interchange format.
The speed of serializing deserializing is very high-speed,
and the data size after serializing becomes small, too.
It is very high-speed and compact though looks like JSON. 


%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the libraries and header files needed for developing with %{name}.

%prep
%setup -q -n %{mytarget}

%build
cd cpp
./bootstrap
%configure

make %{?_smp_mflags}

%install
cd cpp
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la


%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_libdir}/libmsgpack*.so.*


%files devel
%defattr(-, root, root, -)
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Jun  1 2012 Arkady L. Shane <ashejn@russianfedora.ru> 0.5.7-1.R
- initial build
