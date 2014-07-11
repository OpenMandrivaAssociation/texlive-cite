# revision 19955
# category Package
# catalog-ctan /macros/latex/contrib/cite
# catalog-date 2010-09-12 10:54:58 +0200
# catalog-license other-free
# catalog-version 5.3
Name:		texlive-cite
Version:	5.3
Release:	8
Summary:	Improved citation handling in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cite
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cite.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.3-2
+ Revision: 750246
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.3-1
+ Revision: 718062
- texlive-cite
- texlive-cite
- texlive-cite
- texlive-cite
- texlive-cite

