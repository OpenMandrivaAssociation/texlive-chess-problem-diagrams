Name:		texlive-chess-problem-diagrams
Version:	1.5.4
Release:	1
Summary:	A package for typesetting chess problem diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chess-problem-diagrams
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides macros to typeset problem chess diagrams
including fairy chess problems (mostly using rotated images of
pieces) and other boards.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
