#
# TODO:
# - context: review package splitting
# - omega
# - create new packages if there is a need: more latex splitting... others?
# - look at mktexfmt
# - allow using Type1 fonts in others applications (symlink to
#   /usr/share/fonts/Type1 ?)
#

%include	/usr/lib/rpm/macros.perl
Summary:	TeX typesetting system and MetaFont font formatter
Summary(de):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr):	Systéme de compostion TeX et formatteur de MetaFontes
Summary(pl):	System sk³adu publikacji TeX oraz formater fontów MetaFont
Summary(pt_BR):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr):	TeX dizgi sistemi ve MetaFont yazýtipi biçimlendiricisi
Name:		tetex
Version:	2.0.2
Release:	0.2
Epoch:		1
License:	distributable
Group:		Applications/Publishing/TeX
# Release sources at ftp://sunsite.informatik.rwth-aachen.de/pub/comp/tex/teTeX/1.0/distrib/sources/
Source0:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX/2.0/distrib/%{name}-src-%{version}.tar.gz
Source1:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX/2.0/distrib/%{name}-texmf-%{version}.tar.gz
Source3:	%{name}-non-english-man-pages.tar.bz2
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source6:	xdvi.png
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
Patch19:	teTeX-kpathsea.patch
Patch20:        teTeX-locale.patch
URL:		http://www.tug.org/teTeX/
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
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	expat-devel
PreReq:		/sbin/ldconfig
PreReq:		sed
PreReq:		awk
PreReq:		textutils
PreReq:		sh-utils
Requires:	%{name}-fonts-cm = %{version}
Requires:	%{name}-fonts-misc = %{version}
Requires:	dialog
Requires:	tmpwatch
Obsoletes:	tetex-afm
Obsoletes:	tetex-doc
Obsoletes:	tetex-tex-hyphen
Obsoletes:	tetex-fontname
Obsoletes:	tetex-fontinst
Obsoletes:	tetex-fonts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texmf	%{_datadir}/texmf
%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ; 
%define		fixinfodir [ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1 ; 
%define		fmtutil(f:) [ ! \\\( -f %{texmf}/web2c/%{-f*}.fmt.rpmnew -o -f %{texmf}/web2c/%{-f*}.efmt.rpmnew \\\) ] || %{_bindir}/fmtutil --byfmt %{-f*} >/dev/null 2>/dev/null || echo "Regenerating %{-f*} failed. See %{texmf}/web2c/%{-f*}.log for details" 1>&2 && exit 0 ; 

%define 	_noautoreq 'perl(path_tre)'

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
Summary(pl):	Katalog TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-Catalogue
TeX Catalogue.

%description doc-Catalogue -l pl
Katalog TeXa.

%package doc-tug-faq
Summary:	TeX User Group FAQ
Summary(pl):	FAQ Grupy U¿ytkowników TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-doc-uktug-faq
Obsoletes:	tetex-doc-de-tex-faq
Obsoletes:	tetex-doc-LaTeX-FAQ-francaise

%description doc-tug-faq
TeX User Group FAQ.

%description doc-tug-faq -l pl
FAQ Grupy U¿ytkowników TeXa.

%package doc-latex
Summary:	Basic LaTeX packages documentation
Summary(pl):	Podstawowa dokumentacja do pakietów LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-latex
Basic LaTeX packages documentation.

%description doc-latex -l pl
Podstawowa dokumentacja do pakietów LaTeXa.

%package doc-latex2e-html
Summary:	HTML LaTeX2e documentation
Summary(pl):	Dokumentacja LaTeX2e w formacie HTML
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description doc-latex2e-html
HTML LaTeX2e documentation.

%description doc-latex2e-html -l pl
Dokumentacja LaTeX2e w formacie HTML.

#
# libraries
#
%package -n kpathsea
Summary:	File name lookup library
Summary(pl):	Biblioteka szukaj±ca nazw plików
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description -n kpathsea
File name lookup library.

%description -n kpathsea -l pl
Biblioteka szukaj±ca nazw plików.

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
Summary(pl):	Konwerter plików DVI do PostScriptu
Summary(pt_BR):	Conversor dvi para postscript
Summary(tr):	dvi'dan postscript'e dönüþtürücü
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
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
Summary(fr):	convertisseur dvi vers laserjet
Summary(pl):	Konwerter plików DVI do jêzyka PCL
Summary(pt_BR):	Conversor dvi para laserjet
Summary(tr):	dvi'dan laserjet'e dönüþtürücü
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
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

%description dvilj -l pl
dvilj oraz pokrewne narzêdzia (za³±czone w tym pakiecie) konwertuj±
pliki wyj¶ciowe .dvi systemu formatuj±cego tekst TeX na polecenia
HP PCL (HP Printer Control Language). Przy u¿yciu dvilj mo¿na drukowaæ
pliki TeXa na drukarkach HP LaserJet+ i w pe³ni kompatybilnych. Przy
u¿yciu dvilj2p mo¿na drukowaæ na drukarkach HP LaserJet IIP i w pe³ni
kompatybilnych. Przy u¿yciu dvilj4 mo¿na drukowaæ na drukarkach HP
LaserJet4 i w pe³ni kompatybilnych.

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
Summary:	A general purpose hierarchical index generator
Summary(pl):	Generator hierarchicznych indeksów ogólnego przeznaczenia
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-rumakeindex

%description makeindex
A general purpose hierarchical index generator; it accepts one or more
input files (often produced by a text formatter such as TeX or troff),
sorts the entries, and produces an output file which can be formatted.
The formats of the input and output files are specified in a style
file; by default, input is assumed to be an idx file, as generated by
LaTeX.

%description makeindex -l pl
Generator hierarchicznych indeksów ogólnego przeznaczenia; przyjmuje
jeden lub wiêcej plików wej¶ciowych (zazwyczaj zrobionych przez
narzêdzie formatuj±ce tekst, takie jak TeX lub troff), sortuje
elementy i tworzy plik wyj¶ciowy, który mo¿e byæ sformatowany. Formaty
plików wej¶ciowych i wyj¶ciowych podaje siê w pliku stylu; domy¶lnie
przyjmowany jest plik wej¶ciowy w formacie idx, wygenerowany przez
LaTeX.

%package metafont
Summary:	MetaFont
Summary(pl):	Zestaw narzêdzi MetaFont
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description metafont
MetaFont.

%description metafont -l pl
Zestaw narzêdzi MetaFont.

%package metapost
Summary:	MetaPost
Summary(pl):	Zestaw narzêdzi MetaPost
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-matapost

%description metapost
MetaPost.

%description metapost -l pl
Zestaw narzêdzi MetaPost.

%package mptopdf
Summary:	MetaPost to PDF converter
Summary(pl):	Konwerter MetaPost do PDF
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-metapost = %{version}

%description mptopdf
MetaPost to PDF converter.

%description mptopdf -l pl
Konwerter MetaPost do PDF.

%package texdoctk
Summary:	Easy access to TeX documentation
Summary(pl):	£atwy dostêp do dokumentacji TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description texdoctk
A Perl/Tk-based GUI for easy access to package documentation for TeX
on Unix platforms; the databases it uses are based on the texmf/doc
subtrees of teTeX v.1.0.x, but database files for local configurations
with modified/extended directories can be derived from them. Note that
texdoctk is not a viewer itself, but an interface for finding
documentation files and opening them with the appropriate viewer; so
it relies on appropriate programs to be installed on the system.
However, the choice of these programs can be configured by the
sysadmin or user.

%description texdoctk -l pl
Oparty na Perlu i Tk graficzny interfejs daj±cy ³atwy dostêp do
dokumentacji pakietów TeXowych na platformach uniksowych; u¿ywa baz
danych opartych na poddrzewach texmf/doc z teTeXa 1.0.x, ale mo¿e
u¿ywaæ konfiguracji ze zmodyfikowanymi lub rozszerzonymi katalogami.
Nale¿y zauwa¿yæ, ¿e texdoctk sam w sobie nie jest przegl±dark±, ale
interfejsem do wyszukiwania plików dokumentacji i otwierania ich we
w³a¶ciwej przegl±darce; tak wiêc wymaga on odpowiednich programów
zainstalowanych w systemie. Wybór tych programów mo¿e byæ dokonany
przez administratora lub u¿ytkownika.

%package -n texconfig
Summary:	TeX typesetting system configurator
Summary(pl):	Konfigurator systemu sk³adu TeX
Group:		Applications/Publishing/TeX
Requires:	xdvi = %{version}
Requires:	%{name} = %{version}
Requires:	%{name}-dvips = %{version}
Requires:	%{name}-metafont = %{version}
Obsoletes:	tetex-texconfig

%description -n texconfig
TeX typesetting system configurator.

%description -n texconfig -l pl
Konfigurator systemu sk³adu TeX.

%package -n xdvi
Summary:	X11 previewer
Summary(de):	X11-Previewer
Summary(es):	Visualizador TeX X11
Summary(fr):	Prévisualisateur X11
Summary(pl):	Przegl±darka DVI dla X11
Summary(pt_BR):	Visualizador TeX X11
Summary(tr):	X11 öngörüntüleyici
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-metafont = %{version}
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
Summary(pl):	TeX generuj±cy pliki PDF zamiast DVI
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-type1-bluesky = %{version}

%description pdftex
TeX generating PDF files instead DVI.

%description pdftex -l pl
TeX generuj±cy pliki PDF zamiast DVI.

#
# formats
#

# Plain format.

%package plain
Summary:	Plain TeX format basic files
Summary(pl):	Podstawowe pliki dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain
Plain TeX format basic files.

%description plain -l pl
Podstawowe pliki dla formatu Plain TeX.

%package plain-dvips
Summary:	PostScript support for Plain TeX format
Summary(pl):	Obs³uga PostScriptu dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-dvips = %{version}
Requires:	%{name}-plain = %{version}

%description plain-dvips
PostScript support for Plain TeX format.

%description plain-dvips -l pl
Obs³uga PostScriptu dla formatu Plain TeX.

%package plain-mathtime
Summary:	Mathtime fonts for Plain
Summary(pl):	Fonty Mathtime dla formatu Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description plain-mathtime
The Mathtime fonts have a number of characters remapped to positions
different from the ones normally used by the corresponding TeX
CM-fonts. For the symbol font ``operators'' the corresponding mathtime
style files use the Times Roman font (often called something like:
ptmr or ptmr7t or ptmrq).

%description plain-mathtime -l pl
Fonty Mathtime zawieraj± wiele znaków przemapowanych na pozycje
ró¿ni±ce siê od tych normalnie u¿ywanych w odpowiadaj±cych im TeXowych
fontach CM. Dla fontu symboli "operators" odpowiadaj±cy styl mathtime
u¿ywa fontu Times Roman (zazwyczaj nazywanego w stylu ptmr, ptmr7t lub
ptmrq).

%package plain-misc
Summary:	Miscellaneous macros for Plain TeX format
Summary(pl):	Ró¿ne makra dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description plain-misc
Miscellaneous macros for Plain TeX format.

%description plain-misc -l pl
Ró¿ne makra dla formatu Plain TeX.

%package plain-plnfss
Summary:	Simple NFSS macros for Plain TeX
Summary(pl):	Proste makra NFSS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-plnfss
Simple NFSS macros for plain TeX.

%description plain-plnfss -l pl
Proste makra NFSS dla formatu Plain TeX.

%package format-plain
Summary:	TeX Plain format
Summary(pl):	Format TeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description format-plain
TeX Plain format.

%description format-plain -l pl
Format TeX Plain.

%package format-pdftex
Summary:	PDFTeX Plain format
Summary(pl):	Format PDFTeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdftex
PDFTeX Plain format.

%description format-pdftex -l pl
Format PDFTeX Plain.

%package format-pdfetex
Summary:	PDFTeX EPlain format
Summary(pl):	Format PDFTeX EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfetex
PDFTeX EPlain format.

%description format-pdfetex -l pl
Format PDFTeX EPlain.

# MeX Plain format

%package mex
Summary:	MeX Plain Format basic files
Summary(pl):	Podstawowe pliki dla format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	tetex-plain = %{version}
Requires:	tetex-fonts-pl = %{version}

%description mex
MeX Plain Format basic files.

%description mex -l pl
Podstawowe pliki dla formatu MeX Plain.

%package format-mex
Summary:	MeX Plain Format
Summary(pl):	Format MeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-mex = %{version}

%description format-mex
MeX Plain Format.

%description format-mex -l pl
Format MeX Plain.

%package format-pdfmex
Summary:	PDFMeX Plain Format
Summary(pl):	Format PDFMeX Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-mex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfmex
PDFMeX Plain Format.

%description format-pdfmex -l pl
Format PDFMeX Plain.

%package format-pdfemex
Summary:	PDFMeX EPlain Format
Summary(pl):	Format PDFMeX EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-mex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfemex
PDFMeX EPlain Format.

%description format-pdfemex -l pl
Format PDFMeX EPlain.

# AMS TeX format

%package amstex
Summary:	AMS macros for Plain TeX basic files
Summary(pl):	Podstawowe pliki makr AMS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-fonts-ams = %{version}
Obsoletes:	tetex-ams
Obsoletes:	tetex-plain-amsfonts

%description amstex
American Mathematics Society macros for Plain TeX basic files.

%description amstex -l pl
Podstawowe pliki makr AMS (American Mathematics Society) dla formatu
Plain TeX.

%package format-amstex
Summary:	AMS macros for Plain TeX
Summary(pl):	Makra AMS dla formatu Plain TeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-amstex = %{version}
Obsoletes:	tetex-ams

%description format-amstex
American Mathematics Society macros for Plain TeX.

%description format-amstex -l pl
Makra AMS (American Mathematics Society) dla formatu Plain TeX.

%package format-pdfamstex
Summary:	AMS macros for PDFTeX
Summary(pl):	Makra AMS dla formatu PDFTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-amstex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdfamstex
American Mathematics Society macros for PDFTeX.

%description format-pdfamstex -l pl
Makra AMS (American Mathematics Society) dla formatu PDFTeX.

# CSPlain format

%package csplain
Summary:	TeX CSPlain format basic files
Summary(pl):	Podstawowe pliki dla formatu TeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-fonts-cs = %{version}

%description csplain
TeX CSPlain format basic files.

%description csplain -l pl
Podstawowe pliki dla formatu TeX CSPlain.

%package format-csplain
Summary:	TeX CSPlain format
Summary(pl):	Format TeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-csplain = %{version}

%description format-csplain
TeX CSPlain format.

%description format-csplain -l pl
Format TeX CSPlain.

%package format-pdfcsplain
Summary:	PDFTeX CSPlain format
Summary(pl):	Format PDFTeX CSPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-csplain = %{version}

%description format-pdfcsplain
PDFTeX CSPlain format.

%description format-pdfcsplain -l pl
Format PDFTeX CSPlain.

# CSLaTeX format

%package cslatex
Summary:	CSLaTeX format basic files
Summary(pl):	Podstawowe pliki dla formatu CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Requires:	%{name}-fonts-cs = %{version}

%description cslatex
CSLaTeX format basic files.

%description cslatex -l pl
Podstawowe pliki dla formatu CSLaTeX.

%package format-cslatex
Summary:	CSLaTeX format
Summary(pl):	Format CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-cslatex = %{version}

%description format-cslatex
CSLaTeX format.

%description format-cslatex -l pl
Format CSLaTeX.

%package format-pdfcslatex
Summary:	PDF CSLaTeX format
Summary(pl):	Format PDF CSLaTeX
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-cslatex = %{version}

%description format-pdfcslatex
PDF CSLaTeX format.

%description format-pdfcslatex -l pl
Format PDF CSLaTeX.

# Cyrillic Plain format

%package cyrplain
Summary:	Cyrillic Plain format basic files
Summary(pl):	Podstawowe pliki dla formatu Cyrillic Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}

