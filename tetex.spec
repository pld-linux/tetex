#
# TODO:
#
# beta-20020922, rel. 1:
# - error: libkpathsea.so is required by already marked tetex-dvips-1.0.7.beta_20020208-0.1
#
# later:
# - create new packages if there is a need: more latex splitting... others?
# - look at mktexfmt
# - allow using Type1 fonts in others applications (symlink to
#   /usr/share/fonts/Type1 ?)
# - context: split into language packages (cz, de, en, etc.)
#

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

%package doc-Catalogue
Summary:	TeX Catalogue
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-Catalogue
TeX Catalogue.

%package doc-tug-faq
Summary:	TeX User Group FAQ
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-tug-faq
TeX User Group FAQ.

%package doc-latex
Summary:	Basic LaTeX packages documentation
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-latex
Basic LaTeX packages documentation.

%package doc-latex2e-html
Summary:	HTML LaTeX2e documentation
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-latex2e-html
HTML LaTeX2e documentation.

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
Requires:	kpathsea = %{version}

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
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

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
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

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

%package makeindex
Summary:	A general purpose hierarchical index generator.
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description makeindex
A general purpose hierarchical index generator; it accepts one or more
input files (often produced by a text formatter such as TeX or troff),
sorts the entries, and produces an output file which can be formatted. The
formats of the input and output files are specified in a style file; by
default, input is assumed to be an idx file, as generated by LaTeX.

%package metafont
Summary:	MetaFont
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description metafont
MetaFont.

%package metapost
Summary:	MetaPost
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description metapost
MetaPost.

%package texdoctk
Summary:	Easy access to TeX documentation
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description texdoctk
A Perl/Tk-based GUI for easy access to package documentation for TeX on
Unix platforms; the databases it uses are based on the texmf/doc subtrees
of teTeX v.1.0.x, but database files for local configurations with
modified/extended directories can be derived from them. Note that texdoctk
is not a viewer itself, but an interface for finding documentation files
and opening them with the appropriate viewer; so it relies on appropriate
programs to be installed on the system. However, the choice of these
programs can be configured by the sysadmin or user.

%package -n texconfig
Summary:	TeX typesetting system configurator
Group:		Applications/Publishing/TeX
Requires:	xdvi = %{version}
Requires:	%{name} = %{version}
Requires:	%{name}-dvips = %{version}
Requires:	%{name}-metafont = %{version}

%description -n texconfig
TeX typesetting system configurator.

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
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

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

%package plain-plnfss
Summary:	Simple NFSS macros for plain TeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-plnfss
Simple NFSS macros for plain TeX.

%package format-plain
Summary:	TeX Plain format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description format-plain
TeX Plain format.

%package format-bplain
Summary:	TeX BPlain format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
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
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-fonts-ams = %{version}

%description amstex
American Mathematics Society macros for Plain TeX basic files.

%package format-amstex
Summary:	AMS macros for Plain TeX
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-ams
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-amstex = %{version}

%description format-amstex
American Mathematics Society macros for Plain TeX.

%package format-bamstex
Summary:	AMS macros for BPlain TeX
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-ams
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
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
Requires:	%{name}-fonts-cs = %{version}

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

# CSLaTeX format

%package cslatex
Summary:	CSLaTeX format basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-fonts-cs = %{version}

%description cslatex
CSLaTeX format basic files.

%package format-cslatex
Group:		Applications/Publishing/TeX
Summary:	CSLaTeX format
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-cslatex = %{version}

%description format-cslatex
CSLaTeX format.

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

%package format-cyramstex
Summary:	Cyrillic AMSTeX format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description format-cyramstex
Cyrillic AMSTeX format.

%package format-cyrtexinfo
Summary:	Cyrillic TeXInfo format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description format-cyrtexinfo
Cyrillic TeXInfo format.

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

# ConTeXt format.

%package context
Summary:	ConTeXt macro package basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description context
A full featured, parameter driven macro package, which fully supports
advanced interactive documents.

This package contains basic files.

%package format-context
Summary:	ConTeXt format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-context = %{version}

%description format-context
ConTeXt format.

%package format-pdfcontext
Summary:	PDF ConTeXt format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}
Requires:	%{name}-context = %{version}

%description format-pdfcontext
PDF ConTeXt format.

# LaTeX format.

%package latex
Summary:	LaTeX macro package basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-latex = %{version}

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
Requires:	%{name}-fonts-ae = %{version}

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

%package latex-bbold
Summary:	Sans serif blackboard bold for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-bbold = %{version}

%description latex-bbold
A geometric sans serif blackboard bold font, for use in mathematics.

%package latex-bibtex
Summary:	Bibliography management for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-bibtex
Bibliography management for LaTeX.

%package latex-bibtex-ams
Summary:	BibTeX style files for American Meteorological Society publications
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{version}
Requires:	%{name}-latex-bibtex = %{version}

%description latex-bibtex-ams
BibTeX style files for American Meteorological Society publications.

%package latex-bibtex-pl
Summary:	Polish bibliography management for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{version}

%description latex-bibtex-pl
Polish bibliography management for LaTeX.

%package latex-bibtex-german
Summary:	German variants of standard BibTeX styles
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{version}

%description latex-bibtex-german
German variants of standard BibTeX styles.

%package latex-bibtex-revtex4
Summary:	BibTeX styles for REVTeX4
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-bibtex-revtex4
BibTeX styles for REVTeX4.

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

%package latex-cmbright
Summary:	Support for CM Bright fonts in LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-cmbright = %{version}

%description latex-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald Knuth's CM
fonts. It comprises OT1, T1 and TS1 encoded text fonts of various shapes as
well as all the fonts necessary for mathematical typesetting, incl. AMS
symbols. This collection provides all the necessary files for using the
fonts with LaTeX.

%package latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-concmath = %{version}

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

%package latex-mathpple
Summary:	Use PostScript Palatino for typesetting maths
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-mathpple = %{version}

%description latex-mathpple
The package defines the PostScript font family `Palatino' (ppl) as the
default roman font and then uses the `mathpple' fonts for typesetting math.
These virtual fonts have been created for typesetting math in a style that
suits the Palatino text fonts.  The AMS fonts, when used additionally, will
be scaled to fit Palatino.

%package latex-mathtime
Summary:	Mathtime fonts for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-mathtime
The Mathtime fonts have a number of characters remapped to positions
different from the ones normally used by the corresponding TeX CM-fonts.
For the symbol font ``operators'' the corresponding mathtime style files
use the Times Roman font (often called something like: ptmr or ptmr7t or
ptmrq).

%package latex-mflogo
Summary:	LaTeX support for MetaFont and logo fonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-mflogo = %{version}

%description latex-mflogo
LaTeX package and font definition file to access the Knuthian `logo' fonts
described in `The MetaFontbook' and the MetaFont and logos in LaTeX
documents.

%package latex-mfnfss
Summary:	Font description files to use extra fonts like yinit and ygoth
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-mfnfss
Font description files to use extra fonts like yinit and ygoth.

%package latex-minitoc
Summary:	Produce a table of contents for each chapter
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-minitoc
Produce a table of contents for each chapter.

%package latex-mltex
Summary:	Support for MLTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-mltex
Support for MLTeX, the multilingual TeX extension from Michael J. Ferguson.

%package latex-palatcm
Summary:	Palatino + Computer Modern math fonts for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-palatcm
Palatino + Computer Modern math fonts for LaTeX.

%package latex-psnfss
Summary:	LaTeX font support for common PostScript fonts. 
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-adobe = %{version}

%description latex-psnfss
LaTeX font definition files, macros and font metrics for common PostScript
fonts.

%package latex-pxfonts
Summary:	PX fonts LaTeX support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-fonts-px = %{version}
Requires:	%{name}-latex = %{version}

