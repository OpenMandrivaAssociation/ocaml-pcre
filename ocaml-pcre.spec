%define name	ocaml-pcre
%define version	5.11.2
%define release	%mkrel 5
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl compatibility regular expressions for OCaml
Source: 	http://www.ocaml.info/ocaml_sources/pcre-ocaml-5.11.2.tar.bz2
URL:		http://www.ocaml.info/home/ocaml_sources.html
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	pcre-devel
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This OCaml-library interfaces the PCRE (Perl-compatibility regular
expressions) library which is written in C. it can be used for matching
regular expressions which are written in "PERL"-style.
  
Searching for, replacing or splitting text should become much easier with
this library.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:   pcre-devel
Obsoletes:  %{name}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n pcre-ocaml-%{version}

%build
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc Changes INSTALL LICENSE README VERSION
%{ocaml_sitelib}/pcre
%{ocaml_sitelib}/stublibs/dllpcre_stubs.so