%description cyrplain
Cyrillic Plain format basic files.

%description cyrplain -l pl
Podstawowe pliki dla formatu Cyrillic Plain.

%package format-cyrplain
Summary:	Cyrillic Plain format
Summary(pl):	Format Cyrillic Plain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-cyrplain = %{version}

%description format-cyrplain
Cyrillic Plain format.

%description format-cyrplain -l pl
Format Cyrillic Plain.

%package format-cyramstex
Summary:	Cyrillic AMSTeX format
Summary(pl):	Format Cyrillic AMSTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Obsoletes:	tetex-cyramstex

%description format-cyramstex
Cyrillic AMSTeX format.

%description format-cyramstex -l pl
Format Cyrillic AMSTeX.

%package format-cyrtexinfo
Summary:	Cyrillic TeXInfo format
Summary(pl):	Format Cyrillic TeXInfo
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Obsoletes:	tetex-cyrtexinfo

%description format-cyrtexinfo
Cyrillic TeXInfo format.

%description format-cyrtexinfo -l pl
Format Cyrillic TeXInfo.

# EPlain format

%package eplain
Summary:	EPlain format basic files
Summary(pl):	Podstawowe pliki dla formatu EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-plain = %{version}
Obsoletes:	tetex-etex

%description eplain
EPlain format basic files.

%description eplain -l pl
Podstawowe pliki dla formatu EPlain.

%package format-eplain
Summary:	EPlain format
Summary(pl):	Format EPlain
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-eplain = %{version}

%description format-eplain
EPlain format.

%description format-eplain -l pl
Format EPlain.

# ConTeXt format.

%package context
Summary:	ConTeXt macro package basic files
Summary(pl):	Podstawowe pliki pakietu makr ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-latex-context

%define         _noautoreq 'perl(path_tre)'

%description context
A full featured, parameter driven macro package, which fully supports
advanced interactive documents.

This package contains basic files.

%description context -l pl
Pakiet makr sterowanych przez parametry o pe³nych mo¿liwo¶ciach,
ca³kowicie obs³uguj±cy zaawansowane dokumenty interaktywne.

Ten pakiet zawiera podstawowe pliki.

%package format-context-de
Summary:	German ConTeXt format
Summary(pl):	Niemiecka wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-context = %{version}

%description format-context-de
German ConTeXt format.

%description format-context-de -l pl
Niemiecka wersja formatu ConTeXt.

%package format-context-en
Summary:	English ConTeXt format
Summary(pl):	Angielska wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-context = %{version}

%description format-context-en
English ConTeXt format.

%description format-context-en -l pl
Angielska wersja formatu ConTeXt.

%package format-context-nl
Summary:	Dutch ConTeXt format
Summary(pl):	Holenderska wersja formatu ConTeXt
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-context = %{version}

%description format-context-nl
Dutch ConTeXt format.

%description format-context-nl -l pl
Holenderska wersja formatu ConTeXt.

# LaTeX format.

%package latex
Summary:	LaTeX macro package basic files
Summary(pl):	Podstawowe pliki pakietu makr LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-latex = %{version}
# for misc/eurosym:
Requires:	%{name}-fonts-eurosym = %{version}
Obsoletes:	tetex-bibtex-koma-script
Obsoletes:	tetex-latex-graphics
Obsoletes:	tetex-latex-misc
Obsoletes:	tetex-latex-revtex4
Obsoletes:	tetex-latex-caption
Obsoletes:	tetex-latex-mwcls
Obsoletes:	tetex-latex-titlesec
Obsoletes:	tetex-latex-pb-diagram
Obsoletes:	tetex-latex-units
Obsoletes:	tetex-latex-ntgclass
Obsoletes:	tetex-latex-fp
Obsoletes:	tetex-latex-t2
Obsoletes:	tetex-latex-natbib
Obsoletes:	tetex-latex-listings
Obsoletes:	tetex-latex-oberdiek
Obsoletes:	tetex-latex-hyperref
Obsoletes:	tetex-latex-fancyhdr
Obsoletes:	tetex-latex-fancyvrb
Obsoletes:	tetex-latex-koma-script
Obsoletes:	tetex-latex-multirow
Obsoletes:	tetex-latex-ms
Obsoletes:	tetex-latex-pstriks
Obsoletes:	tetex-latex-seminar
Obsoletes:	tetex-latex-endfloat
Obsoletes:	tetex-latex-curves
Obsoletes:	tetex-latex-SIunits
Obsoletes:	tetex-latex-labels
Obsoletes:	tetex-latex-dvilj
Obsoletes:	tetex-latex-dinbrief
Obsoletes:	tetex-latex-eepic
Obsoletes:	tetex-latex-tools
Obsoletes:	tetex-latex-mwdtools
Obsoletes:	tetex-latex-fancyheadings
Obsoletes:	tetex-mwcls
Obsoletes:	tetex-revtex4
# FIXME: I can't find files from this packages in any subpackage in new tetex
Obsoletes:	tetex-latex-algorith
Obsoletes:	tetex-latex-draftcopy

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains basic files.

%description latex -l pl
LaTeX jest frontendem do systemu formatuj±cego tekst TeX. Jest
³atwiejszy w u¿yciu ni¿ TeX. Jest w³a¶ciwie zestawem makr TeXowych,
daj±cych u¿ytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera podstawowe pliki.

%package latex-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl):	Wirtualne fonty dla plików PDF z fontami CMR o kodowaniu T1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-ae = %{version}

%description latex-ae
A set of virtual fonts which emulates T1 coded fonts using the
standard CM fonts. The package is called AE fonts (for Almost
European). The main use of the package is to produce PDF files using
versions of the CM fonts instead of the bitmapped EC fonts.