%description latex-pxfonts
PX fonts LaTeX support.

%package latex-qfonts
Summary:	A collection of PostScript (Adobe Type 1) fonts in QX layout
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-qfonts = %{version}

%description latex-qfonts
A collection of Type 1 fonts; include QuasiBookman, QuasiChancery,
QuasiCourier, QuasiPalatino, QuasiSwiss, QuasiSwissCondensed, and
QuasiTimes (regular, italic, bold and bold italic), based on URW++ fonts
distributed with Ghostscript. The fonts are encoded according to QX layout
which facilitates multilingual and technical typesetting using TeX,
preserving usability in Windows applications.

%package latex-txfonts
Summary:	TX fonts LaTeX support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-fonts-tx = %{version}
Requires:	%{name}-latex = %{version}

%description latex-txfonts
TX fonts LaTeX support.

%package latex-umlaute
Summary:	An interface to inputenc for using alternate input encodings
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-umlaute
An interface to inputenc for using alternate input encodings.

%package latex-vnps
Summary:	VNPS fonts for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-vnps
VNPS fonts for LaTeX.

%package latex-vnr
Summary:	VNR fonts for LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-vnr = %{version}

%description latex-vnr
VNR fonts for LaTeX.

%package latex-wasysym
Summary:	Extra characters from the Waldis symbol fonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-wasy = %{version}

%description latex-wasysym
Makes some additional characters available that come from the wasy fonts
(Waldis symbol fonts). These fonts are not automatically included in
NFSS2/LaTeX2e since they take up important space and often aren't necessary
if one makes use of the packages amsfonts or amssymb. Symbols include: join
box, diamond, leadsto, sqsubset, lhd, rhd, apple, ocircle invneg, logof,
varint, male, female, phone, clock lightning, pointer, sun, bell, permil,
smiley, various electrical symbols, shapes, music notes, circles, signs,
astronomy, etc.

%package format-latex
Summary:	LaTeX macro package
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description format-latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains LaTeX format.

%package format-elatex
Summary:	ELaTeX macro package
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description format-elatex
ELaTeX macro package.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-pdftex = %{version}
Requires:	%{name}-latex-psnfss = %{version}

%description format-pdflatex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF LaTeX format.

%package format-pdfelatex
Summary:	PDF ELaTeX macro package
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfelatex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF ELaTeX format.

# PLaTeX format

%package platex
Summary:	PLaTeX format basic files
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-pl = %{version}

%description platex
PLaTeX format basic files.

%package format-platex
Summary:	PLaTeX format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-platex = %{version}

%description format-platex
PLaTeX format.

%package format-pdfplatex
Summary:	PDF PLaTeX format
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}
Requires:	%{name}-platex = %{version}
Requires:	%{name}-type1-fonts-pl = %{version}

%description format-pdfplatex
PDF PLaTeX format.

#
# TeX generic macros
#

%package tex-babel
Summary:	Multilingual support for TeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-babel
Multilingual support for TeX.

%package tex-german
Summary:	Supports the new German orthography (neue deutsche Rechtschreibung)
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-german
Supports the new German orthography (neue deutsche Rechtschreibung).

%package tex-mfpic
Summary:	Macros which generate Metafont or Metapost for drawing pictures
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-mfpic
Macros which generate Metafont or Metapost for drawing pictures.

%package tex-misc
Summary:	Miscellaneous TeX macros
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-misc
Miscellaneous TeX macros.

%package tex-pictex
Summary:	Picture drawing macros for TeX and LaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-pictex
Picture drawing macros for TeX and LaTeX.

%package tex-pstricks
Summary:	PostScript macros for TeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-pstricks
An extensive collection of PostScript macros that is compatible with most
TeX macro packages, including Plain TeX, LaTeX, AMS-TeX, and AMS-LaTeX.
Included are macros for color, graphics, pie charts, rotation, trees and
overlays. It has many special features, including: a wide variety of
graphics (picture drawing) macros, with a flexible interface and with color
support. There are macros for coloring or shading the cells of tables.

%package tex-qpx
Summary:	QuasiPalatino and PX fonts typesetting support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-qpx = %{version}

%description tex-qpx
QuasiPalatino and PX fonts typesetting support.

%package tex-qtx
Summary:	QuasiTimes and TX fonts typesetting support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-qtx = %{version}

%description tex-qtx
QuasiTimes and TX fonts typesetting support.

%package tex-ruhyphen
Summary:	Russian hyphenation
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-ruhyphen
A collection of Russian hyphenation patterns supporting a number of
Cyrillic font encodings, including T2, UCY (Omega Unicode Cyrillic), LCY,
LWN (OT2), and koi8-r.

%package tex-spanish
Summary:	Various TeX related files for typesetting documents written in Spanish
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-spanish
Various TeX related files for typesetting documents written in Spanish,
including hyphenation and dictionaries.

%package tex-texdraw
Summary:	Graphical macros, using embedded PostScript
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-texdraw
Graphical macros, using embedded PostScript.

%package tex-thumbpdf
Summary:	Thumbnails for PDFTeX and dvips/ps2pdf.
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-thumbpdf
Provides support, using Perl, for thumbnails in pdfTeX and dvips/ps2pdf,
using ghostscript to generate the thumbnails which get represented in a TeX
readable file that is read by the package thumbpdf.sty to automatically
include the thumbnails.  Works with both plain TeX and LaTeX.

%package tex-ukrhyph
Summary:	Ukranian hyphenation
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-ukrhyph
This package allows the use of different hyphenation patterns for the
Ukrainian language for various Cyrillic font encodings. Contains packages
implementing traditional rules, modern rules, and combined
English-Ukrainian hyphenation.

%package tex-vietnam
Summary:	Vietnamese language support
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-vietnam
Vietnamese language support.

%package tex-xypic
Summary:	Package for typesetting a variety of graphs and diagrams with TeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-xypic = %{version}

