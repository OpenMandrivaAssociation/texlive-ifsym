# revision 24868
# category Package
# catalog-ctan /fonts/ifsym
# catalog-date 2011-04-10 22:02:30 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-ifsym
Version:	20110410
Release:	2
Summary:	A collection of symbols
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ifsym
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifsym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifsym.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of symbol fonts, written in Metafont, offering
(respectively) clock-face symbols, geometrical symbols, weather
symbols, mountaineering symbols, electronic circuit symbols and
a set of miscellaneous symbols. A LaTeX package is provided,
that allows the user to load only those symbols needed in a
document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ifsym/ifclk.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifclk10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifclkb10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeo.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeo10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeob10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeobn10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeobw10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeon10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifgeow10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsym.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifsym10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsymb10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsymbi10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifsymi10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifwea.gen
%{_texmfdistdir}/fonts/source/public/ifsym/ifwea10.mf
%{_texmfdistdir}/fonts/source/public/ifsym/ifweab10.mf
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifclk10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifclkb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeo10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeob10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeobn10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeobw10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeon10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifgeow10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsym10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsymb10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsymbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifsymi10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifwea10.tfm
%{_texmfdistdir}/fonts/tfm/public/ifsym/ifweab10.tfm
%{_texmfdistdir}/tex/latex/ifsym/ifsym.sty
%{_texmfdistdir}/tex/latex/ifsym/uifblk.fd
%{_texmfdistdir}/tex/latex/ifsym/uifclk.fd
%{_texmfdistdir}/tex/latex/ifsym/uifgeo.fd
%{_texmfdistdir}/tex/latex/ifsym/uifsym.fd
%{_texmfdistdir}/tex/latex/ifsym/uifwea.fd
%doc %{_texmfdistdir}/doc/fonts/ifsym/ifsym.ps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
