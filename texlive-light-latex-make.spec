Name:		texlive-light-latex-make
Version:	60558
Release:	2
Summary:	llmk: A build tool for LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/light-latex-make
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/light-latex-make.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/light-latex-make.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Light LaTeX Make (llmk) is yet another build tool specific for
LaTeX documents. Its aim is to provide a simple way to specify
a workflow of processing LaTeX documents and encourage people
to always explicitly show the right workflow for each document.
The main features of llmk are all about the above purpose.
First, you can describe the workflows either in an external
file llmk.toml or in a LaTeX document source in the form of
magic comments. Further, multiple magic comment formats can be
used. Second, it is fully cross-platform. The only requirement
of the program is the texlua command; llmk provides a uniform
way to describe the workflows available for nearly all TeX
environments. Third, it behaves exactly the same in any
environment. At this point, llmk intentionally does not provide
any method for user configuration. Therefore one can guarantee
that for a LaTeX document with an llmk setup, the process of
typesetting the document will be reproduced in any TeX
environment with the program.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/light-latex-make
%doc %{_texmfdistdir}/texmf-dist/doc/support/light-latex-make
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/llmk.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/llmk.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