%description tex-xypic
A package for typesetting a variety of graphs and diagrams with TeX. Xy-pic
works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX, and plain
TeX), in particular Xy-pic is provided as a LaTeX2e `supported package'.

#
# Fonts packages
#

%package fonts-adobe
Summary:	Adobe fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-adobe
Adobe fonts.

%package fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%package fonts-ams
Summary:	AMS fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-ams
AMS fonts.

%package fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%package fonts-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%package fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%package fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bbold
Sans serif blackboard bold for LaTeX.

%package fonts-bh
Summary:	Bold & Heavy Fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bh
Bold & Heavy Fonts.

%package fonts-bitstrea
Summary:	Bitstream fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-bitstrea
Bitstream fonts.

%package fonts-cbgreek
Summary:	Complete set of Greek fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cbgreek
Complete set of Greek fonts.

%package fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cc-pl
Polish version of Computer Concrete fonts.

%package fonts-cg
Summary:	Compugraphic fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cg
Compugraphic fonts.

%package fonts-cm
Summary:	Computer Modern fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cm
Computer Modern fonts.

%package fonts-cmbright
Summary:	CM Bright fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cmbright
CM Bright fonts.

%package fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%package fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%package fonts-concmath
Summary:	Concrete Math fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-concmath
Concrete Math fonts.

%package fonts-concrete
Summary:	Concrete Roman fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally for use with
Euler math fonts.

%package fonts-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%package fonts-dstroke
Summary:	Doublestroke font for typesetting the mathematical symbols
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-dstroke
Doublestroke font for typesetting the mathematical symbols.

%package fonts-ecc
Summary:	Sources for the European Concrete fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-ecc
The MetaFont sources and tfm files of the European Concrete Fonts. This is
the EC implementation of Knuth's Concrete fonts, including also the
corresponding text companion fonts.

%package fonts-euxm
Summary:	Fonts similar to EUSM but with two more characters
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-euxm
Fonts like EUSM but with two more characters needed for Concrete Math
Included in TeXLive distribution in fonts3.

%package fonts-gothic
Summary:	Gothic and ornamental initial fonts by Yannis Haralambous
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%package fonts-hoekwater
Summary:	Converted mflogo font
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by Taco
Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2, xipa.

%package fonts-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%package fonts-latex
Summary:	Basic LaTeX fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-latex
Basic LaTeX fonts.

%package fonts-lh
Summary:	Olga Lapko's LH fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%package fonts-marvosym
Summary:	Martin Vogels Symbole (marvosym) font
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols fur structural
engineering; Symbols for steel cross-sections; Astronomy signs (Sun, Moon,
planets); The 12 signs of the zodiac; Scissor symbols; CE sign and others.

%package fonts-mathpple
Summary:	Use PostScript Palatino for typesetting maths
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-mathpple
The package defines the PostScript font family `Palatino' (ppl) as the
default roman font and then uses the `mathpple' fonts for typesetting math.
These virtual fonts have been created for typesetting math in a style that
suits the Palatino text fonts.  The AMS fonts, when used additionally, will
be scaled to fit Palatino.

%package fonts-mflogo
Summary:	Logo fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-mflogo
Logo fonts.

%package fonts-misc
Summary:	Miscellaneous fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-misc
Miscellaneous fonts.

%package fonts-monotype
Summary:	Monotype fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-monotype
Monotype fonts.

%package fonts-pandora
Summary:	The Pandora font family
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-pandora
The Pandora font family.

%package fonts-pazo
Summary:	Pazo fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-pazo
Pazo fonts.

%package fonts-pl
Summary:	Polish fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-pl
Polish fonts.

%package fonts-px
Summary:	PX fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-px
PX fonts.

%package fonts-qfonts
Summary:	Quasi fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-qfonts
Quasi fonts.

%package fonts-qpx
Summary:	Additional fonts for QPX package
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-fonts-qfonts = %{version}
Requires:	%{name}-fonts-px = %{version}

%description fonts-qpx
Additional fonts for QPX package.

%package fonts-qtx
Summary:	Additional fonts for QTX package
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-fonts-qfonts = %{version}
Requires:	%{name}-fonts-tx = %{version}

%description fonts-qtx
Additional fonts for QTX package.

%package fonts-rsfs
Summary:	Fonts of uppercase script letters for use as symbols in scientific and mathematical typesetting
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-rsfs
Fonts of uppercase script letters for use as symbols in scientific and
mathematical typesetting, in contrast to the informal script fonts such as
that used for the `calligraphic' symbols in the TeX math symbol font.

%package fonts-stmaryrd
Summary:	St Mary Road symbols for functional programming
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-stmaryrd
St Mary Road symbols for functional programming.

%package fonts-tx
Summary:	TX fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-tx
TX fonts.

%package fonts-urw
Summary:	URW fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-urw
URW fonts.

%package fonts-vcm
Summary:	VCM fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-vcm
VCM fonts

%package fonts-vnr
Summary:	VNR fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-vnr
VNR fonts.

%package fonts-wasy
Summary:	Waldis symbol fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-wasy
Waldis symbol fonts.

%package fonts-xypic
Summary:	Xy-pic fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-xypic
Xy-pic fonts.

%package fonts-yandy
Summary:	European Modern fonts from Y&Y
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-yandy
European Modern fonts from Y&Y.

%package fonts-type1-adobe
Summary:	Adobe Type1 fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-adobe
Adobe Type1 fonts.

%package fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%package fonts-type1-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%package fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-belleek
Free replacement for basic MathTime fonts.

%package fonts-type1-bitstrea
Summary:	Bitstream fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-bitstrea
Bitstream fonts.

%package fonts-type1-bluesky
Summary:	Computer Modern family fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-bluesky
Computer Modern family fonts.

%package fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%package fonts-type1-cmcyr
Summary:	 Computer Modern fonts extended with Russian letters
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%package fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%package fonts-type1-hoekwater
Summary:	Converted mflogo font
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by Taco
Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2, xipa.

%package fonts-type1-marvosym
Summary:	Martin Vogels Symbole (marvosym) font
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols fur structural
engineering; Symbols for steel cross-sections; Astronomy signs (Sun, Moon,
planets); The 12 signs of the zodiac; Scissor symbols; CE sign and others.

%package fonts-type1-mathpazo
Summary:	Pazo Math fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-mathpazo
Pazo Math fonts.

%package fonts-type1-pl
Summary:	Polish fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-fonts-type1-bluesky = %{version}

%description fonts-type1-pl
Polish fonts.

%package fonts-type1-px
Summary:	PX fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-px
PX fonts.

%package fonts-type1-qfonts
Summary:	Quasi fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-qfonts
Quasi fonts.

%package fonts-type1-tx
Summary:	TX fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-tx
TX fonts.

%package fonts-type1-urw
Summary:	URW fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-urw
URW fonts.

%package fonts-type1-xypic
Summary:	Xy-pic fonts
Group:	Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-type1-xypic
Xy-pic fonts.

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

%post
%fixinfodir
%texhash

%postun
%fixinfodir
%texhash

%post doc-Catalogue
%texhash

%postun doc-Catalogue
%texhash

%post doc-tug-faq
%texhash

%postun doc-tug-faq
%texhash

%post doc-latex2e-html
%texhash

%postun doc-latex2e-html
%texhash

%post -n kpathsea
/sbin/ldconfig
%fixinfodir
%texhash

%postun -n kpathsea
/sbin/ldconfig
%fixinfodir
%texhash

%post -n kpathsea-devel
%texhash

%postun -n kpathsea-devel
%texhash

%post dvips
%fixinfodir
%texhash

%postun dvips
%fixinfodir
%texhash

%post dvilj
%texhash

%postun dvilj
%texhash

%post makeindex
%texhash

%postun makeindex
%texhash

%post metafont
%texhash

%postun metafont
%texhash

%post metapost
%texhash

%postun metapost
%texhash

%post texdoctk
%texhash

%postun texdoctk
%texhash

%post -n xdvi
%texhash

%postun -n xdvi
%texhash

%post pdftex
%texhash

%postun pdftex
%texhash

%post plain
%texhash

%postun plain
%texhash

%post plain-dvips
%texhash

%postun plain-dvips
%texhash

%post plain-mathtime
%texhash

%postun plain-mathtime
%texhash

%post plain-misc
%texhash

%postun plain-misc
%texhash

%post plain-plnfss
%texhash

%postun plain-plnfss
%texhash

%post format-plain
%texhash

%postun format-plain
%texhash

%post format-bplain
%texhash

%postun format-bplain
%texhash

%post format-pdftex
%texhash

%postun format-pdftex
%texhash

%post format-pdfetex
%texhash

%postun format-pdfetex
%texhash

%post mex
%texhash

%postun mex
%texhash

%post format-mex
%texhash

%postun format-mex
%texhash

%post format-pdfmex
%texhash

%postun format-pdfmex
%texhash

%post format-pdfemex
%texhash

%postun format-pdfemex
%texhash

%post amstex
%texhash

%postun amstex
%texhash

%post format-amstex
%texhash

%postun format-amstex
%texhash

%post format-bamstex
%texhash

%postun format-bamstex
%texhash

%post format-pdfamstex
%texhash

%postun format-pdfamstex
%texhash

%post csplain
%texhash

%postun csplain
%texhash

%post format-csplain
%texhash

%postun format-csplain
%texhash

%post format-pdfcsplain
%texhash

%postun format-pdfcsplain
%texhash

%post cslatex
%texhash

%postun cslatex
%texhash

%post format-cslatex
%texhash

%postun format-cslatex
%texhash

%post cyrplain
%texhash

%postun cyrplain
%texhash

%post format-cyrplain
%texhash

%postun format-cyrplain
%texhash

%post format-cyramstex
%texhash

