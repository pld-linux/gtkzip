%define ver      0.5.1
%define prefix   /usr

Summary: program for maintaining your Zip drive disks
Name: gtkzip
Version: 0.5.1
Release: 1
Copyright: GPL
Packager: KaYue Mak <gtkzip@yahoo.com>
Vendor: KaYue Mak <gtkzip@yahoo.com>
Group: X11/Applications/
Source: http://home.netvigator.com/~sallymak/gtkzip/gtkzip-%{ver}.src.tar.gz 
BuildRoot: /tmp/%{name}-%{version}-root
URL: http://home.netvigator.com/~sallymak/gtkzip/

%description
GtkZip is a program for maintaining your 
Iomega Zip drive disks under Linux.  
This program is based on a command 
line program ziptool, and is written 
fully in c using the GTK widget set.

%prep
%setup

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
cp ./src/gtkzip $RPM_BUILD_ROOT/usr/bin/gtkzip

%files
%doc AUTHORS COPYING ChangeLog NEWS README
/usr/bin/gtkzip
