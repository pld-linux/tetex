#
# Please note, that some packages are missing. I will add them in few days.
#
# TODO:
# - error: libkpathsea.so is required by already marked tetex-dvips-1.0.7.beta_20020208-0.1
# - what with texinfo ?
# - error: tetex-format-context-1.0.7.beta_20020402-0.1: req perl(path_tre) not found
#   _noautoreqdep perl(path_tre) ?
# - move new files to proper subpackages
# - split dvips configs and maps to fonts subpackages
# - allow using Type1 fonts in others applications (symlink to
#   /usr/share/fonts/Type1 ?)
# - look at mktexfmt


%define		_ver	beta-20020922
%define		texmf_ver	beta-20020922

Summary:	TeX typesetting system and MetaFont font formatter
Summary(de):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr):	Systéme de compostion TeX et formatteur de MetaFontes
Summary(pl):	System sk³adu publikacji TeX oraz formater fontów MetaFont
Summary(pt_BR):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr):	TeX dizgi sistemi ve MetaFont yazýtipi biçimlendiricisi
Name:		tetex
Version:	1.0.7.%(echo %{_ver}|tr -- - _)
Release:	0.1
License:	distributable
Group:		Applications/Publishing/TeX
# Release sources at ftp://sunsite.informatik.rwth-aachen.de/pub/comp/tex/teTeX/1.0/distrib/sources/
Source0:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX-beta/teTeX-src-%{_ver}.tar.gz
Source1:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX-beta/teTeX-texmf-%{texmf_ver}.tar.gz
Source3:	%{name}-non-english-man-pages.tar.bz2
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source7:	%{name}-updmap
Patch0:		teTeX-rhconfig.patch
Patch1:		teTeX-buildr.patch
Patch2:		teTeX-manpages.patch
Patch4:		teTeX-info.patch
Patch5:		teTeX-klibtool.patch
Patch6:		teTeX-texi2html.patch
Patch7:		teTeX-texmfcnf.patch
Patch9:		teTeX-texmf-dvipsgeneric.patch
Patch10:	teTeX-fmtutil.patch
Patch11:	teTeX-grep.patch
Patch12:	teTeX-all-languages.patch
Patch13:	teTeX-bug19278.patch
Patch14:	teTeX-protos.patch
Patch15:	teTeX-tektronix.patch
Patch16:	teTeX-cx.patch
Patch17:	teTeX-cpp_macros.patch
Patch18:	teTeX-trie_size_max.patch
URL:		http://www.tug.org/teTeX/
Requires:	tmpwatch
Requires:	dialog
Requires:	tetex-fonts-cm = %{version}
Requires:	tetex-fonts-misc = %{version}
PreReq:		/sbin/ldconfig
PreReq:		sed
PreReq:		awk
PreReq:		textutils
PreReq:		sh-utils
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	rpm-perlprov
BuildRequires:	t1lib-devel
BuildRequires:	texinfo
BuildRequires:	w3c-libwww-devel
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
%include	/usr/lib/rpm/macros.perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ; 
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ; 
%define		fmtutil(f:) [ ! \\\( -f %{texmf}/web2c/%{-f*}.fmt.rpmnew -o -f %{texmf}/web2c/%{-f*}.efmt.rpmnew \\\) ] || %{_bindir}/fmtutil --byfmt %{-f*} >/dev/null 2>/dev/null || echo "Regenerating %{-f*} failed. See %{texmf}/web2c/%{-f*}.log for details" 1>&2 && exit 0 ; 

%define 	_noautoreqdep perl\\(path_tre\\)

%description
teTeX is an implementation of TeX for Linux or UNIX systems. TeX takes
a text file and a set of formatting commands as input and creates a
typesetter independent .dvi (DeVice Independent) file as output.
Usually, TeX is used in conjunction with a higher level formatting
package like LaTeX or PlainTeX, since TeX by itself is not very
user-friendly.

%description -l es
Tex formata archivos de texto y órdenes para una salida independiente
de dispositivo (que se llama DVI - DeVice Independent). En The TeXbook
de Knut se describen las capacidades y el lenguaje TeX.

%description -l de
TeX formatiert eine Datei, die abwechselnd Text und Befehle enthält
und gibt eine geräteunabhängige Datei aus (DVI genannt, Abk. für
DeVice Independent). Die Funktionen und Sprache von TeX werden in The
TeXbook von Knuth beschrieben.

%description -l fr
TeX formate un fichier de commandes et de texte mélandés, et produit
un fichier de indépendant de toute plate-forme (appelé DVI, qui est un
raccourci pour Device Independant). Les possibilités de TeX et son
langage sont décrites dans l'ouvrage TeXbook, de Knuth.

%description -l pl
TeX formatuje przygotowany tekst oraz komendy i produkuje niezale¿ny
od urz±dzenia plik wynikowy (tzw. DVI -- skrót od DeVice Independent).
Mo¿liwo¶ci TeXa, oraz jego jêzyk zosta³y opisane w ,,The TeXbook''
Donalda E. Knutha.

%description -l pt_BR
Tex formata arquivos de texto e comandos para uma saída independente
de dispositivo (chamado DVI - DeVice Independent). As capacidades e a
linguagem TeX são descritas no The TeXbook, de Knuth.

%description -l tr
TeX, içinde metin ve komutlarýn yer aldýðý bir dosyayý okur ve dizgi
aygýtýndan baðýmsýz bir çýktý (DeVice Independent - DVI) oluþturur.
TeX'in becerileri ve dizgi dili, dili geliþtiren Knuth'un 'The
TeXbook' baþlýklý kitabýnda anlatýlmaktadýr.

#
# libraries
#
%package -n kpathsea
Summary:	File name lookup library
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description -n kpathsea
File name lookup library.

%package -n kpathsea-devel
Summary:	Kpathsea library filename lookup header files and documentation
Summary(es):	Bibliotecas y archivos de inclusión para desarrollo TeX
Summary(pl):	Pliki nag³ówkowe oraz dokumetacja kpathsea
Summary(pt_BR):	Bibliotecas e headers para desenvolvimento TeX
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description -n kpathsea-devel
Kpathsea library filename lookup header files and documentation.

%description -n kpathsea-devel -l es
Bibliotecas, archivos de inclusión, etc, para que puedas desarrollar
aplicaciones TeX.

%description -n kpathsea-devel -l pl
Pliki nag³ówkowe oraz dokumentacja biblioteki kpathsea.

%description -n kpathsea-devel -l pt_BR
Bibliotecas, headers e outros componentes que podem ser utilizados
para desenvolver aplicações TeX.

#
# programs
#
%package dvips
Summary:	DVI to PostScript converter
Summary(de):	dvi-Postscript-Konvertierungsprogramm
Summary(es):	Convertidor dvi para postscript
Summary(fr):	Convertisseur dvi vers PostScript
Summary(pl):	Konwerter plików DVI do PostScript-u
Summary(pt_BR):	Conversor dvi para postscript
Summary(tr):	dvi'dan postscript'e dönüþtürücü
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%description dvips -l de
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX bzw.
durch einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und
konvertiert diese in PostScript, wobei das Ergebnis in der Regel
direkt an einen Laserdrucker gesandt wird.

%description dvips -l es
El programa dvips coge un archivo DVI (.dvi) producido por TeX (o por
otro procesador como GFtoDVI) y lo convierte a PostScript, normalmente
enviando el resultado directamente a la impresora láser.

%description dvips -l fr
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le résultat directement sur une imprimante Laser.

%description dvips -l pl
Program dvips bierze plik DVI wygenerowany przez TeXa (lub jaki¶ inny
program, jak na przyk³ad GFtoDVI) i konwertuje go do PostScriptu.
Domy¶lnie wynik jest wysy³any bezpo¶rednio do drukarki.

%description dvips -l pt_BR
O programa dvips toma um arquivo DVI (.dvi) produzido pelo TeX (ou por
outro processador como o GFtoDVI) e o converte para PostScript,
normalmente enviando o resultado diretamente para a impressora laser.

%description dvips -l tr
dvips programý, dvi biçiminde bir girdi dosyasý alýr ve onu
PostScript'e dönüþtürür. Kaynak dosya TeX tarafýndan oluþturulmuþ
olabileceði gibi baþka iþleyiciler tarafýndan da (GFtoDVI gibi)
üretilmiþ olabilir.

%package dvilj
Summary:	DVI to PCL converter
Summary(de):	Ein dvi-->Laserjet-Konvertierer
Summary(es):	Convertidor dvi para laserjet
Summary(fr):	convertisseur dvi vers laserjet.
Summary(pl):	Konwerter plików DVI do jêzyka PCL
Summary(pt_BR):	Conversor dvi para laserjet
Summary(tr):	dvi'dan laserjet'e dönüþtürücü
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description dvilj
Dvilj and dvilj's siblings (included in this package) will convert TeX
text formatting system output .dvi files to HP PCL (HP Printer Control
Language) commands. Using dvilj, you can print TeX files to HP
LaserJet+ and fully compatible printers. With dvilj2p, you can print
to HP LaserJet IIP and fully compatible printers. And with dvilj4, you
can print to HP LaserJet4 and fully compatible printers.

%description dvilj -l de
Dvilj und Gebrüder konvertieren TeX-Ausgabe-.dvi-Dateien in HP PCL (HP
Printer Control Language) Befehle zum Drucken auf HP LaserJet+, HP
LaserJet IIP (mit dvilj2p), HP LaserJet 4 (mit dvilj4) und vollständig
kompatiblen Druckern.

%description dvilj -l es
Dvilj y semejantes convierten archivos de salida TeX.dvi en comandos
HP PCL (i.e. Lenguaje de Control de Impresoras HP) adecuados a
impresión de impresoras HP LaserJEt+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) y compatibles.

%description dvilj -l fr
dvilj et ses cousins convertissent les fichiers dvi en commandes HPPCL
(le langage des imprimantes HP) pour les imprimer sur HP LaserJet+, HP
LaserJet IIP (avec dvilj2p), HP LaserJet 4 (avec dvilj4), et autres
imprimantes totalement compatibles.

%description dvilj -l pt_BR
Dvilj e semelhantes convertem arquivos de saída TeX .dvi em comandos
HP PCL (i.e. Linguagem de Controle de Impressoras HP) adequados para
impressão em impressoras HP LaserJet+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) e compatíveis.

%description dvilj -l tr
TeX çýktýsý dvi dosyalarýný HP PCL (HP'nin geliþtirdiði bir yazýcý
denetim dili) komutlarýna çevirir ve böylece bir LaserJet+, HP
LaserJet IIP (dvilj2p ile), HP LaserJet4 (dvilj4 ile) ve tam
uyumlularýndan yazýcý çýktýsý alýnabilir.

