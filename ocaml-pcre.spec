%define name	ocaml-pcre
%define version	6.0.1
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl compatibility regular expressions for OCaml
Source: 	http://hg.ocaml.info/release/pcre-ocaml/archive/pcre-ocaml-release-%{version}.tar.bz2
# curl http://hg.ocaml.info/release/pcre-ocaml/archive/release-%{version}.tar.bz2 > pcre-ocaml-release-%{version}.tar.bz2
URL:		http://ocaml.info/home/ocaml_sources.html#pcre-ocaml
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	pcre-devel
BuildRequires:  ocaml-findlib
Conflicts:      %{name}-devel < 5.12.2
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%build
%make
%make doc

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml"

%clean
rm -rf %{buildroot}

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
%{_libdir}/ocaml/pcre/*.a
%{_libdir}/ocaml/pcre/*.cmxa
%{_libdir}/ocaml/pcre/*.mli
