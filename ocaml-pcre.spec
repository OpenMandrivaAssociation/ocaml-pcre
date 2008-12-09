%define name	ocaml-pcre
%define version	5.15.0
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl compatibility regular expressions for OCaml
Source: 	http://www.ocaml.info/ocaml_sources/pcre-ocaml-%{version}.tar.bz2
URL:		http://www.ocaml.info/home/ocaml_sources.html
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	pcre-devel
BuildRequires:  findlib
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

%files
%defattr(-,root,root)
%doc Changes INSTALL LICENSE README VERSION
%dir %{ocaml_sitelib}/pcre
%{ocaml_sitelib}/pcre/*.cmi
%{ocaml_sitelib}/stublibs/dllpcre_stubs.so

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/pcre/*
%exclude %{ocaml_sitelib}/pcre/*.cmi
