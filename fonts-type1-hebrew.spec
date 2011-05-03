%define name fonts-type1-hebrew
%define version 0.120
%define release %mkrel 2

Summary:	Hebrew Type1 fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/Type1
URL:		http://culmus.sourceforge.net/
Source:		http://belnet.dl.sourceforge.net/sourceforge/culmus/culmus-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools, t1utils
# Added to avoid conflicts with the official RPM released by Culmus project
Conflicts:	culmus-fonts

%description
This Package provides free Hebrew Type1 fonts, courtesy of the Culmus project.

Since version 0.100, all default sizes have been reduced and names have been
changed. Once you install this version or a later one, all letters in your
documents will shrink; manual tuning may therefore be necessary.

%prep

%setup -q -n culmus-%{version}

%build
for i in *.pfa ; do 
  t1binary $i `basename $i .pfa`.pfb
done 
sed -i -e '1,$s/\.pfa/.pfb/' fonts.scale-type1

%install
%__rm -fr %buildroot

mkdir -p %buildroot/%_datadir/fonts/Type1/hebrew/
mkdir -p %buildroot/%_datadir/fonts/TTF/hebrew/
%__install -m 0644 *.pfb %buildroot/%_datadir/fonts/Type1/hebrew
%__install -m 0644 *.afm %buildroot/%_datadir/fonts/Type1/hebrew
%__install -m 0644 *.ttf %buildroot/%_datadir/fonts/TTF/hebrew
%__install -m 0644 fonts.scale-type1 %buildroot/%_datadir/fonts/Type1/hebrew/fonts.scale
%__install -m 0644 fonts.scale-ttf %buildroot/%_datadir/fonts/TTF/hebrew/fonts.scale
# Added for version 0.100
mkdir -p %buildroot/%_sysconfdir/fonts/conf.d
mkdir -p %buildroot/%_sysconfdir/fonts/conf.avail
%__install -m 0644 culmus.conf %buildroot/%_sysconfdir/fonts/conf.avail/01-culmus.conf
ln -s %_sysconfdir/fonts/conf.avail/01-culmus.conf %buildroot/%_sysconfdir/fonts/conf.d/01-culmus.conf

(
cd %buildroot/%_datadir/fonts/Type1/hebrew/
cp fonts.scale fonts.dir
)
(
cd %buildroot/%_datadir/fonts/TTF/hebrew/
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/Type1/hebrew \
    %{buildroot}%_sysconfdir/X11/fontpath.d/Type1-hebrew:pri=50
ln -s ../../..%_datadir/fonts/TTF/hebrew \
    %{buildroot}%_sysconfdir/X11/fontpath.d/TTF-hebrew:pri=50

%clean
%__rm -fr %buildroot

%files
%defattr(0644,root,root,0755)
%doc CHANGES LICENSE LICENSE-BITSTREAM GNU-GPL
%_datadir/fonts/Type1/hebrew
%_datadir/fonts/TTF/hebrew
# Added for version 0.100
%_sysconfdir/fonts/conf.d/01-culmus.conf
%_sysconfdir/fonts/conf.avail/01-culmus.conf
%_sysconfdir/X11/fontpath.d/Type1-hebrew:pri=50
%_sysconfdir/X11/fontpath.d/TTF-hebrew:pri=50