%package -n xdvi
Summary:	X11 previewer
Summary(de):	X11-Previewer
Summary(es):	Visualizador TeX X11
Summary(fr):	Prévisualisateur X11
Summary(pl):	Przegl±darka DVI dla X11
Summary(pt_BR):	Visualizador TeX X11
Summary(tr):	X11 öngörüntüleyici
Requires:	%{name} = %{version}
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-xdvi

%description -n xdvi
xdvi is a program which runs under the X window system. It is used to
preview dvi files, such as are produced by tex and latex.

%description -n xdvi -l de
xdvi ist ein Programm, das unter dem X-Window-System läuft und gewohnt
ist, dvi-Dateien als Vorschau anzuzeigen, etwa solche, die von tex und
latex erzeugt wurden.

%description -n xdvi -l es
xdvi es un programa que se ejecuta en el sistema X Window. Se usa para
visualizar archivos dvi, como los producidos por tex y latex.

%description -n xdvi -l fr
xdvi est un programme s'exécutant sous le système X Window. Il sert à
visualiser les fichiers dvi tels que ceux produits par tex et latex.

%description -n xdvi -l pl
Xdvi jest programem (dzia³aj±cym w X Window System) do przegl±dania
plików DVI, produkowanych przez TeXa i LaTeXa.

%description -n xdvi -l pt_BR
xdvi é um programa que roda no sistema X Window. É usado para
visualizar arquivos dvi, como os produzidos por tex e latex.

%package pdftex
Summary:	TeX generating PDF files instead DVI
Summary(pl):	PDFtex
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}

%description pdftex
TeX generating PDF files instead DVI.

#
# formats
#

# Plain format.

%package plain
Summary:	Plain TeX format basic files
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description plain
Plain TeX format basic files.

%package plain-dvips
Summary:	PostScript support for Plain TeX format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-dvips = %{version}
Requires:	%{name}-plain = %{version}

%description plain-dvips
PostScript support for Plain TeX format.

%package plain-mathtime
Summary:	Mathtime fonts for Plain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description plain-mathtime
The Mathtime fonts have a number of characters remapped to positions
different from the ones normally used by the corresponding TeX CM-fonts.
For the symbol font ``operators'' the corresponding mathtime style files
use the Times Roman font (often called something like: ptmr or ptmr7t or
ptmrq).

%package plain-misc
Summary:	Miscellaneous macros for Plain TeX format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description plain-misc
Miscellaneous macros for Plain TeX format.

%package format-plain
Summary:	TeX Plain format
Group:		Applications/Publishing/TeX
PreReq:		%{_bindir}/texhash
Requires:	%{name}-plain = %{version}

%description format-plain
TeX Plain format.

%package format-bplain
Summary:	TeX BPlain format
Group:		Applications/Publishing/TeX
PreReq:		%{_bindir}/texhash
Requires:	%{name}-plain = %{version}

%description format-bplain
TeX BPlain format.

%package format-pdftex
Summary:	PDFTeX Plain format
Group:		Applications/Publishing/TeX
Requires:	%{name}-plain = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdftex
PDFTeX Plain format.

%package format-pdfetex
Summary:	PDFTeX EPlain format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfetex
PDFTeX EPlain format.

# MeX Plain format

%package mex
Summary:	MeX Plain Format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	tetex-plain = %{version}
Requires:	tetex-fonts-pl = %{version}

%description mex
MeX Plain Format.

%package format-mex
Summary:	MeX Plain Format basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	tetex-mex = %{version}

%description format-mex
MeX Plain Format basic files.

%package format-pdfmex
Group:		Applications/Publishing/TeX
Summary:	PDFMeX Plain Format
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-mex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfmex
PDFMeX Plain Format.

%package format-pdfemex
Summary:	PDFMeX EPlain Format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-mex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfemex
PDFMeX EPlain Format.

# AMS TeX format

%package amstex
Summary:	AMS macros for Plain TeX basic files
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-ams
PreReq:		%{_bindir}/texhash
Requires:	%{name}-plain = %{version}

%description amstex
American Mathematics Society macros for Plain TeX basic files.

%package format-amstex
Summary:	AMS macros for Plain TeX
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-ams
PreReq:		%{_bindir}/texhash
Requires:	%{name}-amstex = %{version}

%description format-amstex
American Mathematics Society macros for Plain TeX.

%package format-bamstex
Summary:	AMS macros for BPlain TeX
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-ams
PreReq:		%{_bindir}/texhash
Requires:	%{name}-amstex = %{version}

%description format-bamstex
American Mathematics Society macros for BPlain TeX.

%package format-pdfamstex
Summary:	AMS macros for PDFTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-amstex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfamstex
American Mathematics Society macros for PDFTeX.

# CSPlain format

%package csplain
Summary:	TeX CSPlain format basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description csplain
TeX CSPlain format basic files.

%package format-csplain
Summary:	TeX CSPlain format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-csplain = %{version}

%description format-csplain
TeX CSPlain format.

%package format-pdfcsplain
Summary:	PDFTeX CSPlain format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-csplain = %{version}

%description format-pdfcsplain
PDFTeX CSPlain format.

# Cyryillc Plain format

%package cyrplain
Summary:	Cyryillc Plain format basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description cyrplain
Cyryillc Plain format basic files.

%package format-cyrplain
Summary:	Cyryillc Plain format.
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-cyrplain = %{version}

%description format-cyrplain
Cyryillc Plain format.

# EPlain format

%package eplain
Summary:	EPlain format basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description eplain
EPlain format basic files.

%package format-eplain
Summary:	EPlain format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-eplain = %{version}

%description format-eplain
EPlain format.

# LaTeX format.

%package latex
Summary:	LaTeX macro package basic files
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-latex = %{version}
Requires:	tetex-tex-hyphen = %{version}
PreReq:		%{_bindir}/texhash

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains basic files.

%package latex-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-ae
A set of virtual fonts which emulates T1 coded fonts using the standard CM
fonts. The package is called AE fonts (for Almost European). The main use
of the package is to produce PDF files using versions of the CM fonts
instead of the bitmapped EC fonts.

%package latex-ams
Summary:	AMS math facilities for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-ams = %{version}

%description latex-ams
This package is the principal package in the AMS-LaTeX distribution. It
adapts for use in LaTeX most of the mathematical features found in AMS-TeX.

%package latex-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-antp = %{version}

%description latex-antp
A replica of Antykwa Poltawskiego font in PostScript Type 1 format
-- preliminary version. This font was designed in the 'twenties and the 'thirties
of XX century by a Polish graphic artist and a typographer Adam Poltawski.
It was widely used by Polish printing houses as long as metal
types were in use (until ca the 'sixties). Perhaps the first complete font
family programmed and parametrized in METAPOST.

%package latex-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-antt = %{version}

%description latex-antt
Antykwa Torunska is a serif font designed by the late Polish typographer
Zygfryd Gardzielewski, reconstructed and digitized as as Type 1.

%package latex-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-bbm = %{version}

%description latex-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%package latex-carlisle
Summary:	Miscellaneous small packages by David Carlisle
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-carlisle
Miscellaneous small packages by David Carlisle.

%package latex-ccfonts
Summary:	Support for Concrete text and math fonts in LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX package for
typesetting documents using Concrete as the default font family.  The files
support OT1, T1, TS1, and Concrete math including AMS fonts (Ulrik Vieth's
concmath).

%package latex-cite
Summary:	Supports compressed, sorted lists of numerical citations
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-cite
Supports compressed, sorted lists of numerical citations.

%package latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-concmath = %{version}

%description latex-concmath
LaTeX package and font definition files to access the Concrete math fonts,
which were derived from Computer Modern math fonts using parameters from
Concrete Roman text fonts.

%package latex-custom-bib
Summary:	Customised BibTeX styles for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-custom-bib
Package generating customized BibTeX bibliography styles from a generic
file using docstrip. Includes support for the Harvard style.

%package latex-cyrillic
Summary:	LaTeX Cyrillic support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-cyrillic
LaTeX Cyrillic support.

%package latex-dstroke
Summary:	LaTeX doublestroke font
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-dstroke = %{version}

%description latex-dstroke
Doublestroke font for typesetting the mathematical symbols for the natural
numbers, whole numbers, rational numbers, real numbers and complex numbers.

%package latex-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-jknappen = %{version}

%description latex-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%package latex-lucidabr
Summary:	Package to make Lucida Bright fonts usable with LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-lucidabr
Package to make Lucida Bright fonts usable with LaTeX.

%package latex-psnfss
Summary:	LaTeX font support for common PostScript fonts. 
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-psnfss
LaTeX font definition files, macros and font metrics for common PostScript
fonts.

%package format-latex
Summary:	LaTeX macro package
Group:		Applications/Publishing/TeX
Requires:	%{name}-latex = %{version}
PreReq:		%{_bindir}/texhash

%description format-latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains LaTeX format.

%package format-elatex
Summary:	ELaTeX macro package
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description format-elatex
ELaTeX macro package.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Group:		Applications/Publishing/TeX
#Provides:	%{name}-format-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF LaTeX format.

%package format-pdfelatex
Summary:	PDF ELaTeX macro package
Group:		Applications/Publishing/TeX
#Provides:	%{name}-format-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfelatex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF ELaTeX format.

# ------------------------



%package bibtex
Summary:	LaTeX macro package
Summary(pl):	Dodatkowe makra dla LaTeXa
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description bibtex
LaTeX macro package.

%description bibtex -l pl
Dodatkowe makra dla LaTeXa.

%package etex
Summary:	e-TeX
Summary(pl):	e-TeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description etex
e-TeX: a 100%-compatible successor to TeX.

%description etex -l pl
e-TeX -- Pierwsza przymiarka do New Typesetting System.

%package format-omega
Summary:	extended unicode TeX
Summary(pl):	Rozszerzony unicode TeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description format-omega
Omega is extended unicode TeX.

%description format-omega -l pl
Omega -- TeX ze wsparciem dla Unicode.

%package oxdvi
Summary:	xdvi viewer for Omega
Summary(pl):	Przegl±darka xdvi dla Omegi
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}

%description oxdvi
xdvi viewer for Omega - extended unicode TeX.

%description oxdvi -l pl
Przegl±darka xdvi dla Omegi -- TeXa ze wsparciem dla Unicode.

%package fonts
Summary:	The font files for the TeX text formatting system
Summary(pl):	Fonty dla TeXa
Group:		Applications/Publishing/TeX
PreReq:		%{_bindir}/texhash