%postun format-cyramstex
%texhash

%post format-cyrtexinfo
%texhash

%postun format-cyrtexinfo
%texhash

%post eplain
%texhash

%postun eplain
%texhash

%post format-eplain
%texhash

%postun format-eplain
%texhash

%post context
%texhash

%postun context
%texhash

%post format-context
%texhash

%postun format-context
%texhash

%post format-pdfcontext
%texhash

%postun format-pdfcontext
%texhash

%post latex
%fixinfodir
%texhash

%postun latex
%fixinfodir
%texhash

%post latex-ae
%texhash

%postun latex-ae
%texhash

%post latex-ams
%texhash

%postun latex-ams
%texhash

%post latex-antp
%texhash

%postun latex-antp
%texhash

%post latex-antt
%texhash

%postun latex-antt
%texhash

%post latex-bbm
%texhash

%postun latex-bbm
%texhash

%post latex-bbold
%texhash

%postun latex-bbold
%texhash

%post latex-bibtex
%texhash

%postun latex-bibtex
%texhash

%post latex-bibtex-ams
%texhash

%postun latex-bibtex-ams
%texhash

%post latex-bibtex-pl
%texhash

%postun latex-bibtex-pl
%texhash

%post latex-bibtex-german
%texhash

%postun latex-bibtex-german
%texhash

%post latex-bibtex-revtex4
%texhash

%postun latex-bibtex-revtex4
%texhash

%post latex-carlisle
%texhash

%postun latex-carlisle
%texhash

%post latex-ccfonts
%texhash

%postun latex-ccfonts
%texhash

%post latex-cite
%texhash

%postun latex-cite
%texhash

%post latex-cmbright
%texhash

%postun latex-cmbright
%texhash

%post latex-concmath
%texhash

%postun latex-concmath
%texhash

%post latex-custom-bib
%texhash

%postun latex-custom-bib
%texhash

%post latex-cyrillic
%texhash

%postun latex-cyrillic
%texhash

%post latex-dstroke
%texhash

%postun latex-dstroke
%texhash

%post latex-jknappen
%texhash

%postun latex-jknappen
%texhash

%post latex-lucidabr
%texhash

%postun latex-lucidabr
%texhash

%post latex-mathpple
%texhash

%postun latex-mathpple
%texhash

%post latex-mathtime
%texhash

%postun latex-mathtime
%texhash

%post latex-mflogo
%texhash

%postun latex-mflogo
%texhash

%post latex-mfnfss
%texhash

%postun latex-mfnfss
%texhash

%post latex-minitoc
%texhash

%postun latex-minitoc
%texhash

%post latex-mltex
%texhash

%postun latex-mltex
%texhash

%post latex-palatcm
%texhash

%postun latex-palatcm
%texhash

%post latex-psnfss
%texhash

%postun latex-psnfss
%texhash

%post latex-pxfonts
%texhash

%postun latex-pxfonts
%texhash

%post latex-qfonts
%texhash

%postun latex-qfonts
%texhash

%post latex-txfonts
%texhash

%postun latex-txfonts
%texhash

%post latex-umlaute
%texhash

%postun latex-umlaute
%texhash

%post latex-vnps
%texhash

%postun latex-vnps
%texhash

%post latex-vnr
%texhash

%postun latex-vnr
%texhash

%post latex-wasysym
%texhash

%postun latex-wasysym
%texhash

%post format-latex
%texhash

%postun format-latex
%texhash

%post format-elatex
%texhash

%postun format-elatex
%texhash

%post format-pdflatex
%texhash

%postun format-pdflatex
%texhash

%post format-pdfelatex
%texhash

%postun format-pdfelatex
%texhash

%post platex
%texhash

%postun platex
%texhash

%post format-platex
%texhash

%postun format-platex
%texhash

%post format-pdfplatex
%texhash

%postun format-pdfplatex
%texhash

%post tex-babel
%texhash

%postun tex-babel
%texhash

%post tex-german
%texhash

%postun tex-german
%texhash

%post tex-mfpic
%texhash

%postun tex-mfpic
%texhash

%post tex-misc
%texhash

%postun tex-misc
%texhash

%post tex-pictex
%texhash

%postun tex-pictex
%texhash

%post tex-pstricks
%texhash

%postun tex-pstricks
%texhash

%post tex-qpx
%texhash

%postun tex-qpx
%texhash

%post tex-qtx
%texhash

%postun tex-qtx
%texhash

%post tex-ruhyphen
%texhash

%postun tex-ruhyphen
%texhash

%post tex-spanish
%texhash

%postun tex-spanish
%texhash

%post tex-texdraw
%texhash

%postun tex-texdraw
%texhash

%post tex-thumbpdf
%texhash

%postun tex-thumbpdf
%texhash

%post tex-ukrhyph
%texhash

%postun tex-ukrhyph
%texhash

%post tex-vietnam
%texhash

%postun tex-vietnam
%texhash

%post tex-xypic
%texhash

%postun tex-xypic
%texhash

%post fonts-adobe
%texhash

%postun fonts-adobe
%texhash

%post fonts-ae
%texhash

%postun fonts-ae
%texhash

%post fonts-ams
%texhash

%postun fonts-ams
%texhash

%post fonts-antp
%texhash

%postun fonts-antp
%texhash

%post fonts-antt
%texhash

%postun fonts-antt
%texhash

%post fonts-bbm
%texhash

%postun fonts-bbm
%texhash

%post fonts-bbold
%texhash

%postun fonts-bbold
%texhash

%post fonts-bh
%texhash

%postun fonts-bh
%texhash

%post fonts-bitstrea
%texhash

%postun fonts-bitstrea
%texhash

%post fonts-cbgreek
%texhash

%postun fonts-cbgreek
%texhash

%post fonts-cc-pl
%texhash

%postun fonts-cc-pl
%texhash

%post fonts-cg
%texhash

%postun fonts-cg
%texhash

%post fonts-cm
%texhash

%postun fonts-cm
%texhash

%post fonts-cmbright
%texhash

%postun fonts-cmbright
%texhash

%post fonts-cmcyr
%texhash

%postun fonts-cmcyr
%texhash

%post fonts-cmextra
%texhash

%postun fonts-cmextra
%texhash

%post fonts-concmath
%texhash

%postun fonts-concmath
%texhash

%post fonts-concrete
%texhash

%postun fonts-concrete
%texhash

%post fonts-cs
%texhash

%postun fonts-cs
%texhash

%post fonts-dstroke
%texhash

%postun fonts-dstroke
%texhash

%post fonts-ecc
%texhash

%postun fonts-ecc
%texhash

%post fonts-euxm
%texhash

%postun fonts-euxm
%texhash

%post fonts-gothic
%texhash

%postun fonts-gothic
%texhash

%post fonts-hoekwater
%texhash

%postun fonts-hoekwater
%texhash

%post fonts-jknappen
%texhash

%postun fonts-jknappen
%texhash

%post fonts-latex
%texhash

%postun fonts-latex
%texhash

%post fonts-lh
%texhash

%postun fonts-lh
%texhash

%post fonts-marvosym
%texhash

%postun fonts-marvosym
%texhash

%post fonts-mathpple
%texhash

%postun fonts-mathpple
%texhash

%post fonts-mflogo
%texhash

%postun fonts-mflogo
%texhash

%post fonts-misc
%texhash

%postun fonts-misc
%texhash

%post fonts-monotype
%texhash

%postun fonts-monotype
%texhash

%post fonts-pandora
%texhash

%postun fonts-pandora
%texhash

%post fonts-pazo
%texhash

%postun fonts-pazo
%texhash

%post fonts-pl
%texhash

%postun fonts-pl
%texhash

%post fonts-px
%texhash

%postun fonts-px
%texhash

%post fonts-qfonts
%texhash

