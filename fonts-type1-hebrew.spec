%define name fonts-type1-hebrew
%define version 0.101
%define release %mkrel 8

Summary:	Hebrew Type1 fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/Type1
URL:		http://culmus.sourceforge.net/
Source:		http://belnet.dl.sourceforge.net/sourceforge/culmus/culmus-%{version}.tar.bz2
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools, t1utils
Requires(post): fontconfig
Requires(postun): fontconfig
# Added to avoid conflicts with the official RPM released by Culmus project
Conflicts:	culmus-fonts

%description
This Package provides Free Hebrew Type1 fonts, courtesy of the Culmus project.

Since version 0.100 all default sizes have been reduced and names have been
changed. Once you install this version or a later one, all letters in your
documents will shrink and a manual tuning will be needed in most cases.

%prep

%setup -q -n culmus-%{version}

%build
for i in *.pfa ; do 
  t1binary $i `basename $i .pfa`.pfb
done 
sed -i -e '1,$s/\.pfa/.pfb/' fonts.scale

%install
rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/type1/hebrew/
install -m 0644 *.pfb %buildroot/%_datadir/fonts/type1/hebrew
install -m 0644 *.afm %buildroot/%_datadir/fonts/type1/hebrew
install -m 0644 fonts.alias %buildroot/%_datadir/fonts/type1/hebrew
install -m 0644 fonts.scale %buildroot/%_datadir/fonts/type1/hebrew
# Added for version 0.100
mkdir -p %buildroot/%_sysconfdir/fonts/conf.d
mkdir -p %buildroot/%_sysconfdir/fonts/conf.avail
install -m 0644 culmus.conf %buildroot/%_sysconfdir/fonts/conf.avail/01-culmus.conf
ln -s %_sysconfdir/fonts/conf.avail/01-culmus.conf %buildroot/%_sysconfdir/fonts/conf.d/01-culmus.conf

(
cd %buildroot/%_datadir/fonts/type1/hebrew/
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/type1/hebrew \
    %{buildroot}%_sysconfdir/X11/fontpath.d/type1-hebrew:pri=50

%post
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc CHANGES LICENSE LICENSE-BITSTREAM GNU-GPL
%_datadir/fonts/type1/hebrew
# Added for version 0.100
%_sysconfdir/fonts/conf.d/01-culmus.conf
%_sysconfdir/fonts/conf.avail/01-culmus.conf
%_sysconfdir/X11/fontpath.d/type1-hebrew:pri=50

