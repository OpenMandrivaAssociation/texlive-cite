Name:		texlive-cite
Version:	36428
Release:	2
Summary:	Improved citation handling in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cite
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cite.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports compressed, sorted lists of numerical
citations, and also deals with various punctuation and other
issues of representation, including comprehensive management of
break points. The package is compatible with both hyperref and
backref. The package is (unsurprisingly) part of the cite
bundle of the author's citation-related packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cite/chapterbib.sty
%{_texmfdistdir}/tex/latex/cite/cite.sty
%{_texmfdistdir}/tex/latex/cite/drftcite.sty
%{_texmfdistdir}/tex/latex/cite/overcite.sty
%doc %{_texmfdistdir}/doc/latex/cite/README
%doc %{_texmfdistdir}/doc/latex/cite/chapterbib.ltx
%doc %{_texmfdistdir}/doc/latex/cite/chapterbib.pdf
%doc %{_texmfdistdir}/doc/latex/cite/cite.ltx
%doc %{_texmfdistdir}/doc/latex/cite/cite.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
