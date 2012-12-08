%define name fonts-type1-hebrew
%define version 0.120
%define release %mkrel 5

Summary:	Hebrew Type1 fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/Type1
URL:		http://culmus.sourceforge.net/
Source:		http://belnet.dl.sourceforge.net/sourceforge/culmus/culmus-%{version}.tar.gz
BuildArch:	noarch
BuildRequires: fontconfig
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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.120-4mdv2011.0
+ Revision: 675434
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.120-3
+ Revision: 675193
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.120-2
+ Revision: 664343
- mass rebuild

* Thu Nov 25 2010 Jani Välimaa <wally@mandriva.org> 0.120-1mdv2011.0
+ Revision: 601156
- new version 0.120

* Tue Nov 09 2010 Jani Välimaa <wally@mandriva.org> 0.110-1mdv2011.0
+ Revision: 595463
- new version 0.110

* Tue Aug 31 2010 Lev Givon <lev@mandriva.org> 0.105-1mdv2011.0
+ Revision: 574862
- Update to 0.105.

* Sun Feb 07 2010 Lev Givon <lev@mandriva.org> 0.104-1mdv2010.1
+ Revision: 501553
- Update to 0.104.

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.103-2mdv2010.1
+ Revision: 494130
- fc-cache is now called by an rpm filetrigger

* Mon Mar 23 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.103-1mdv2009.1
+ Revision: 360574
- Updated to version 0.103
- Install Type1 fonts at /usr/share/fonts/Type1/... instead of
  /usr/share/fonts/type1/...
- Install new TTF fonts at /usr/share/fonts/TTF/hebrew

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.101-10mdv2009.1
+ Revision: 351152
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.101-9mdv2009.0
+ Revision: 220959
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.101-8mdv2008.1
+ Revision: 170840
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.101-7mdv2008.1
+ Revision: 150077
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 23 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.101-6mdv2008.0
+ Revision: 54815
- use type1/ as the destination dir, not Type1/
  (minor font paths cleanup)

* Thu Jul 05 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.101-5mdv2008.0
+ Revision: 48749
- fontpath.d conversion (#31756)
- minor cleanups

* Thu Jun 14 2007 Adam Williamson <awilliamson@mandriva.org> 0.101-4mdv2008.0
+ Revision: 39788
- we use /usr/share/fonts/Type1, not /usr/share/fonts/type1

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 0.101-3mdv2008.0
+ Revision: 18893
- rebuild for new era
- install conf to conf.avail and link to conf.d per policy
- clean spec


* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.101-2mdk
- Don't package fonts.cache-2 file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

* Sat Feb 19 2005 Pablo Saratxaga <pablo@mandrakesoft.com> 0.101-1mdk
- new version (solves bug #2295 with "tet" letter)

* Tue Jan 11 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.100-6mdk 
- use /etc/fonts/conf.d to store culmus.conf file

* Tue Aug 10 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.100-5mdk
- converted to binary  format

* Mon Aug 09 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.100-4mdk
- spec file cleanup

* Tue Jun 15 2004 Dovix <dovix2003@yahoo.com> 0.100-3mdk
- Avoid conflicts with the official RPM released by Culmus project

* Sun Jun 13 2004 Dovix <dovix2003@yahoo.com> 0.100-2mdk
- update to 0.10.0
- This major release introduces two new typefaces: Miriam and Yehuda
 and removed the Ktav Yad font. It also reduces the size of most
 fonts to make them closer to the corresponding Windows/Mac fonts

* Sun Apr 11 2004 Dovix <dovix2003@yahoo.com> 0.9.3-1mdk
- update to 0.9.3

* Fri Oct 10 2003 nadav mavor <nadav@mavor.com> 0.9.0-1mdk
- update to 0.9 and add 2 more new fonts

* Wed Jul 23 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 0.8-1mdk
- first release

