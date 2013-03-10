Name:		ocaml-pcre
Version:	7.0.2
Release:	1
Summary:	Perl compatibility regular expressions for OCaml
Source: 	http://bitbucket.org/mmottl/pcre-ocaml/downloads/pcre-ocaml-%{version}.tar.gz
# curl http://hg.ocaml.info/release/pcre-ocaml/archive/release-%{version}.tar.bz2 > pcre-ocaml-release-%{version}.tar.bz2
URL:		http://ocaml.info/home/ocaml_sources.html#pcre-ocaml
Patch0:		pcre-ocaml-examples-makefile.patch
License:	LGPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	pcre-devel
BuildRequires:  ocaml-findlib
BuildRequires:  texlive
Conflicts:      %{name}-devel < 5.12.2

%description
This OCaml-library interfaces the PCRE (Perl-compatibility regular
expressions) library which is written in C. it can be used for matching
regular expressions which are written in "PERL"-style.
  
Searching for, replacing or splitting text should become much easier with
this library.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	pcre-devel
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n pcre-ocaml-release-%{version}
%patch0 -p1

%build
%make
%make doc

%install
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml"

%files
%defattr(-,root,root)
%doc Changelog INSTALL LICENSE README.txt
%dir %{_libdir}/ocaml/pcre
%{_libdir}/ocaml/pcre/*.cmi
%{_libdir}/ocaml/pcre/*.cma
%{_libdir}/ocaml/pcre/META
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/pcre/html
%doc doc/pcre/latex/*.{dvi,pdf}
%doc examples/
%{_libdir}/ocaml/pcre/*.a
%{_libdir}/ocaml/pcre/*.cmxa
%{_libdir}/ocaml/pcre/*.mli


%changelog
* Fri Sep 16 2011 Alexandre Lissy <alissy@mandriva.com> 6.2.2-1
+ Revision: 700009
- Updating BuildRequires for texlive
  Removing %%mkrel
- Updating to latest 6.2.2 release

* Wed Apr 14 2010 Florent Monnier <blue_prawn@mandriva.org> 6.1.0-1mdv2011.0
+ Revision: 534831
- updated to version 6.1.0

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.1-6mdv2010.1
+ Revision: 496243
- rebuild

* Fri Sep 11 2009 Florent Monnier <blue_prawn@mandriva.org> 6.0.1-5mdv2010.0
+ Revision: 438502
- corrected the license field for LGPL

* Fri Sep 04 2009 Florent Monnier <blue_prawn@mandriva.org> 6.0.1-4mdv2010.0
+ Revision: 430978
- added the examples, with patched makefiles

* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 6.0.1-3mdv2010.0
+ Revision: 415791
- buildrequires latex
- increm mkrel
- added documentation, and .so.owner

* Tue Jul 28 2009 Florent Monnier <blue_prawn@mandriva.org> 6.0.1-2mdv2010.0
+ Revision: 401387
- updated version

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.0-2mdv2010.0
+ Revision: 389825
- rebuild

* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 6.0.0-1mdv2010.0
+ Revision: 385090
- updated version

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.15.1-1mdv2009.1
+ Revision: 318326
- new version
- move non-devel files in main package
- site-lib hierarchy doesn't exist anymore

* Tue Dec 09 2008 Pixel <pixel@mandriva.com> 5.15.0-2mdv2009.1
+ Revision: 312238
- rebuild

* Thu Sep 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.15.0-1mdv2009.0
+ Revision: 280408
- update to new version 5.15.0

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.14.0-1mdv2009.0
+ Revision: 272042
- update to new version 5.14.0

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 5.12.2-4mdv2009.0
+ Revision: 254345
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.12.2-2mdv2008.1
+ Revision: 178369
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.12.2-1mdv2008.0
+ Revision: 78165
- add conflict to help upgrade
- new version
- fix interdependencies
  swap stubs libs into non-devel package

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.11.4-2mdv2008.0
+ Revision: 77623
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Thu Jun 07 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 5.11.4-1mdv2008.0
+ Revision: 36707
- new release: 5.11.4