%description latex-ae -l pl
Zestaw wirtualnych fontów emuluj±cych fonty o kodowaniu T1 przy u¿yciu
standardowych fontów CM. Ten pakiet zosta³ nazwany AE (Almost European
- prawie europejskie). G³ównym przeznaczeniem tego pakietu jest
produkowanie plików PDF przy u¿yciu wersji fontów CM zamiast
bitmapowych fontów EC.

%package latex-ams
Summary:	AMS math facilities for LaTeX
Summary(pl):	Udogodnienia matematyczne AMS dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-ams = %{version}
Obsoletes:	tetex-latex-amscls
Obsoletes:	tetex-latex-amsfonts
Obsoletes:	tetex-latex-amsmath

%description latex-ams
This package is the principal package in the AMS-LaTeX distribution.
It adapts for use in LaTeX most of the mathematical features found in
AMS-TeX.

%description latex-ams -l pl
To jest g³ówny pakiet dystrybucji AMS-LaTeX. Jest adaptacj± wiêkszo¶ci
mo¿liwo¶ci matematycznych AMS-TeXa do u¿ywania w LaTeXu.

%package latex-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl):	Antykwa Pó³tawskiego - rodzina tradycyjnych czcionek polskich jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-antp = %{version}

%description latex-antp
A replica of Antykwa Poltawskiego font in PostScript Type 1 format
-- preliminary version. This font was designed in the 'twenties and
the 'thirties of XX century by a Polish graphic artist and a
typographer Adam Poltawski. It was widely used by Polish printing
houses as long as metal types were in use (until ca the 'sixties).
Perhaps the first complete font family programmed and parametrized in
METAPOST.

%description latex-antp -l pl
Wstêpna wersja repliki kroju Antykwa Pó³tawskiego w formacie
PostScript Type 1. Ten krój zosta³ opracowany w latach 30-tych i
40-tych XX wieku przez polskiego grafika i typografa Adama
Pó³tawskiego. By³a szeroko u¿ywana przez polskie drukarnie dopóki
u¿ywano metalowych czcionek (do lat 60-tych). Prawdopodobnie pierwsza
kompletna rodzina fontów zaprogramowana i zparametryzowana w
METAPOSCIE.

%package latex-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl):	Antykwa Turuñska - rodzina tradycyjnych czcionek polskich jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-antt = %{version}

%description latex-antt
Antykwa Torunska is a serif font designed by the late Polish
typographer Zygfryd Gardzielewski, reconstructed and digitized as
Type 1.

%description latex-antt -l pl
Antykwa Toruñska to krój szeryfowy opracowany niedawno przez polskiego
typografa Zygfryda Gardzielewskiego, zrekonstruowany i przerobiony na
postaæ cyfrow± jako Type 1.

%package latex-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl):	Tablicowy wariant fontów Computer Modern z obs³ug± LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-bbm = %{version}

%description latex-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description latex-bbm -l pl
Tablicowy wariant fontów Computer Modern z obs³ug± LaTeXa.

%package latex-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl):	Tablicowy t³usty font sans serif dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-bbold = %{version}

%description latex-bbold
A geometric sans serif blackboard bold font, for use in mathematics.

%description latex-bbold -l pl
Geometryczny tablicowy t³usty font sans serif, do u¿ywania w
matematyce.

%package latex-bibtex
Summary:	Bibliography management for LaTeX
Summary(pl):	Zarz±dzenie bibliografi± dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Obsoletes:	tetex-bibtex
Obsoletes:	tetex-rubibtex
Obsoletes:	tetex-natbib

%description latex-bibtex
Bibliography management for LaTeX.

%description latex-bibtex -l pl
Zarz±dzanie bibliografi± dla LaTeXa.

%package latex-bibtex-ams
Summary:	BibTeX style files for American Meteorological Society publications
Summary(pl):	Pliki stylów BibTeXa do publikacji American Meteorological Society
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-ams = %{version}
Requires:	%{name}-latex-bibtex = %{version}
Obsoletes:	tetex-bibtex-ams

%description latex-bibtex-ams
BibTeX style files for American Meteorological Society publications.

%description latex-bibtex-ams -l pl
Pliki stylów BibTeXa do publikacji American Meteorological Society.

%package latex-bibtex-pl
Summary:	Polish bibliography management for LaTeX
Summary(pl):	Polska wersja zarz±dzania bibliografi± dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{version}
Obsoletes:	tetex-bibtex-plbib

%description latex-bibtex-pl
Polish bibliography management for LaTeX.

%description latex-bibtex-pl -l pl
Polska wersja zarz±dzania bibliografi± dla LaTeXa.

%package latex-bibtex-german
Summary:	German variants of standard BibTeX styles
Summary(pl):	Niemieckie wersje standardowych stylów BibTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex-bibtex = %{version}
Obsoletes:	tetex-bibtex-germbib

%description latex-bibtex-german
German variants of standard BibTeX styles.

%description latex-bibtex-german -l pl
Niemieckie wersje standardowych stylów BibTeXa.

%package latex-bibtex-revtex4
Summary:	BibTeX styles for REVTeX4
Summary(pl):	Style BibTeXa dla REVTeX4
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-bibtex-revtex4

%description latex-bibtex-revtex4
BibTeX styles for REVTeX4.

%description latex-bibtex-revtex4 -l pl
Style BibTeXa dla REVTeX4.

%package latex-carlisle
Summary:	Miscellaneous small packages by David Carlisle
Summary(pl):	Ró¿ne ma³e pakiety autorstwa Davida Carlisle
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-carlisle
Miscellaneous small packages by David Carlisle.

%description latex-carlisle -l pl
Ró¿ne ma³e pakiety autorstwa Davida Carlisle.

