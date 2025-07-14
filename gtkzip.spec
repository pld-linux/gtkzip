Summary:	Program for maintaining your Zip drive disks
Summary(pl.UTF-8):	Program zarządzający napędami Zip
Name:		gtkzip
Version:	0.5.1
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	%{name}-%{version}.src.tar.gz
# Source0-md5:	54b8f902e3bdc94f52f557b2085cff6e
Patch0:		%{name}-config.patch
Patch1:		%{name}-ac_am.patch
# no longer valid
#URL:		http://smallpig.net/gtkzip/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdbm-devel
BuildRequires:	gtk+-devel >= 1.0.6
BuildRequires:	imlib-devel >= 1.8.1
BuildRequires:	libgtop-devel >= 1.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkZip is a program for maintaining your Iomega Zip drive disks under
Linux. This program is based on a command line program ziptool, and is
written fully in C using the GTK+ widget set.

%description -l pl.UTF-8
GtkZip jest programem do zarządzania napędami Iomega Zip pod Linuksem.
Program ten jest oparty na programie ziptool, został napisany w
całości w C, z wykorzystaniem biblioteki GTK+.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/gtkzip.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gtkzip
%{_pixmapsdir}/gtkzip.xpm