%postun fonts-qfonts
%texhash

%post fonts-qpx
%texhash

%postun fonts-qpx
%texhash

%post fonts-qtx
%texhash

%postun fonts-qtx
%texhash

%post fonts-rsfs
%texhash

%postun fonts-rsfs
%texhash

%post fonts-stmaryrd
%texhash

%postun fonts-stmaryrd
%texhash

%post fonts-tx
%texhash

%postun fonts-tx
%texhash

%post fonts-urw
%texhash

%postun fonts-urw
%texhash

%post fonts-vcm
%texhash

%postun fonts-vcm
%texhash

%post fonts-vnr
%texhash

%postun fonts-vnr
%texhash

%post fonts-wasy
%texhash

%postun fonts-wasy
%texhash

%post fonts-xypic
%texhash

%postun fonts-xypic
%texhash

%post fonts-yandy
%texhash

%postun fonts-yandy
%texhash

%post fonts-type1-adobe
%texhash

%postun fonts-type1-adobe
%texhash

%post fonts-type1-antp
%texhash

%postun fonts-type1-antp
%texhash

%post fonts-type1-antt
%texhash

%postun fonts-type1-antt
%texhash

%post fonts-type1-belleek
%texhash

%postun fonts-type1-belleek
%texhash

%post fonts-type1-bitstrea
%texhash

%postun fonts-type1-bitstrea
%texhash

%post fonts-type1-bluesky
%texhash

%postun fonts-type1-bluesky
%texhash

%post fonts-type1-cc-pl
%texhash

%postun fonts-type1-cc-pl
%texhash

%post fonts-type1-cmcyr
%texhash

%postun fonts-type1-cmcyr
%texhash

%post fonts-type1-cs
%texhash

%postun fonts-type1-cs
%texhash

%post fonts-type1-hoekwater
%texhash

%postun fonts-type1-hoekwater
%texhash

%post fonts-type1-marvosym
%texhash

%postun fonts-type1-marvosym
%texhash

%post fonts-type1-mathpazo
%texhash

%postun fonts-type1-mathpazo
%texhash

%post fonts-type1-pl
%texhash

%postun fonts-type1-pl
%texhash

%post fonts-type1-px
%texhash

%postun fonts-type1-px
%texhash

%post fonts-type1-qfonts
%texhash

%postun fonts-type1-qfonts
%texhash

%post fonts-type1-tx
%texhash

%postun fonts-type1-tx
%texhash

%post fonts-type1-urw
%texhash

%postun fonts-type1-urw
%texhash

%post fonts-type1-xypic
%texhash

%postun fonts-type1-xypic
%texhash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{texmf}/doc/help
%doc %{texmf}/ChangeLog
%doc %{texmf}/doc/README
%doc %{texmf}/doc/README.knuth
%doc %{texmf}/doc/tetex/CREDITS
%doc %{texmf}/doc/tetex/FEATURES
%doc %{texmf}/doc/tetex/NEWS
%doc %{texmf}/doc/tetex/README
%doc %{texmf}/doc/tetex/TETEXDOC.*
%doc %{texmf}/doc/tetex/teTeX-FAQ
%doc %{texmf}/doc/tetex.gif
%doc %{texmf}/doc/tetex.png
%doc %{texmf}/doc/fontinst
%doc %{texmf}/doc/fonts/fontname
%doc %{texmf}/doc/generic/nohyph
%doc %{texmf}/doc/help/tds.dvi
%doc %{texmf}/doc/images
%doc %{texmf}/doc/programs/web2c*

%attr(755,root,root) %{_bindir}/MakeTeXPK
%attr(755,root,root) %{_bindir}/access
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/e2pall
%attr(755,root,root) %{_bindir}/fdf2tan
%attr(755,root,root) %{_bindir}/fmtutil
%attr(755,root,root) %{_bindir}/fontexport
%attr(755,root,root) %{_bindir}/fontimport
%attr(755,root,root) %{_bindir}/fontinst
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/gsftopk
%attr(755,root,root) %{_bindir}/initex
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/makempx
%attr(755,root,root) %{_bindir}/makempy
%attr(755,root,root) %{_bindir}/mkfontdesc
%attr(755,root,root) %{_bindir}/mktexfmt
%attr(755,root,root) %{_bindir}/mktexlsr
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%attr(755,root,root) %{_bindir}/newer
%attr(755,root,root) %{_bindir}/patgen
%attr(755,root,root) %{_bindir}/pfb2pfa
%attr(755,root,root) %{_bindir}/pk2bm
%attr(755,root,root) %{_bindir}/pktogf
%attr(755,root,root) %{_bindir}/pktype
%attr(755,root,root) %{_bindir}/pltotf
%attr(755,root,root) %{_bindir}/pooltype
%attr(755,root,root) %{_bindir}/ps2frag
%attr(755,root,root) %{_bindir}/ps2pk
%attr(755,root,root) %{_bindir}/readlink
%attr(755,root,root) %{_bindir}/t1mapper
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tetex-updmap
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texdoc
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texfind
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texi2html
%attr(755,root,root) %{_bindir}/texi2pdf
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/texshow
%attr(755,root,root) %{_bindir}/texutil
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/ttf2afm
%attr(755,root,root) %{_bindir}/updmap
%attr(755,root,root) %{_bindir}/vftovp
%attr(755,root,root) %{_bindir}/virtex
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave

%attr(755,root,root) %{texmf}/web2c/mktexnam
%attr(755,root,root) %{texmf}/web2c/mktexdir
%attr(755,root,root) %{texmf}/web2c/mktexupd

%{_sysconfdir}/cron.daily/tetex

%dir %{_sysconfdir}/sysconfig/tetex-updmap
%verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/sysconfig/tetex-updmap/maps.lst

%config(noreplace) %verify(not size md5 mtime) %{texmf}/ls-R
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/fmtutil.cnf
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/mktex.cnf
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/mktex.opt
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/mktexdir.opt
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/mktexnam.opt
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/texmf.cnf
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/updmap.cfg

%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/fontmath.cfg
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/fonttext.cfg
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/language.dat
%config(noreplace) %verify(not size md5 mtime) %{texmf}/tex/generic/config/preload.cfg

%dir %{texmf}
%dir %{texmf}/fonts
%dir %{texmf}/fonts/afm
%dir %{texmf}/fonts/afm/public
%dir %{texmf}/fonts/ovf
%dir %{texmf}/fonts/ovf/public
%dir %{texmf}/fonts/ovp
%dir %{texmf}/fonts/ovp/public
%dir %{texmf}/fonts/pk
%dir %{texmf}/fonts/source
%dir %{texmf}/fonts/source/public
%dir %{texmf}/fonts/tfm
%dir %{texmf}/fonts/tfm/public
%dir %{texmf}/fonts/type1
%dir %{texmf}/fonts/type1/public
%dir %{texmf}/fonts/vf
%dir %{texmf}/fonts/vf/public
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%dir %{texmf}/web2c

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*
%{texmf}/updates.dat

