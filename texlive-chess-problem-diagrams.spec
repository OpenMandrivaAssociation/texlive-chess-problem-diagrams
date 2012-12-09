# revision 26206
# category Package
# catalog-ctan /macros/latex/contrib/chess-problem-diagrams
# catalog-date 2012-05-01 11:47:32 +0200
# catalog-license lppl1.2
# catalog-version 1.6
Name:		texlive-chess-problem-diagrams
Version:	1.6
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros to typeset chess problem diagrams
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


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 804524
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5.4-2
+ Revision: 750160
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5.4-1
+ Revision: 718051
- texlive-chess-problem-diagrams
- texlive-chess-problem-diagrams
- texlive-chess-problem-diagrams
- texlive-chess-problem-diagrams
- texlive-chess-problem-diagrams