%package latex-ccfonts
Summary:	Support for Concrete text and math fonts in LaTeX
Summary(pl):	Obs³uga fontów tekstowych i matematycznych Concrete w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX package
for typesetting documents using Concrete as the default font family.
The files support OT1, T1, TS1, and Concrete math including AMS fonts
(Ulrik Vieth's concmath).

%description latex-ccfonts -l pl
Pliki definicji fontów LaTeXowych dla fontów Concrete oraz pakiet
LaTeXa do sk³adania dokumentów przy u¿yciu Concrete jako domy¶lnej
rodziny fontów. Pliki obs³uguj± fonty OT1, T1, TS1 oraz matematyczny
Concrete wraz z AMS (concmath Ulrika Vietha).

%package latex-cite
Summary:	Supports compressed, sorted lists of numerical citations
Summary(pl):	Obs³uga kompresowanych, sortowanych list numerowanych cytatów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-cite
Supports compressed, sorted lists of numerical citations.

%description latex-cite -l pl
Obs³uga kompresowanych, sortowanych list numerowanych cytatów.

%package latex-cmbright
Summary:	Support for CM Bright fonts in LaTeX
Summary(pl):	Obs³uga fontów CM Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-cmbright = %{version}

%description latex-cmbright
A family of sans serif fonts for TeX and LaTeX, based on Donald
Knuth's CM fonts. It comprises OT1, T1 and TS1 encoded text fonts of
various shapes as well as all the fonts necessary for mathematical
typesetting, incl. AMS symbols. This collection provides all the
necessary files for using the fonts with LaTeX.

%description latex-cmbright -l pl
Rodzina fontów sans serif dla TeXa i LaTeXa, oparta na fontach CM
Donalda Knutha. Obejmuje fonty dla kodowañ OT1, T1 i TS1 ró¿nych
kszta³tów oraz fonty niezbêdne do sk³adu matematycznego, w³±cznie z
symbolami AMS. Ten zestaw dostarcza wszystkie niezbêdne pliki do
u¿ywania fontów w LaTeXu.

%package latex-concmath
Summary:	LaTeX package and font definition files to access the Concrete math fonts
Summary(pl):	Pakiet LaTeXa i pliki definicji fontów udostêpniaj±ce fonty matematyczne Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-concmath = %{version}

%description latex-concmath
LaTeX package and font definition files to access the Concrete math
fonts, which were derived from Computer Modern math fonts using
parameters from Concrete Roman text fonts.

%description latex-concmath -l pl
Pakiet LaTeXa i pliki definicji fontów udostêpniaj±ce fonty
matematyczne Concrete wywodz±ce siê z fontów matematycznych Computer
Modern poprzez zastosowanie parametrów fontów tekstowych Concrete
Roman.

%package latex-custom-bib
Summary:	Customized BibTeX styles for LaTeX
Summary(pl):	Dostosowywanie stylów BibTeXa dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-custom-bib
Package generating customized BibTeX bibliography styles from a
generic file using docstrip. Includes support for the Harvard style.

%description latex-custom-bib -l pl
Pakiet generuj±cy dostosowane style bibliografii BibTeXa z ogólnego
pliki przy u¿yciu docstrip. Zawiera obs³ugê stylu Harvard.

%package latex-cyrillic
Summary:	LaTeX Cyrillic support
Summary(pl):	Obs³uga cyrylicy dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-cyrillic
LaTeX Cyrillic support.

%description latex-cyrillic -l pl
Obs³uga cyrylicy dla LaTeXa.

%package latex-dstroke
Summary:	LaTeX doublestroke font
Summary(pl):	Podwójnie kre¶lony font dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-dstroke = %{version}

%description latex-dstroke
Doublestroke font for typesetting the mathematical symbols for the
natural numbers, whole numbers, rational numbers, real numbers and
complex numbers.

%description latex-dstroke -l pl
Podwójnie kre¶lony font do sk³adania symboli matematycznych liczb
naturalnych, ca³kowitych, wymiernych, rzeczywistych i zespolonych.

%package latex-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Summary(pl):	Ró¿ne pakiety autorstwa Joerga Knappena
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-jknappen = %{version}

%description latex-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%description latex-jknappen -l pl
Ró¿ne makra, g³ównie do u¿ywania dodatkowych fontów autorstwa Joerga
Knappena. Zawiera sgmlcmpt.

%package latex-lucidabr
Summary:	Package to make Lucida Bright fonts usable with LaTeX
Summary(pl):	Pakiet umo¿liwiaj±cy u¿ywanie fontów Lucida Bright w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-lucidabr
Package to make Lucida Bright fonts usable with LaTeX.

%description latex-lucidabr -l pl
Pakiet umo¿liwiaj±cy u¿ywanie fontów Lucida Bright w LaTeXu.

%package latex-mathpple
Summary:	Use PostScript Palatino for typesetting maths
Summary(pl):	U¿ywanie postscriptowych fontów Palatino do sk³adania wzorów matematycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-adobe = %{version}

%description latex-mathpple
The package defines the PostScript font family `Palatino' (ppl) as the
default roman font and then uses the `mathpple' fonts for typesetting
math. These virtual fonts have been created for typesetting math in a
style that suits the Palatino text fonts. The AMS fonts, when used
additionally, will be scaled to fit Palatino.

%description latex-mathpple -l pl
Pakiet definiuje rodzinê fontów postscriptowych Palatino (ppl) jako
domy¶lny font roman i u¿ywa fontów mathpple do sk³adania wzorów
matematycznych. Te wirtualne fonty zosta³y stworzone do sk³adania
wzorów matematycznych w stylu pasuj±cym do fontów tekstowych Palatino.
Fonty AMS, je¶li s± dodatkowo u¿ywane, zostan± przeskalowane tak, by
pasowaæ do Palatino.

%package latex-mathtime
Summary:	Mathtime fonts for LaTeX
Summary(pl):	Fonty Mathtime dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-mathtime
The Mathtime fonts have a number of characters remapped to positions
different from the ones normally used by the corresponding TeX
CM-fonts. For the symbol font ``operators'' the corresponding mathtime
style files use the Times Roman font (often called something like:
ptmr or ptmr7t or ptmrq).

%description latex-mathtime -l pl
Fonty Mathtime zawieraj± wiele znaków przemapowanych na pozycje
ró¿ni±ce siê od tych normalnie u¿ywanych w odpowiadaj±cych im TeXowych
fontach CM. Dla fontu symboli "operators" odpowiadaj±cy styl mathtime
u¿ywa fontu Times Roman (zazwyczaj nazywanego w stylu ptmr, ptmr7t lub
ptmrq).

%package latex-mflogo
Summary:	LaTeX support for MetaFont and logo fonts
Summary(pl):	Obs³uga LaTeXa dla MetaFonta i fontów logo
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-mflogo = %{version}

%description latex-mflogo
LaTeX package and font definition file to access the Knuthian `logo'
fonts described in `The MetaFontbook' and the MetaFont and logos in
LaTeX documents.

%description latex-mflogo -l pl
Pakiet LaTeXa i plik definicji fontów udostêpniaj±cy fonty logo Knutha
opisane w "The MetaFontbook" oraz MetaFont i loga w dokumentach
LaTeXa.

%package latex-mfnfss
Summary:	Font description files to use extra fonts like yinit and ygoth
Summary(pl):	Pliki opisów fontów udostêpniaj±ce dodatkowe fonty, jak yinit i ygoth
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-mfnfss
Font description files to use extra fonts like yinit and ygoth.

%description latex-mfnfss -l pl
Pliki opisów fontów udostêpniaj±ce dodatkowe fonty, jak yinit i ygoth.

%package latex-minitoc
Summary:	Produce a table of contents for each chapter
Summary(pl):	Tworzenie spisów tre¶ci dla ka¿dego rozdzia³u
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-minitoc
Produce a table of contents for each chapter.

%description latex-minitoc -l pl
Tworzenie spisów tre¶ci dla ka¿dego rozdzia³u.

%package latex-mltex
Summary:	Support for MLTeX
Summary(pl):	Wsparcie dla MLTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-mltex
Support for MLTeX, the multilingual TeX extension from Michael J.
Ferguson.

%description latex-mltex -l pl
Wsparcie dla MLTeXa - rozszerzenia TeXa z obs³ug± wielu jêzyków,
autorstwa Michaela J. Fergusona.

%package latex-palatcm
Summary:	Palatino + Computer Modern math fonts for LaTeX
Summary(pl):	Fonty matematyczne Palatino i Computer Modern dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-palatcm
Palatino + Computer Modern math fonts for LaTeX.

%description latex-palatcm -l pl
Fonty matematyczne Palatino i Computer Modern dla LaTeXa.

%package latex-psnfss
Summary:	LaTeX font support for common PostScript fonts
Summary(pl):	Obs³uga popularnych fontów postscriptowych w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-adobe = %{version}
Obsoletes:	tetex-latex-mathptm
Obsoletes:	tetex-latex-mathptmx

%description latex-psnfss
LaTeX font definition files, macros and font metrics for common
PostScript fonts.

%description latex-psnfss
LaTeXowe pliki definicji fontów, makra i metryki fontów dla
popularnych fontów postscriptowych.

%package latex-pxfonts
Summary:	PX fonts LaTeX support
Summary(pl):	Obs³uga fontów PX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-px = %{version}
Requires:	%{name}-latex = %{version}

%description latex-pxfonts
PX fonts LaTeX support.

%description latex-pxfonts -l pl
Obs³uga fontów PX w LaTeXu.

%package latex-qfonts
Summary:	A collection of PostScript (Adobe Type 1) fonts in QX layout
Summary(pl):	Zestaw fontów postscriptowych (Adobe Type 1) w uk³adzie QX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-qfonts = %{version}

%description latex-qfonts
A collection of Type 1 fonts; include QuasiBookman, QuasiChancery,
QuasiCourier, QuasiPalatino, QuasiSwiss, QuasiSwissCondensed, and
QuasiTimes (regular, italic, bold and bold italic), based on URW++
fonts distributed with Ghostscript. The fonts are encoded according to
QX layout which facilitates multilingual and technical typesetting
using TeX, preserving usability in Windows applications.

%description latex-qfonts -l pl
Zestaw fontów Type 1; zawiera QuasiBookman, QuasiChancery,
QuasiCourier, QuasiPalatino, QuasiSwiss, QuasiSwissCondensed oraz
QuasiTimes (zwyk³e, pochy³e, t³uste i t³uste pochy³e), oparte na
fontach URW++ rozpowszechnianych z Ghostscriptem. Fonty s± kodowane
zgodnie z uk³adem QX, który u³atwia sk³ad wielojêzyczny i techniczny w
TeXu, zachowuj±c przydatno¶æ dla aplikacji windowsowych.

%package latex-txfonts
Summary:	TX fonts LaTeX support
Summary(pl):	Obs³uga fontów TX w LaTeXu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-tx = %{version}
Requires:	%{name}-latex = %{version}

%description latex-txfonts
TX fonts LaTeX support.

%description latex-txfonts -l pl
Obs³uga fontów TX w LaTeXu.

%package latex-umlaute
Summary:	An interface to inputenc for using alternate input encodings
Summary(pl):	Interfejs inputenc do u¿ywania alternatywnych kodowañ wej¶ciowych
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-umlaute
An interface to inputenc for using alternate input encodings.

%description latex-umlaute -l pl
Interfejs inputenc do u¿ywania alternatywnych kodowañ wej¶ciowych.

%package latex-vnps
Summary:	VNPS fonts for LaTeX
Summary(pl):	Fonty VNPS dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description latex-vnps
VNPS fonts for LaTeX.

%description latex-vnps -l pl
Fonty VNPS dla LaTeXa.

%package latex-vnr
Summary:	VNR fonts for LaTeX
Summary(pl):	Fonty VNR dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-vnr = %{version}

%description latex-vnr
VNR fonts for LaTeX.

%description latex-vnr -l pl
Fonty VNR dla LaTeXa.

%package latex-wasysym
Summary:	Extra characters from the Waldis symbol fonts
Summary(pl):	Dodatkowe znaki z fontów Waldis symbol
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-wasy = %{version}

%description latex-wasysym
Makes some additional characters available that come from the wasy
fonts (Waldis symbol fonts). These fonts are not automatically
included in NFSS2/LaTeX2e since they take up important space and often
aren't necessary if one makes use of the packages amsfonts or amssymb.
Symbols include: join box, diamond, leadsto, sqsubset, lhd, rhd,
apple, ocircle invneg, logof, varint, male, female, phone, clock,
lightning, pointer, sun, bell, permil, smiley, various electrical
symbols, shapes, music notes, circles, signs, astronomy, etc.

%description latex-wasysym -l pl
Pakiet udostêpniaj±cy dodatkowe symbole pochodz±ce z fontów wasy
(Waldis symbol). Te fonty nie s± automatycznie do³±czane w
NFSS2/LaTeX2e, poniewa¿ zajmuj± miejsce i zazwyczaj nie s± potrzebne
je¶li u¿ywa siê pakietów amsfonts lub amssymb. Zestaw symboli zawiera
m.in.: symbole join box, diamond, leadsto, sqsubset, lhd, rhd, apple,
ocircle invneg, logof, varint, male, female, phone, clock, lightning,
pointer, sun, bell, permil, smiley oraz ró¿ne symbole elektryczne,
kszta³ty, nuty, okrêgi, znaki, symbole astronomiczne itp.

%package format-latex
Summary:	LaTeX macro package
Summary(pl):	Pakiet makr LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}

%description format-latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains LaTeX format.

%description format-latex -l pl
LaTeX jest frontendem do systemu formatuj±cego tekst TeX. Jest
³atwiejszy w u¿yciu ni¿ TeX. Jest w³a¶ciwie zestawem makr TeXowych,
daj±cych u¿ytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera format LaTeX.

%package format-elatex
Summary:	ELaTeX macro package
Summary(pl):	Pakiet makr ELaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-eplain = %{version}
Requires:	%{name}-latex = %{version}

%description format-elatex
ELaTeX macro package.

%description format-elatex -l pl
Pakiet makr ELaTeX.

%package format-pdflatex
Summary:	PDF LaTeX macro package
Summary(pl):	Pakiet makr PDF LaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-pdftex = %{version}
Requires:	%{name}-latex-psnfss = %{version}

%description format-pdflatex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF LaTeX format.

%description format-pdflatex -l pl
LaTeX jest frontendem do systemu formatuj±cego tekst TeX. Jest
³atwiejszy w u¿yciu ni¿ TeX. Jest w³a¶ciwie zestawem makr TeXowych,
daj±cych u¿ytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera format PDF LaTeX.

%package format-pdfelatex
Summary:	PDF ELaTeX macro package
Summary(pl):	Pakiet makr PDF ELaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-format-pdfetex = %{version}
Requires:	%{name}-latex = %{version}

%description format-pdfelatex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

This package contains PDF ELaTeX format.

%description format-pdfelatex -l pl
LaTeX jest frontendem do systemu formatuj±cego tekst TeX. Jest
³atwiejszy w u¿yciu ni¿ TeX. Jest w³a¶ciwie zestawem makr TeXowych,
daj±cych u¿ytkownikom wygodne, predefiniowane formaty dokumentów.

Ten pakiet zawiera format PDF ELaTeX.

# PLaTeX format

%package platex
Summary:	PLaTeX format basic files
Summary(pl):	Podstawowe pliki dla formatu PLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-fonts-pl = %{version}

%description platex
PLaTeX format basic files.

%description platex -l pl
Podstawowe pliki dla formatu PLaTeX.

%package format-platex
Summary:	PLaTeX format
Summary(pl):	Format PLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-platex = %{version}

%description format-platex
PLaTeX format.

%description format-platex -l pl
Format PLaTeX.

%package format-pdfplatex
Summary:	PDF PLaTeX format
Summary(pl):	Format PDF PLaTeX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}
Requires:	%{name}-platex = %{version}
Requires:	%{name}-fonts-type1-pl = %{version}

%description format-pdfplatex
PDF PLaTeX format.

%description format-pdfplatex -l pl
Format PDF PLaTeX.

#
# TeX generic macros
#