%description fonts
The tetex-fonts package contains fonts used by both the Xdvi previewer
and the TeX text formatting system.

You will need to install tetex-fonts if you wish to use either
tetex-xdvi (for previewing .dvi files in X) or the tetex package (the
core of the TeX text formatting system).

%description fonts -l pl
Pakiet tetex-fonts zawiera czcionki u¿ywane przez TeXa oraz Xdvi.
Je¿eli chcesz korzystaæ z którego¶ z tych programów, musisz
zainstalowaæ ten pakiet.

%package doc
Summary:	The documentation files for the TeX text formatting system
Summary(pl):	Pliki dokumentacji TeXa
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}

%description doc
The tetex-doc package contains documentation for the TeX text
formatting system.

If you want to use TeX and you're not an expert at it, you should
install the tetex-doc package. You'll also need to install the tetex
package, tetex-afm (a PostScript font converter for TeX), tetex-dvilj
(for converting .dvi files to HP PCL format for printing on HP and HP
compatible printers), tetex-dvips (for converting .dvi files to
PostScript format for printing on PostScript printers), tetex-latex (a
higher level formatting package which provides an easier-to-use
interface for TeX) and tetex-xdvi (for previewing .dvi files).

%description doc -l pl
Dokumentacja do TeXa. Je¿eli chcesz korzystaæ z TeXa to powiniene¶
zainstalowaæ ten pakiet.

%package bibtex-ams
Summary:	bibtex-ams
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-ams
bibtex-ams

%package bibtex-adrconv
Summary:	bibtex-adrconv
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-adrconv
bibtex-adrconv


%package bibtex-plbib
Summary:	bibtex-plbib
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-plbib
bibtex-plbib

%package bibtex-germbib
Summary:	bibtex-germbib
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-germbib
bibtex-germbib

%package bibtex-koma-script
Summary:	bibtex-koma-script
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-koma-script
bibtex-koma-script

%package bibtex-natbib
Summary:	bibtex-natbib
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-natbib
bibtex-natbib

%package bibtex-revtex4
Summary:	bibtex-revtex4
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-revtex4
bibtex-revtex4

%package fonts-adobe
Summary:	fonts-adobe
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-adobe
fonts-adobe

%package fonts-bitstrea
Summary:	fonts-bitstrea
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bitstrea
fonts-bitstrea

%package fonts-antp
Summary:	fonts-antp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-antp
fonts-antp

%package fonts-antt
Summary:	fonts-antt
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-antt
fonts-antt

%package fonts-marvosym
Summary:	fonts-marvosym
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-marvosym
fonts-marvosym

%package fonts-omega
Summary:	fonts-omega
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-omega
fonts-omega

%package fonts-qfonts
Summary:	fonts-qfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-qfonts
fonts-qfonts

%package fonts-xypic
Summary:	fonts-xypic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-xypic
fonts-xypic

%package fonts-urw
Summary:	fonts-urw
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-urw
fonts-urw

%package fonts-yandy
Summary:	fonts-yandy
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-yandy
fonts-yandy

%package fonts-ams
Summary:	fonts-ams
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-ams
fonts-ams

%package fonts-lh
Summary:	fonts-lh
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-lh
fonts-lh

%package fonts-bbm
Summary:	fonts-bbm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bbm
fonts-bbm

%package fonts-bbold
Summary:	fonts-bbold
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bbold
fonts-bbold

%package fonts-cbgreek
Summary:	fonts-cbgreek
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cbgreek
fonts-cbgreek

%package fonts-cc-pl
Summary:	fonts-cc-pl
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cc-pl
fonts-cc-pl

%package fonts-cm
Summary:	fonts-cm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cm
fonts-cm

%package fonts-cmcyr
Summary:	fonts-cmcyr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cmcyr
fonts-cmcyr

%package fonts-cm-bold
Summary:	fonts-cm-bold
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cm-bold
fonts-cm-bold

%package fonts-cmextra
Summary:	fonts-cmextra
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cmextra
fonts-cmextra

%package fonts-concmath
Summary:	fonts-concmath
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-concmath
fonts-concmath

%package fonts-concrete
Summary:	fonts-concrete
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-concrete
fonts-concrete

%package fonts-cs
Summary:	fonts-cs
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cs
fonts-cs

%package fonts-dstroke
Summary:	fonts-dstroke
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-dstroke
fonts-dstroke

%package fonts-ecc
Summary:	fonts-ecc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-ecc
fonts-ecc

%package fonts-euxm
Summary:	fonts-euxm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-euxm
fonts-euxm

%package fonts-gothic
Summary:	fonts-gothic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-gothic
fonts-gothic

%package fonts-latex
Summary:	fonts-latex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-latex
fonts-latex

%package fonts-mflogo
Summary:	fonts-mflogo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-mflogo
fonts-mflogo

%package fonts-misc
Summary:	fonts-misc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-misc
fonts-misc

%package fonts-pandora
Summary:	fonts-pandora
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-pandora
fonts-pandora

%package fonts-pl
Summary:	fonts-pl
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-pl
fonts-pl

%package fonts-rsfs
Summary:	fonts-rsfs
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-rsfs
fonts-rsfs

%package fonts-stmaryrd
Summary:	fonts-stmaryrd
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-stmaryrd
fonts-stmaryrd

%package fonts-vnr
Summary:	fonts-vnr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-vnr
fonts-vnr

%package fonts-wasy
Summary:	fonts-wasy
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-wasy
fonts-wasy

%package fonts-bh
Summary:	fonts-bh
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bh
fonts-bh

%package fonts-cg
Summary:	fonts-cg
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cg
fonts-cg

%package fonts-hoekwater
Summary:	fonts-hoekwater
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-hoekwater
fonts-hoekwater

%package fonts-monotype
Summary:	fonts-monotype
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-monotype
fonts-monotype

%package fonts-ae
Summary:	fonts-ae
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-ae
fonts-ae

%package fonts-mathpple
Summary:	fonts-mathpple
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-mathpple
fonts-mathpple

%package fonts-pazo
Summary:	fonts-pazo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-pazo
fonts-pazo

%package fonts-vcm
Summary:	fonts-vcm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-vcm
fonts-vcm

%package fonts-type1-adobe
Summary:	fonts-type1-adobe
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-adobe
fonts-type1-adobe

%package fonts-type1-bitstrea
Summary:	fonts-type1-bitstrea
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-bitstrea
fonts-type1-bitstrea

%package fonts-type1-bluesky
Summary:	fonts-type1-bluesky
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-bluesky
fonts-type1-bluesky

%package fonts-type1-hoekwater
Summary:	fonts-type1-hoekwater
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-hoekwater
fonts-type1-hoekwater

%package fonts-type1-antp
Summary:	fonts-type1-antp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-antp
fonts-type1-antp

%package fonts-type1-antt
Summary:	fonts-type1-antt
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-antt
fonts-type1-antt

%package fonts-type1-belleek
Summary:	fonts-type1-belleek
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-belleek
fonts-type1-belleek

%package fonts-type1-cmcyr
Summary:	fonts-type1-cmcyr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-cmcyr
fonts-type1-cmcyr

%package fonts-type1-cs
Summary:	fonts-type1-cs
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-cs
fonts-type1-cs

%package fonts-type1-marvosym
Summary:	fonts-type1-marvosym
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-marvosym
fonts-type1-marvosym

%package fonts-type1-mathpazo
Summary:	fonts-type1-mathpazo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-mathpazo
fonts-type1-mathpazo

%package fonts-type1-omega
Summary:	fonts-type1-omega
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-omega
fonts-type1-omega

%package fonts-type1-pl
Summary:	fonts-type1-pl
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-fonts-type1-bluesky = %{version}

%description fonts-type1-pl
fonts-type1-pl

%package fonts-type1-qfonts
Summary:	fonts-type1-qfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-qfonts
fonts-type1-qfonts

%package fonts-type1-xypic
Summary:	fonts-type1-xypic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-xypic
fonts-type1-xypic

%package fonts-type1-urw
Summary:	fonts-type1-urw
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-urw
fonts-type1-urw

%package makeindex
Summary:	makeindex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description makeindex
makeindex

%package metafont
Summary:	metafont
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description metafont
metafont

%package matapost
Summary:	matapost
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description matapost
matapost

%package format-omega-lambda
Summary:	omega-lambda
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description format-omega-lambda
omega-lambda

%package omega-ocp
Summary:	omega-ocp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description omega-ocp
omega-ocp

%package omega-otp
Summary:	omega-otp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description omega-otp
omega-otp

%package format-pdftex-context
Summary:	pdftex-context
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdftex-context
pdftex-context

%description format-pdflatex
pdflatex

%package format-pdfplatex
Summary:	pdfplatex
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdfplatex
pdfplatex

%package tex
Summary:	tex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex
tex

%package texconfig
Summary:	texconfig
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description texconfig
texconfig

%package format-context
Summary:	context
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description format-context
context

%package cyramstex
Summary:	cyramstex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description cyramstex
cyramstex

%package rubibtex
Summary:	rubibtex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description rubibtex
rubibtex

%package rumakeindex
Summary:	rubibtex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description rumakeindex
rumakeindex

%package cyrtexinfo
Summary:	rubibtex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description cyrtexinfo
cyrtexinfo

%package texdoctk
Summary:	texdoctk
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description texdoctk
texdoctk

%package fontinst
Summary:	fontinst
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fontinst
fontinst

%package doc-Catalogue
Summary:	doc-Catalogue
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-Catalogue
doc-Catalogue

%package doc-de-tex-faq
Summary:	doc-de-tex-faq
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-de-tex-faq
doc-de-tex-faq

%package doc-LaTeX-FAQ-francaise
Summary:	doc-LaTeX-FAQ-francaise
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-LaTeX-FAQ-francaise
doc-LaTeX-FAQ-francaise

%package doc-uktug-faq
Summary:	doc-uktug-faq
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-uktug-faq
doc-uktug-faq

%package doc-latex2e-html
Summary:	doc-latex2e-html
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-latex2e-html
doc-latex2e-html

%package platex
Summary:	platex base
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description platex
platex base

%package format-platex
Summary:	platex
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-platex = %{version}

%description format-platex
platex

%package plain-plnfss
Summary:	plain-plnfss
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-plnfss
plain-plnfss

%package latex-wasysym
Summary:	latex-wasysym
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-wasysym
latex-wasysym

%package latex-vnr
Summary:	latex-vnr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-vnr
latex-vnr

%package latex-vnps
Summary:	latex-vnps
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-vnps
latex-vnps

%package latex-umlaute
Summary:	latex-umlaute
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-umlaute
latex-umlaute