%{texmf}/aliases
%{texmf}/fontname
%{texmf}/tex/fontinst
%{texmf}/tex/generic/hyphen
%{texmf}/tex/texinfo
%{texmf}/web2c/*.tcx
%{texmf}/web2c/metafun.mem
%{texmf}/web2c/tex-pl.pool
%{texmf}/web2c/tex.pool

%lang(fi) %{_mandir}/fi/man1/afm2tfm.1*
%lang(fi) %{_mandir}/fi/man1/allcm.1*
%lang(fi) %{_mandir}/fi/man1/allneeded.1*
%lang(fr) %{_mandir}/fr/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/newer.1*
%lang(hu) %{_mandir}/hu/man1/readlink.1*
%lang(pl) %{_mandir}/pl/man1/access.1*
%lang(pl) %{_mandir}/pl/man1/newer.1*
%{_mandir}/man1/MakeTeXPK.1*
%{_mandir}/man1/access.1*
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/fontexport.1*
%{_mandir}/man1/fontimport.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/initex.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/newer.1*
%{_mandir}/man1/patgen.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/pooltype.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/ps2pk.1*
%{_mandir}/man1/readlink.1*
%{_mandir}/man1/t1mapper.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texdoc.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texi2html.1*
%{_mandir}/man1/texi2pdf.1*
%{_mandir}/man1/texshow.1*
%{_mandir}/man1/texutil.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/virtex.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*
%{_mandir}/man5/fmtutil.cnf.5*
%{_mandir}/man8/fmtutil.8*
%{_mandir}/man8/mkfontdesc.8*
%{_mandir}/man8/texlinks.8*

%files doc-Catalogue
%defattr(644,root,root,755)
%{texmf}/doc/help/Catalogue

%files doc-tug-faq
%defattr(644,root,root,755)
%{texmf}/doc/help/faq/uktug-faq

%files doc-latex
%defattr(644,root,root,755)
%{texmf}/doc/latex
%{texmf}/doc/latex/styles
%{texmf}/doc/latex/SIunits
%{texmf}/doc/latex/acronym
%{texmf}/doc/latex/aeguill
%{texmf}/doc/latex/anysize
%{texmf}/doc/latex/base
%{texmf}/doc/latex/booktabs
%{texmf}/doc/latex/caption
%{texmf}/doc/latex/ccaption
%{texmf}/doc/latex/changebar
%{texmf}/doc/latex/currvita
%{texmf}/doc/latex/dinbrief
%{texmf}/doc/latex/draftcopy
%{texmf}/doc/latex/eepic
%{texmf}/doc/latex/fancy*
%{texmf}/doc/latex/float*
%{texmf}/doc/latex/footmisc
%{texmf}/doc/latex/g-brief
%{texmf}/doc/latex/geometry
%{texmf}/doc/latex/graphics
%{texmf}/doc/latex/hyperref
%{texmf}/doc/latex/koma-script
%{texmf}/doc/latex/leftidx
%{texmf}/doc/latex/mdwtools
%{texmf}/doc/latex/ms
%{texmf}/doc/latex/mwcls
%{texmf}/doc/latex/natbib
%{texmf}/doc/latex/nomencl
%{texmf}/doc/latex/ntgclass
%{texmf}/doc/latex/oberdiek
%{texmf}/doc/latex/overpic
%{texmf}/doc/latex/pb-diagram
%{texmf}/doc/latex/pdfpages
%{texmf}/doc/latex/preprint
%{texmf}/doc/latex/program
%{texmf}/doc/latex/psfrag
%{texmf}/doc/latex/psgo
%{texmf}/doc/latex/rotating
%{texmf}/doc/latex/rotfloat
%{texmf}/doc/latex/revtex4
%{texmf}/doc/latex/scale
%{texmf}/doc/latex/showlabels
%{texmf}/doc/latex/sidecap
%{texmf}/doc/latex/styles/a4.dvi
%{texmf}/doc/latex/styles/adrguide.dvi
%{texmf}/doc/latex/styles/beton.dvi
%{texmf}/doc/latex/styles/blkarray.dvi
%{texmf}/doc/latex/styles/chappg.txt
%{texmf}/doc/latex/styles/comm_test_l.tex
%{texmf}/doc/latex/styles/concmath.dvi
%{texmf}/doc/latex/styles/crop.dvi
%{texmf}/doc/latex/styles/curves.dvi
%{texmf}/doc/latex/styles/endfloat.dvi
%{texmf}/doc/latex/styles/euler.dvi
%{texmf}/doc/latex/styles/examdoc.dvi
%{texmf}/doc/latex/styles/fancybox.dvi
%{texmf}/doc/latex/styles/float.dvi
%{texmf}/doc/latex/styles/footnpag-user.dvi
%{texmf}/doc/latex/styles/hyphenat.dvi
%{texmf}/doc/latex/styles/index.dvi
%{texmf}/doc/latex/styles/labels.dvi
%{texmf}/doc/latex/styles/lastpage.dvi
%{texmf}/doc/latex/styles/layman.dvi
%{texmf}/doc/latex/styles/listings.dvi
%{texmf}/doc/latex/styles/lucidabr.txt
%{texmf}/doc/latex/styles/mathcomp.dvi
%{texmf}/doc/latex/styles/moreverb.dvi
%{texmf}/doc/latex/styles/paralist.dvi
%{texmf}/doc/latex/styles/picinpar.dvi
%{texmf}/doc/latex/styles/picins.txt
%{texmf}/doc/latex/styles/placeins.txt
%{texmf}/doc/latex/styles/readme.fp
%{texmf}/doc/latex/styles/sectsty.dvi
%{texmf}/doc/latex/styles/slashbox.tex
%{texmf}/doc/latex/styles/soul.dvi
%{texmf}/doc/latex/styles/stdclsdv.dvi
%{texmf}/doc/latex/styles/subfigure.dvi
%{texmf}/doc/latex/styles/textfit.dvi
%{texmf}/doc/latex/styles/titlesec.dvi
%{texmf}/doc/latex/styles/tocloft.dvi
%{texmf}/doc/latex/styles/type1cm.txt
%{texmf}/doc/latex/styles/vmargin.dvi
%{texmf}/doc/latex/seminar
%{texmf}/doc/latex/supertab
%{texmf}/doc/latex/textmerg
%{texmf}/doc/latex/tocbibind
%{texmf}/doc/latex/treesvr
%{texmf}/doc/latex/tools
%{texmf}/doc/latex/units
%{texmf}/doc/latex/xtab
%{texmf}/doc/latex/yfonts
%{texmf}/doc/latex/general
%{texmf}/doc/latex/pslatex
%{texmf}/doc/latex/images

%files doc-latex2e-html
%defattr(644,root,root,755)
%{texmf}/doc/latex/latex2e-html

%files -n kpathsea
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/kpathsea.dvi
%doc %{texmf}/doc/programs/kpathsea.pdf
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_libdir}/libkpathsea.so.*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhich.1*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkpathsea.so
%{_includedir}/kpathsea
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
%{texmf}/dvips/gsftopk
%{texmf}/dvips/psfrag
%{texmf}/dvips/psnfss
%dir %{texmf}/dvips/config
%{texmf}/dvips/config/builtin35.map
%config(noreplace) %verify(not size md5 mtime) %{texmf}/dvips/config/config.ps
%{texmf}/dvips/config/download35.map
%{texmf}/dvips/config/ps2pk.map
%{texmf}/dvips/config/psfonts_pk.map
%{texmf}/dvips/config/config.generic
%{texmf}/dvips/config/psfonts.map
%{texmf}/dvips/config/psfonts_t1.map

%dir %{texmf}/dvips/tetex
%{texmf}/dvips/tetex/config.*
%{texmf}/dvips/tetex/dvips35.map
%{texmf}/dvips/tetex/lucidabr.map
%{texmf}/dvips/tetex/mathpple.map
%{texmf}/dvips/tetex/mt-belleek.map
%{texmf}/dvips/tetex/mt-plus.map
%{texmf}/dvips/tetex/mt-yy.map
%{texmf}/dvips/tetex/pdftex35.map
%{texmf}/dvips/tetex/ps2pk35.map
%{texmf}/dvips/tetex/ttcmex.map

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

%files makeindex
%defattr(644,root,root,755)
%doc %{texmf}/doc/makeindex

%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/rumakeindex

%{texmf}/makeindex

%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_mandir}/man1/rumakeindex.1*

%files metafont
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mfw
%attr(755,root,root) %{_bindir}/virmf
%attr(755,root,root) %{_bindir}/inimf
%{texmf}/metafont
%dir %{texmf}/mft
%{texmf}/mft/cmbase.mft
%{texmf}/mft/e.mft
%{texmf}/mft/mplain.mft
%{texmf}/mft/plain.mft
%{texmf}/mft/pl.mft
%{texmf}/web2c/mf.base
%{texmf}/web2c/mf-nowin.base
%{texmf}/web2c/mf.pool
%{texmf}/web2c/mfw.base

%{_mandir}/man1/mf.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/inimf.1*
%{_mandir}/man1/virmf.1*

%files metapost
%defattr(644,root,root,755)
%doc %{texmf}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%attr(755,root,root) %{_bindir}/mptopdf
%attr(755,root,root) %{_bindir}/virmpost
%attr(755,root,root) %{_bindir}/inimpost
%dir %{texmf}/metapost
%{texmf}/metapost/base
%{texmf}/metapost/config
%{texmf}/metapost/mfpic
%{texmf}/metapost/misc
%{texmf}/web2c/mpost.mem
%{texmf}/web2c/mp.pool
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
%{_mandir}/man1/inimpost.1*
%{_mandir}/man1/virmpost.1*

%files texdoctk
%doc %{texmf}/doc/texdoctk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texdoctk
%{texmf}/texdoctk

%{_mandir}/man1/texdoctk.1*

%files -n texconfig
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texconfig
%{_mandir}/man1/texconfig.1*
%{texmf}/texconfig

%files -n xdvi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xdvi
%attr(755,root,root) %{_bindir}/xdvi.bin
%{_mandir}/man1/xdvi.1*
%{_prefix}/X11R6/share/applnk/Graphics/Viewers/xdvi.desktop
%dir %{texmf}/xdvi
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

%files plain-plnfss
%defattr(644,root,root,755)
%{texmf}/tex/plain/plnfss

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

%files cslatex
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex/INSTALL.cslatex
%doc %{texmf}/doc/cstex/README.cslatex
%{texmf}/tex/cslatex
%{texmf}/tex/latex/cslatex

%files format-cslatex
%attr(755,root,root) %{_bindir}/cslatex
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/cslatex.fmt

%files cyrplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cyrplain
%{texmf}/tex/cyrplain/

%files format-cyrplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyrtex
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cyrtex.fmt

%files format-cyramstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyramstex
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cyramstex.fmt

%files format-cyrtexinfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cyrtexinfo
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cyrtexinfo.fmt

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

%files context
%defattr(644,root,root,755)
%doc %{texmf}/doc/context
%dir %{texmf}/context
%dir %{texmf}/context/config
%dir %{texmf}/context/data
%{texmf}/context/config/texexec.ini
%{texmf}/context/config/texexec.rme
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
%{texmf}/tex/generic/context
%{texmf}/tex/latex/context
%{texmf}/tex/context/base

%dir %{texmf}/tex/context
%dir %{texmf}/tex/context/config
%{texmf}/tex/context/config/cont-usr.tex
%{texmf}/tex/context/extra
%{texmf}/tex/context/sample
%{texmf}/tex/context/user

%{texmf}/metapost/context
%{texmf}/dvips/config/context.map

%files format-context
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/cont-cz
%attr(755,root,root) %{_bindir}/cont-de
%attr(755,root,root) %{_bindir}/cont-en
%attr(755,root,root) %{_bindir}/cont-nl
#%attr(755,root,root) %{_bindir}/cont-uk
%{texmf}/tex/context/config/cont-cz.ini
%{texmf}/tex/context/config/cont-de.ini
%{texmf}/tex/context/config/cont-en.ini
%{texmf}/tex/context/config/cont-it.ini
%{texmf}/tex/context/config/cont-nl.ini
%{texmf}/tex/context/config/cont-ro.ini
%{texmf}/tex/context/config/cont-uk.ini

%{_mandir}/man1/cont-de.1*
%{_mandir}/man1/cont-en.1*
%{_mandir}/man1/cont-nl.1*

%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-cz.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-de.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-en.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-nl.efmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/cont-uk.efmt

%files format-pdfcontext
%defattr(644,root,root,755)
%{texmf}/pdftex/config/context

%files latex
%defattr(644,root,root,755)
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%lang(fi) %{_mandir}/fi/man1/latex.1*
%lang(pl) %{_mandir}/pl/man1/latex.1*
%{_infodir}/latex.info*

%dir %{texmf}/tex/latex
%{texmf}/tex/latex/SIunits
%{texmf}/tex/latex/adrconv
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
%{texmf}/tex/latex/preprint
%{texmf}/tex/latex/pstricks
%{texmf}/tex/latex/revtex4
%{texmf}/tex/latex/seminar
%{texmf}/tex/latex/t2
%{texmf}/tex/latex/textmerg
%{texmf}/tex/latex/titlesec
%{texmf}/tex/latex/texmacs
%{texmf}/tex/latex/tools
%{texmf}/tex/latex/units

%files latex-ae
%defattr(644,root,root,755)
%{texmf}/tex/latex/ae

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

%files latex-bbm
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/styles/bbm.dvi
%{texmf}/tex/latex/bbm

%files latex-bbold
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/styles/bbold.dvi
%{texmf}/tex/latex/bbold

%files latex-bibtex
%defattr(644,root,root,755)
%doc %{texmf}/bibtex/bib/README
%doc %{texmf}/doc/bibtex/base

%attr(755,root,root) %{_bindir}/bibtex
%attr(755,root,root) %{_bindir}/rubibtex

%dir %{texmf}/doc/bibtex
%dir %{texmf}/bibtex
%dir %{texmf}/bibtex/bib
%dir %{texmf}/bibtex/bst

%{texmf}/bibtex/bib/base
%{texmf}/bibtex/bst/adrconv
%{texmf}/bibtex/bst/base
%{texmf}/bibtex/bst/misc
%{texmf}/bibtex/bst/natbib

%{_mandir}/man1/bibtex.1*
%{_mandir}/man1/rubibtex.1*

%files latex-bibtex-ams
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/ams
%{texmf}/bibtex/bst/ams

%files latex-bibtex-pl
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/plbib
%{texmf}/bibtex/bst/plbib

%files latex-bibtex-german
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/germbib

%files latex-bibtex-revtex4
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/revtex4

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

%files latex-cmbright
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cmbright
%{texmf}/tex/latex/cmbright

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

%files latex-mathpple
%defattr(644,root,root,755)
%{texmf}/tex/latex/mathpple

%files latex-mathtime
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mathtime
%{texmf}/tex/latex/mathtime

%files latex-mflogo
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/styles/mflogo.dvi
%{texmf}/tex/latex/mflogo

%files latex-mfnfss
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mfnfss
%{texmf}/tex/latex/mfnfss

%files latex-minitoc
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/minitoc
%{texmf}/tex/latex/minitoc

%files latex-mltex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mltex
%{texmf}/tex/latex/mltex

%files latex-palatcm
%defattr(644,root,root,755)
%{texmf}/tex/latex/palatcm

%files latex-psnfss
%doc %{texmf}/doc/latex/psnfss
%defattr(644,root,root,755)
%{texmf}/tex/latex/psnfss

%files latex-pxfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/pxfonts
%{texmf}/tex/latex/pxfonts

%files latex-qfonts
%defattr(644,root,root,755)
%{texmf}/tex/latex/qfonts

%files latex-txfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/txfonts
%{texmf}/tex/latex/txfonts

%files latex-umlaute
%defattr(644,root,root,755)
%{texmf}/tex/latex/umlaute

%files latex-vnps
%defattr(644,root,root,755)
%{texmf}/tex/latex/vnps

%files latex-vnr
%defattr(644,root,root,755)
%{texmf}/tex/latex/vnr

%files latex-wasysym
%doc %{texmf}/doc/latex/wasysym
%defattr(644,root,root,755)
%{texmf}/tex/latex/wasysym

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

%files platex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/platex
%dir %{texmf}/tex/platex
%{texmf}/tex/platex/config
%{texmf}/tex/latex/platex

%files format-platex
%attr(755,root,root) %{_bindir}/platex
%attr(755,root,root) %{_bindir}/platex-pl
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/platex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/platex-pl.fmt

%files format-pdfplatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/platex
%{texmf}/pdftex/platex/config
%attr(755,root,root) %{_bindir}/pdfplatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfplatex.fmt

%files tex-babel
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/babel
%{texmf}/tex/generic/babel

%files tex-german
%defattr(644,root,root,755)
%{texmf}/tex/generic/german

%files tex-mfpic
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/mfpic
%{texmf}/tex/generic/mfpic

%files tex-misc
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/poligraf
%doc %{texmf}/doc/generic/localloc
%doc %{texmf}/doc/generic/cmyk-hax
%doc %{texmf}/doc/generic/multido
%doc %{texmf}/doc/generic/tap

%{texmf}/tex/generic/eijkhout
%{texmf}/tex/generic/multido
%{texmf}/tex/generic/misc

%files tex-pictex
%defattr(644,root,root,755)
%{texmf}/tex/generic/pictex

%files tex-pstricks
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/pstricks
%{texmf}/dvips/pstricks
%{texmf}/tex/generic/pstricks

%files tex-qpx
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qpx
%{texmf}/tex/generic/qpx

%files tex-qtx
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qtx
%{texmf}/tex/generic/qtx

%files tex-ruhyphen
%defattr(644,root,root,755)
%doc %{texmf}/doc/generic/ruhyphen
%{texmf}/tex/generic/ruhyphen

%files tex-spanish
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

%files fonts-adobe
%defattr(644,root,root,755)
%{texmf}/fonts/afm/adobe
%{texmf}/fonts/tfm/adobe
%{texmf}/fonts/vf/adobe

%files fonts-ae
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/ae
%{texmf}/fonts/tfm/public/ae
%{texmf}/fonts/vf/public/ae

%files fonts-ams
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/amsfonts
%{texmf}/fonts/source/ams
%{texmf}/fonts/tfm/ams

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

%files fonts-bbm
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/bbm
%{texmf}/fonts/tfm/public/bbm

%files fonts-bbold
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/bbold
%{texmf}/fonts/tfm/public/bbold

%files fonts-bh
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/bh
%{texmf}/fonts/vf/bh

%files fonts-bitstrea
%defattr(644,root,root,755)
%{texmf}/fonts/afm/bitstrea
%{texmf}/fonts/tfm/bitstrea
%{texmf}/fonts/vf/bitstrea

%files fonts-cbgreek
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cbgreek
%{texmf}/fonts/source/public/cbgreek

%files fonts-cc-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/cc-pl
%{texmf}/fonts/source/public/cc-pl
%{texmf}/fonts/tfm/public/cc-pl

%files fonts-cg
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/cg
%{texmf}/fonts/vf/cg

%files fonts-cm
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/cm
%{texmf}/fonts/source/public/cm
%{texmf}/fonts/tfm/public/cm
%{texmf}/fonts/source/public/cm-bold

%files fonts-cmbright
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/cmbright
%{texmf}/fonts/tfm/public/cmbright

%files fonts-cmcyr
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/cmcyr
%{texmf}/fonts/vf/public/cmcyr

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

%files fonts-hoekwater
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/hoekwater
%{texmf}/fonts/tfm/hoekwater
%{texmf}/dvips/tetex/hoekwater.map

%files fonts-jknappen
%defattr(644,root,root,755)
%{texmf}/fonts/source/jknappen
%{texmf}/fonts/tfm/jknappen

%files fonts-latex
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/latex
%{texmf}/fonts/tfm/public/latex

%files fonts-lh
%defattr(644,root,root,755)
%{texmf}/fonts/source/lh

%files fonts-marvosym
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/marvosym
%{texmf}/fonts/afm/public/marvosym
%{texmf}/fonts/tfm/public/marvosym

%files fonts-mflogo
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/mflogo
%{texmf}/fonts/tfm/public/mflogo

%files fonts-misc
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/misc
%{texmf}/fonts/tfm/public/misc

%files fonts-monotype
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/monotype
%{texmf}/fonts/vf/monotype

%files fonts-pandora
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/pandora
%{texmf}/fonts/tfm/public/pandora

%files fonts-pazo
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/pazo
%{texmf}/fonts/vf/public/pazo

%files fonts-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/pl
%{texmf}/dvips/pl
%{texmf}/fonts/source/public/pl
%{texmf}/fonts/afm/public/pl
%{texmf}/fonts/tfm/public/pl

%files fonts-px
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/pxfonts
%{texmf}/fonts/vf/public/pxfonts
%{texmf}/dvips/tetex/pxfonts.map

%files fonts-qfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qfonts
%{texmf}/dvips/qfonts/
%{texmf}/fonts/afm/public/qfonts
%{texmf}/fonts/tfm/public/qfonts

%files fonts-qpx
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/qpx
%{texmf}/fonts/vf/public/qpx

%files fonts-qtx
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/qtx
%{texmf}/fonts/vf/public/qtx

%files fonts-rsfs
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/rsfs
%{texmf}/fonts/tfm/public/rsfs

%files fonts-stmaryrd
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/styles/stmaryrd.dvi
%{texmf}/fonts/source/public/stmaryrd
%{texmf}/fonts/tfm/public/stmaryrd

%files fonts-tx
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/txfonts
%{texmf}/fonts/vf/public/txfonts
%{texmf}/dvips/tetex/txfonts.map

%files fonts-urw
%defattr(644,root,root,755)
%{texmf}/fonts/afm/urw

%files fonts-vcm
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/vcm
%{texmf}/fonts/vf/public/vcm

%files fonts-vnr
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/vnr
%{texmf}/fonts/tfm/public/vnr

%files fonts-wasy
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/wasy
%{texmf}/fonts/tfm/public/wasy

%files fonts-xypic
%defattr(644,root,root,755)
%{texmf}/fonts/afm/public/xypic
%{texmf}/fonts/source/public/xypic
%{texmf}/fonts/tfm/public/xypic

%files fonts-yandy
%defattr(644,root,root,755)
%{texmf}/fonts/afm/yandy
%{texmf}/fonts/source/yandy
%{texmf}/fonts/tfm/yandy
%{texmf}/fonts/vf/yandy

%files fonts-type1-adobe
%defattr(644,root,root,755)
%{texmf}/fonts/type1/adobe

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

%files fonts-type1-bitstrea
%defattr(644,root,root,755)
%{texmf}/fonts/type1/bitstrea

%files fonts-type1-bluesky
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/bluesky
%{texmf}/dvips/bluesky
%{texmf}/fonts/type1/bluesky

%files fonts-type1-cc-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/cc-plps
%{texmf}/dvips/cc-pl
%{texmf}/fonts/type1/public/cc-pl

%files fonts-type1-cmcyr
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/cmcyr

%files fonts-type1-cs
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/cs

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
%{texmf}/fonts/type1/hoekwater

%files fonts-type1-marvosym
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/mathpazo
%{texmf}/fonts/afm/public/mathpazo
%{texmf}/fonts/type1/public/mathpazo

%files fonts-type1-pl
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/plpsfont
%{texmf}/fonts/type1/public/pl

%files fonts-type1-px
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/pxfonts

%files fonts-type1-qfonts
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/qfonts

%files fonts-type1-tx
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/txfonts

%files fonts-type1-urw
%defattr(644,root,root,755)
%{texmf}/fonts/type1/urw

%files fonts-type1-xypic
%defattr(644,root,root,755)
%{texmf}/dvips/xypic
%{texmf}/fonts/type1/public/xypic