%package tex-babel
Summary:	Multilingual support for TeX
Summary(pl):	Obs³uga wielu jêzyków dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-babel
Multilingual support for TeX.

%description tex-babel -l pl
Obs³uga wielu jêzyków dla TeXa.

%package tex-german
Summary:	Supports the new German orthography (neue deutsche Rechtschreibung)
Summary(pl):	Obs³uga nowej ortografii niemieckiej (neue deutsche Rechtschreibung)
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-german
Supports the new German orthography (neue deutsche Rechtschreibung).

%description tex-german -l pl
Obs³uga nowej ortografii niemieckiej (neue deutsche Rechtschreibung).

%package tex-mfpic
Summary:	Macros which generate Metafont or Metapost for drawing pictures
Summary(pl):	Makra generuj±ce Metafont lub Metapost do rysowania obrazków
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-mfpic
Macros which generate Metafont or Metapost for drawing pictures.

%description tex-mfpic -l pl
Makra generuj±ce Metafont lub Metapost do rysowania obrazków.

%package tex-misc
Summary:	Miscellaneous TeX macros
Summary(pl):	Ró¿ne makra TeXowe
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-tex-eijkhout

%description tex-misc
Miscellaneous TeX macros.

%description tex-misc -l pl
Ró¿ne makra TeXowe.

%package tex-pictex
Summary:	Picture drawing macros for TeX and LaTeX
Summary(pl):	Makra do rysowania obrazków dla TeXa i LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-pictex
Picture drawing macros for TeX and LaTeX.

%description tex-pictex -l pl
Makra do rysowania obrazków dla TeXa i LaTeXa.

%package tex-pstricks
Summary:	PostScript macros for TeX
Summary(pl):	Makra postscriptowe dla TeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-pstricks
An extensive collection of PostScript macros that is compatible with
most TeX macro packages, including Plain TeX, LaTeX, AMS-TeX, and
AMS-LaTeX. Included are macros for color, graphics, pie charts,
rotation, trees and overlays. It has many special features, including:
a wide variety of graphics (picture drawing) macros, with a flexible
interface and with color support. There are macros for coloring or
shading the cells of tables.

%description tex-pstricks -l pl
Du¿y zestaw makr postscriptowych kompatybilny z wiêkszo¶ci± pakietów
makr TeXowych, w tym: Plain TeX, LaTeX, AMS-TeX i AMS-LaTeX. Za³±czono
makra obs³uguj±ce kolory, grafikê, wykresy ko³owe, obroty, drzewa i
nak³adanie. Maj± wiele mo¿liwo¶ci, w tym du¿o makr graficznych (do
rysowania obrazków) z elastycznym interfejsem i obs³ug± koloru. S± te¿
makra do kolorowania lub cieniowania komórek tabel.

%package tex-qpx
Summary:	QuasiPalatino and PX fonts typesetting support
Summary(pl):	Wsparcie dla sk³adu fontami QuasiPalatino i PX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-qpx = %{version}

%description tex-qpx
QuasiPalatino and PX fonts typesetting support.

%description tex-qpx -l pl
Wsparcie dla sk³adu fontami QuasiPalatino i PX.

%package tex-qtx
Summary:	QuasiTimes and TX fonts typesetting support
Summary(pl):	Wsparcie dla sk³adu fontami QuasiTimes i TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-qtx = %{version}

%description tex-qtx
QuasiTimes and TX fonts typesetting support.

%description tex-qtx -l pl
Wsparcie dla sk³adu fontami QuasiTimes i TX.

%package tex-ruhyphen
Summary:	Russian hyphenation
Summary(pl):	Rosyjskie regu³y przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-ruhyphen
A collection of Russian hyphenation patterns supporting a number of
Cyrillic font encodings, including T2, UCY (Omega Unicode Cyrillic),
LCY, LWN (OT2), and koi8-r.

%package tex-spanish
Summary:	Various TeX related files for typesetting documents written in Spanish
Summary(pl):	Ró¿ne pliki TeXowe s³u¿±ce do sk³adu dokumentów w jêzyku hiszpañskim
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Obsoletes:	tetex-tex-spanishb

%description tex-spanish
Various TeX related files for typesetting documents written in
Spanish, including hyphenation and dictionaries.

%description tex-spanish -l pl
Ró¿ne pliki TeXowe s³u¿±ce do sk³adu dokumentów napisanych w jêzyku
hiszpañskim - w tym regu³y przenoszenia wyrazów i s³owniki.

%package tex-texdraw
Summary:	Graphical macros, using embedded PostScript
Summary(pl):	Makra graficzne u¿ywaj±ce osadzanego PostScriptu
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-texdraw
Graphical macros, using embedded PostScript.

%description tex-texdraw -l pl
Makra graficzne u¿ywaj±ce osadzanego PostScriptu.

%package tex-thumbpdf
Summary:	Thumbnails for PDFTeX and dvips/ps2pdf
Summary(pl):	Ikonki dla PDFTeXa i dvips/ps2pdf
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-thumbpdf
Provides support, using Perl, for thumbnails in pdfTeX and
dvips/ps2pdf, using ghostscript to generate the thumbnails which
get represented in a TeX readable file that is read by the package
thumbpdf.sty to automatically include the thumbnails. Works with both
plain TeX and LaTeX.

%description tex-thumbpdf -l pl
Pakiet przy pomocy Perla dodaje ikonki w pdfTeXu i dvips/ps2pdf przy
u¿yciu ghostscripta. Ikonki s± reprezentowane w pliku czytanym przez
TeXa, który jest wywo³ywany z thumbpdf.sty, aby automatycznie do³±czyæ
ikonki. Dzia³a z formatami plain TeX i LaTeX.

%package tex-ukrhyph
Summary:	Ukranian hyphenation
Summary(pl):	Ukraiñskie zasady przenoszenia wyrazów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-ukrhyph
This package allows the use of different hyphenation patterns for the
Ukrainian language for various Cyrillic font encodings. Contains
packages implementing traditional rules, modern rules, and combined
English-Ukrainian hyphenation.

%description tex-ukrhyph -l pl
Ten pakiet pozwala na u¿ywanie ró¿nych wzorców przenoszenia wyrazów
dla jêzyka ukraiñskiego z ró¿nymi kodowaniami fontów z cyrylic±.
Zawiera pakiety z implementacj± regu³ tradycyjnych, wspó³czesnych i
³±czonych angielsko-ukraiñskich.

%package tex-vietnam
Summary:	Vietnamese language support
Summary(pl):	Wsparcie dla jêzyka wietnamskiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description tex-vietnam
Vietnamese language support.

%description tex-vietnam -l pl
Wsparcie dla jêzyka wietnamskiego.

%package tex-xypic
Summary:	Package for typesetting a variety of graphs and diagrams with TeX
Summary(pl):	Pakiet do sk³adania w TeXu ró¿nych wykresów i diagramów
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-xypic = %{version}