%package latex-tools
Summary:	latex-tools
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-tools
latex-tools

%package latex-titlesec
Summary:	latex-titlesec
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-titlesec
latex-titlesec

%package latex-t2
Summary:	latex-t2
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-t2
latex-t2

%package latex-SIunits
Summary:	latex-SIunits
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-SIunits
latex-SIunits

%package latex-seminar
Summary:	latex-seminar
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-seminar
latex-seminar

%package latex-revtex4
Summary:	latex-revtex4
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-revtex4
latex-revtex4

%package latex-qfonts
Summary:	latex-qfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-qfonts
latex-qfonts

%package latex-pb-diagram
Summary:	latex-pb-diagram
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-pb-diagram
latex-pb-diagram

%package latex-palatcm
Summary:	latex-palatcm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-palatcm
latex-palatcm

%package latex-oberdiek
Summary:	latex-oberdiek
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-oberdiek
latex-oberdiek

%package latex-ntgclass
Summary:	latex-ntgclass
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-ntgclass
latex-ntgclass

%package latex-natbib
Summary:	latex-natbib
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-natbib
latex-natbib

%package latex-mwcls
Summary:	latex-mwcls
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mwcls
latex-mwcls

%package latex-multirow
Summary:	latex-multirow
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-multirow
latex-multirow

%package latex-ms
Summary:	latex-ms
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-ms
latex-ms

%package latex-mltex
Summary:	latex-mltex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mltex
latex-mltex

%package latex-minitoc
Summary:	latex-minitoc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-minitoc
latex-minitoc

%package latex-mfnfss
Summary:	latex-mfnfss
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mfnfss
latex-mfnfss

%package latex-mflogo
Summary:	latex-mflogo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mflogo
latex-mflogo

%package latex-mdwtools
Summary:	latex-mdwtools
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mdwtools
latex-mdwtools

%package latex-mathtime
Summary:	latex-mathtime
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mathtime
latex-mathtime

%package latex-mathptmx
Summary:	latex-mathptmx
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mathptmx
latex-mathptmx

%package latex-mathptm
Summary:	latex-mathptm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mathptm
latex-mathptm

%package latex-mathpple
Summary:	latex-mathpple
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-mathpple
latex-mathpple

%package latex-listings
Summary:	latex-listings
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-listings
latex-listings

%package latex-labels
Summary:	latex-labels
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-labels
latex-labels

%package latex-koma-script
Summary:	latex-koma-script
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-koma-script
latex-koma-script

%package latex-hyperref
Summary:	latex-hyperref
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-hyperref
latex-hyperref

%package latex-graphics
Summary:	latex-graphics
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-graphics
latex-graphics

%package latex-g-brief
Summary:	latex-g-brief
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-g-brief
latex-g-brief

%package latex-fp
Summary:	latex-fp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-fp
latex-fp

%package latex-fancyvrb
Summary:	latex-fancyvrb
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-fancyvrb
latex-fancyvrb

%package latex-fancyheadings
Summary:	latex-fancyheadings
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-fancyheadings
latex-fancyheadings

%package latex-fancyhdr
Summary:	latex-fancyhdr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-fancyhdr
latex-fancyhdr

%package latex-endfloat
Summary:	latex-endfloat
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-endfloat
latex-endfloat

%package latex-eepic
Summary:	latex-eepic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-eepic
latex-eepic

%package latex-dvilj
Summary:	latex-dvilj
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-dvilj
latex-dvilj

%package latex-draftcopy
Summary:	latex-draftcopy
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-draftcopy
latex-draftcopy

%package latex-dinbrief
Summary:	latex-dinbrief
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-dinbrief
latex-dinbrief

%package latex-curves
Summary:	latex-curves
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-curves
latex-curves

%package cslatex
Summary:	cslatex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description cslatex
cslatex

%package pdfcslatex
Summary:	pdfcslatex
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfcslatex
pdfcslatex

%package odvips
Summary:	odvips
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-format-omega = %{version}

%description odvips
odvips


%package fontname
Summary:	fontname
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fontname
fontname

%package babel
Summary:	babel
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description babel
babel

%package tex-misc
Summary:	tex-misc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-misc
tex-misc

%package tex-pstriks
Summary:	tex-pstriks
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-pstriks
tex-pstriks

%package tex-pictex
Summary:	tex-pictex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-pictex
tex-pictex

%package tex-ruhyphen
Summary:	tex-ruhyphen
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-ruhyphen
tex-ruhyphen

%package tex-spanishb
Summary:	tex-spanishb
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-spanishb
tex-spanishb

%package tex-texdraw
Summary:	tex-texdraw
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-texdraw
tex-texdraw

%package tex-thumbpdf
Summary:	tex-thumbpdf
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-thumbpdf
tex-thumbpdf

%package tex-ukrhyph
Summary:	tex-ukrhyph
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-ukrhyph
tex-ukrhyph

%package tex-vietnam
Summary:	tex-vietnam
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-vietnam
tex-vietnam

%package tex-xypic
Summary:	tex-xypic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-xypic
tex-xypic

%package tex-mfpic
Summary:	tex-mfpic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-mfpic
tex-mfpic

%package tex-hyphen
Summary:	tex-hyphen
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-hyphen
tex-hyphen

%package tex-german
Summary:	tex-german
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-german
tex-german

%package tex-eijkhout
Summary:	tex-eijkhout
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-eijkhout
tex-eijkhout

%prep
%setup  -q -n teTeX-src-%{_ver}
install -d texmf
tar xzf %{SOURCE1} -C texmf

%patch0  -p1
%patch1  -p1
%patch2  -p1
%patch4  -p1
%patch5  -p1
%patch6  -p1
# default values are OK
#patch7  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
#%patch16 -p1
#%patch17 -p1
%patch18 -p1

%build
#sh ./reautoconf
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure2_13 \
	--with-system-ncurses \
	--with-system-zlib \
	--with-system-pnglib \
	--with-system-tifflib \
	--with-system-wwwlib \
	--with-system-t1lib \
	--disable-multiplatform \
	--without-dialog \
	--without-texinfo \
	--without-t1utils \
	--with-fonts-dir=/var/cache/fonts \
	--with-texmf-dir=../../texmf \
	--with-ncurses \
	--enable-shared \
	--enable-gf \
	--enable-a4 \
	--enable-ipc \
	--disable-static

