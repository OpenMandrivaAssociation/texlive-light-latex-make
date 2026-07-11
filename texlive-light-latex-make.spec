%global tl_name light-latex-make
%global tl_revision 66473

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	llmk: A build tool for LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/light-latex-make
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/light-latex-make.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/light-latex-make.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(light-latex-make.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Light LaTeX Make (llmk) is yet another build tool specific for LaTeX
documents. Its aim is to provide a simple way to specify a workflow of
processing LaTeX documents and encourage people to always explicitly
show the right workflow for each document. The main features of llmk are
all about the above purpose. First, you can describe the workflows
either in an external file llmk.toml or in a LaTeX document source in
the form of magic comments. Further, multiple magic comment formats can
be used. Second, it is fully cross-platform. The only requirement of the
program is the texlua command; llmk provides a uniform way to describe
the workflows available for nearly all TeX environments. Third, it
behaves exactly the same in any environment. At this point, llmk
intentionally does not provide any method for user configuration.
Therefore one can guarantee that for a LaTeX document with an llmk
setup, the process of typesetting the document will be reproduced in any
TeX environment with the program.