%description tex-xypic
A package for typesetting a variety of graphs and diagrams with TeX.
Xy-pic works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX,
and plain TeX), in particular Xy-pic is provided as a LaTeX2e
`supported package'.

%description tex-xypic -l pl
Pakiet do sk³adania w TeXu ró¿nych wykresów i diagramów. Xy-pic dzia³a
z wiêkszo¶ci± formatów (w tym LaTeX, AMS-LaTeX, AMS-TeX i plain TeX),
w szczególno¶ci jest do³±czany jako "wspierany pakiet" LaTeX2e.

#
# Fonts packages
#

%package fonts-adobe
Summary:	Adobe fonts
Summary(pl):	Fonty Adobe
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-adobe
Adobe fonts.

%description fonts-adobe -l pl
Fonty Adobe.

%package fonts-ae
Summary:	Virtual fonts for PDF-files with T1 encoded CMR-fonts
Summary(pl):	Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-ae
Virtual fonts for PDF-files with T1 encoded CMR-fonts.

%description fonts-ae -l pl
Wirtualne fonty do plików PDF z fontami CMR o kodowaniu T1.

%package fonts-ams
Summary:	AMS fonts
Summary(pl):	Fonty AMS
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-ams
AMS fonts.

%description fonts-ams -l pl
Fonty AMS.

%package fonts-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl):	Antykwa Pó³tawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description fonts-antp -l pl
Antykwa Pó³tawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package fonts-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl):	Antykwa Toruñska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-antt -l pl
Antykwa Toruñska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-bbm
Summary:	Blackboard variant fonts for Computer Modern, with LaTeX support
Summary(pl):	Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-bbm
Blackboard variant fonts for Computer Modern, with LaTeX support.

%description fonts-bbm -l pl
Tablicowy wariant fontów Computer Modern ze wsparciem dla LaTeXa.

%package fonts-bbold
Summary:	Sans serif blackboard bold for LaTeX
Summary(pl):	Tablicowy t³usty font sans serif dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-bbold
Sans serif blackboard bold for LaTeX.

%description fonts-bbold -l pl
Tablicowy t³usty font sans serif dla LaTeXa.

%package fonts-bh
Summary:	Bold & Heavy Fonts
Summary(pl):	Fonty Bold i Heavy
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-bh
Bold & Heavy Fonts.

%description fonts-bh -l pl
Fonty Bold i Heavy.

%package fonts-bitstrea
Summary:	Bitstream fonts
Summary(pl):	Fonty Bitstream
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-bitstrea
Bitstream fonts.

%description fonts-bitstrea -l pl
Fonty Bitstream.

%package fonts-cbgreek
Summary:	Complete set of Greek fonts
Summary(pl):	Pe³ny zestaw fontów greckich
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cbgreek
Complete set of Greek fonts.

%description fonts-cbgreek -l pl
Pe³ny zestaw fontów greckich.

%package fonts-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl):	Polska wersja fontów Computer Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-cc-pl -l pl
Polska wersja fontów Computer Concrete.

%package fonts-cg
Summary:	Compugraphic fonts
Summary(pl):	Fonty Compugraphic
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cg
Compugraphic fonts.

%description fonts-cg -l pl
Fonty Compugraphic.

%package fonts-cm
Summary:	Computer Modern fonts
Summary(pl):	Fonty Computer Modern
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cm
Computer Modern fonts.

%description fonts-cm -l pl
Fonty Computer Modern.

%package fonts-cmbright
Summary:	CM Bright fonts
Summary(pl):	Fonty CM Bright
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cmbright
CM Bright fonts.

%description fonts-cmbright -l pl
Fonty CM Bright.

%package fonts-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-cmcyr -l pl
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-cmextra
Summary:	Extra Computer Modern fonts, from the American Mathematical Society
Summary(pl):	Dodatkowe fonty Computer Modern z AMS
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cmextra
Extra Computer Modern fonts, from the American Mathematical Society.

%description fonts-cmextra -l pl
Dodatkowe fonty Computer Modern z AMS (American Mathematical Society).

%package fonts-concmath
Summary:	Concrete Math fonts
Summary(pl):	Fonty matematyczne Concrete Math
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-concmath
Concrete Math fonts.

%description fonts-concmath -l pl
Fonty matematyczne Concrete Math.

%package fonts-concrete
Summary:	Concrete Roman fonts
Summary(pl):	Fonty Concrete Roman
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-concrete
Concrete Roman fonts, designed by Donald E. Knuth, originally for use
with Euler math fonts.

%description fonts-concrete -l pl
Fonty Concrete Roman, opracowane przez Donalda E. Knutha, oryginalnie
przeznaczone do u¿ywania z fontami matematycznymi Euler.

%package fonts-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl):	Fonty MetaFont Computer Modern dla jêzyków czeskiego i s³owackiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-cs -l pl
Fonty MetaFont Computer Modern zmodyfikowane pod k±tem jêzyków
czeskiego i s³owackiego.

%package fonts-dstroke
Summary:	Doublestroke font for typesetting the mathematical symbols
Summary(pl):	Podwójnie kre¶lony font do sk³adania symboli matematycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-dstroke
Doublestroke font for typesetting the mathematical symbols.

%description fonts-dstroke -l pl
Podwójnie kre¶lony font do sk³adania symboli matematycznych.

%package fonts-ecc
Summary:	Sources for the European Concrete fonts
Summary(pl):	¬ród³a dla fontów European Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-ecc
The MetaFont sources and tfm files of the European Concrete Fonts.
This is the EC implementation of Knuth's Concrete fonts, including
also the corresponding text companion fonts.

%description fonts-ecc -l pl
¬ród³a MetaFonta i pliki tfm dla fontów European Concrete. Jest to
implementacja EC fontów Concrete Knutha, w³±cznie z odpowiadaj±cymi
tekstowymi fontami towarzysz±cymi.

%package fonts-eurosym
Summary:	The new European currency symbol for the Euro
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing several
shapes (normal, slanted, bold, outline).

%package fonts-euxm
Summary:	Fonts similar to EUSM but with two more characters
Summary(pl):	Fonty podobne do EUSM, ale z dwoma dodatkowymi znakami
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-euxm
Fonts like EUSM but with two more characters needed for Concrete Math
included in TeXLive distribution in fonts3.

%description fonts-euxm -l pl
Fonty podobne do EUSM, ale z dwoma dodatkowymi znakami, potrzebnymi
dla Concrete Math do³±czonego w fonts3 dystrybucji TeXLive.

%package fonts-gothic
Summary:	Gothic and ornamental initial fonts by Yannis Haralambous
Summary(pl):	Pocz±tkowe fonty gotyckie i ornamentowe Yannisa Haralambousa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-gothic
Gothic and ornamental initial fonts by Yannis Haralambous.

%description fonts-gothic -l pl
Pocz±tkowe fonty gotyckie i ornamentowe Yannisa Haralambousa.

%package fonts-hoekwater
Summary:	Converted mflogo font
Summary(pl):	Przekonwertowany font mflogo
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by
Taco Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2,
xipa.

%description fonts-hoekwater -l pl
Fonty oryginalnie stworzone w MetaFoncie, przekszta³cone do
PostScriptu przez Taco Hoekwatera; zawieraj±: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package fonts-jknappen
Summary:	Miscellaneous packages by Joerg Knappen
Summary(pl):	Ró¿ne pakiety autorstwa Joerga Knappena
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-jknappen
Miscellaneous macros, mostly for making use of extra fonts, by Joerg
Knappen, including sgmlcmpt.

%description fonts-jknappen -l pl
Ró¿ne makra, g³ównie do u¿ywania dodatkowych fontów autorstwa Joerga
Knappena. Zawiera sgmlcmpt.

%package fonts-latex
Summary:	Basic LaTeX fonts
Summary(pl):	Podstawowe fonty dla LaTeXa
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-latex
Basic LaTeX fonts.

%description fonts-latex -l pl
Podstawowe fonty dla LaTeXa.

%package fonts-lh
Summary:	Olga Lapko's LH fonts
Summary(pl):	Fonty LH Olgi Lapko
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-lh
The lh fonts for the `T2'/X2 encodings (for cyrillic languages).

%description fonts-lh -l pl
Fonty lh dla kodowañ `T2'/X2 (dla jêzyków zapisywanych cyrylic±).

%package fonts-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Summary(pl):	Font Symbol Martina Vogela (marvosym)
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description fonts-marvosym -l pl
Font Symbol Martina Vogela (marvosym) to font zawieraj±cy: symbol
waluty Euro zdefiniowany przez Komisjê Europejsk±; symbole waluty
Euro dla krojów Times, Helvetica i Courier; symbole dla in¿ynierii
strukturalnej; symbole dla przekroi poprzecznych; symbole
astronomiczne (S³oñce, Ksiê¿yc, planety); 12 znaków Zodiaku; symbole
krawieckie; znak CE i inne.

%package fonts-mflogo
Summary:	Logo fonts
Summary(pl):	Fonty logo
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-mflogo
Logo fonts.

%description fonts-mflogo -l pl
Fonty logo.

%package fonts-misc
Summary:	Miscellaneous fonts
Summary(pl):	Ró¿ne fonty
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-misc
Miscellaneous fonts.

%description fonts-misc -l pl
Ró¿ne fonty.

%package fonts-monotype
Summary:	Monotype fonts
Summary(pl):	Fonty Monotype
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-monotype
Monotype fonts.

%description fonts-monotype -l pl
Fonty Monotype.

%package fonts-pandora
Summary:	The Pandora font family
Summary(pl):	Rodzina fontów Pandora
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-pandora
The Pandora font family.

%description fonts-pandora -l pl
Rodzina fontów Pandora.

%package fonts-pazo
Summary:	Pazo fonts
Summary(pl):	Fonty Pazo
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-pazo
Pazo fonts.

%description fonts-pazo -l pl
Fonty Pazo.

%package fonts-pl
Summary:	Polish fonts
Summary(pl):	Polskie fonty
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-pl
Polish fonts.

%description fonts-pl -l pl
Polskie fonty.

%package fonts-px
Summary:	PX fonts
Summary(pl):	Fonty PX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-px
PX fonts.

%description fonts-px -l pl
Fonty PX.

%package fonts-qfonts
Summary:	Quasi fonts
Summary(pl):	Fonty Quasi
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-qfonts
Quasi fonts.

%description fonts-qfonts -l pl
Fonty Quasi.

%package fonts-qpx
Summary:	Additional fonts for QPX package
Summary(pl):	Dodatkowe fonty dla pakietu QPX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-qfonts = %{version}
Requires:	%{name}-fonts-px = %{version}

%description fonts-qpx
Additional fonts for QPX package.

%description fonts-qpx -l pl
Dodatkowe fonty dla pakietu QPX.

%package fonts-qtx
Summary:	Additional fonts for QTX package
Summary(pl):	Dodatkowe fonty dla pakietu QTX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-qfonts = %{version}
Requires:	%{name}-fonts-tx = %{version}

%description fonts-qtx
Additional fonts for QTX package.

%description fonts-qtx -l pl
Dodatkowe fonty dla pakietu QTX.

%package fonts-rsfs
Summary:	Fonts of uppercase script letters for scientific and mathematical typesetting
Summary(pl):	Fonty wielkich liter pisanych do sk³adania dokumentów naukowych i matematycznych
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-rsfs
Fonts of uppercase script letters for use as symbols in scientific and
mathematical typesetting, in contrast to the informal script fonts
such as that used for the `calligraphic' symbols in the TeX math
symbol font.

%description fonts-rsfs -l pl
Fonty wielkich liter pisanych do u¿ywania jako symbole przy sk³adaniu
dokumentów naukowych i matematycznych, w odró¿nieniu od nieformalnych
fontów pisanych takich jak u¿ywane do symboli "kaligraficznych" w
matematycznym foncie TeXowym symbol.

%package fonts-stmaryrd
Summary:	St Mary Road symbols for functional programming
Summary(pl):	Symbole St Mary Road do programowania funkcyjnego
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-stmaryrd
St Mary Road symbols for functional programming.

%description fonts-stmaryrd -l pl
Symbole St Mary Road do programowania funkcyjnego.

%package fonts-tx
Summary:	TX fonts
Summary(pl):	Fonty TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-tx
TX fonts.

%description fonts-tx -l pl
Fonty TX.

%package fonts-urw
Summary:	URW fonts
Summary(pl):	Fonty URW
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-urw
URW fonts.

%description fonts-urw -l pl
Fonty URW.

%package fonts-vcm
Summary:	VCM fonts
Summary(pl):	Fonty VCM
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-vcm
VCM fonts.

%description fonts-vcm -l pl
Fonty VCM.

%package fonts-vnr
Summary:	VNR fonts
Summary(pl):	Fonty VNR
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-vnr
VNR fonts.

%description fonts-vnr -l pl
Fonty VNR.

%package fonts-wasy
Summary:	Waldis symbol fonts
Summary(pl):	Fonty Waldis symbol
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-wasy
Waldis symbol fonts.

%description fonts-wasy -l pl
Fonty Waldis symbol.

%package fonts-xypic
Summary:	Xy-pic fonts
Summary(pl):	Fonty Xy-pic
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-xypic
Xy-pic fonts.

%description fonts-xypic -l pl
Fonty Xy-pic.

%package fonts-yandy
Summary:	European Modern fonts from Y&Y
Summary(pl):	Fonty European Modern od Y&Y
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-yandy
European Modern fonts from Y&Y.

%description fonts-yandy -l pl
Fonty European Modern od Y&Y.

%package fonts-type1-adobe
Summary:	Adobe Type1 fonts
Summary(pl):	Fonty Type1 Adobe
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-adobe
Adobe Type1 fonts.

%description fonts-type1-adobe -l pl
Fonty Type1 Adobe.

%package fonts-type1-antp
Summary:	Antykwa Poltawskiego, a Type 1 family of Polish traditional type
Summary(pl):	Antykwa Pó³tawskiego - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-antp
Antykwa Poltawskiego, a Type 1 family of Polish traditional type.

%description fonts-type1-antp -l pl
Antykwa Pó³tawskiego - rodzina tradycyjnych polskich czcionek jako
Type 1.

%package fonts-type1-antt
Summary:	Antykwa Torunska, a Type 1 family of a Polish traditional type
Summary(pl):	Antykwa Toruñska - rodzina tradycyjnych polskich czcionek jako Type 1
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-antt
Antykwa Torunska, a Type 1 family of a Polish traditional type.

%description fonts-type1-antt -l pl
Antykwa Toruñska - rodzina tradycyjnych polskich czcionek jako Type 1.

%package fonts-type1-belleek
Summary:	Free replacement for basic MathTime fonts
Summary(pl):	Wolnodostêpny zamiennik podstawowych fontów MathTime
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-belleek
Free replacement for basic MathTime fonts.