rm -f texk/{tetex,dvipsk}/*.info*
cd texk/dvipsk
makeinfo dvips.texi
cd ../..

cd texk/tetex
makeinfo latex2e.texi
cd ../..

%{__make}

cd texk/kpathsea
makeinfo kpathsea.texi
cd ../..

cd texk/web2c/doc
makeinfo web2c.texi
cd ../../..


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/cron.daily\
	$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/tetex-updmap/

perl -pi \
	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
	texmf/web2c/texmf.cnf

cp -a texmf $RPM_BUILD_ROOT%{_datadir}/texmf

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{texmf}

install %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/
touch $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/tetex-updmap/maps.lst

%{__make} init \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{texmf}

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{texmf}/web2c/texmf.cnf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/tetex

install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# remove all *.log
#rm -f $RPM_BUILD_ROOT%{texmf}/web2c/*.log

%post
%fixinfodir
/sbin/ldconfig
%fmtutil -f tex
#fmtutil -f bplain
%texhash

%postun
/sbin/ldconfig
%fixinfodir
%texhash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# czy to jest ci±gle potrzebne ?
%dir /etc/sysconfig/tetex-updmap
%verify(not size md5 mtime) %config(noreplace) /etc/sysconfig/tetex-updmap/maps.lst
/etc/cron.daily/tetex
%dir %{texmf}/web2c
%attr(755,root,root) %{_bindir}/fmtutil
%{_mandir}/man5/fmtutil.cnf.5*
%{_mandir}/man8/fmtutil.8*
# do czego jest fontexport, fontimport i fontinst ?
%attr(755,root,root) %{_bindir}/fontexport
%{_mandir}/man1/fontexport.1*
%attr(755,root,root) %{_bindir}/fontimport
%{_mandir}/man1/fontimport.1*
%attr(755,root,root) %{_bindir}/fontinst
%{_mandir}/man1/fontinst.1*
%attr(755,root,root) %{_bindir}/initex
%{_mandir}/man1/initex.1*
%attr(755,root,root) %{_bindir}/texhash
%{_mandir}/man1/texhash.1*
%attr(755,root,root) %{_bindir}/mktexfmt
%attr(755,root,root) %{_bindir}/mktexlsr
%{_mandir}/man1/mktexlsr.1*
%attr(755,root,root) %{_bindir}/tex
%{_mandir}/man1/tex.1*
%attr(755,root,root) %{_bindir}/texdoc
%{_mandir}/man1/texdoc.1*
%attr(755,root,root) %{_bindir}/texexec
%{_mandir}/man1/texexec.1*
%attr(755,root,root) %{_bindir}/texfind
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texutil
%{_mandir}/man1/texutil.1*
%attr(755,root,root) %{_bindir}/virtex
%{_mandir}/man1/virtex.1*
%attr(755,root,root) %{_bindir}/updmap

# do przej¿enia
%attr(755,root,root) %{_bindir}/access
%{_mandir}/man1/access.1*
%lang(fr) %{_mandir}/fr/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/access.1*
%lang(pl) %{_mandir}/pl/man1/access.1*
%attr(755,root,root) %{_bindir}/afm2tfm
%lang(fi) %{_mandir}/fi/man1/afm2tfm.1*
%{_mandir}/man1/afm2tfm.1*
%attr(755,root,root) %{_bindir}/allcm
%{_mandir}/man1/allcm.1*
%lang(fi) %{_mandir}/fi/man1/allcm.1*
%attr(755,root,root) %{_bindir}/allec
%{_mandir}/man1/allec.1*
%attr(755,root,root) %{_bindir}/allneeded
%{_mandir}/man1/allneeded.1*
%lang(fi) %{_mandir}/fi/man1/allneeded.1*
%attr(755,root,root) %{_bindir}/dmp
%{_mandir}/man1/dmp.1*
%attr(755,root,root) %{_bindir}/e2pall
%{_mandir}/man1/e2pall.1*
%attr(755,root,root) %{_bindir}/fdf2tan
%attr(755,root,root) %{_bindir}/gftodvi
%{_mandir}/man1/gftodvi.1*
%attr(755,root,root) %{_bindir}/gftopk
%{_mandir}/man1/gftopk.1*
%attr(755,root,root) %{_bindir}/gftype
%{_mandir}/man1/gftype.1*
%attr(755,root,root) %{_bindir}/gsftopk
%{_mandir}/man1/gsftopk.1*
%attr(755,root,root) %{_bindir}/mag
%{_mandir}/man1/mag.1*
%attr(755,root,root) %{_bindir}/makempx
%{_mandir}/man1/makempx.1*
%attr(755,root,root) %{_bindir}/makempy
%attr(755,root,root) %{_bindir}/MakeTeXPK
%{_mandir}/man1/MakeTeXPK.1*
#%attr(755,root,root) %{_bindir}/metafun
%attr(755,root,root) %{_bindir}/mkfontdesc
%{_mandir}/man8/mkfontdesc.8*
%attr(755,root,root) %{_bindir}/mktexmf
%{_mandir}/man1/mktexmf.1*
%attr(755,root,root) %{_bindir}/mktexpk
%{_mandir}/man1/mktexpk.1*
%attr(755,root,root) %{_bindir}/mktextfm
%{_mandir}/man1/mktextfm.1*
%attr(755,root,root) %{_bindir}/pfb2pfa
%{_mandir}/man1/pfb2pfa.1*
%attr(755,root,root) %{_bindir}/pk2bm
%{_mandir}/man1/pk2bm.1*
%attr(755,root,root) %{_bindir}/pktogf
%{_mandir}/man1/pktogf.1*
%attr(755,root,root) %{_bindir}/pktype
%{_mandir}/man1/pktype.1*
%attr(755,root,root) %{_bindir}/pltotf
%{_mandir}/man1/pltotf.1*
%attr(755,root,root) %{_bindir}/pooltype
%{_mandir}/man1/pooltype.1*
%attr(755,root,root) %{_bindir}/ps2frag
%{_mandir}/man1/ps2frag.1*
%attr(755,root,root) %{_bindir}/ps2pk
%{_mandir}/man1/ps2pk.1*
%attr(755,root,root) %{_bindir}/readlink
%{_mandir}/man1/readlink.1*
%lang(hu) %{_mandir}/hu/man1/readlink.1*
%attr(755,root,root) %{_bindir}/t1mapper
%{_mandir}/man1/t1mapper.1*
%attr(755,root,root) %{_bindir}/tangle
%{_mandir}/man1/tangle.1*
%attr(755,root,root) %{_bindir}/texshow
%{_mandir}/man1/texshow.1*
%attr(755,root,root) %{_bindir}/texlinks
%{_mandir}/man8/texlinks.8*
%attr(755,root,root) %{_bindir}/tftopl
%{_mandir}/man1/tftopl.1*
%attr(755,root,root) %{_bindir}/ttf2afm
%attr(755,root,root) %{_bindir}/vftovp
%{_mandir}/man1/vftovp.1*
%attr(755,root,root) %{_bindir}/vptovf
%{_mandir}/man1/vptovf.1*
%attr(755,root,root) %{_bindir}/newer
%{_mandir}/man1/newer.1*
%lang(pl) %{_mandir}/pl/man1/newer.1*
%lang(hu) %{_mandir}/hu/man1/newer.1*
%attr(755,root,root) %{_bindir}/patgen
%{_mandir}/man1/patgen.1*
# a mo¿e do podpakietu ?
%attr(755,root,root) %{_bindir}/texi2html
%{_mandir}/man1/texi2html.1*
%attr(755,root,root) %{_bindir}/texi2pdf
%{_mandir}/man1/texi2pdf.1*

# czy to jest jeszvze potrzebne ?
%attr(755,root,root) %{_bindir}/tetex-updmap
# do programowania w web2c
%attr(755,root,root) %{_bindir}/weave
%{_mandir}/man1/weave.1*
%attr(755,root,root) %{_bindir}/tie
%{_mandir}/man1/tie.1*

%{_datadir}/info/web2c.info*
%{_datadir}/texmf/updates.dat

%dir %{_datadir}/texmf/fonts
%dir %{_datadir}/texmf/fonts/afm
%dir %{_datadir}/texmf/fonts/afm/public
#%dir %{_datadir}/texmf/fonts/ofm
#%dir %{_datadir}/texmf/fonts/ofm/public
%dir %{_datadir}/texmf/fonts/ovf
%dir %{_datadir}/texmf/fonts/ovf/public
%dir %{_datadir}/texmf/fonts/ovp
%dir %{_datadir}/texmf/fonts/ovp/public
#%dir %{_datadir}/texmf/fonts/pfm
#%dir %{_datadir}/texmf/fonts/pfm/public
%dir %{_datadir}/texmf/fonts/pk
%dir %{_datadir}/texmf/fonts/source
%dir %{_datadir}/texmf/fonts/source/public
%dir %{_datadir}/texmf/fonts/tfm
%dir %{_datadir}/texmf/fonts/tfm/public
%dir %{_datadir}/texmf/fonts/type1
%dir %{_datadir}/texmf/fonts/type1/public
%dir %{_datadir}/texmf/fonts/vf
%dir %{_datadir}/texmf/fonts/vf/public
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/ls-R
%dir %{_datadir}/texmf
%{_datadir}/texmf/aliases
%{_datadir}/texmf/ChangeLog
#%dir %{_datadir}/texmf/source
%{_datadir}/texmf/web2c/metafun.mem
%attr(1777,root,root) /var/cache/fonts

%{_datadir}/texmf/web2c/tex-pl.pool
%{_datadir}/texmf/web2c/tex.pool
%{_datadir}/texmf/web2c/*.tcx
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/texmf.cnf
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/mktex.cnf
%attr(755,root,root) %{_datadir}/texmf/web2c/mktexdir
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/mktexdir.opt
%attr(755,root,root) %{_datadir}/texmf/web2c/mktexnam
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/mktexnam.opt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/mktex.opt
%attr(755,root,root) %{_datadir}/texmf/web2c/mktexupd
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/fmtutil.cnf
#%files tex
#%defattr(644,root,root,755)
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/fontmath.cfg
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/fonttext.cfg
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/preload.cfg

%{texmf}/tex/texinfo

%files -n kpathsea
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/kpathsea.dvi
%doc %{texmf}/doc/programs/kpathsea.pdf
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*
%{_libdir}/libkpathsea.so.*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so
%{_infodir}/kpathsea.info*

%files dvips
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/dvips.dvi
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%attr(755,root,root) %{_bindir}/dvicopy
# dvi2fax requires ghostscript
%attr(755,root,root) %{_bindir}/dvi2fax
%{_infodir}/dvips.info*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%lang(fi) %{_mandir}/fi/man1/dvips.1*
%dir %{texmf}/dvips
%{texmf}/dvips/base
%{texmf}/dvips/misc
%{texmf}/dvips/tetex
%{texmf}/dvips/gsftopk
%{texmf}/dvips/psfrag
%{texmf}/dvips/psnfss
%{texmf}/dvips/pstricks
%dir %{texmf}/dvips/config
%{texmf}/dvips/config/builtin35.map
%config(noreplace) %verify(not size md5 mtime) %{texmf}/dvips/config/config.ps
%{texmf}/dvips/config/download35.map
%{texmf}/dvips/config/ps2pk.map
%{texmf}/dvips/config/psfonts_pk.map
%{texmf}/dvips/config/config.generic
%{texmf}/dvips/config/context.map
%{texmf}/dvips/config/psfonts.map
%{texmf}/dvips/config/psfonts_t1.map

%files dvilj
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvihp
%attr(755,root,root) %{_bindir}/dvilj
%attr(755,root,root) %{_bindir}/dvilj2p
%attr(755,root,root) %{_bindir}/dvilj4
%attr(755,root,root) %{_bindir}/dvilj4l
%attr(755,root,root) %{_bindir}/dvilj6
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvilj.1*

%files -n xdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvi
%attr(755,root,root) %{_bindir}/xdvi.bin
%{_mandir}/man1/xdvi.1*
%{_prefix}/X11R6/share/applnk/Graphics/Viewers/xdvi.desktop
%dir %{texmf}/xdvi
#%{texmf}/xdvi/ps2pk.map
%{texmf}/xdvi/XDvi
%{texmf}/xdvi/xdvi.cfg

%files pdftex
%doc %{texmf}/doc/pdftex
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/pdfvirtex
%attr(755,root,root) %{_bindir}/pdfinitex
%{texmf}/dvips/config/pdftex.map
%{texmf}/dvips/config/pdftex_dl14.map
%{texmf}/dvips/config/pdftex_ndl14.map
%dir %{texmf}/pdftex
%dir %{texmf}/pdftex/config
%{texmf}/pdftex/config/cmttf.map
%{texmf}/pdftex/config/pdftex.cfg
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdfinitex.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/pdfvirtex.1*

%files plain
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain
%dir %{texmf}/tex/plain/base
%dir %{texmf}/tex/plain/config
%dir %{texmf}/tex/plain/graphics
%{texmf}/tex/plain/config/tex.ini
%{texmf}/tex/plain/base/*
%{texmf}/tex/plain/graphics/*
%{texmf}/web2c/plain.mem
%{texmf}/web2c/plain.base

%files plain-dvips
%defattr(644,root,root,755)
%{texmf}/tex/plain/dvips/

%files plain-mathtime
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mathtime
%{texmf}/tex/plain/mathtime

%files plain-misc
%defattr(644,root,root,755)
%{texmf}/tex/plain/misc/

%files format-plain
%defattr(644,root,root,755)
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/tex.fmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/plain.fmt

%files format-bplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bplain
%{texmf}/tex/plain/config/bplain.ini
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/bplain.fmt

%files format-pdftex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/plain
%{texmf}/pdftex/plain/config
%{texmf}/pdftex/plain/misc
%{_datadir}/texmf/web2c/pdftex-pl.pool
%{_datadir}/texmf/web2c/pdftex.pool
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdftex.fmt

%files format-pdfetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pdfevirtex
%attr(755,root,root) %{_bindir}/pdfeinitex
%dir %{texmf}/pdfetex
%dir %{texmf}/pdfetex/tex
%{texmf}/pdfetex/tex/config
%{_mandir}/man1/pdfetex.1*
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfetex.efmt
%{_datadir}/texmf/web2c/pdfetex-pl.pool
%{_datadir}/texmf/web2c/pdfetex.pool

%files mex
%defattr(644,root,root,755)
%doc %{texmf}/doc/polish/mex
%dir %{texmf}/tex/mex
%dir %{texmf}/tex/mex/base
%{texmf}/tex/mex/base/mex1.tex
%{texmf}/tex/mex/base/mex2.tex
%{texmf}/tex/mex/base/mex.tex
%dir %{texmf}/tex/mex/config
%{texmf}/tex/mex/config/mexconf.tex
%{texmf}/tex/mex/config/mex.ini

%files format-mex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mex
%attr(755,root,root) %{_bindir}/mex-pl
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/mex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/mex-pl.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfmex
%attr(755,root,root) %{_bindir}/pdfmex-pl
%dir %{texmf}/pdftex/mex
%{texmf}/pdftex/mex/config
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfmex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfmex-pl.fmt

%files format-pdfemex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfemex
%attr(755,root,root) %{_bindir}/pdfemex-pl
%dir %{texmf}/pdfetex/mex
%{texmf}/pdfetex/mex/config
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfemex.efmt

%files amstex
%defattr(644,root,root,755)
%{texmf}/tex/amstex/base
%{texmf}/tex/amstex/config
%{texmf}/tex/plain/amsfonts

%files format-amstex
%defattr(644,root,root,755)
%doc %{texmf}/doc/amstex
%attr(755,root,root) %{_bindir}/amstex
%{_mandir}/man1/amstex.1*
%lang(fi) %{_mandir}/fi/man1/amstex.1*
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/amstex.fmt

%files format-bamstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bamstex
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/bamstex.fmt

%files format-pdfamstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfamstex
%{texmf}/pdftex/amstex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfamstex.fmt

%files csplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex
%attr(755,root,root) %{_bindir}/csplain
%{texmf}/tex/csplain

%files format-csplain
%defattr(644,root,root,755)
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/csplain.fmt

%files format-pdfcsplain
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/pdfcsplain
#%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/pdfcsplain.fmt

%files cyrplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cyrplain
%{texmf}/tex/cyrplain/

%files format-cyrplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyrtex
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cyrtex.fmt

%files eplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/etex
%doc %{texmf}/doc/eplain
%attr(755,root,root) %{_bindir}/etex
%attr(755,root,root) %{_bindir}/evirtex
%attr(755,root,root) %{_bindir}/einitex
%attr(755,root,root) %{_bindir}/eplain
%{_mandir}/man1/einitex.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{_mandir}/man1/evirtex.1*
%dir %{texmf}/etex
%dir %{texmf}/etex/plain
%dir %{texmf}/etex/plain/base
%dir %{texmf}/etex/plain/config
%{texmf}/tex/eplain
%{texmf}/etex/plain/base/etexdefs.lib
%{texmf}/etex/plain/base/etex.src
%{texmf}/etex/plain/config/etex.ini
%{texmf}/etex/plain/config/language.def
%{texmf}/web2c/etex.pool
%{texmf}/web2c/etex-pl.pool

%files format-eplain
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/etex.efmt
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/eplain.fmt

%files latex
%defattr(644,root,root,755)
%dir %{texmf}/doc/latex
%doc %{texmf}/doc/latex/SIunits
%doc %{texmf}/doc/latex/base
%doc %{texmf}/doc/latex/caption
%doc %{texmf}/doc/latex/dinbrief
%doc %{texmf}/doc/latex/eepic
%doc %{texmf}/doc/latex/fancy*
%doc %{texmf}/doc/latex/float*
%doc %{texmf}/doc/latex/g-brief
%doc %{texmf}/doc/latex/geometry
%doc %{texmf}/doc/latex/graphics
%doc %{texmf}/doc/latex/hyperref
%doc %{texmf}/doc/latex/koma-script
%doc %{texmf}/doc/latex/mdwtools
%doc %{texmf}/doc/latex/ms
%doc %{texmf}/doc/latex/mwcls
%doc %{texmf}/doc/latex/natbib
%doc %{texmf}/doc/latex/ntgclass
%doc %{texmf}/doc/latex/oberdiek
%doc %{texmf}/doc/latex/pb-diagram
%doc %{texmf}/doc/latex/rotating
%doc %{texmf}/doc/latex/rotfloat
%doc %{texmf}/doc/latex/revtex4
%doc %{texmf}/doc/latex/scale
%doc %{texmf}/doc/latex/showlabels
%doc %{texmf}/doc/latex/sidecap
%doc %{texmf}/doc/latex/supertab
%doc %{texmf}/doc/latex/units
%doc %{texmf}/doc/latex/seminar
%doc %{texmf}/doc/latex/tools
%doc %{texmf}/doc/latex/general
%doc %{texmf}/doc/latex/pslatex
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%lang(fi) %{_mandir}/fi/man1/latex.1*
%lang(pl) %{_mandir}/pl/man1/latex.1*
%{_infodir}/latex.info*

%dir %{texmf}/tex/latex
%{texmf}/tex/latex/SIunits
%{texmf}/tex/latex/base
%{texmf}/tex/latex/caption
%{texmf}/tex/latex/config
%{texmf}/tex/latex/curves
%{texmf}/tex/latex/dinbrief
%{texmf}/tex/latex/dvilj
%{texmf}/tex/latex/eepic
%{texmf}/tex/latex/endfloat
%{texmf}/tex/latex/fancy*
%{texmf}/tex/latex/fp
%{texmf}/tex/latex/g-brief
%{texmf}/tex/latex/graphics
%{texmf}/tex/latex/hyperref
%{texmf}/tex/latex/koma-script
%{texmf}/tex/latex/labels
%{texmf}/tex/latex/listings
%{texmf}/tex/latex/mdwtools
%{texmf}/tex/latex/misc
%{texmf}/tex/latex/ms
%{texmf}/tex/latex/multirow
%{texmf}/tex/latex/mwcls
%{texmf}/tex/latex/natbib
%{texmf}/tex/latex/ntgclass
%{texmf}/tex/latex/oberdiek
%{texmf}/tex/latex/pb-diagram
%{texmf}/tex/latex/revtex4
%{texmf}/tex/latex/seminar
%{texmf}/tex/latex/t2
%{texmf}/tex/latex/titlesec
%{texmf}/tex/latex/tools
%{texmf}/tex/latex/units

%files latex-ae
%defattr(644,root,root,755)
%{texmf}/tex/latex/ae

%files latex-bbm
%defattr(644,root,root,755)
%{texmf}/tex/latex/bbm

%files latex-ams
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/amscls
%doc %{texmf}/doc/latex/amsmath
%doc %{texmf}/doc/latex/amsfonts
%{texmf}/tex/latex/amscls
%{texmf}/tex/latex/amsmath
%{texmf}/tex/latex/amsfonts

%files latex-antp
%defattr(644,root,root,755)
%{texmf}/tex/latex/antp

%files latex-antt
%defattr(644,root,root,755)
%{texmf}/tex/latex/antt

%files latex-carlisle
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/carlisle
%{texmf}/tex/latex/carlisle

%files latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/ccfonts
%{texmf}/tex/latex/ccfonts

%files latex-cite
%defattr(644,root,root,755)
%{texmf}/tex/latex/cite

%files latex-concmath
%defattr(644,root,root,755)
%{texmf}/tex/latex/concmath

%files latex-custom-bib
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/custom-bib
%{texmf}/tex/latex/custom-bib

%files latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/cyrillic
%{texmf}/tex/latex/cyrillic

%files latex-dstroke
%defattr(644,root,root,755)
%{texmf}/tex/latex/dstroke

%files latex-jknappen
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/jknappen
%{texmf}/tex/latex/jknappen

%files latex-lucidabr
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/lucidabr
%{texmf}/tex/latex/lucidabr

%files latex-psnfss
%doc %{texmf}/doc/latex/psnfss
%defattr(644,root,root,755)
%{texmf}/tex/latex/psnfss

%files format-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/latex.fmt

%files format-elatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elatex
%{_mandir}/man1/elatex.1*
%{texmf}/etex/latex/config
%{texmf}/etex/latex/misc
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/elatex.efmt

%files format-pdflatex
%defattr(644,root,root,755)
%{texmf}/pdftex/latex/config
%dir %{texmf}/pdftex/latex
%attr(755,root,root) %{_bindir}/pdflatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdflatex.fmt
%{_mandir}/man1/pdflatex.1*

%files format-pdfelatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfelatex
%dir %{texmf}/pdfetex/latex
%{texmf}/pdfetex/latex/config
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfelatex.efmt

# ----------------------------


%files bibtex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bibtex
%{_mandir}/man1/bibtex.1*
%dir %{texmf}/doc/bibtex
%doc %{texmf}/doc/bibtex/base
%dir %{texmf}/bibtex
%dir %{texmf}/bibtex/bib
%{texmf}/bibtex/bib/base
%dir %{texmf}/bibtex/bst
%doc %{texmf}/bibtex/bib/README
%{texmf}/bibtex/bst/base
%{texmf}/bibtex/bst/misc

%files bibtex-ams
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/ams
%{texmf}/bibtex/bst/ams

%files bibtex-adrconv
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/adrconv

%files bibtex-plbib
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/plbib
%{texmf}/bibtex/bst/plbib

%files bibtex-germbib
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/germbib

#%files bibtex-koma-script
#%defattr(644,root,root,755)
#%{texmf}/bibtex/bst/koma-script

%files bibtex-natbib
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/natbib

%files bibtex-revtex4
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/revtex4

%files fonts-adobe
%defattr(644,root,root,755)
%{texmf}/fonts/afm/adobe
%{texmf}/fonts/tfm/adobe
%{texmf}/fonts/vf/adobe

%files fonts-bitstrea
%defattr(644,root,root,755)
%{texmf}/fonts/afm/bitstrea
%{texmf}/fonts/tfm/bitstrea
%{texmf}/fonts/vf/bitstrea

%files fonts-antp
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/antp
%{texmf}/fonts/afm/public/antp
%{texmf}/fonts/tfm/public/antp

%files fonts-antt
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/antt
%{texmf}/fonts/afm/public/antt
%{texmf}/fonts/tfm/public/antt

%files fonts-marvosym
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/marvosym
%{texmf}/fonts/afm/public/marvosym
%{texmf}/fonts/tfm/public/marvosym

#%files fonts-omega
#%defattr(644,root,root,755)
#%{texmf}/fonts/afm/public/omega
#%{texmf}/fonts/ofm/public/omega
#%{texmf}/fonts/ovf/public/omega
#%{texmf}/fonts/ovp/public/omega
#%{texmf}/fonts/tfm/public/omega

%files fonts-qfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qfonts
%{texmf}/dvips/qfonts/
%{texmf}/fonts/afm/public/qfonts
%{texmf}/fonts/tfm/public/qfonts

%files fonts-xypic
%defattr(644,root,root,755)
%{texmf}/fonts/afm/public/xypic
#%{texmf}/fonts/pfm/public/xypic
%{texmf}/fonts/source/public/xypic
%{texmf}/fonts/tfm/public/xypic

%files fonts-urw
%defattr(644,root,root,755)
%{texmf}/fonts/afm/urw

%files fonts-yandy
%defattr(644,root,root,755)
%{texmf}/fonts/afm/yandy
%{texmf}/fonts/source/yandy
%{texmf}/fonts/tfm/yandy
%{texmf}/fonts/vf/yandy

%files fonts-ams
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/amsfonts
%{texmf}/fonts/source/ams
%{texmf}/fonts/tfm/ams

%files fonts-jknappen
%defattr(644,root,root,755)
%{texmf}/fonts/source/jknappen
%{texmf}/fonts/tfm/jknappen

%files fonts-lh
%defattr(644,root,root,755)
%{texmf}/fonts/source/lh

%files fonts-bbm
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/bbm
%{texmf}/fonts/tfm/public/bbm

%files fonts-bbold
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/bbold
%{texmf}/fonts/tfm/public/bbold

%files fonts-cbgreek
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cbgreek
%{texmf}/fonts/source/public/cbgreek

%files fonts-cc-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/cc-pl
%{texmf}/dvips/cc-pl
%{texmf}/fonts/source/public/cc-pl
%{texmf}/fonts/tfm/public/cc-pl

%files fonts-cm
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cm
%{texmf}/fonts/source/public/cm
%{texmf}/fonts/tfm/public/cm

%files fonts-cmcyr
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/cmcyr
%{texmf}/fonts/vf/public/cmcyr

%files fonts-cm-bold
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/cm-bold

%files fonts-cmextra
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/cmextra
%{texmf}/fonts/tfm/public/cmextra

%files fonts-concmath
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/concmath
%{texmf}/fonts/tfm/public/concmath

%files fonts-concrete
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/concrete
%{texmf}/fonts/tfm/public/concrete

%files fonts-cs
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/cs
%{texmf}/fonts/tfm/public/cs

%files fonts-dstroke
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/dstroke
%{texmf}/fonts/source/public/dstroke

%files fonts-ecc
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/ecc
%{texmf}/fonts/source/public/ecc
%{texmf}/fonts/tfm/public/ecc

%files fonts-euxm
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/euxm
%{texmf}/fonts/tfm/public/euxm

%files fonts-gothic
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/gothic
%{texmf}/fonts/tfm/public/gothic

%files fonts-latex
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/latex
%{texmf}/fonts/tfm/public/latex

%files fonts-mflogo
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/mflogo
%{texmf}/fonts/tfm/public/mflogo

%files fonts-misc
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/misc
%{texmf}/fonts/tfm/public/misc

%files fonts-pandora
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/pandora
%{texmf}/fonts/tfm/public/pandora

%files fonts-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/pl
%{texmf}/dvips/pl
%{texmf}/fonts/source/public/pl
%{texmf}/fonts/afm/public/pl
%{texmf}/fonts/tfm/public/pl

%files fonts-rsfs
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/rsfs
%{texmf}/fonts/tfm/public/rsfs

%files fonts-stmaryrd
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/stmaryrd
%{texmf}/fonts/tfm/public/stmaryrd

%files fonts-vnr
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/vnr
%{texmf}/fonts/tfm/public/vnr

%files fonts-wasy
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/wasy
%{texmf}/fonts/tfm/public/wasy

%files fonts-bh
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/bh
%{texmf}/fonts/vf/bh

%files fonts-cg
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/cg
%{texmf}/fonts/vf/cg

%files fonts-hoekwater
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/hoekwater
%{texmf}/fonts/tfm/hoekwater

%files fonts-monotype
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/monotype
%{texmf}/fonts/vf/monotype

%files fonts-ae
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/ae
%{texmf}/fonts/tfm/public/ae
%{texmf}/fonts/vf/public/ae

#%files fonts-mathpple
#%defattr(644,root,root,755)
#%{texmf}/fonts/tfm/public/mathpple
#%{texmf}/fonts/vf/public/mathpple

%files fonts-pazo
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/pazo
%{texmf}/fonts/vf/public/pazo

%files fonts-vcm
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/vcm
%{texmf}/fonts/vf/public/vcm

%files fonts-type1-adobe
%defattr(644,root,root,755)
%{texmf}/fonts/type1/adobe

%files fonts-type1-bitstrea
%defattr(644,root,root,755)
%{texmf}/fonts/type1/bitstrea

%files fonts-type1-bluesky
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/bluesky
%{texmf}/dvips/bluesky
%{texmf}/fonts/type1/bluesky

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
# hmm, mo¿e jeszcze rozpisaæ?
%{texmf}/fonts/type1/hoekwater

%files fonts-type1-antp
%defattr(644,root,root,755)
%{texmf}/dvips/antp
%{texmf}/fonts/type1/public/antp

%files fonts-type1-antt
%defattr(644,root,root,755)
%{texmf}/dvips/antt
%{texmf}/fonts/type1/public/antt

%files fonts-type1-belleek
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/belleek
%{texmf}/fonts/type1/public/belleek

%files fonts-type1-cmcyr
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/cmcyr

%files fonts-type1-cs
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/cs

%files fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/mathpazo
%{texmf}/fonts/type1/public/mathpazo

#%files fonts-type1-omega
#%defattr(644,root,root,755)
#%{texmf}/fonts/type1/public/omega

%files fonts-type1-pl
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/pl

%files fonts-type1-qfonts
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/qfonts

%files fonts-type1-xypic
%defattr(644,root,root,755)
%{texmf}/dvips/xypic
%{texmf}/fonts/type1/public/xypic

%files fonts-type1-urw
%defattr(644,root,root,755)
%{texmf}/fonts/type1/urw

%files makeindex
%defattr(644,root,root,755)
%doc %{texmf}/doc/makeindex
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/makeindex
%{texmf}/makeindex
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*

%files metafont
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mfw
%attr(755,root,root) %{_bindir}/virmf
%attr(755,root,root) %{_bindir}/inimf
%{texmf}/metafont
%dir %{_datadir}/texmf/mft
%{_datadir}/texmf/mft/cmbase.mft
%{_datadir}/texmf/mft/e.mft
%{_datadir}/texmf/mft/mplain.mft
%{_datadir}/texmf/mft/plain.mft
%{_datadir}/texmf/mft/pl.mft
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/inimf.1*
%{_mandir}/man1/virmf.1*
%{_datadir}/texmf/web2c/mf.base
%{_datadir}/texmf/web2c/mf-nowin.base
%{_datadir}/texmf/web2c/mf.pool
%{_datadir}/texmf/web2c/mfw.base

%files matapost
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%attr(755,root,root) %{_bindir}/mptopdf
%attr(755,root,root) %{_bindir}/virmpost
%attr(755,root,root) %{_bindir}/inimpost
%doc %{texmf}/doc/metapost
%dir %{texmf}/metapost
%{texmf}/metapost/base
%{texmf}/metapost/config
%{texmf}/metapost/mfpic
%{texmf}/metapost/misc
#%files metapost-context
%{texmf}/metapost/context
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{_mandir}/man1/inimpost.1*
%{_mandir}/man1/virmpost.1*
%{_datadir}/texmf/web2c/mpost.mem
%{_datadir}/texmf/web2c/mp.pool

#%files format-omega
#%defattr(644,root,root,755)
##%doc %{texmf}/doc/omega
#%attr(755,root,root) %{_bindir}/mkocp
#%attr(755,root,root) %{_bindir}/mkofm
#%attr(755,root,root) %{_bindir}/ofm2opl
#%attr(755,root,root) %{_bindir}/omega
#%attr(755,root,root) %{_bindir}/omfonts
#%attr(755,root,root) %{_bindir}/opl2ofm
#%attr(755,root,root) %{_bindir}/otangle
#%attr(755,root,root) %{_bindir}/otp2ocp
#%attr(755,root,root) %{_bindir}/outocp
#%attr(755,root,root) %{_bindir}/ovf2ovp
#%attr(755,root,root) %{_bindir}/ovp2ovf
#%attr(755,root,root) %{_bindir}/viromega
#%{_mandir}/man1/viromega.1*
#%attr(755,root,root) %{_bindir}/iniomega
#%{_mandir}/man1/iniomega.1*
#%{_mandir}/man1/omega.1*
#%dir %{texmf}/omega
#%{texmf}/omega/encodings
##%files omega-plain
#%dir %{texmf}/omega/plain
#%{texmf}/omega/plain/base
#%{texmf}/omega/plain/config
##%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/omega.fmt
#%{_datadir}/texmf/web2c/omega.pool

#%files format-omega-lambda
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/lambda
#%{_mandir}/man1/lambda.1*
#%dir %{texmf}/omega/lambda
#%{texmf}/omega/lambda/base
#%{texmf}/omega/lambda/config
#%{texmf}/omega/lambda/misc
#%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/lambda.fmt

#%files omega-ocp
#%defattr(644,root,root,755)
#%dir %{texmf}/omega/ocp
#%{texmf}/omega/ocp/char2uni
#%{texmf}/omega/ocp/misc
#%{texmf}/omega/ocp/omega
#%{texmf}/omega/ocp/uni2char

#%files omega-otp
#%defattr(644,root,root,755)
#%dir %{texmf}/omega/otp
#%{texmf}/omega/otp/char2uni
#%{texmf}/omega/otp/misc
#%{texmf}/omega/otp/omega
#%{texmf}/omega/otp/uni2char

# format?
%files format-pdftex-context
%defattr(644,root,root,755)
# zferyfikowac pliki z fontami
%{texmf}/pdftex/config/context

#%files format-pdfcslatex
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/pdfcslatex
# jaki¶ problem z generowaniem
#%config(noreplace) %verify(not md5 size mtime) /usr/share/texmf/web2c/pdfcslatex.fmt

%files format-pdfplatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/platex
%{texmf}/pdftex/platex/config
%attr(755,root,root) %{_bindir}/pdfplatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfplatex.fmt

%files texconfig
%defattr(644,root,root,755)
%{texmf}/texconfig
%attr(755,root,root) %{_bindir}/texconfig
%{_mandir}/man1/texconfig.1*

%files format-context
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/cont-cz
%attr(755,root,root) %{_bindir}/cont-de
%attr(755,root,root) %{_bindir}/cont-en
%attr(755,root,root) %{_bindir}/cont-nl
#%attr(755,root,root) %{_bindir}/cont-uk
%{_mandir}/man1/cont-de.1*
%{_mandir}/man1/cont-en.1*
%{_mandir}/man1/cont-nl.1*
%dir %{texmf}/doc/context
%doc %{texmf}/doc/context/base
%dir %{texmf}/doc/context/ppchtex
%doc %{texmf}/doc/context/ppchtex/mp-ch-en.pdf
%dir %{texmf}/context
%dir %{texmf}/context/config
%{texmf}/context/config/texexec.ini
%{texmf}/context/config/texexec.rme
%dir %{texmf}/context/data
%{texmf}/context/data/conedt.ini
%{texmf}/context/data/cont-cz.tws
%{texmf}/context/data/cont-de.tws
%{texmf}/context/data/cont-en.tws
%{texmf}/context/data/cont-it.tws
%{texmf}/context/data/cont-nl.tws
%{texmf}/context/data/cont-ro.tws
%{texmf}/context/data/type-buy.dat
%{texmf}/context/data/type-tmf.dat
%{texmf}/context/perltk
%{texmf}/tex/generic/context/
%{texmf}/tex/latex/context/
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-cz.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-de.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-en.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-nl.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-uk.efmt


%dir %{texmf}/tex/context
%{texmf}/tex/context/base
%dir %{texmf}/tex/context/config
%{texmf}/tex/context/config/cont-cz.ini
%{texmf}/tex/context/config/cont-de.ini
%{texmf}/tex/context/config/cont-en.ini
%{texmf}/tex/context/config/cont-it.ini
%{texmf}/tex/context/config/cont-nl.ini
%{texmf}/tex/context/config/cont-ro.ini
%{texmf}/tex/context/config/cont-uk.ini
%{texmf}/tex/context/config/cont-usr.tex
%{texmf}/tex/context/extra
%{texmf}/tex/context/sample
%{texmf}/tex/context/user

%files texdoctk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texdoctk
%{_mandir}/man1/texdoctk.1*
%doc %{texmf}/doc/texdoctk
%{texmf}/texdoctk

%files fontinst
%defattr(644,root,root,755)
# zferyfikowaæ zawarto¶æ z tym co jest w pakietach z fontami
%doc %{texmf}/doc/fontinst
%dir %{texmf}/tex/fontinst
%{texmf}/tex/fontinst/base

%files doc-Catalogue
%defattr(644,root,root,755)
%{texmf}/doc/help/Catalogue

#%files doc-de-tex-faq
#%defattr(644,root,root,755)
#%{texmf}/doc/help/faq/de-tex-faq

#%files doc-LaTeX-FAQ-francaise
#%defattr(644,root,root,755)
#%{texmf}/doc/help/faq/LaTeX-FAQ-francaise

%files doc-uktug-faq
%defattr(644,root,root,755)
%{texmf}/doc/help/faq/uktug-faq

%files doc-latex2e-html
%defattr(644,root,root,755)
%{texmf}/doc/latex/latex2e-html

%files doc
%defattr(644,root,root,755)
%{texmf}/doc/README
%{texmf}/doc/README.knuth
%{texmf}/doc/tetex/teTeX-FAQ
%dir %{texmf}/doc/tetex
%{texmf}/doc/tetex.gif
%{texmf}/doc/tetex.png

%files platex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/platex
%attr(755,root,root) %{_bindir}/platex
%attr(755,root,root) %{_bindir}/platex-pl
%dir %{texmf}/tex/platex
%dir %{texmf}/tex/platex/config
%{texmf}/tex/platex/config/hyphen.cfg
%{texmf}/tex/platex/config/language.dat
%{texmf}/tex/platex/config/platex.ini
# a mo¿e jako¶ osobno to daæ?
%dir %{texmf}/tex/latex/platex
%{texmf}/tex/latex/platex/amigapl.def
%{texmf}/tex/latex/platex/mazovia.def
%{texmf}/tex/latex/platex/omlplcm.fd
%{texmf}/tex/latex/platex/omlplm.fd
%{texmf}/tex/latex/platex/omsplsy.fd
%{texmf}/tex/latex/platex/omxplex.fd
%{texmf}/tex/latex/platex/ot1patch.sty
%{texmf}/tex/latex/platex/ot4ccr.fd
%{texmf}/tex/latex/platex/ot4cmdh.fd
%{texmf}/tex/latex/platex/ot4cmfib.fd
%{texmf}/tex/latex/platex/ot4cmfr.fd
%{texmf}/tex/latex/platex/ot4cmr.fd
%{texmf}/tex/latex/platex/ot4cmss.fd
%{texmf}/tex/latex/platex/ot4cmtt.fd
%{texmf}/tex/latex/platex/plprefix.sty
%{texmf}/tex/latex/platex/polski.sty
%{texmf}/tex/latex/platex/qxenc.def

%files format-platex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/platex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/platex-pl.fmt

%files plain-plnfss
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain/plnfss
%{texmf}/tex/plain/plnfss/ams.pfd
%{texmf}/tex/plain/plnfss/il2cmr.pfd
%{texmf}/tex/plain/plnfss/MIKmathf.tex
%{texmf}/tex/plain/plnfss/ot1cmr.pfd
%{texmf}/tex/plain/plnfss/plnfss.tex
%{texmf}/tex/plain/plnfss/t5cmr.pfd
%{texmf}/tex/plain/plnfss/t5vcmr.pfd

%files cslatex
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex/INSTALL.cslatex
%doc %{texmf}/doc/cstex/README.cslatex
%attr(755,root,root) %{_bindir}/cslatex
%{texmf}/tex/cslatex
%dir %{texmf}/tex/latex/cslatex
%{texmf}/tex/latex/cslatex/cspsfont.il2
%{texmf}/tex/latex/cslatex/cspsfont.tex
%{texmf}/tex/latex/cslatex/cspsfont.xl2
%{texmf}/tex/latex/cslatex/il2pag.fd
%{texmf}/tex/latex/cslatex/il2pbk.fd
%{texmf}/tex/latex/cslatex/il2pcr.fd
%{texmf}/tex/latex/cslatex/il2phv.fd
%{texmf}/tex/latex/cslatex/il2phvn.fd
%{texmf}/tex/latex/cslatex/il2pnc.fd
%{texmf}/tex/latex/cslatex/il2ppl.fd
%{texmf}/tex/latex/cslatex/il2ptm.fd
%{texmf}/tex/latex/cslatex/il2pzc.fd
%{texmf}/tex/latex/cslatex/nhelvet.sty
%{texmf}/tex/latex/cslatex/ntimes.sty
%{texmf}/tex/latex/cslatex/xl2pag.fd
%{texmf}/tex/latex/cslatex/xl2pbk.fd
%{texmf}/tex/latex/cslatex/xl2pcr.fd
%{texmf}/tex/latex/cslatex/xl2phv.fd
%{texmf}/tex/latex/cslatex/xl2phvn.fd
%{texmf}/tex/latex/cslatex/xl2pnc.fd
%{texmf}/tex/latex/cslatex/xl2ppl.fd
%{texmf}/tex/latex/cslatex/xl2ptm.fd
%{texmf}/tex/latex/cslatex/xl2pzc.fd


%files fontname
%defattr(644,root,root,755)
# z dokumentacji wynika ¿e nie ma sensu tego rozdzielaæ po pakietach
%doc %{texmf}/doc/fonts/fontname
%dir %{texmf}/fontname
%{texmf}/fontname/adobe.map
%{texmf}/fontname/apple.map
%{texmf}/fontname/bitstrea.map
%{texmf}/fontname/dtc.map
%{texmf}/fontname/itc.map
%{texmf}/fontname/linot-cd.map
%{texmf}/fontname/linotype.map
%{texmf}/fontname/monotype.map
%{texmf}/fontname/skey1250.map
%{texmf}/fontname/skey1555.map
%{texmf}/fontname/softkey.map
%{texmf}/fontname/special.map
%{texmf}/fontname/supplier.map
%{texmf}/fontname/texfonts.map
%{texmf}/fontname/typeface.map
%{texmf}/fontname/urw.map
%{texmf}/fontname/variant.map
%{texmf}/fontname/weight.map
%{texmf}/fontname/width.map
%{texmf}/fontname/wolfram.map
%{texmf}/fontname/yandy.map


%files babel
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/babel
%{texmf}/tex/generic/babel

%files tex-misc
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/poligraf
%doc %{texmf}/doc/generic/localloc
%doc %{texmf}/doc/generic/cmyk-hax
%dir %{texmf}/tex/generic/misc
%{texmf}/tex/generic/misc/cmyk-hax.tex
%{texmf}/tex/generic/misc/epsfx.tex
%{texmf}/tex/generic/misc/letterspacing.tex
%{texmf}/tex/generic/misc/localloc.sty
%{texmf}/tex/generic/misc/null.tex
%{texmf}/tex/generic/misc/path.sty
%{texmf}/tex/generic/misc/poligraf.sty
%{texmf}/tex/generic/misc/psfig.sty
%{texmf}/tex/generic/misc/random.tex
%{texmf}/tex/generic/misc/tap.tex
%{texmf}/tex/generic/misc/texnames.sty
%{texmf}/tex/generic/misc/trans.tex

%files tex-pstriks
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/pstricks
%{texmf}/tex/generic/pstricks

%files tex-pictex
%defattr(644,root,root,755)
%{texmf}/tex/generic/pictex

%files tex-ruhyphen
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/ruhyphen
%{texmf}/tex/generic/ruhyphen

%files tex-spanishb
%defattr(644,root,root,755)
%{texmf}/tex/generic/spanishb

%files tex-texdraw
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/texdraw
%{texmf}/tex/generic/texdraw

%files tex-thumbpdf
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/thumbpdf
%attr(755,root,root) %{_bindir}/thumbpdf
%{texmf}/tex/generic/thumbpdf
%{_mandir}/man1/thumbpdf.1*

%files tex-ukrhyph
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/ukrhyph
%{texmf}/tex/generic/ukrhyph

%files tex-vietnam
%defattr(644,root,root,755)
%{texmf}/tex/generic/vietnam

%files tex-xypic
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/xypic
%{texmf}/tex/generic/xypic

%files tex-mfpic
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/mfpic
%{texmf}/tex/generic/mfpic

%files tex-hyphen
%defattr(644,root,root,755)
%{texmf}/tex/generic/hyphen

%files tex-german
%defattr(644,root,root,755)
%{texmf}/tex/generic/german

%files tex-eijkhout
%defattr(644,root,root,755)
%{texmf}/tex/generic/eijkhout

%files oxdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oxdvi
%attr(755,root,root) %{_bindir}/oxdvi.bin

%files odvips
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvips
#%attr(755,root,root) %{_bindir}/odvitype

%files cyramstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyramstex

%files cyrtexinfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyrtexinfo

%files rubibtex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rubibtex
%{_mandir}/man1/rubibtex.1*

%files rumakeindex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rumakeindex
%{_mandir}/man1/rumakeindex.1*
