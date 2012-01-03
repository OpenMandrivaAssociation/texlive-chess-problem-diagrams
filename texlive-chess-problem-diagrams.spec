# revision 23555
# category Package
# catalog-ctan /macros/latex/contrib/chess-problem-diagrams
# catalog-date 2011-06-09 20:28:23 +0200
# catalog-license lppl1.2
# catalog-version 1.5.4
Name:		texlive-chess-problem-diagrams
Version:	1.5.4
Release:	2
Summary:	A package for typesetting chess problem diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chess-problem-diagrams
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%define		_unpackaged_subdirs_terminate_build	0

%description
This package provides macros to typeset problem chess diagrams
including fairy chess problems (mostly using rotated images of
pieces) and other boards.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chess-problem-diagrams/diagram.sty
%doc %{_texmfdistdir}/doc/latex/chess-problem-diagrams/README
%doc %{_texmfdistdir}/doc/latex/chess-problem-diagrams/diagram.pdf
#- source
%doc %{_texmfdistdir}/source/latex/chess-problem-diagrams/diagram.dtx
%doc %{_texmfdistdir}/source/latex/chess-problem-diagrams/diagram.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