%description fonts-type1-belleek
Wolnodostêpny zamiennik podstawowych fontów MathTime.

%package fonts-type1-bitstrea
Summary:	Bitstream fonts
Summary(pl):	Fonty Bitstream
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-bitstrea
Bitstream fonts.

%description fonts-type1-bitstrea -l pl
Fonty Bitstream.

%package fonts-type1-bluesky
Summary:	Computer Modern family fonts
Summary(pl):	Fonty z rodziny Computer Modern
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-bluesky
Computer Modern family fonts.

%description fonts-type1-bluesky -l pl
Fonty z rodzony Computer Modern.

%package fonts-type1-cc-pl
Summary:	Polish version of Computer Concrete fonts
Summary(pl):	Polska wersja fontów Computer Concrete
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-cc-pl
Polish version of Computer Concrete fonts.

%description fonts-type1-cc-pl -l pl
Polska wersja fontów Computer Concrete.

%package fonts-type1-cmcyr
Summary:	Computer Modern fonts extended with Russian letters
Summary(pl):	Fonty Computer Modern rozszerzone o litery rosyjskie
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-cmcyr
Computer Modern fonts extended with Russian letters.

%description fonts-type1-cmcyr -l pl
Fonty Computer Modern rozszerzone o litery rosyjskie.

%package fonts-type1-cs
Summary:	Czech/Slovak-tuned MetaFont Computer Modern fonts
Summary(pl):	Fonty MetaFont Computer Modern dla jêzyków czeskiego i s³owackiego
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-cs
Czech/Slovak-tuned MetaFont Computer Modern fonts.

%description fonts-type1-cs -l pl
Fonty MetaFont Computer Modern zmodyfikowane pod k±tem jêzyków
czeskiego i s³owackiego.

%package fonts-type1-eurosym
Summary:	The new European currency symbol for the Euro
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-eurosym
The new European currency symbol for the Euro implemented in Metafont,
using the official European Commission dimensions, and providing several
shapes (normal, slanted, bold, outline).

%package fonts-type1-hoekwater
Summary:	Converted mflogo font
Summary(pl):	Przekonwertowany font mflogo
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-hoekwater
Fonts originally created in MetaFont, transformed to PostScript by Taco
Hoekwater; includes logo, manfnt, rsfs, stmaryrd, wasy, wasy2, xipa.

%description fonts-type1-hoekwater -l pl
Fonty oryginalnie stworzone w MetaFoncie, przekszta³cone do
PostScriptu przez Taco Hoekwatera; zawieraj±: logo, manfnt, rsfs,
stmaryrd, wasy, wasy2, xipa.

%package fonts-type1-marvosym
Summary:	Martin Vogel's Symbol (marvosym) font
Summary(pl):	Font Symbol Martina Vogela (marvosym)
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-marvosym
Martin Vogel's Symbol (marvosym) font is a font containing: the Euro
currency symbol as defined by the European commission; Euro currency
symbols in typefaces Times, Helvetica and Courier; Symbols for
structural engineering; Symbols for steel cross-sections; Astronomy
signs (Sun, Moon, planets); The 12 signs of the zodiac; Scissor
symbols; CE sign and others.

%description fonts-type1-marvosym -l pl
Font Symbol Martina Vogela (marvosym) to font zawieraj±cy: symbol
waluty Euro zdefiniowany przez Komisjê Europejsk±; symbole waluty
Euro dla krojów Times, Helvetica i Courier; symbole dla in¿ynierii
strukturalnej; symbole dla przekroi poprzecznych; symbole
astronomiczne (S³oñce, Ksiê¿yc, planety); 12 znaków Zodiaku; symbole
krawieckie; znak CE i inne.

%package fonts-type1-mathpazo
Summary:	Pazo Math fonts
Summary(pl):	Fonty matematyczne Pazo Math
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-mathpazo
Pazo Math fonts.

%description fonts-type1-mathpazo -l pl
Fonty matematyczne Pazo Math.

%package fonts-type1-pl
Summary:	Polish fonts
Summary(pl):	Polskie fonty
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash
Requires:	%{name}-fonts-type1-bluesky = %{version}

%description fonts-type1-pl
Polish fonts.

%description fonts-type1-pl -l pl
Polskie fonty.

%package fonts-type1-px
Summary:	PX fonts
Summary(pl):	Fonty PX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-px
PX fonts.

%description fonts-type1-px -l pl
Fonty PX.

%package fonts-type1-qfonts
Summary:	Quasi fonts
Summary(pl):	Fonty Quasi
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-qfonts
Quasi fonts.

%description fonts-type1-qfonts -l pl
Fonty Quasi.

%package fonts-type1-tx
Summary:	TX fonts
Summary(pl):	Fonty TX
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-tx
TX fonts.

%description fonts-type1-tx -l pl
Fonty TX.

%package fonts-type1-urw
Summary:	URW fonts
Summary(pl):	Fonty URW
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-urw
URW fonts.

%description fonts-type1-urw -l pl
Fonty URW.

%package fonts-type1-xypic
Summary:	Xy-pic fonts
Summary(pl):	Fonty Xy-pic
Group:		Applications/Publishing/TeX
Requires(post,postun):	/usr/bin/texhash

%description fonts-type1-xypic
Xy-pic fonts.

%description fonts-type1-xypic -l pl
Fonty Xy-pic.

%prep
%setup -q -n tetex-src-%{version}
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
%patch19 -p1
%patch20 -p1

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
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT/etc/cron.daily\
	$RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap/

# commented out because of following (non-fatal) error:
# Can't open texmf/web2c/texmf.cnf: No such file or directory.
#perl -pi \
#	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{texmf}|g;" \
#	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
#	texmf/web2c/texmf.cnf

