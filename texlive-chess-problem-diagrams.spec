%global tl_name chess-problem-diagrams
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.23
Release:	%{tl_revision}.1
Summary:	A package for typesetting chess problem diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chess-problem-diagrams
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chess-problem-diagrams.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros to typeset chess problem diagrams including
fairy chess problems (mostly using rotated images of pieces) and other
boards.

