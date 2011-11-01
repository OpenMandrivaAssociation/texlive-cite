Name:		texlive-cite
Version:	5.3
Release:	1
Summary:	Improved citation handling in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cite
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cite.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package supports compressed, sorted lists of numerical
citations, and also deals with various punctuation and other
issues of representation, including comprehensive management of
break points. The package is compatible with both hyperref and
backref. The package is (unsurprisingly) part of the cite
bundle of the author's citation-related packages.

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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
