Summary: 	Program for maintaining your Zip drive disks
Summary(pl):	Program zarz±dzaj±cy napêdami Zip
Name: 		gtkzip
Version: 	0.5.1
Release: 	2
Copyright: 	GPL
Group: 		X11/Utilities
Group(pl):	X11/Narzêdzia
Source: 	http://home.netvigator.com/~sallymak/gtkzip/%{name}-%{version}.src.tar.gz
Icon:		gtkzip.xpm
Patch:		gtkzip-config.patch
URL: 		http://home.netvigator.com/~sallymak/gtkzip/
BuildRequires:	gtk+-devel >= 1.0.6
BuildRequires:	imlib-devel >= 1.8.1
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	gdbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description
GtkZip is a program for maintaining your Iomega Zip drive disks under Linux.  
This program is based on a command line program ziptool, and is written 
fully in C using the GTK widget set.

%description -l pl
GtkZip jest programem do zarz±dzania napêdami Iomega Zip pod Linuxem.
Program ten jest oparty na programie ziptool, zosta³ napisany w ca³o¶ci 
w C, z wykorzystaniem biblioteki GTK.

%prep
%setup -q
%patch -p0

%build
autoconf
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

install icon.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/gtkzip.xpm

gzip -9nf AUTHORS COPYING ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/gtkzip
%{_datadir}/pixmaps/gtkzip.xpm