cp -a texmf $RPM_BUILD_ROOT%{texmf}

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	infodir=$RPM_BUILD_ROOT%{_infodir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{texmf}

install %{SOURCE7} $RPM_BUILD_ROOT%{_bindir}/
touch $RPM_BUILD_ROOT/etc/sysconfig/tetex-updmap/maps.lst

%{__make} init \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
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
install %{SOURCE6} $RPM_BUILD_ROOT%{_pixmapsdir}
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

%post mptopdf
%texhash

%postun mptopdf
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

%post format-pdfcslatex
%texhash

%postun format-pdfcslatex
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

# ConTeXt format

%post context
%texhash

%postun context
%texhash

%post format-context-de
%texhash

%postun format-context-de
%texhash

%post format-context-en
%texhash

%postun format-context-en
%texhash

%post format-context-nl
%texhash

%postun format-context-nl
%texhash

# LaTeX format.

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

%post fonts-eurosym
%texhash

%postun fonts-eurosym
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

%post fonts-type1-eurosym
%texhash

%postun fonts-type1-eurosym
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
%dir %{texmf}/doc/cstex
%doc texmf/LICENSE.texmf
%doc %{texmf}/ChangeLog
%doc %{texmf}/doc/README
%doc %{texmf}/doc/README.knuth
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
%doc %{texmf}/doc/knuth

%attr(755,root,root) %{_bindir}/MakeTeXPK
%attr(755,root,root) %{_bindir}/access
%attr(755,root,root) %{_bindir}/afm2tfm
%attr(755,root,root) %{_bindir}/allcm
%attr(755,root,root) %{_bindir}/allec
%attr(755,root,root) %{_bindir}/allneeded
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/e2pall
%attr(755,root,root) %{_bindir}/ebb
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
%attr(755,root,root) %{_bindir}/t1mapper
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tetex-updmap
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texdoc
%attr(755,root,root) %{_bindir}/texfind
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texi2html
%attr(755,root,root) %{_bindir}/texi2pdf
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/texshow
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

%dir /etc/sysconfig/tetex-updmap
%verify(not size md5 mtime) %config(noreplace) /etc/sysconfig/tetex-updmap/maps.lst

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
%dir %{texmf}/dvips
%dir %{texmf}/dvips/config
%dir %{texmf}/dvips/tetex

%attr(1777,root,root) /var/cache/fonts

%{_datadir}/info/web2c.info*
%{texmf}/updates.dat

%{texmf}/aliases
%{texmf}/fontname
%{texmf}/tex/fontinst
%{texmf}/tex/generic/hyphen
%{texmf}/tex/texinfo
%{texmf}/tex/enctex
%{texmf}/web2c/*.tcx
%{texmf}/web2c/metafun.mem
%{texmf}/web2c/tex-pl.pool
%{texmf}/web2c/tex.pool
%{texmf}/dvips/config/ps2pk.map
%{texmf}/dvips/tetex/ps2pk35.map
%{texmf}/dvips/tetex/09fbbfac.enc
%{texmf}/dvips/tetex/0ef0afca.enc
%{texmf}/dvips/tetex/10037936.enc
%{texmf}/dvips/tetex/1b6d048e.enc
%{texmf}/dvips/tetex/71414f53.enc
%{texmf}/dvips/tetex/74afc74c.enc
%{texmf}/dvips/tetex/aae443f0.enc
%{texmf}/dvips/tetex/b6a4d7c7.enc
%{texmf}/dvips/tetex/bbad153f.enc
%{texmf}/dvips/tetex/d9b29452.enc
%{texmf}/dvips/tetex/f7b6d320.enc

%lang(fi) %{_mandir}/fi/man1/afm2tfm.1*
%lang(fi) %{_mandir}/fi/man1/allcm.1*
%lang(fi) %{_mandir}/fi/man1/allneeded.1*
%lang(fr) %{_mandir}/fr/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/access.1*
%lang(hu) %{_mandir}/hu/man1/newer.1*
%lang(pl) %{_mandir}/pl/man1/access.1*
%lang(pl) %{_mandir}/pl/man1/newer.1*
#%%{_mandir}/man1/MakeTeXPK.1*
%{_mandir}/man1/access.1*
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/allcm.1*
#%%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/cweb.1*
%{_mandir}/man1/dmp.1*
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/fontexport.1*
%{_mandir}/man1/fontimport.1*
%{_mandir}/man1/fontinst.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/gsftopk.1*
#%%{_mandir}/man1/initex.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/mktexlsr.1*
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
%{_mandir}/man1/t1mapper.1*
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texdoc.1*
#%%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texi2html.1*
%{_mandir}/man1/texi2pdf.1*
%{_mandir}/man1/texshow.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/vftovp.1*
#%%{_mandir}/man1/virtex.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/updmap.1*
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
%dir %{texmf}/doc/latex
%dir %{texmf}/doc/latex/styles
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
%{texmf}/doc/latex/extsizes
%{texmf}/doc/latex/fancy*
%{texmf}/doc/latex/float*
%{texmf}/doc/latex/footmisc
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
#%%{texmf}/doc/latex/styles/listings.dvi
#%%{texmf}/doc/latex/styles/lucidabr.txt
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
%doc %{texmf}/doc/latex/psnfssx
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvipdfm
%attr(755,root,root) %{_bindir}/dvipdft
# dvi2fax requires ghostscript
%attr(755,root,root) %{_bindir}/dvi2fax
%{_infodir}/dvips.info*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%lang(fi) %{_mandir}/fi/man1/dvips.1*
%{texmf}/dvips/base
%{texmf}/dvips/misc
%{texmf}/dvips/gsftopk
%{texmf}/dvips/psfrag
%{texmf}/dvips/psnfss
%{texmf}/dvips/psnfssx
%{texmf}/dvips/config/builtin35.map
%config(noreplace) %verify(not size md5 mtime) %{texmf}/dvips/config/config.ps
%{texmf}/dvips/config/download35.map
%{texmf}/dvips/config/dvipdfm_dl14.map
%{texmf}/dvips/config/dvipdfm_ndl14.map
%{texmf}/dvips/config/psfonts_pk.map
%{texmf}/dvips/config/config.generic
%{texmf}/dvips/config/psfonts.map
%{texmf}/dvips/config/psfonts_t1.map

%{texmf}/dvips/tetex/config.*
%{texmf}/dvips/tetex/dvipdfm35.map
%{texmf}/dvips/tetex/bsr.map
%{texmf}/dvips/tetex/bsr-interpolated.map
%{texmf}/dvips/tetex/dvips35.map
%{texmf}/dvips/lucida
%{texmf}/dvips/tetex/lucidabr*
%{texmf}/dvips/tetex/lumath*
%{texmf}/dvips/tetex/mathpple.map
%{texmf}/dvips/tetex/mt-belleek.map
%{texmf}/dvips/tetex/mt-plus.map
%{texmf}/dvips/tetex/mt-yy.map
%{texmf}/dvips/tetex/mtex.enc
%{texmf}/dvips/tetex/pdftex35.map
%{texmf}/dvips/tetex/ttcmex.map

%dir %{texmf}/dvipdfm
%{texmf}/dvipdfm/config

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
%attr(755,root,root) %{_bindir}/mf-nowin
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mfw
%attr(755,root,root) %{_bindir}/virmf
%attr(755,root,root) %{_bindir}/inimf
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
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
#%%{_mandir}/man1/inimf.1*
#%%{_mandir}/man1/virmf.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*

%files metapost
%defattr(644,root,root,755)
%doc %{texmf}/doc/metapost
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
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
#%%{_mandir}/man1/inimpost.1*
#%%{_mandir}/man1/virmpost.1*

%files mptopdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mptopdf
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/mptopdf.efmt

%files texdoctk
%defattr(644,root,root,755)
%doc %{texmf}/doc/texdoctk
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
%attr(755,root,root) %{_bindir}/xdvizilla
%{_mandir}/man1/xdvi.1*
%{_mandir}/man1/xdvizilla.1*
%{_applnkdir}/Graphics/Viewers/xdvi.desktop
%{_pixmapsdir}/xdvi.png
%dir %{texmf}/xdvi
%{texmf}/xdvi/XDvi
%{texmf}/xdvi/xdvi.cfg

%files pdftex
%defattr(644,root,root,755)
%doc %{texmf}/doc/pdftex
%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdfinitex
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/pdftosrc
%attr(755,root,root) %{_bindir}/pdfvirtex
%{texmf}/dvips/config/pdftex.map
%{texmf}/dvips/config/pdftex_dl14.map
%{texmf}/dvips/config/pdftex_ndl14.map
%dir %{texmf}/pdftex
%dir %{texmf}/pdftex/config
%{texmf}/pdftex/config/cmttf.map
%{texmf}/pdftex/config/pdftex.cfg
%{_mandir}/man1/epstopdf.1*
#%%{_mandir}/man1/pdfinitex.1*
%{_mandir}/man1/pdftex.1*
#%%{_mandir}/man1/pdfvirtex.1*

%files plain
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain
%dir %{texmf}/tex/plain/base
%dir %{texmf}/tex/plain/config
%dir %{texmf}/tex/plain/graphics
%{texmf}/tex/plain/config/tex.ini
%{texmf}/tex/plain/config/bplain.ini
%{texmf}/tex/plain/base/*
%{texmf}/tex/plain/graphics/*
%{texmf}/web2c/plain.mem
%{texmf}/web2c/plain.base

%files plain-dvips
%defattr(644,root,root,755)
%{texmf}/tex/plain/dvips/

%files plain-mathtime
%defattr(644,root,root,755)
#%%{texmf}/tex/plain/mathtime

%files plain-misc
%defattr(644,root,root,755)
%{texmf}/tex/plain/misc/

%files plain-plnfss
%defattr(644,root,root,755)
%{texmf}/tex/plain/plnfss

%files format-plain
%defattr(644,root,root,755)
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/tex.fmt
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/plain.fmt

%files format-pdftex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/plain
%{texmf}/pdftex/plain/config
%{texmf}/pdftex/plain/misc
%{texmf}/web2c/pdftex-pl.pool
%{texmf}/web2c/pdftex.pool
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdftex.fmt

%files format-pdfetex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pdfevirtex
%attr(755,root,root) %{_bindir}/pdfeinitex
%dir %{texmf}/pdfetex
%dir %{texmf}/pdfetex/tex
%{texmf}/pdfetex/tex/config
%{_mandir}/man1/pdfetex.1*
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfetex.efmt
%{texmf}/web2c/pdfetex-pl.pool
%{texmf}/web2c/pdfetex.pool

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
#%attr(755,root,root) %{_bindir}/mex-pl
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/mex.fmt
#%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/mex-pl.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfmex
#%attr(755,root,root) %{_bindir}/pdfmex-pl
%dir %{texmf}/pdftex/mex
%{texmf}/pdftex/mex/config
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfmex.fmt
#%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfmex-pl.fmt

%files format-pdfemex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfemex
#%attr(755,root,root) %{_bindir}/pdfemex-pl
%dir %{texmf}/pdfetex/mex
%{texmf}/pdfetex/mex/config
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfemex.efmt

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

%files format-pdfamstex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfamstex
%{texmf}/pdftex/amstex
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfamstex.fmt

%files csplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex/README-cspsfont
%doc %{texmf}/doc/cstex/cs-fonts.doc
%doc %{texmf}/doc/cstex/cscorr.tab
%doc %{texmf}/doc/cstex/csplain.doc
%doc %{texmf}/doc/cstex/parpozn.tex
%doc %{texmf}/doc/cstex/test8z.tex
%doc %{texmf}/doc/cstex/testlat.tex
%attr(755,root,root) %{_bindir}/csplain
%{texmf}/tex/csplain

%files format-csplain
%defattr(644,root,root,755)
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/csplain.fmt

%files format-pdfcsplain
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcsplain
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/pdfcsplain.fmt

%files cslatex
%defattr(644,root,root,755)
%doc %{texmf}/doc/cstex/INSTALL.cslatex
%doc %{texmf}/doc/cstex/README.cslatex
%{texmf}/tex/cslatex
%{texmf}/tex/latex/cslatex

%files format-cslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cslatex
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/cslatex.fmt

%files format-pdfcslatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfcslatex
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfcslatex.fmt

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
#%%{_mandir}/man1/einitex.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
#%%{_mandir}/man1/evirtex.1*
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
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texfont
%attr(755,root,root) %{_bindir}/texutil
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texutil.1*
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
%{texmf}/pdftex/config/context

%dir %{texmf}/tex/context
%dir %{texmf}/tex/context/config
%{texmf}/tex/context/config/cont-usr.tex
%{texmf}/tex/context/extra
%{texmf}/tex/context/sample
%{texmf}/tex/context/user

%{texmf}/metapost/context
%{texmf}/dvips/config/context.map

# no fmt, so commented out
#%files format-context-cz
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-cz.ini
# does not build with beta 20021025
#%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cont-cz.efmt

%files format-context-de
%defattr(644,root,root,755)
%{texmf}/tex/context/config/cont-de.ini
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cont-de.efmt
#%%{_mandir}/man1/cont-de.1*

%files format-context-en
%defattr(644,root,root,755)
%{texmf}/tex/context/config/cont-en.ini
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cont-en.efmt
#%%{_mandir}/man1/cont-en.1*
# what is the difference betwen uk and en in this particular situation?
%{texmf}/tex/context/config/cont-uk.ini
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cont-uk.efmt

# no fmt, so commented out
#%files format-context-it
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-it.ini

%files format-context-nl
%defattr(644,root,root,755)
%{texmf}/tex/context/config/cont-nl.ini
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/cont-nl.efmt
#%%{_mandir}/man1/cont-nl.1*

# no fmt, so commented out
#%files format-context-ro
#%defattr(644,root,root,755)
#%%{texmf}/tex/context/config/cont-ro.ini

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
%{texmf}/tex/latex/extsizes
%{texmf}/tex/latex/fancy*
%{texmf}/tex/latex/fp
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
#%doc %{texmf}/doc/fonts/lucidabr
%{texmf}/tex/latex/lucidabr
%{texmf}/tex/latex/lucida

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
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/psnfss
%{texmf}/tex/latex/psnfss
%{texmf}/tex/latex/psnfssx

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
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/wasysym
%{texmf}/tex/latex/wasysym

%files format-latex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/latex.fmt

%files format-elatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elatex
#%%{_mandir}/man1/elatex.1*
%{texmf}/etex/latex/config
%{texmf}/etex/latex/misc
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/elatex.efmt

%files format-pdflatex
%defattr(644,root,root,755)
%{texmf}/pdftex/latex/config
%dir %{texmf}/pdftex/latex
%attr(755,root,root) %{_bindir}/pdflatex
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdflatex.fmt
#%%{_mandir}/man1/pdflatex.1*

%files format-pdfelatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdfelatex
%dir %{texmf}/pdfetex/latex
%{texmf}/pdfetex/latex/config
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfelatex.efmt

%files platex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/platex
%dir %{texmf}/tex/platex
%{texmf}/tex/platex/config
%{texmf}/tex/latex/platex

%files format-platex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/platex
#%attr(755,root,root) %{_bindir}/platex-pl
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/platex.fmt
#%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/platex-pl.fmt

%files format-pdfplatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/platex
%{texmf}/pdftex/platex/config
%attr(755,root,root) %{_bindir}/pdfplatex
%config(noreplace) %verify(not md5 size mtime) %{texmf}/web2c/pdfplatex.fmt

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

%files fonts-eurosym
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/eurosym
%{texmf}/fonts/tfm/public/eurosym

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
#%%{texmf}/fonts/tfm/jknappen

%files fonts-latex
%defattr(644,root,root,755)
%{texmf}/fonts/source/public/latex
%{texmf}/fonts/tfm/public/latex

%files fonts-lh
%defattr(644,root,root,755)
%{texmf}/fonts/source/lh
%{texmf}/fonts/tfm/lh

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
#%%{texmf}/fonts/type1/adobe

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

%files fonts-type1-eurosym
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/eurosym

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
