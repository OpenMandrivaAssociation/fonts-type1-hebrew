Summary:	Hebrew Type1 fonts
Name:		fonts-type1-hebrew
Version:	0.120
Release:	5
License:	GPLv2
Group:		System/Fonts/Type1
Url:		http://culmus.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/culmus/culmus-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
BuildRequires:	t1utils
# Added to avoid conflicts with the official RPM released by Culmus project

%description
This Package provides free Hebrew Type1 fonts, courtesy of the Culmus project.

Since version 0.100, all default sizes have been reduced and names have been
changed. Once you install this version or a later one, all letters in your
documents will shrink; manual tuning may therefore be necessary.

%prep
%setup -qn culmus-%{version}

%build
for i in *.pfa ; do 
	t1binary $i `basename $i .pfa`.pfb
done 
sed -i -e '1,$s/\.pfa/.pfb/' fonts.scale-type1

%install
mkdir -p %{buildroot}/%{_datadir}/fonts/Type1/hebrew/
mkdir -p %{buildroot}/%{_datadir}/fonts/TTF/hebrew/
install -m 0644 *.pfb %{buildroot}/%{_datadir}/fonts/Type1/hebrew
install -m 0644 *.afm %{buildroot}/%{_datadir}/fonts/Type1/hebrew
install -m 0644 *.ttf %{buildroot}/%{_datadir}/fonts/TTF/hebrew
install -m 0644 fonts.scale-type1 %{buildroot}/%{_datadir}/fonts/Type1/hebrew/fonts.scale
install -m 0644 fonts.scale-ttf %{buildroot}/%{_datadir}/fonts/TTF/hebrew/fonts.scale
# Added for version 0.100
mkdir -p %{buildroot}/%{_sysconfdir}/fonts/conf.d
mkdir -p %{buildroot}/%{_sysconfdir}/fonts/conf.avail
install -m 0644 culmus.conf %{buildroot}/%{_sysconfdir}/fonts/conf.avail/01-culmus.conf
ln -s %{_sysconfdir}/fonts/conf.avail/01-culmus.conf %{buildroot}/%{_sysconfdir}/fonts/conf.d/01-culmus.conf

(
cd %{buildroot}/%{_datadir}/fonts/Type1/hebrew/
cp fonts.scale fonts.dir
)
(
cd %{buildroot}/%{_datadir}/fonts/TTF/hebrew/
cp fonts.scale fonts.dir
)

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/Type1/hebrew \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/Type1-hebrew:pri=50
ln -s ../../..%{_datadir}/fonts/TTF/hebrew \
	%{buildroot}%{_sysconfdir}/X11/fontpath.d/TTF-hebrew:pri=50

%files
%doc CHANGES LICENSE LICENSE-BITSTREAM GNU-GPL
%{_datadir}/fonts/Type1/hebrew
%{_datadir}/fonts/TTF/hebrew
# Added for version 0.100
%{_sysconfdir}/fonts/conf.d/01-culmus.conf
%{_sysconfdir}/fonts/conf.avail/01-culmus.conf
%{_sysconfdir}/X11/fontpath.d/Type1-hebrew:pri=50
%{_sysconfdir}/X11/fontpath.d/TTF-hebrew:pri=50

