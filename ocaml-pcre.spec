Summary:	Perl compatibility regular expressions for OCaml
Name:		ocaml-pcre
Version:	7.0.2
Release:	3
License:	LGPLv2.1+
Group:		Development/Other
Url:		https://ocaml.info/home/ocaml_sources.html#pcre-ocaml
# curl http://hg.ocaml.info/release/pcre-ocaml/archive/release-%{version}.tar.bz2 > pcre-ocaml-release-%{version}.tar.bz2
Source0:	http://bitbucket.org/mmottl/pcre-ocaml/downloads/pcre-ocaml-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	texlive
BuildRequires:	pkgconfig(libpcre)

%description
This OCaml-library interfaces the PCRE (Perl-compatibility regular
expressions) library which is written in C. it can be used for matching
regular expressions which are written in "PERL"-style.

Searching for, replacing or splitting text should become much easier with
this library.

%files
%doc README.md COPYING.txt AUTHORS.txt CHANGES.txt
%dir %{_libdir}/ocaml/pcre
%{_libdir}/ocaml/pcre/*.cmi
%{_libdir}/ocaml/pcre/*.cma
%{_libdir}/ocaml/pcre/*.cmxs
%{_libdir}/ocaml/pcre/META
%{_libdir}/ocaml/stublibs/*.so*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	pkgconfig(libpcre)
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%doc html/
%doc examples/
%{_libdir}/ocaml/pcre/*.a
%{_libdir}/ocaml/pcre/*.cmxa
%{_libdir}/ocaml/pcre/*.mli
%{_libdir}/ocaml/pcre/*.cmx

#----------------------------------------------------------------------------

%prep
%setup -q -n pcre-ocaml-%{version}

%build
./configure --prefix=%{_prefix}
make
make doc
mv _build/API.docdir/ html/

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install

