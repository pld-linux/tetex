# TODO:
# error: libkpathsea.so is required by already marked tetex-dvips-1.0.7.beta_20020208-0.1
# what with texinfo ?
# error: tetex-format-context-1.0.7.beta_20020402-0.1: req perl(path_tre) not found
# _noautoreqdep perl(path_tre) ?


%define		_ver	beta-20020402
%define		texmf_ver	beta-20020207

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
Patch19:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX-beta/teTeX-src-beta-20020402-expdvips.patch.gz
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

#define 	_noautoreqdep perl(path_tre)

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

%package format-latex
Summary:	format-latex
Group:		Applications/Publishing/TeX
Requires:	%{name}-latex = %{version}
PreReq:		%{_bindir}/texhash

%description format-latex

%package latex
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(es):	Paquete de macros LaTeX
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makro-pakiet LaTeX
Summary(pt_BR):	Pacote de macros LaTeX
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-latex = %{version}
Requires:	tetex-tex-hyphen = %{version}
PreReq:		%{_bindir}/texhash

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

%description latex -l de
LaTeX ist ein TeX-Makropaket. Die LaTeX-Makros regen den Autor an,
über den Inhalt - und nicht die Form - ihrer Dokumente nachzudenken.
Ideal, wenn auch schwer zu realisieren, wäre ein Dokument, das
keinerlei Formatierungsbefehle (von der Art 'Kursiv ein/aus' oder
'Zeilenabstand um 2 Pica vergrößern') enthielte. Stattdessen würde all
dies durch spezifische 'redaktionelle' Instruktionen ersetzt
('auszeichnen', 'neues Kapitel starten').

%description latex -l es
LaTeX es un paquete de macros TeX. Las macros LaTeX impulsionan
escritores a pensar sobre el contenido de sus documentos, y no en su
forma. Lo ideal, muy difícil de realizar, es no tener ningún comando
de fomatear (como ''switch to italic'' 0 ''skip 2 points'') en el
documento; en lugar de esto, todo se hace especificando instrucciones
de marcado: : ''emphasize'', ''start la section''.

%description latex -l fr
LaTeX est un paquetage de macros TeX. Les macros LaTeX permettent aux
auteurs de se concentrer sur le contenu des leurs documents, plutôt
que sur la forme. L'idéal, très difficile à réaliser, est de n'avoir
aucune commande de formatage (comme « mettre en italique », ou «
sauter 2 picas ») dans le document ; au lieu de cela, tout est fait
par des balises : « début de section », « gras ».

%description latex -l pl
LaTeX jest zestawem makr TeXowych. Makra LaTeXa u³atwiaj± pisz±cym
my¶lenie o zawarto¶ci dokumentu, zamiast o jego wygl±dzie. Idealny,
bardzo trudny do implementacji system nie powinien posiadaæ komend
formatuj±cych (takich jak ,,pisz kursyw±'', czy prze³±cz na font 8
punktowy) a jedynie polecenia znakuj±ce takie jak np. podkre¶l, czy
zacznij sekcjê. LaTeX powoli zbli¿a siê do tego idea³u, nie odrzucaj±c
mo¿liwo¶ci ingerencji w wygl±d dokumentu.

%description latex -l pt_BR
LaTeX é um pacote de macros TeX. Os macros LaTeX encorajam escritores
a pensar sobre o conteúdo de seus documentos, e não na forma. O ideal,
muito difícil de realizar, é não ter nenhum comando de formatação
(como ``switch to italic'' ou ``skip 2 picas'') no documento; no lugar
disto, tudo é feito especificando instruções de marcação:
``emphasize'', ``start a section''.

%description latex -l tr
LaTeX bir TeX makro paketidir. LaTeX makrolarý, yazarlarý belgelerinin
biçimlerinden çok içerikleri üzerinde yoðunlaþmlarýna özendirir.
Ýdealde, gerçekleþtirilmesi çok zor olsa da, hiç biçimlendirme
komutuna yer vermeksizin (``2 birim aralýk býrak'' gibi), yalnýzca
özel iþaretleme yönergeleri ile (``yeni bir kesime geç'' gibi) bunu
baþarmaya çalýþýr.

%package dvips
Summary:	dvi to postscript convertor
Summary(de):	dvi-Postscript-Konvertierungsprogramm
Summary(es):	Convertidor dvi para postscript
Summary(fr):	Convertisseur dvi vers PostScript
Summary(pl):	Konwerter dvi do postscriptu
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
Summary:	dvi to laserjet convertor
Summary(de):	Ein dvi-->Laserjet-Konvertierer
Summary(es):	Convertidor dvi para laserjet
Summary(fr):	convertisseur dvi vers laserjet.
Summary(pl):	Konwerter dvi do laserjet
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

%package format-amstex
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makra dla LaTeX
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
Obsoletes:	tetex-ams
PreReq:		%{_bindir}/texhash

%description format-amstex
American Mathematics Society macros for plainTeX.

%description format-amstex -l pl
Makra American Mathematics Society do sk³adania publikacji
matematycznych.

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

%package pdftex
Summary:	PDFtex
Summary(pl):	PDFtex
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}

%description pdftex
TeX generating PDFs instead DVI.

%package format-pdftex
Summary:	PDFTeX format
Summary(pl):	Format PDFTeX
Group:		Applications/Publishing/TeX
Requires:	%{name}-pdftex = %{version}

%description format-pdftex
PDFTeX format.

%description format-pdftex -l pl
Format PDFTeX.

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

%package -n kpathsea
Summary:	-n kpathsea
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description -n kpathsea
kpathsea

%package bibtex-ams
Summary:	bibtex-ams
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description bibtex-ams
bibtex-ams

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

%package fonts-jknappen
Summary:	fonts-jknappen
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash

%description fonts-jknappen
fonts-jknappen

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

%package format-pdfetex
Summary:	pdfetex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdfetex
pdfetex

%package format-pdfelatex
Summary:	format-pdfelatex
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdfelatex
pdfelatex

%package format-pdfemex
Summary:	pdfemex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdfemex
pdfemex

%package format-pdfamstex
Summary:	pdftex-amstex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdfamstex
pdftex-amstex

%package format-pdftex-context
Summary:	pdftex-context
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdftex-context
pdftex-context

%package format-pdflatex
Summary:	pdflatex
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-latex = %{version}
Requires:	%{name}-pdftex = %{version}

%description format-pdflatex
pdflatex

%package format-pdfmex
Summary:	pdfmex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name}-pdftex = %{version}

%description format-pdfmex
pdfmex

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

%package csplain
Summary:	csplain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description csplain
csplain

%package cyrplain
Summary:	cyrplain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description cyrplain
cyrplain

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

%package plain-misc
Summary:	plain-misc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-misc
plain-misc

%package plain-plnfss
Summary:	plain-plnfss
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-plnfss
plain-plnfss

%package plain-mathtime
Summary:	plain-mathtime
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-mathtime
plain-mathtime

%package plain-dvips
Summary:	plain-dvips
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-dvips
plain-dvips

%package plain
Summary:	plain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain
plain

%package plain-amsfonts
Summary:	plain-amsfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description plain-amsfonts
plain-amsfonts

%package mex
Summary:	mex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	tetex-fonts-pl = %{version}

%description mex
mex

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

%package latex-units
Summary:	latex-units
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-units
latex-units

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

%package latex-psnfss
Summary:	latex-psnfss
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-psnfss
latex-psnfss

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

%package latex-misc
Summary:	latex-misc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-misc
latex-misc

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

%package latex-lucidabr
Summary:	latex-lucidabr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-lucidabr
latex-lucidabr

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

%package latex-jknappen
Summary:	latex-jknappen
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-fonts-jknappen = %{version}

%description latex-jknappen
latex-jknappen

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

%package latex-dstroke
Summary:	latex-dstroke
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-dstroke
latex-dstroke

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

%package latex-cyrillic
Summary:	latex-cyrillic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-cyrillic
latex-cyrillic

%package latex-custom-bib
Summary:	latex-custom-bib
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-custom-bib
latex-custom-bib

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

%package pdfcsplain
Summary:	pdfcsplain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfcsplain
pdfcsplain

%package odvips
Summary:	pdfcsplain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}
Requires:	%{name}-format-omega = %{version}

%description odvips
odvips

%package latex-context
Summary:	latex-context
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-context
latex-context

%package latex-concmath
Summary:	latex-concmath
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-concmath
latex-concmath

%package latex-cite
Summary:	latex-cite
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-cite
latex-cite

%package latex-ccfonts
Summary:	latex-ccfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-ccfonts
latex-ccfonts

%package latex-carlisle
Summary:	latex-carlisle
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-carlisle
latex-carlisle

%package latex-caption
Summary:	latex-caption
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-caption
latex-caption

%package latex-bbm
Summary:	latex-bbm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-bbm
latex-bbm

%package latex-antt
Summary:	latex-antt
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-antt
latex-antt

%package latex-antp
Summary:	latex-antp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-antp
latex-antp

%package latex-amsmath
Summary:	latex-amsmath
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-amsmath
latex-amsmath

%package latex-amsfonts
Summary:	latex-amsfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-amsfonts
latex-amsfonts

%package latex-amscls
Summary:	latex-amscls
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-amscls
latex-amscls

%package latex-algorith
Summary:	latex-algorith
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-algorith
latex-algorith

%package latex-ae
Summary:	latex-ae
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description latex-ae
latex-ae

%package eplain
Summary:	eplain
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description eplain
eplain

%package format-elatex
Summary:	elatex
Group:		Applications/Publishing/TeX
Provides:	%{name}-latex
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description format-elatex
elatex

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
%patch0 -p1
%patch1 -p1

install -d texmf
tar xzf %{SOURCE1} -C texmf
#tar xzf %{SOURCE2} -C texmf

%patch2  -p1
%patch4  -p1
%patch5  -p1
%patch6  -p1
%patch7  -p1
%patch9  -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1
%patch15 -p1
#%patch16 -p1 -b .wiget
#%patch17 -p1
%patch18 -p1
%patch19 -p1

%build
#sh ./reautoconf
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CFLAGS="%{rpmcflags} `pkg-config libpng12 --cflags`"
	CXXFLAGS="`pkg-config libpng12 --cflags` $CXXFLAGS"
fi
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
#jakie formaty trzzeba przegenerowaæ ?
%fmtutil -f tex

#%fmtutil -f bplain

%texhash

%postun
/sbin/ldconfig
%fixinfodir
%texhash

%post babel 
%texhash

%postun babel 
%texhash


%post bibtex 
%texhash

%postun bibtex 
%texhash


%post bibtex-ams 
%texhash

%postun bibtex-ams 
%texhash


%post bibtex-germbib 
%texhash

%postun bibtex-germbib 
%texhash


%post bibtex-koma-script 
%texhash

%postun bibtex-koma-script 
%texhash


%post bibtex-natbib 
%texhash

%postun bibtex-natbib 
%texhash


%post bibtex-plbib 
%texhash

%postun bibtex-plbib 
%texhash


%post bibtex-revtex4 
%texhash

%postun bibtex-revtex4 
%texhash


%post cslatex 
%texhash

%postun cslatex 
%texhash


%post csplain 
%texhash

%postun csplain 
%texhash


%post cyramstex 
%texhash

%postun cyramstex 
%texhash


%post cyrplain 
%texhash

%postun cyrplain 
%texhash


%post cyrtexinfo 
%texhash

%postun cyrtexinfo 
%texhash


%post doc 
%texhash

%postun doc 
%texhash


%post doc-Catalogue 
%texhash

%postun doc-Catalogue 
%texhash


%post doc-de-tex-faq 
%texhash

%postun doc-de-tex-faq 
%texhash


%post doc-latex2e-html 
%texhash

%postun doc-latex2e-html 
%texhash


%post doc-LaTeX-FAQ-francaise 
%texhash

%postun doc-LaTeX-FAQ-francaise 
%texhash


%post doc-uktug-faq 
%texhash

%postun doc-uktug-faq 
%texhash


%post dvilj 
%texhash

%postun dvilj 
%texhash


%post dvips 
%fixinfodir
%texhash

%postun dvips 
%fixinfodir
%texhash


%post eplain 
%texhash

%postun eplain 
%texhash


%post etex 
%texhash

%postun etex 
%texhash


%post fontinst 
%texhash

%postun fontinst 
%texhash


%post fontname 
%texhash

%postun fontname 
%texhash


%post fonts 
%texhash

%postun fonts 
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


%post fonts-cm-bold 
%texhash

%postun fonts-cm-bold 
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


%post fonts-omega 
%texhash

%postun fonts-omega 
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


%post fonts-qfonts 
%texhash

%postun fonts-qfonts 
%texhash


%post fonts-rsfs 
%texhash

%postun fonts-rsfs 
%texhash


%post fonts-stmaryrd 
%texhash

%postun fonts-stmaryrd 
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


%post fonts-type1-omega 
%texhash

%postun fonts-type1-omega 
%texhash


%post fonts-type1-pl 
%texhash

%postun fonts-type1-pl 
%texhash


%post fonts-type1-qfonts 
%texhash

%postun fonts-type1-qfonts 
%texhash


%post fonts-type1-urw 
%texhash

%postun fonts-type1-urw 
%texhash


%post fonts-type1-xypic 
%texhash

%postun fonts-type1-xypic 
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


%post format-amstex 
%texhash

%postun format-amstex 
%texhash


%post format-context 
%texhash

%postun format-context 
%texhash


%post format-elatex 
%texhash

%postun format-elatex 
%texhash


%post format-latex
%fixinfodir
%fmtutil -f latex

%texhash

%postun format-latex 
%fixinfodir
%texhash


%post format-omega 
%fmtutil -f omega

%texhash

%postun format-omega 
%texhash


%post format-omega-lambda
%fmtutil -f lambda

%texhash

%postun format-omega-lambda 
%texhash


%post format-pdfamstex 
%texhash

%postun format-pdfamstex 
%texhash


%post format-pdfelatex 
%texhash

%postun format-pdfelatex 
%texhash


%post format-pdfemex 
%texhash

%postun format-pdfemex 
%texhash


%post format-pdfetex 
%texhash

%postun format-pdfetex 
%texhash


%post format-pdflatex 
%texhash

%postun format-pdflatex 
%texhash


%post format-pdfmex 
%texhash

%postun format-pdfmex 
%texhash


%post format-pdfplatex 
%texhash

%postun format-pdfplatex 
%texhash


%post format-pdftex 
%texhash

%postun format-pdftex 
%texhash


%post format-pdftex-context 
%texhash

%postun format-pdftex-context 
%texhash


%post format-platex 
%texhash

%postun format-platex 
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


%post latex-algorith 
%texhash

%postun latex-algorith 
%texhash


%post latex-amscls 
%texhash

%postun latex-amscls 
%texhash


%post latex-amsfonts 
%texhash

%postun latex-amsfonts 
%texhash


%post latex-amsmath 
%texhash

%postun latex-amsmath 
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


%post latex-caption 
%texhash

%postun latex-caption 
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


%post latex-concmath 
%texhash

%postun latex-concmath 
%texhash


%post latex-context 
%texhash

%postun latex-context 
%texhash


%post latex-curves 
%texhash

%postun latex-curves 
%texhash


%post latex-custom-bib 
%texhash

%postun latex-custom-bib 
%texhash


%post latex-cyrillic 
%texhash

%postun latex-cyrillic 
%texhash


%post latex-dinbrief 
%texhash

%postun latex-dinbrief 
%texhash


%post latex-draftcopy 
%texhash

%postun latex-draftcopy 
%texhash


%post latex-dstroke 
%texhash

%postun latex-dstroke 
%texhash


%post latex-dvilj 
%texhash

%postun latex-dvilj 
%texhash


%post latex-eepic 
%texhash

%postun latex-eepic 
%texhash


%post latex-endfloat 
%texhash

%postun latex-endfloat 
%texhash


%post latex-fancyhdr 
%texhash

%postun latex-fancyhdr 
%texhash


%post latex-fancyheadings 
%texhash

%postun latex-fancyheadings 
%texhash


%post latex-fancyvrb 
%texhash

%postun latex-fancyvrb 
%texhash


%post latex-fp 
%texhash

%postun latex-fp 
%texhash


%post latex-g-brief 
%texhash

%postun latex-g-brief 
%texhash


%post latex-graphics 
%texhash

%postun latex-graphics 
%texhash


%post latex-hyperref 
%texhash

%postun latex-hyperref 
%texhash


%post latex-jknappen 
%texhash

%postun latex-jknappen 
%texhash


%post latex-koma-script 
%texhash

%postun latex-koma-script 
%texhash


%post latex-labels 
%texhash

%postun latex-labels 
%texhash


%post latex-listings 
%texhash

%postun latex-listings 
%texhash


%post latex-lucidabr 
%texhash

%postun latex-lucidabr 
%texhash


%post latex-mathpple 
%texhash

%postun latex-mathpple 
%texhash


%post latex-mathptm 
%texhash

%postun latex-mathptm 
%texhash


%post latex-mathptmx 
%texhash

%postun latex-mathptmx 
%texhash


%post latex-mathtime 
%texhash

%postun latex-mathtime 
%texhash


%post latex-mdwtools 
%texhash

%postun latex-mdwtools 
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


%post latex-misc 
%texhash

%postun latex-misc 
%texhash


%post latex-mltex 
%texhash

%postun latex-mltex 
%texhash


%post latex-ms 
%texhash

%postun latex-ms 
%texhash


%post latex-multirow 
%texhash

%postun latex-multirow 
%texhash


%post latex-mwcls 
%texhash

%postun latex-mwcls 
%texhash


%post latex-natbib 
%texhash

%postun latex-natbib 
%texhash


%post latex-ntgclass 
%texhash

%postun latex-ntgclass 
%texhash


%post latex-oberdiek 
%texhash

%postun latex-oberdiek 
%texhash


%post latex-palatcm 
%texhash

%postun latex-palatcm 
%texhash


%post latex-pb-diagram 
%texhash

%postun latex-pb-diagram 
%texhash


%post latex-psnfss 
%texhash

%postun latex-psnfss 
%texhash


%post latex-qfonts 
%texhash

%postun latex-qfonts 
%texhash


%post latex-revtex4 
%texhash

%postun latex-revtex4 
%texhash


%post latex-seminar 
%texhash

%postun latex-seminar 
%texhash


%post latex-SIunits 
%texhash

%postun latex-SIunits 
%texhash


%post latex-t2 
%texhash

%postun latex-t2 
%texhash


%post latex-titlesec 
%texhash

%postun latex-titlesec 
%texhash


%post latex-tools 
%texhash

%postun latex-tools 
%texhash


%post latex-umlaute 
%texhash

%postun latex-umlaute 
%texhash


%post latex-units 
%texhash

%postun latex-units 
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


%post makeindex 
%texhash

%postun makeindex 
%texhash


%post matapost 
%texhash

%postun matapost 
%texhash


%post metafont 
%texhash

%postun metafont 
%texhash


%post mex 
%texhash

%postun mex 
%texhash


%post -n kpathsea
%texhash

%postun -n kpathsea
%texhash


%post -n kpathsea-devel
%texhash

%postun -n kpathsea-devel
%texhash


%post -n xdvi
%texhash

%postun -n xdvi
%texhash


%post odvips 
%texhash

%postun odvips 
%texhash


%post omega-ocp 
%texhash

%postun omega-ocp 
%texhash


%post omega-otp 
%texhash

%postun omega-otp 
%texhash


%post oxdvi 
%texhash

%postun oxdvi 
%texhash


%post pdfcslatex 
%texhash

%postun pdfcslatex 
%texhash


%post pdfcsplain 
%texhash

%postun pdfcsplain 
%texhash


%post pdftex 
%texhash

%postun pdftex 
%texhash


%post plain 
%texhash

%postun plain 
%texhash


%post plain-amsfonts 
%texhash

%postun plain-amsfonts 
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


%post platex 
%texhash

%postun platex 
%texhash


%post rubibtex 
%texhash

%postun rubibtex 
%texhash


%post rumakeindex 
%texhash

%postun rumakeindex 
%texhash


%post tex 
%texhash

%postun tex 
%texhash


%post texconfig 
%texhash

%postun texconfig 
%texhash


%post texdoctk 
%texhash

%postun texdoctk 
%texhash


%post tex-eijkhout 
%texhash

%postun tex-eijkhout 
%texhash


%post tex-german 
%texhash

%postun tex-german 
%texhash


%post tex-hyphen 
%texhash

%postun tex-hyphen 
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


%post tex-pstriks 
%texhash

%postun tex-pstriks 
%texhash


%post tex-ruhyphen 
%texhash

%postun tex-ruhyphen 
%texhash


%post tex-spanishb 
%texhash

%postun tex-spanishb 
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


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# czy to jest ci±gle potrzebne ?
%dir /etc/sysconfig/tetex-updmap
%verify(not size md5 mtime) %config(noreplace) /etc/sysconfig/tetex-updmap/maps.lst
/etc/cron.daily/tetex
#do czego jest bplain ?
%attr(755,root,root) %{_bindir}/bplain
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
%attr(755,root,root) %{_bindir}/metafun
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
%dir %{_datadir}/texmf/fonts/ofm
%dir %{_datadir}/texmf/fonts/ofm/public
%dir %{_datadir}/texmf/fonts/ovf
%dir %{_datadir}/texmf/fonts/ovf/public
%dir %{_datadir}/texmf/fonts/ovp
%dir %{_datadir}/texmf/fonts/ovp/public
%dir %{_datadir}/texmf/fonts/pfm
%dir %{_datadir}/texmf/fonts/pfm/public
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
%dir %{_datadir}/texmf/source
%{_datadir}/texmf/web2c/metafun.mem
%attr(1777,root,root) /var/cache/fonts

#%files plain
#%defattr(644,root,root,755)
%dir %{texmf}/tex/plain/config
# bplain tu czy mo¿e gdzie¶ indziej?
%{texmf}/tex/plain/config/bplain.ini
%{texmf}/tex/plain/config/tex.ini
%dir %{texmf}/tex/plain/base
%{texmf}/tex/plain/base/gkpmac.tex
%{texmf}/tex/plain/base/letter.tex
%{texmf}/tex/plain/base/logmac.tex
%{texmf}/tex/plain/base/manmac.tex
%{texmf}/tex/plain/base/mftmac.tex
%{texmf}/tex/plain/base/mptmac.tex
%{texmf}/tex/plain/base/picmac.tex
%{texmf}/tex/plain/base/plain.tex
%{texmf}/tex/plain/base/story.tex
%{texmf}/tex/plain/base/testfont.tex
%{texmf}/tex/plain/base/webmac.tex
%dir %{_datadir}/texmf/web2c
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/tex.fmt
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/web2c/plain.fmt
%{_datadir}/texmf/web2c/plain.mem
%{_datadir}/texmf/web2c/plain.base
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


%files -n kpathsea-devel
%defattr(644,root,root,755)
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so
%{_infodir}/kpathsea.info*

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
%{_libdir}/libkpathsea.so.3.3.7

%files dvips
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/dvips.dvi
%attr(755,root,root) %{_bindir}/dvips
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%attr(755,root,root) %{_bindir}/dvicopy
# dvi2fax wymaga gs-a
%attr(755,root,root) %{_bindir}/dvi2fax
%{_infodir}/dvips.info*
%lang(fi) %{_mandir}/fi/man1/dvips.1*
%{_mandir}/man1/dvips.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/dvitype.1*
%dir %{texmf}/dvips
# rozpisaæ
%dir %{_datadir}/texmf/dvips/antp
%{_datadir}/texmf/dvips/antp/antp.enc
%dir %{_datadir}/texmf/dvips/antt
%{_datadir}/texmf/dvips/antt/antt.enc
%dir %{_datadir}/texmf/dvips/base
%{_datadir}/texmf/dvips/base/8a.enc
%{_datadir}/texmf/dvips/base/8r.enc
%{_datadir}/texmf/dvips/base/ad.enc
%{_datadir}/texmf/dvips/base/asex.enc
%{_datadir}/texmf/dvips/base/asexp.enc
%{_datadir}/texmf/dvips/base/color.pro
%{_datadir}/texmf/dvips/base/cork.enc
%{_datadir}/texmf/dvips/base/crop.pro
%{_datadir}/texmf/dvips/base/dc.enc
%{_datadir}/texmf/dvips/base/dvips.enc
%{_datadir}/texmf/dvips/base/EC.enc
%{_datadir}/texmf/dvips/base/extex.enc
%{_datadir}/texmf/dvips/base/finclude.pro
%{_datadir}/texmf/dvips/base/funky.enc
%{_datadir}/texmf/dvips/base/hps.pro
%{_datadir}/texmf/dvips/base/mh2scr.enc
%{_datadir}/texmf/dvips/base/mtex.enc
%{_datadir}/texmf/dvips/base/psfonts.map
%{_datadir}/texmf/dvips/base/special.pro
%{_datadir}/texmf/dvips/base/tex256.enc
%{_datadir}/texmf/dvips/base/texc.pro
%{_datadir}/texmf/dvips/base/texmext.enc
%{_datadir}/texmf/dvips/base/texmital.enc
%{_datadir}/texmf/dvips/base/texmsym.enc
%{_datadir}/texmf/dvips/base/texnansi.enc
%{_datadir}/texmf/dvips/base/texnansx.enc
%{_datadir}/texmf/dvips/base/tex.pro
%{_datadir}/texmf/dvips/base/texps.pro
%{_datadir}/texmf/dvips/base/xl2.enc
%{_datadir}/texmf/dvips/base/xt2.enc
%dir %{_datadir}/texmf/dvips/bluesky
%{_datadir}/texmf/dvips/bluesky/psfonts.ams
%{_datadir}/texmf/dvips/bluesky/psfonts.amz
%{_datadir}/texmf/dvips/bluesky/psfonts.cm
%{_datadir}/texmf/dvips/bluesky/psfonts.cmz
%dir %{_datadir}/texmf/dvips/config
%{_datadir}/texmf/dvips/config/antp.cfg
%{_datadir}/texmf/dvips/config/antp.map
%{_datadir}/texmf/dvips/config/antt.cfg
%{_datadir}/texmf/dvips/config/antt.map
%{_datadir}/texmf/dvips/config/ar-ext-adobe-bi.map
%{_datadir}/texmf/dvips/config/ar-ext-adobe-kb.map
%{_datadir}/texmf/dvips/config/ar-ext-urw-kb.map
%{_datadir}/texmf/dvips/config/ar-ext-urw-urw.map
%{_datadir}/texmf/dvips/config/ar-std-adobe-bi.map
%{_datadir}/texmf/dvips/config/ar-std-adobe-kb.map
%{_datadir}/texmf/dvips/config/ar-std-urw-kb.map
%{_datadir}/texmf/dvips/config/ar-std-urw-urw.map
%{_datadir}/texmf/dvips/config/bakoma-extra.map
%{_datadir}/texmf/dvips/config/bsr-interpolated.map
%{_datadir}/texmf/dvips/config/bsr.map
%{_datadir}/texmf/dvips/config/charter.map
%{_datadir}/texmf/dvips/config/cmcyr.map
%{_datadir}/texmf/dvips/config/config.ams
%{_datadir}/texmf/dvips/config/config.amz
%{_datadir}/texmf/dvips/config/config.antp
%{_datadir}/texmf/dvips/config/config.antt
%{_datadir}/texmf/dvips/config/config.cm
%{_datadir}/texmf/dvips/config/config.cmz
%{_datadir}/texmf/dvips/config/config.dfaxhigh
%{_datadir}/texmf/dvips/config/config.dfaxlo
%{_datadir}/texmf/dvips/config/config.generic
%{_datadir}/texmf/dvips/config/config.mirr
%{_datadir}/texmf/dvips/config/config.pdf
%{_datadir}/texmf/dvips/config/config.pl
%config(noreplace) %verify(not size md5 mtime) %{_datadir}/texmf/dvips/config/config.ps
%{_datadir}/texmf/dvips/config/config.qbk
%{_datadir}/texmf/dvips/config/config.qcr
%{_datadir}/texmf/dvips/config/config.qf
%{_datadir}/texmf/dvips/config/config.qhv
%{_datadir}/texmf/dvips/config/config.qpl
%{_datadir}/texmf/dvips/config/config.qtm
%{_datadir}/texmf/dvips/config/config.qzc
%{_datadir}/texmf/dvips/config/config.www
%{_datadir}/texmf/dvips/config/context.map
%{_datadir}/texmf/dvips/config/cs.map
%{_datadir}/texmf/dvips/config/hoekwater.map
%{_datadir}/texmf/dvips/config/lucidabr.map
%{_datadir}/texmf/dvips/config/lw35extra-adobe-bi.map
%{_datadir}/texmf/dvips/config/lw35extra-adobe-kb.map
%{_datadir}/texmf/dvips/config/lw35extra-urw-kb.map
%{_datadir}/texmf/dvips/config/lw35extra-urw-urw.map
%{_datadir}/texmf/dvips/config/marvosym.map
%{_datadir}/texmf/dvips/config/mathpi.map
%{_datadir}/texmf/dvips/config/mathpple-ext.map
%{_datadir}/texmf/dvips/config/mt-belleek.map
%{_datadir}/texmf/dvips/config/mt-plus.map
%{_datadir}/texmf/dvips/config/mtsupp-ext-adobe-bi.map
%{_datadir}/texmf/dvips/config/mtsupp-ext-adobe-kb.map
%{_datadir}/texmf/dvips/config/mtsupp-ext-urw-kb.map
%{_datadir}/texmf/dvips/config/mtsupp-ext-urw-urw.map
%{_datadir}/texmf/dvips/config/mtsupp-std-adobe-bi.map
%{_datadir}/texmf/dvips/config/mtsupp-std-adobe-kb.map
%{_datadir}/texmf/dvips/config/mtsupp-std-urw-kb.map
%{_datadir}/texmf/dvips/config/mtsupp-std-urw-urw.map
%{_datadir}/texmf/dvips/config/mt-yy.map
%{_datadir}/texmf/dvips/config/omega.map
%{_datadir}/texmf/dvips/config/pazo.map
%{_datadir}/texmf/dvips/config/pdftex.map
%{_datadir}/texmf/dvips/config/pl.cfg
%{_datadir}/texmf/dvips/config/pl.map
%{_datadir}/texmf/dvips/config/ps2pk.map
%{_datadir}/texmf/dvips/config/psfonts.map
%{_datadir}/texmf/dvips/config/psnfss.map
%{_datadir}/texmf/dvips/config/qbk.map
%{_datadir}/texmf/dvips/config/qcr.map
%{_datadir}/texmf/dvips/config/qhv.map
%{_datadir}/texmf/dvips/config/qpl.map
%{_datadir}/texmf/dvips/config/qtm.map
%{_datadir}/texmf/dvips/config/qzc.map
%{_datadir}/texmf/dvips/config/raw-ar-ext-adobe-bi.map
%{_datadir}/texmf/dvips/config/raw-ar-ext-adobe-kb.map
%{_datadir}/texmf/dvips/config/raw-ar-ext-urw-kb.map
%{_datadir}/texmf/dvips/config/raw-ar-ext-urw-urw.map
%{_datadir}/texmf/dvips/config/raw-ar-std-adobe-bi.map
%{_datadir}/texmf/dvips/config/raw-ar-std-adobe-kb.map
%{_datadir}/texmf/dvips/config/raw-ar-std-urw-kb.map
%{_datadir}/texmf/dvips/config/raw-ar-std-urw-urw.map
%{_datadir}/texmf/dvips/config/raw-lw35extra-adobe-bi.map
%{_datadir}/texmf/dvips/config/raw-lw35extra-adobe-kb.map
%{_datadir}/texmf/dvips/config/raw-lw35extra-urw-kb.map
%{_datadir}/texmf/dvips/config/raw-lw35extra-urw-urw.map
%{_datadir}/texmf/dvips/config/updmap
%{_datadir}/texmf/dvips/config/utopia.map
%{_datadir}/texmf/dvips/config/xypic.map
%dir %{_datadir}/texmf/dvips/gsftopk
%{_datadir}/texmf/dvips/gsftopk/render.ps
%dir %{_datadir}/texmf/dvips/misc
%{_datadir}/texmf/dvips/misc/alt-rule.pro
%{_datadir}/texmf/dvips/misc/mirr.hd
%{_datadir}/texmf/dvips/misc/pspicture.ps
%{_datadir}/texmf/dvips/misc/resolution400.ps
%dir %{_datadir}/texmf/dvips/pl
%{_datadir}/texmf/dvips/pl/plin.enc
%{_datadir}/texmf/dvips/pl/plit.enc
%{_datadir}/texmf/dvips/pl/plitt.enc
%{_datadir}/texmf/dvips/pl/plme.enc
%{_datadir}/texmf/dvips/pl/plmi.enc
%{_datadir}/texmf/dvips/pl/plms.enc
%{_datadir}/texmf/dvips/pl/plrm.enc
%{_datadir}/texmf/dvips/pl/plsc.enc
%{_datadir}/texmf/dvips/pl/plte.enc
%{_datadir}/texmf/dvips/pl/pltt.enc
%dir %{_datadir}/texmf/dvips/psfrag
%{_datadir}/texmf/dvips/psfrag/psfrag.pro
%dir %{_datadir}/texmf/dvips/pstricks
%{_datadir}/texmf/dvips/pstricks/pst-blur.pro
%{_datadir}/texmf/dvips/pstricks/pst-coil.pro
%{_datadir}/texmf/dvips/pstricks/pst-dots.pro
%{_datadir}/texmf/dvips/pstricks/pst-ghsb.pro
%{_datadir}/texmf/dvips/pstricks/pst-grad.pro
%{_datadir}/texmf/dvips/pstricks/pst-node.pro
%{_datadir}/texmf/dvips/pstricks/pstricks.pro
%{_datadir}/texmf/dvips/pstricks/pst-slpe.pro
%{_datadir}/texmf/dvips/pstricks/pst-text.pro
%dir %{_datadir}/texmf/dvips/qfonts
%{_datadir}/texmf/dvips/qfonts/config.qbk
%{_datadir}/texmf/dvips/qfonts/config.qcr
%{_datadir}/texmf/dvips/qfonts/config.qhv
%{_datadir}/texmf/dvips/qfonts/config.qpl
%{_datadir}/texmf/dvips/qfonts/config.qtm
%{_datadir}/texmf/dvips/qfonts/config.qzc
%{_datadir}/texmf/dvips/qfonts/qbk.enc
%{_datadir}/texmf/dvips/qfonts/qbk.map
%{_datadir}/texmf/dvips/qfonts/qcr.enc
%{_datadir}/texmf/dvips/qfonts/qcr.map
%{_datadir}/texmf/dvips/qfonts/qhv.enc
%{_datadir}/texmf/dvips/qfonts/qhv.map
%{_datadir}/texmf/dvips/qfonts/qpl.enc
%{_datadir}/texmf/dvips/qfonts/qpl.map
%{_datadir}/texmf/dvips/qfonts/qtm.enc
%{_datadir}/texmf/dvips/qfonts/qtm.map
%{_datadir}/texmf/dvips/qfonts/qzc.enc
%{_datadir}/texmf/dvips/qfonts/qzc.map
%dir %{_datadir}/texmf/dvips/xypic
%{_datadir}/texmf/dvips/xypic/xy36dict.pro
%{_datadir}/texmf/dvips/xypic/xy37dict.pro

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
%{_mandir}/man1/xdvi.1*
%attr(755,root,root) %{_bindir}/xdvi
%attr(755,root,root) %{_bindir}/xdvi.bin
%{_prefix}/X11R6/share/applnk/Graphics/Viewers/xdvi.desktop
%dir %{texmf}/xdvi
%{texmf}/xdvi/ps2pk.map
%{texmf}/xdvi/XDvi
%{texmf}/xdvi/xdvi.cfg

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

%files bibtex-plbib
%defattr(644,root,root,755)
%{texmf}/bibtex/bib/plbib
%{texmf}/bibtex/bst/plbib

%files bibtex-germbib
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/germbib

%files bibtex-koma-script
%defattr(644,root,root,755)
%{texmf}/bibtex/bst/koma-script

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

%files fonts-omega
%defattr(644,root,root,755)
%{texmf}/fonts/afm/public/omega
%{texmf}/fonts/ofm/public/omega
%{texmf}/fonts/ovf/public/omega
%{texmf}/fonts/ovp/public/omega
%{texmf}/fonts/tfm/public/omega

%files fonts-qfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/fonts/polish/qfonts
%{texmf}/fonts/afm/public/qfonts
%{texmf}/fonts/tfm/public/qfonts

%files fonts-xypic
%defattr(644,root,root,755)
%{texmf}/fonts/afm/public/xypic
%{texmf}/fonts/pfm/public/xypic
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
%{texmf}/fonts/source/ams
%{texmf}/fonts/tfm/ams
%doc %{texmf}/doc/fonts/amsfonts

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

%files fonts-mathpple
%defattr(644,root,root,755)
%{texmf}/fonts/tfm/public/mathpple
%{texmf}/fonts/vf/public/mathpple

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
%{texmf}/fonts/type1/bluesky

%files fonts-type1-hoekwater
%defattr(644,root,root,755)
# hmm, mo¿e jeszcze rozpisaæ?
%{texmf}/fonts/type1/hoekwater

%files fonts-type1-antp
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/antp

%files fonts-type1-antt
%defattr(644,root,root,755)
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

%files fonts-type1-omega
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/omega

%files fonts-type1-pl
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/pl

%files fonts-type1-qfonts
%defattr(644,root,root,755)
%{texmf}/fonts/type1/public/qfonts

%files fonts-type1-xypic
%defattr(644,root,root,755)
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

%files format-omega
%defattr(644,root,root,755)
%doc %{texmf}/doc/omega
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/omega
%attr(755,root,root) %{_bindir}/omfonts
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
%attr(755,root,root) %{_bindir}/viromega
%{_mandir}/man1/viromega.1*
%attr(755,root,root) %{_bindir}/iniomega
%{_mandir}/man1/iniomega.1*
%{_mandir}/man1/omega.1*
%dir %{texmf}/omega
%{texmf}/omega/encodings
#%files omega-plain
%dir %{texmf}/omega/plain
%{texmf}/omega/plain/base
%{texmf}/omega/plain/config
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/omega.fmt
%{_datadir}/texmf/web2c/omega.pool

%files format-omega-lambda
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lambda
%{_mandir}/man1/lambda.1*
%dir %{texmf}/omega/lambda
%{texmf}/omega/lambda/base
%{texmf}/omega/lambda/config
%{texmf}/omega/lambda/misc
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/lambda.fmt

%files omega-ocp
%defattr(644,root,root,755)
%dir %{texmf}/omega/ocp
%{texmf}/omega/ocp/char2uni
%{texmf}/omega/ocp/misc
%{texmf}/omega/ocp/omega
%{texmf}/omega/ocp/uni2char

%files omega-otp
%defattr(644,root,root,755)
%dir %{texmf}/omega/otp
%{texmf}/omega/otp/char2uni
%{texmf}/omega/otp/misc
%{texmf}/omega/otp/omega
%{texmf}/omega/otp/uni2char

%files format-pdfetex
%defattr(644,root,root,755)
%dir %{texmf}/pdfetex
%dir %{texmf}/pdfetex/tex
%{texmf}/pdfetex/tex/config
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pdfevirtex
%attr(755,root,root) %{_bindir}/pdfeinitex
%{_mandir}/man1/pdfetex.1*
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfetex.efmt
%{_datadir}/texmf/web2c/pdfetex-pl.pool
%{_datadir}/texmf/web2c/pdfetex.pool

%files format-pdfelatex
%defattr(644,root,root,755)
%dir %{texmf}/pdfetex/latex
%{texmf}/pdfetex/latex/config
%attr(755,root,root) %{_bindir}/pdfelatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfelatex.efmt

%files format-pdfemex
%defattr(644,root,root,755)
%dir %{texmf}/pdfetex/mex
%{texmf}/pdfetex/mex/config
%attr(755,root,root) %{_bindir}/pdfemex
%attr(755,root,root) %{_bindir}/pdfemex-pl
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfemex.efmt

%files pdftex
%doc %{texmf}/doc/pdftex

%attr(755,root,root) %{_bindir}/epstopdf
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/pdfvirtex
%attr(755,root,root) %{_bindir}/pdfinitex

%dir %{texmf}/pdftex
%dir %{texmf}/pdftex/config

%{texmf}/pdftex/config/cmttf.map
%{texmf}/pdftex/config/pdftex.cfg
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/pdfinitex.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/pdfvirtex.1*

%files format-pdftex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/plain
%{texmf}/pdftex/plain/config
%{texmf}/pdftex/plain/misc
%{_datadir}/texmf/web2c/pdftex-pl.pool
%{_datadir}/texmf/web2c/pdftex.pool
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdftex.fmt

%files format-pdfamstex
%defattr(644,root,root,755)
%doc %{texmf}/doc/amstex
%dir %{texmf}/pdftex/amstex
%{texmf}/pdftex/amstex/config
%attr(755,root,root) %{_bindir}/pdfamstex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfamstex.fmt

# format?
%files format-pdftex-context
%defattr(644,root,root,755)
# zferyfikowac pliki z fontami
%{texmf}/pdftex/config/context

%files format-pdflatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/latex
%{texmf}/pdftex/latex/config
%attr(755,root,root) %{_bindir}/pdflatex
%{_mandir}/man1/pdflatex.1*
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdflatex.fmt

#%files format-pdfcslatex
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/pdfcslatex
# jaki¶ problem z generowaniem
#%config(noreplace) %verify(not md5 size mtime) /usr/share/texmf/web2c/pdfcslatex.fmt

#%files format-pdfcsplain
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/pdfcsplain
# jaki¶ problem z generowaniem
#%config(noreplace) %verify(not md5 size mtime) /usr/share/texmf/web2c/pdfcstex.fmt

%files format-pdfmex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/mex
%{texmf}/pdftex/mex/config
%attr(755,root,root) %{_bindir}/pdfmex
%attr(755,root,root) %{_bindir}/pdfmex-pl
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfmex.fmt

%files format-pdfplatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/platex
%{texmf}/pdftex/platex/config
%attr(755,root,root) %{_bindir}/pdfplatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfplatex.fmt

%files format-amstex
%defattr(644,root,root,755)
%dir %{texmf}/tex/amstex
%attr(755,root,root) %{_bindir}/amstex
%{_mandir}/man1/amstex.1*
%lang(fi) %{_mandir}/fi/man1/amstex.1*
# do czego jest bamstex ?
%attr(755,root,root) %{_bindir}/bamstex
%{texmf}/tex/amstex/base
%{texmf}/tex/amstex/config
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/amstex.fmt
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/bamstex.fmt

%files texconfig
%defattr(644,root,root,755)
%{texmf}/texconfig
%attr(755,root,root) %{_bindir}/texconfig
%{_mandir}/man1/texconfig.1*

%files format-context
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cont-cz
%attr(755,root,root) %{_bindir}/cont-de
%attr(755,root,root) %{_bindir}/cont-en
%attr(755,root,root) %{_bindir}/cont-nl
%attr(755,root,root) %{_bindir}/cont-uk
%{_mandir}/man1/cont-de.1*
%{_mandir}/man1/cont-en.1*
%{_mandir}/man1/cont-nl.1*
%dir %{texmf}/doc/context
%doc %{texmf}/doc/context/base
%dir %{texmf}/context
%dir %{texmf}/context/config
%{texmf}/context/config/texexec.ini
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
%{texmf}/tex/generic/context
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

%files csplain
%defattr(644,root,root,755)
%dir %{texmf}/doc/cstex
%doc %{texmf}/doc/cstex/cscorr.tab
%doc %{texmf}/doc/cstex/cs-fonts.doc
%doc %{texmf}/doc/cstex/csplain.doc
%doc %{texmf}/doc/cstex/parpozn.tex
%doc %{texmf}/doc/cstex/README-cspsfont
%doc %{texmf}/doc/cstex/test8z.tex
%doc %{texmf}/doc/cstex/testlat.tex
%attr(755,root,root) %{_bindir}/csplain

%{texmf}/tex/csplain

%files cyrplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cyrplain
%dir %{texmf}/tex/cyrplain
%{texmf}/tex/cyrplain/base
%{texmf}/tex/cyrplain/config
%attr(755,root,root) %{_bindir}/cyrtex

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

%files doc-de-tex-faq
%defattr(644,root,root,755)
%{texmf}/doc/help/faq/de-tex-faq

%files doc-LaTeX-FAQ-francaise
%defattr(644,root,root,755)
%{texmf}/doc/help/faq/LaTeX-FAQ-francaise

%files doc-uktug-faq
%defattr(644,root,root,755)
%{texmf}/doc/help/faq/uktug-faq

%files doc-latex2e-html
%defattr(644,root,root,755)
%{texmf}/doc/latex/latex2e-html

%files doc
%defattr(644,root,root,755)
%{texmf}/doc/README
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

%files plain-misc
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain/misc
%{texmf}/tex/plain/misc/arrow.tex
%{texmf}/tex/plain/misc/btxmac.tex
%{texmf}/tex/plain/misc/fontchart.tex
%{texmf}/tex/plain/misc/idxmac.tex
%{texmf}/tex/plain/misc/list.tex
%{texmf}/tex/plain/misc/llist.tex
%{texmf}/tex/plain/misc/mimulcol.tex
%{texmf}/tex/plain/misc/mproof.tex
%{texmf}/tex/plain/misc/scrload.tex
%{texmf}/tex/plain/misc/verbatim.tex
%{texmf}/tex/plain/misc/wasyfont.tex
%{texmf}/tex/plain/misc/wlist.tex
%{texmf}/tex/plain/misc/xepsf.tex

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

%files plain-mathtime
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mathtime
%dir %{texmf}/tex/plain/mathtime
%{texmf}/tex/plain/mathtime/ansiacce.tex
%{texmf}/tex/plain/mathtime/chironmt.tex
%{texmf}/tex/plain/mathtime/dcaccent.tex
%{texmf}/tex/plain/mathtime/encodean.tex
%{texmf}/tex/plain/mathtime/encodese.tex
%{texmf}/tex/plain/mathtime/encode.tex
%{texmf}/tex/plain/mathtime/encodetx.tex
%{texmf}/tex/plain/mathtime/mtextra.tex
%{texmf}/tex/plain/mathtime/mtmacs.tex
%{texmf}/tex/plain/mathtime/mtplain.tex
%{texmf}/tex/plain/mathtime/mtplainx.tex
%{texmf}/tex/plain/mathtime/mtplus.tex
%{texmf}/tex/plain/mathtime/plain-mt.tex
%{texmf}/tex/plain/mathtime/stanacce.tex
%{texmf}/tex/plain/mathtime/texnansi.tex

%files plain-dvips
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain/dvips
%{texmf}/tex/plain/dvips/blackdvi.tex
%{texmf}/tex/plain/dvips/colordvi.tex
%{texmf}/tex/plain/dvips/dvipsmac.tex
%{texmf}/tex/plain/dvips/epsf.tex
%{texmf}/tex/plain/dvips/rotate.tex
%{texmf}/tex/plain/dvips/rotsample.tex

%files plain-amsfonts
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain/amsfonts
%{texmf}/tex/plain/amsfonts/amssym.def
%{texmf}/tex/plain/amsfonts/amssym.tex
%{texmf}/tex/plain/amsfonts/cyracc.def

%files mex
%defattr(644,root,root,755)
%doc %{texmf}/doc/polish/mex
%attr(755,root,root) %{_bindir}/mex
%attr(755,root,root) %{_bindir}/mex-pl
%dir %{texmf}/tex/mex
%dir %{texmf}/tex/mex/base
%{texmf}/tex/mex/base/mex1.tex
%{texmf}/tex/mex/base/mex2.tex
%{texmf}/tex/mex/base/mex.tex
%dir %{texmf}/tex/mex/config
%{texmf}/tex/mex/config/mexconf.tex
%{texmf}/tex/mex/config/mex.ini
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/mex.fmt

%files latex-wasysym
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/wasysym
%dir %{texmf}/tex/latex/wasysym
%{texmf}/tex/latex/wasysym/uwasy.fd
%{texmf}/tex/latex/wasysym/wasysym.sty

%files latex-vnr
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/vnr
%{texmf}/tex/latex/vnr/t5cmdh.fd
%{texmf}/tex/latex/vnr/t5cmfib.fd
%{texmf}/tex/latex/vnr/t5cmfr.fd
%{texmf}/tex/latex/vnr/t5cmr.fd
%{texmf}/tex/latex/vnr/t5cmss.fd
%{texmf}/tex/latex/vnr/t5cmtt.fd
%{texmf}/tex/latex/vnr/t5cmvtt.fd

%files latex-vnps
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/vnps
%{texmf}/tex/latex/vnps/t5bch.fd
%{texmf}/tex/latex/vnps/t5pag.fd
%{texmf}/tex/latex/vnps/t5pbk.fd
%{texmf}/tex/latex/vnps/t5pcr.fd
%{texmf}/tex/latex/vnps/t5phv.fd
%{texmf}/tex/latex/vnps/t5pnc.fd
%{texmf}/tex/latex/vnps/t5ppl.fd
%{texmf}/tex/latex/vnps/t5ptm.fd
%{texmf}/tex/latex/vnps/t5put.fd
%{texmf}/tex/latex/vnps/t5vcmdh.fd
%{texmf}/tex/latex/vnps/t5vcmfib.fd
%{texmf}/tex/latex/vnps/t5vcmfr.fd
%{texmf}/tex/latex/vnps/t5vcmr.fd
%{texmf}/tex/latex/vnps/t5vcmss.fd
%{texmf}/tex/latex/vnps/t5vcmtt.fd
%{texmf}/tex/latex/vnps/t5vcmvtt.fd

%files latex-units
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/units
%dir %{texmf}/tex/latex/units
%{texmf}/tex/latex/units/nicefrac.sty
%{texmf}/tex/latex/units/units.sty

%files latex-umlaute
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/umlaute
%{texmf}/tex/latex/umlaute/atari.def
%{texmf}/tex/latex/umlaute/isolatin.def
%{texmf}/tex/latex/umlaute/mac.def
%{texmf}/tex/latex/umlaute/pc850.def
%{texmf}/tex/latex/umlaute/roman8.def
%{texmf}/tex/latex/umlaute/umlaute.sty
%{texmf}/tex/latex/umlaute/umlaut.sty

%files latex-tools
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/tools
%dir %{texmf}/tex/latex/tools
%{texmf}/tex/latex/tools/afterpage.sty
%{texmf}/tex/latex/tools/array.sty
%{texmf}/tex/latex/tools/bm.sty
%{texmf}/tex/latex/tools/calc.sty
%{texmf}/tex/latex/tools/dcolumn.sty
%{texmf}/tex/latex/tools/delarray.sty
%{texmf}/tex/latex/tools/enumerate.sty
%{texmf}/tex/latex/tools/e.tex
%{texmf}/tex/latex/tools/fontsmpl.sty
%{texmf}/tex/latex/tools/fontsmpl.tex
%{texmf}/tex/latex/tools/ftnright.sty
%{texmf}/tex/latex/tools/hhline.sty
%{texmf}/tex/latex/tools/h.tex
%{texmf}/tex/latex/tools/indentfirst.sty
%{texmf}/tex/latex/tools/layout.sty
%{texmf}/tex/latex/tools/longtable.sty
%{texmf}/tex/latex/tools/multicol.sty
%{texmf}/tex/latex/tools/q.tex
%{texmf}/tex/latex/tools/rawfonts.sty
%{texmf}/tex/latex/tools/r.tex
%{texmf}/tex/latex/tools/showkeys.sty
%{texmf}/tex/latex/tools/somedefs.sty
%{texmf}/tex/latex/tools/s.tex
%{texmf}/tex/latex/tools/tabularx.sty
%{texmf}/tex/latex/tools/.tex
%{texmf}/tex/latex/tools/thb.sty
%{texmf}/tex/latex/tools/thcb.sty
%{texmf}/tex/latex/tools/thc.sty
%{texmf}/tex/latex/tools/theorem.sty
%{texmf}/tex/latex/tools/thmb.sty
%{texmf}/tex/latex/tools/thm.sty
%{texmf}/tex/latex/tools/thp.sty
%{texmf}/tex/latex/tools/trace.sty
%{texmf}/tex/latex/tools/varioref.sty
%{texmf}/tex/latex/tools/verbatim.sty
%{texmf}/tex/latex/tools/verbtest.tex
%{texmf}/tex/latex/tools/xr.sty
%{texmf}/tex/latex/tools/xspace.sty
%{texmf}/tex/latex/tools/x.tex

%files latex-titlesec
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/titlesec
%{texmf}/tex/latex/titlesec/block.tss
%{texmf}/tex/latex/titlesec/drop.tss
%{texmf}/tex/latex/titlesec/frame.tss
%{texmf}/tex/latex/titlesec/leftmargin.tss
%{texmf}/tex/latex/titlesec/margin.tss
%{texmf}/tex/latex/titlesec/page.tsk
%{texmf}/tex/latex/titlesec/rightmargin.tss
%{texmf}/tex/latex/titlesec/titlesec.new
%{texmf}/tex/latex/titlesec/titlesec.sty
%{texmf}/tex/latex/titlesec/titletoc.sty
%{texmf}/tex/latex/titlesec/wrap.tss

%files latex-t2
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/t2
%{texmf}/tex/latex/t2/citehack.sty
%{texmf}/tex/latex/t2/mathtext.sty
%{texmf}/tex/latex/t2/misccorr.sty

%files latex-SIunits
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/SIunits
%dir %{texmf}/tex/latex/SIunits
%{texmf}/tex/latex/SIunits/binary.sty
%{texmf}/tex/latex/SIunits/SIunits.sty

%files latex-seminar
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/seminar
%dir %{texmf}/tex/latex/seminar
%{texmf}/tex/latex/seminar/2up.sty
%{texmf}/tex/latex/seminar/2up.tex
%{texmf}/tex/latex/seminar/npsfont.sty
%{texmf}/tex/latex/seminar/sem-a4.sty
%{texmf}/tex/latex/seminar/semcolor.sty
%{texmf}/tex/latex/seminar/semhelv.sty
%{texmf}/tex/latex/seminar/seminar.bg2
%{texmf}/tex/latex/seminar/seminar.bug
%{texmf}/tex/latex/seminar/seminar.cls
%{texmf}/tex/latex/seminar/seminar.sty
%{texmf}/tex/latex/seminar/semlayer.sty
%{texmf}/tex/latex/seminar/semlcmss.sty
%{texmf}/tex/latex/seminar/sem-page.sty
%{texmf}/tex/latex/seminar/semrot.sty
%{texmf}/tex/latex/seminar/slidesec.sty
%{texmf}/tex/latex/seminar/xcomment.sty

%files latex-revtex4
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/revtex4
%dir %{texmf}/tex/latex/revtex4
%{texmf}/tex/latex/revtex4/10pt.rtx
%{texmf}/tex/latex/revtex4/11pt.rtx
%{texmf}/tex/latex/revtex4/12pt.rtx
%{texmf}/tex/latex/revtex4/aps.rtx
%{texmf}/tex/latex/revtex4/revsymb.sty
%{texmf}/tex/latex/revtex4/revtex4.cls
%{texmf}/tex/latex/revtex4/rmp.rtx

%files latex-qfonts
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/qfonts
%{texmf}/tex/latex/qfonts/ot1qbk.fd
%{texmf}/tex/latex/qfonts/ot1qcr.fd
%{texmf}/tex/latex/qfonts/ot1qhv.fd
%{texmf}/tex/latex/qfonts/ot1qpl.fd
%{texmf}/tex/latex/qfonts/ot1qtm.fd
%{texmf}/tex/latex/qfonts/ot1qzc.fd
%{texmf}/tex/latex/qfonts/ot4qbk.fd
%{texmf}/tex/latex/qfonts/ot4qcr.fd
%{texmf}/tex/latex/qfonts/ot4qhv.fd
%{texmf}/tex/latex/qfonts/ot4qpl.fd
%{texmf}/tex/latex/qfonts/ot4qtm.fd
%{texmf}/tex/latex/qfonts/ot4qzc.fd
%{texmf}/tex/latex/qfonts/qbookman.sty
%{texmf}/tex/latex/qfonts/qcourier.sty
%{texmf}/tex/latex/qfonts/qpalatin.sty
%{texmf}/tex/latex/qfonts/qswiss.sty
%{texmf}/tex/latex/qfonts/qtimes.sty
%{texmf}/tex/latex/qfonts/qxqbk.fd
%{texmf}/tex/latex/qfonts/qxqcr.fd
%{texmf}/tex/latex/qfonts/qxqhv.fd
%{texmf}/tex/latex/qfonts/qxqpl.fd
%{texmf}/tex/latex/qfonts/qxqtm.fd
%{texmf}/tex/latex/qfonts/qxqzc.fd
%{texmf}/tex/latex/qfonts/qzapfcha.sty

%files latex-psnfss
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/psnfss
%{texmf}/tex/latex/psnfss/8rbch.fd
%{texmf}/tex/latex/psnfss/8rpag.fd
%{texmf}/tex/latex/psnfss/8rpbk.fd
%{texmf}/tex/latex/psnfss/8rpcr.fd
%{texmf}/tex/latex/psnfss/8rphv.fd
%{texmf}/tex/latex/psnfss/8rpnc.fd
%{texmf}/tex/latex/psnfss/8rppl.fd
%{texmf}/tex/latex/psnfss/8rptm.fd
%{texmf}/tex/latex/psnfss/8rput.fd
%{texmf}/tex/latex/psnfss/8rpzc.fd
%{texmf}/tex/latex/psnfss/8r.sty
%{texmf}/tex/latex/psnfss/avant.sty
%{texmf}/tex/latex/psnfss/bookman.sty
%{texmf}/tex/latex/psnfss/chancery.sty
%{texmf}/tex/latex/psnfss/charter.sty
%{texmf}/tex/latex/psnfss/courier.sty
%{texmf}/tex/latex/psnfss/helvet.sty
%{texmf}/tex/latex/psnfss/mathpazo.sty
%{texmf}/tex/latex/psnfss/mathpple.sty
%{texmf}/tex/latex/psnfss/mathptm.sty
%{texmf}/tex/latex/psnfss/mathptmx.sty
%{texmf}/tex/latex/psnfss/newcent.sty
%{texmf}/tex/latex/psnfss/omlbch.fd
%{texmf}/tex/latex/psnfss/omlpag.fd
%{texmf}/tex/latex/psnfss/omlpbk.fd
%{texmf}/tex/latex/psnfss/omlpcr.fd
%{texmf}/tex/latex/psnfss/omlphv.fd
%{texmf}/tex/latex/psnfss/omlpnc.fd
%{texmf}/tex/latex/psnfss/omlppl.fd
%{texmf}/tex/latex/psnfss/omlptmcm.fd
%{texmf}/tex/latex/psnfss/omlptm.fd
%{texmf}/tex/latex/psnfss/omlput.fd
%{texmf}/tex/latex/psnfss/omlpzc.fd
%{texmf}/tex/latex/psnfss/omlzplm.fd
%{texmf}/tex/latex/psnfss/omlzpple.fd
%{texmf}/tex/latex/psnfss/omlztmcm.fd
%{texmf}/tex/latex/psnfss/omsbch.fd
%{texmf}/tex/latex/psnfss/omspag.fd
%{texmf}/tex/latex/psnfss/omspbk.fd
%{texmf}/tex/latex/psnfss/omspcr.fd
%{texmf}/tex/latex/psnfss/omsphv.fd
%{texmf}/tex/latex/psnfss/omspnc.fd
%{texmf}/tex/latex/psnfss/omsppl.fd
%{texmf}/tex/latex/psnfss/omsptm.fd
%{texmf}/tex/latex/psnfss/omsput.fd
%{texmf}/tex/latex/psnfss/omspzccm.fd
%{texmf}/tex/latex/psnfss/omspzc.fd
%{texmf}/tex/latex/psnfss/omszplm.fd
%{texmf}/tex/latex/psnfss/omszpple.fd
%{texmf}/tex/latex/psnfss/omsztmcm.fd
%{texmf}/tex/latex/psnfss/omxpsycm.fd
%{texmf}/tex/latex/psnfss/omxzplm.fd
%{texmf}/tex/latex/psnfss/omxzpple.fd
%{texmf}/tex/latex/psnfss/omxztmcm.fd
%{texmf}/tex/latex/psnfss/ot1bch.fd
%{texmf}/tex/latex/psnfss/ot1fplmbb.fd
%{texmf}/tex/latex/psnfss/ot1pag.fd
%{texmf}/tex/latex/psnfss/ot1pbk.fd
%{texmf}/tex/latex/psnfss/ot1pcr.fd
%{texmf}/tex/latex/psnfss/ot1phv.fd
%{texmf}/tex/latex/psnfss/ot1pnc.fd
%{texmf}/tex/latex/psnfss/ot1ppl.fd
%{texmf}/tex/latex/psnfss/ot1ptmcm.fd
%{texmf}/tex/latex/psnfss/ot1ptm.fd
%{texmf}/tex/latex/psnfss/ot1put.fd
%{texmf}/tex/latex/psnfss/ot1pzc.fd
%{texmf}/tex/latex/psnfss/ot1zplm.fd
%{texmf}/tex/latex/psnfss/ot1zpple.fd
%{texmf}/tex/latex/psnfss/ot1ztmcm.fd
%{texmf}/tex/latex/psnfss/palatino.sty
%{texmf}/tex/latex/psnfss/pifont.sty
%{texmf}/tex/latex/psnfss/t1bch.fd
%{texmf}/tex/latex/psnfss/t1fplmbb.fd
%{texmf}/tex/latex/psnfss/t1pag.fd
%{texmf}/tex/latex/psnfss/t1pbk.fd
%{texmf}/tex/latex/psnfss/t1pcr.fd
%{texmf}/tex/latex/psnfss/t1phv.fd
%{texmf}/tex/latex/psnfss/t1pnc.fd
%{texmf}/tex/latex/psnfss/t1ppl.fd
%{texmf}/tex/latex/psnfss/t1ptm.fd
%{texmf}/tex/latex/psnfss/t1put.fd
%{texmf}/tex/latex/psnfss/t1pzc.fd
%{texmf}/tex/latex/psnfss/times.sty
%{texmf}/tex/latex/psnfss/ts1bch.fd
%{texmf}/tex/latex/psnfss/ts1pag.fd
%{texmf}/tex/latex/psnfss/ts1pbk.fd
%{texmf}/tex/latex/psnfss/ts1pcr.fd
%{texmf}/tex/latex/psnfss/ts1phv.fd
%{texmf}/tex/latex/psnfss/ts1pnc.fd
%{texmf}/tex/latex/psnfss/ts1ppl.fd
%{texmf}/tex/latex/psnfss/ts1ptm.fd
%{texmf}/tex/latex/psnfss/ts1put.fd
%{texmf}/tex/latex/psnfss/ts1pzc.fd
%{texmf}/tex/latex/psnfss/ufplm.fd
%{texmf}/tex/latex/psnfss/upsy.fd
%{texmf}/tex/latex/psnfss/upzd.fd
%{texmf}/tex/latex/psnfss/utopia.sty

%files latex-pb-diagram
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/pb-diagram
%dir %{texmf}/tex/latex/pb-diagram
%{texmf}/tex/latex/pb-diagram/lamsarrow.sty
%{texmf}/tex/latex/pb-diagram/pb-diagram.sty
%{texmf}/tex/latex/pb-diagram/pb-lams.sty
%{texmf}/tex/latex/pb-diagram/pb-xy.sty

%files latex-palatcm
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/palatcm
%{texmf}/tex/latex/palatcm/omlpplcm.fd
%{texmf}/tex/latex/palatcm/omspplcm.fd
%{texmf}/tex/latex/palatcm/omxpplcm.fd
%{texmf}/tex/latex/palatcm/ot1pplcm.fd
%{texmf}/tex/latex/palatcm/palatcm.sty

%files latex-oberdiek
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/oberdiek
%dir %{texmf}/tex/latex/oberdiek
%{texmf}/tex/latex/oberdiek/alphalph.sty
%{texmf}/tex/latex/oberdiek/chemarr.sty
%{texmf}/tex/latex/oberdiek/dvipscol.sty
%{texmf}/tex/latex/oberdiek/engord.sty
%{texmf}/tex/latex/oberdiek/epstopdf.sty
%{texmf}/tex/latex/oberdiek/hypbmsec.sty
%{texmf}/tex/latex/oberdiek/hypcap.sty
%{texmf}/tex/latex/oberdiek/ifpdf.sty
%{texmf}/tex/latex/oberdiek/ifvtex.sty
%{texmf}/tex/latex/oberdiek/pagesel.sty
%{texmf}/tex/latex/oberdiek/pdfcolmk.sty
%{texmf}/tex/latex/oberdiek/pdfcrypt.sty
%{texmf}/tex/latex/oberdiek/pdflscape.sty
%{texmf}/tex/latex/oberdiek/refcount.sty
%{texmf}/tex/latex/oberdiek/settobox.sty
%{texmf}/tex/latex/oberdiek/twoopt.sty
%{texmf}/tex/latex/oberdiek/vpe.sty

%files latex-ntgclass
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/ntgclass
%dir %{texmf}/tex/latex/ntgclass
%{texmf}/tex/latex/ntgclass/a4.sty
%{texmf}/tex/latex/ntgclass/artikel1.cls
%{texmf}/tex/latex/ntgclass/artikel2.cls
%{texmf}/tex/latex/ntgclass/artikel3.cls
%{texmf}/tex/latex/ntgclass/boek3.cls
%{texmf}/tex/latex/ntgclass/boek.cls
%{texmf}/tex/latex/ntgclass/brief.cls
%{texmf}/tex/latex/ntgclass/ntg10.clo
%{texmf}/tex/latex/ntgclass/ntg11.clo
%{texmf}/tex/latex/ntgclass/ntg12.clo
%{texmf}/tex/latex/ntgclass/rapport1.cls
%{texmf}/tex/latex/ntgclass/rapport3.cls

%files latex-natbib
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/natbib
%dir %{texmf}/tex/latex/natbib
%{texmf}/tex/latex/natbib/bibentry.sty
%{texmf}/tex/latex/natbib/natbib.sty

%files latex-mwcls
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mwcls
%dir %{texmf}/tex/latex/mwcls
%{texmf}/tex/latex/mwcls/mw10.clo
%{texmf}/tex/latex/mwcls/mw11.clo
%{texmf}/tex/latex/mwcls/mw12.clo
%{texmf}/tex/latex/mwcls/mwart.cls
%{texmf}/tex/latex/mwcls/mwbk10.clo
%{texmf}/tex/latex/mwcls/mwbk11.clo
%{texmf}/tex/latex/mwcls/mwbk12.clo
%{texmf}/tex/latex/mwcls/mwbk.cls
%{texmf}/tex/latex/mwcls/mwrep.cls

%files latex-multirow
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/multirow
%{texmf}/tex/latex/multirow/bigdelim.sty
%{texmf}/tex/latex/multirow/bigstrut.sty
%{texmf}/tex/latex/multirow/multirow.sty

%files latex-ms
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/ms
%dir %{texmf}/tex/latex/ms
%{texmf}/tex/latex/ms/count1to.sty
%{texmf}/tex/latex/ms/eso-pic.sty
%{texmf}/tex/latex/ms/everysel.sty
%{texmf}/tex/latex/ms/everyshi.sty
%{texmf}/tex/latex/ms/multitoc.sty
%{texmf}/tex/latex/ms/prelim2e.sty
%{texmf}/tex/latex/ms/ragged2e.sty

%files latex-mltex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mltex
%dir %{texmf}/tex/latex/mltex
%{texmf}/tex/latex/mltex/lo1enc.def
%{texmf}/tex/latex/mltex/mlltxchg.def
%{texmf}/tex/latex/mltex/mltex.sty

%files latex-misc
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/tocbibind
%doc %{texmf}/doc/latex/xtab
%doc %{texmf}/doc/latex/yfonts
%doc %{texmf}/doc/latex/supertab
%doc %{texmf}/doc/latex/sidecap
%doc %{texmf}/doc/latex/showlabels
%doc %{texmf}/doc/latex/scale
%doc %{texmf}/doc/latex/rotfloat
%doc %{texmf}/doc/latex/rotating
%doc %{texmf}/doc/latex/leftidx
%doc %{texmf}/doc/latex/geometry
%doc %{texmf}/doc/latex/footmisc
%doc %{texmf}/doc/latex/floatflt
%doc %{texmf}/doc/latex/draftcopy
%doc %{texmf}/doc/latex/changebar
%doc %{texmf}/doc/latex/ccaption
%doc %{texmf}/doc/latex/booktabs
%doc %{texmf}/doc/latex/anysize
%doc %{texmf}/doc/latex/aeguill
%doc %{texmf}/doc/latex/acronym
%dir %{texmf}/tex/latex/misc
%{texmf}/tex/latex/misc/a4dutch.sty
%{texmf}/tex/latex/misc/a4wide.sty
%{texmf}/tex/latex/misc/acronym.sty
%{texmf}/tex/latex/misc/aeguill.sty
%{texmf}/tex/latex/misc/anysize.sty
%{texmf}/tex/latex/misc/apalike.sty
%{texmf}/tex/latex/misc/avantgar.sty
%{texmf}/tex/latex/misc/bar.sty
%{texmf}/tex/latex/misc/bbold.sty
%{texmf}/tex/latex/misc/beton.sty
%{texmf}/tex/latex/misc/bibgerm.sty
%{texmf}/tex/latex/misc/bold-extra.sty
%{texmf}/tex/latex/misc/booktabs.sty
%{texmf}/tex/latex/misc/boxedminipage.sty
%{texmf}/tex/latex/misc/cancel.sty
%{texmf}/tex/latex/misc/capt-of.sty
%{texmf}/tex/latex/misc/ccaption.sty
%{texmf}/tex/latex/misc/changebar.sty
%{texmf}/tex/latex/misc/chappg.sty
%{texmf}/tex/latex/misc/citesort.sty
%{texmf}/tex/latex/misc/comment.sty
%{texmf}/tex/latex/misc/concrete.sty
%{texmf}/tex/latex/misc/crop.sty
%{texmf}/tex/latex/misc/doublespace.sty
%{texmf}/tex/latex/misc/draftcopy.sty
%{texmf}/tex/latex/misc/eclbip.sty
%{texmf}/tex/latex/misc/ecltree.sty
%{texmf}/tex/latex/misc/endnotes.sty
%{texmf}/tex/latex/misc/euler.sty
%{texmf}/tex/latex/misc/exam.cls
%{texmf}/tex/latex/misc/example.sty
%{texmf}/tex/latex/misc/fancybox.sty
%{texmf}/tex/latex/misc/fguill.sty
%{texmf}/tex/latex/misc/floatflt.sty
%{texmf}/tex/latex/misc/float.sty
%{texmf}/tex/latex/misc/fltpage.sty
%{texmf}/tex/latex/misc/fnpara.sty
%{texmf}/tex/latex/misc/footbib.sty
%{texmf}/tex/latex/misc/footmisc.sty
%{texmf}/tex/latex/misc/footnpag.sty
%{texmf}/tex/latex/misc/framed.sty
%{texmf}/tex/latex/misc/fullpage.sty
%{texmf}/tex/latex/misc/geometry.sty
%{texmf}/tex/latex/misc/gletter.sty
%{texmf}/tex/latex/misc/hangcaption.sty
%{texmf}/tex/latex/misc/helvetic.sty
%{texmf}/tex/latex/misc/here.sty
%{texmf}/tex/latex/misc/hyphenat.sty
%{texmf}/tex/latex/misc/index.sty
%{texmf}/tex/latex/misc/isolatin1.sty
%{texmf}/tex/latex/misc/landscape.sty
%{texmf}/tex/latex/misc/lastpage.sty
%{texmf}/tex/latex/misc/layouts.sty
%{texmf}/tex/latex/misc/leftidx.sty
%{texmf}/tex/latex/misc/marvosym.sty
%{texmf}/tex/latex/misc/mathcomp.sty
%{texmf}/tex/latex/misc/moreverb.sty
%{texmf}/tex/latex/misc/multibox.sty
%{texmf}/tex/latex/misc/multind.sty
%{texmf}/tex/latex/misc/ncntrsbk.sty
%{texmf}/tex/latex/misc/nomencl.sty
%{texmf}/tex/latex/misc/optional.sty
%{texmf}/tex/latex/misc/overpic.sty
%{texmf}/tex/latex/misc/paralist.sty
%{texmf}/tex/latex/misc/parskip.sty
%{texmf}/tex/latex/misc/pdfpages.sty
%{texmf}/tex/latex/misc/picinpar.sty
%{texmf}/tex/latex/misc/picins.sty
%{texmf}/tex/latex/misc/placeins.sty
%{texmf}/tex/latex/misc/portland.sty
%{texmf}/tex/latex/misc/prettyref.sty
%{texmf}/tex/latex/misc/program.sty
%{texmf}/tex/latex/misc/psboxit.sty
%{texmf}/tex/latex/misc/psfrag.sty
%{texmf}/tex/latex/misc/pslatex.sty
%{texmf}/tex/latex/misc/relsize.sty
%{texmf}/tex/latex/misc/rotating.sty
%{texmf}/tex/latex/misc/rotfloat.sty
%{texmf}/tex/latex/misc/scale.sty
%{texmf}/tex/latex/misc/sectsty.sty
%{texmf}/tex/latex/misc/selectp.sty
%{texmf}/tex/latex/misc/setspace.sty
%{texmf}/tex/latex/misc/shadow.sty
%{texmf}/tex/latex/misc/shapepar.sty
%{texmf}/tex/latex/misc/showdim.sty
%{texmf}/tex/latex/misc/showlabels.sty
%{texmf}/tex/latex/misc/showtags.sty
%{texmf}/tex/latex/misc/sidecap.sty
%{texmf}/tex/latex/misc/SIunits.sty
%{texmf}/tex/latex/misc/slashbox.sty
%{texmf}/tex/latex/misc/soul.sty
%{texmf}/tex/latex/misc/stdclsdv.sty
%{texmf}/tex/latex/misc/stmaryrd.sty
%{texmf}/tex/latex/misc/subfigure.sty
%{texmf}/tex/latex/misc/supertabular.sty
%{texmf}/tex/latex/misc/sz.sty
%{texmf}/tex/latex/misc/tabls.sty
%{texmf}/tex/latex/misc/textfit.sty
%{texmf}/tex/latex/misc/threeparttable.sty
%{texmf}/tex/latex/misc/tocbibind.sty
%{texmf}/tex/latex/misc/tocloft.sty
%{texmf}/tex/latex/misc/trees.sty
%{texmf}/tex/latex/misc/type1cm.sty
%{texmf}/tex/latex/misc/ulem.sty
%{texmf}/tex/latex/misc/url.sty
%{texmf}/tex/latex/misc/ustmry.fd
%{texmf}/tex/latex/misc/version.sty
%{texmf}/tex/latex/misc/vmargin.sty
%{texmf}/tex/latex/misc/vpage.sty
%{texmf}/tex/latex/misc/wrapfig.sty
%{texmf}/tex/latex/misc/xtab.sty
%{texmf}/tex/latex/misc/yfonts.sty
%{texmf}/tex/latex/misc/zapfchan.sty

%files latex-minitoc
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/minitoc
%dir %{texmf}/tex/latex/minitoc
%{texmf}/tex/latex/minitoc/afrikaan.mld
%{texmf}/tex/latex/minitoc/afrikaans.mld
%{texmf}/tex/latex/minitoc/american.mld
%{texmf}/tex/latex/minitoc/arabic.mld
%{texmf}/tex/latex/minitoc/arab.mld
%{texmf}/tex/latex/minitoc/armenian.mld
%{texmf}/tex/latex/minitoc/austrian.mld
%{texmf}/tex/latex/minitoc/bahasa.mld
%{texmf}/tex/latex/minitoc/basque.mld
%{texmf}/tex/latex/minitoc/bicig.mld
%{texmf}/tex/latex/minitoc/brazil.mld
%{texmf}/tex/latex/minitoc/breton.mld
%{texmf}/tex/latex/minitoc/buryat.mld
%{texmf}/tex/latex/minitoc/catalan.mld
%{texmf}/tex/latex/minitoc/croatian.mld
%{texmf}/tex/latex/minitoc/czech.mld
%{texmf}/tex/latex/minitoc/danish.mld
%{texmf}/tex/latex/minitoc/dutch.mld
%{texmf}/tex/latex/minitoc/english.mld
%{texmf}/tex/latex/minitoc/esperant.mld
%{texmf}/tex/latex/minitoc/esperanto.mld
%{texmf}/tex/latex/minitoc/estonian.mld
%{texmf}/tex/latex/minitoc/ethiopia.mld
%{texmf}/tex/latex/minitoc/ethiopian.mld
%{texmf}/tex/latex/minitoc/finnish.mld
%{texmf}/tex/latex/minitoc/francais.mld
%{texmf}/tex/latex/minitoc/french.mld
%{texmf}/tex/latex/minitoc/galician.mld
%{texmf}/tex/latex/minitoc/germanb.mld
%{texmf}/tex/latex/minitoc/german.mld
%{texmf}/tex/latex/minitoc/greek.mld
%{texmf}/tex/latex/minitoc/hungarian.mld
%{texmf}/tex/latex/minitoc/irish.mld
%{texmf}/tex/latex/minitoc/italian.mld
%{texmf}/tex/latex/minitoc/lithuanian.mld
%{texmf}/tex/latex/minitoc/lsorbian.mld
%{texmf}/tex/latex/minitoc/magyar.mld
%{texmf}/tex/latex/minitoc/minitoc.sty
%{texmf}/tex/latex/minitoc/mongol.mld
%{texmf}/tex/latex/minitoc/mtcoff.sty
%{texmf}/tex/latex/minitoc/ngermanb.mld
%{texmf}/tex/latex/minitoc/norsk.mld
%{texmf}/tex/latex/minitoc/nynorsk.mld
%{texmf}/tex/latex/minitoc/polish.mld
%{texmf}/tex/latex/minitoc/portuges.mld
%{texmf}/tex/latex/minitoc/romanian.mld
%{texmf}/tex/latex/minitoc/russianb.mld
%{texmf}/tex/latex/minitoc/russianc.mld
%{texmf}/tex/latex/minitoc/russian.mld
%{texmf}/tex/latex/minitoc/scottish.mld
%{texmf}/tex/latex/minitoc/serbian.mld
%{texmf}/tex/latex/minitoc/slovak.mld
%{texmf}/tex/latex/minitoc/slovene.mld
%{texmf}/tex/latex/minitoc/spanish.mld
%{texmf}/tex/latex/minitoc/swedish.mld
%{texmf}/tex/latex/minitoc/turkish.mld
%{texmf}/tex/latex/minitoc/ukraineb.mld
%{texmf}/tex/latex/minitoc/usorbian.mld
%{texmf}/tex/latex/minitoc/vietnamese.mld
%{texmf}/tex/latex/minitoc/vietnam.mld
%{texmf}/tex/latex/minitoc/welsh.mld

%files latex-mfnfss
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mfnfss
%dir %{texmf}/tex/latex/mfnfss
%{texmf}/tex/latex/mfnfss/oldgerm.sty
%{texmf}/tex/latex/mfnfss/ot1panr.fd
%{texmf}/tex/latex/mfnfss/ot1pss.fd
%{texmf}/tex/latex/mfnfss/pandora.sty
%{texmf}/tex/latex/mfnfss/uyfrak.fd
%{texmf}/tex/latex/mfnfss/uygoth.fd
%{texmf}/tex/latex/mfnfss/uyinit.fd
%{texmf}/tex/latex/mfnfss/uyswab.fd

%files latex-mflogo
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/mflogo
%{texmf}/tex/latex/mflogo/mflogo.sty
%{texmf}/tex/latex/mflogo/ulogo.fd

%files latex-mdwtools
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/mdwtools
%dir %{texmf}/tex/latex/mdwtools
%{texmf}/tex/latex/mdwtools/at.sty
%{texmf}/tex/latex/mdwtools/cmtt.sty
%{texmf}/tex/latex/mdwtools/doafter.sty
%{texmf}/tex/latex/mdwtools/doafter.tex
%{texmf}/tex/latex/mdwtools/footnote.sty
%{texmf}/tex/latex/mdwtools/mathenv.sty
%{texmf}/tex/latex/mdwtools/mdwlist.sty
%{texmf}/tex/latex/mdwtools/mdwmath.sty
%{texmf}/tex/latex/mdwtools/mdwtab.sty
%{texmf}/tex/latex/mdwtools/mTTcmtt.fd
%{texmf}/tex/latex/mdwtools/mTTenc.def
%{texmf}/tex/latex/mdwtools/sverb.sty
%{texmf}/tex/latex/mdwtools/syntax.sty

%files latex-mathtime
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/mathtime
%{texmf}/tex/latex/mathtime/lfonts-m.tex
%{texmf}/tex/latex/mathtime/lplain-m.tex
%{texmf}/tex/latex/mathtime/mathpi.sty
%{texmf}/tex/latex/mathtime/mathtime.sty
%{texmf}/tex/latex/mathtime/mt11p.sty
%{texmf}/tex/latex/mathtime/mtlatex.tex
%{texmf}/tex/latex/mathtime/mtltplus.tex
%{texmf}/tex/latex/mathtime/my1mtt.fd
%{texmf}/tex/latex/mathtime/my2mtt.fd
%{texmf}/tex/latex/mathtime/my3mtt.fd
%{texmf}/tex/latex/mathtime/omslby.fd
%{texmf}/tex/latex/mathtime/umh2.fd
%{texmf}/tex/latex/mathtime/umh2scr.fd
%{texmf}/tex/latex/mathtime/umh6.fd
%{texmf}/tex/latex/mathtime/umtms.fd

%files latex-mathptmx
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/mathptmx
%{texmf}/tex/latex/mathptmx/mathptmx.sty
%{texmf}/tex/latex/mathptmx/omlztmcm.fd
%{texmf}/tex/latex/mathptmx/omsztmcm.fd
%{texmf}/tex/latex/mathptmx/omxztmcm.fd
%{texmf}/tex/latex/mathptmx/ot1ztmcm.fd

%files latex-mathptm
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/mathptm
%{texmf}/tex/latex/mathptm/mathptm.sty
%{texmf}/tex/latex/mathptm/omlptmcm.fd
%{texmf}/tex/latex/mathptm/omspzccm.fd
%{texmf}/tex/latex/mathptm/omxpsycm.fd
%{texmf}/tex/latex/mathptm/ot1ptmcm.fd

%files latex-mathpple
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/mathpple
%{texmf}/tex/latex/mathpple/mathpple.sty
%{texmf}/tex/latex/mathpple/omlzpple.fd
%{texmf}/tex/latex/mathpple/omszpple.fd
%{texmf}/tex/latex/mathpple/omxzpple.fd
%{texmf}/tex/latex/mathpple/ot1phvv.fd
%{texmf}/tex/latex/mathpple/ot1zpple.fd
%{texmf}/tex/latex/mathpple/t1phvv.fd
%{texmf}/tex/latex/mathpple/ts1phvv.fd

%files latex-lucidabr
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/lucidabr
%{texmf}/tex/latex/lucidabr/8rhlce.fd
%{texmf}/tex/latex/lucidabr/8rhlcf.fd
%{texmf}/tex/latex/lucidabr/8rhlcn.fd
%{texmf}/tex/latex/lucidabr/8rhlct.fd
%{texmf}/tex/latex/lucidabr/8rhlcw.fd
%{texmf}/tex/latex/lucidabr/8rhlh.fd
%{texmf}/tex/latex/lucidabr/8rhls.fd
%{texmf}/tex/latex/lucidabr/8rhlst.fd
%{texmf}/tex/latex/lucidabr/8rhlx.fd
%{texmf}/tex/latex/lucidabr/lmrhlcm.fd
%{texmf}/tex/latex/lucidabr/lucbmath.sty
%{texmf}/tex/latex/lucidabr/lucfont.tex
%{texmf}/tex/latex/lucidabr/lucidabr.sty
%{texmf}/tex/latex/lucidabr/lucidbrb.sty
%{texmf}/tex/latex/lucidabr/lucidbry.sty
%{texmf}/tex/latex/lucidabr/lucmin.sty
%{texmf}/tex/latex/lucidabr/lucmtime.sty
%{texmf}/tex/latex/lucidabr/ly1enc.def
%{texmf}/tex/latex/lucidabr/ly1hlce.fd
%{texmf}/tex/latex/lucidabr/ly1hlcf.fd
%{texmf}/tex/latex/lucidabr/ly1hlcn.fd
%{texmf}/tex/latex/lucidabr/ly1hlct.fd
%{texmf}/tex/latex/lucidabr/ly1hlcw.fd
%{texmf}/tex/latex/lucidabr/ly1hlh.fd
%{texmf}/tex/latex/lucidabr/ly1hls.fd
%{texmf}/tex/latex/lucidabr/ly1hlst.fd
%{texmf}/tex/latex/lucidabr/ly1hlx.fd
%{texmf}/tex/latex/lucidabr/ly1pcr.fd
%{texmf}/tex/latex/lucidabr/ly1phv.fd
%{texmf}/tex/latex/lucidabr/ly1ptm.fd
%{texmf}/tex/latex/lucidabr/omlhlcm.fd
%{texmf}/tex/latex/lucidabr/omlhlh.fd
%{texmf}/tex/latex/lucidabr/omshlcy.fd
%{texmf}/tex/latex/lucidabr/omshlh.fd
%{texmf}/tex/latex/lucidabr/omxhlcv.fd
%{texmf}/tex/latex/lucidabr/ot1hlce.fd
%{texmf}/tex/latex/lucidabr/ot1hlcf.fd
%{texmf}/tex/latex/lucidabr/ot1hlcn.fd
%{texmf}/tex/latex/lucidabr/ot1hlct.fd
%{texmf}/tex/latex/lucidabr/ot1hlcw.fd
%{texmf}/tex/latex/lucidabr/ot1hlh.fd
%{texmf}/tex/latex/lucidabr/ot1hls.fd
%{texmf}/tex/latex/lucidabr/ot1hlst.fd
%{texmf}/tex/latex/lucidabr/ot1hlx.fd
%{texmf}/tex/latex/lucidabr/t1hlce.fd
%{texmf}/tex/latex/lucidabr/t1hlcf.fd
%{texmf}/tex/latex/lucidabr/t1hlcn.fd
%{texmf}/tex/latex/lucidabr/t1hlct.fd
%{texmf}/tex/latex/lucidabr/t1hlcw.fd
%{texmf}/tex/latex/lucidabr/t1hlh.fd
%{texmf}/tex/latex/lucidabr/t1hls.fd
%{texmf}/tex/latex/lucidabr/t1hlst.fd
%{texmf}/tex/latex/lucidabr/t1hlx.fd
%{texmf}/tex/latex/lucidabr/texnansi.sty
%{texmf}/tex/latex/lucidabr/ts1hlce.fd
%{texmf}/tex/latex/lucidabr/ts1hlcf.fd
%{texmf}/tex/latex/lucidabr/ts1hlcn.fd
%{texmf}/tex/latex/lucidabr/ts1hlct.fd
%{texmf}/tex/latex/lucidabr/ts1hlcw.fd
%{texmf}/tex/latex/lucidabr/ts1hlh.fd
%{texmf}/tex/latex/lucidabr/ts1hls.fd
%{texmf}/tex/latex/lucidabr/ts1hlst.fd
%{texmf}/tex/latex/lucidabr/ts1hlx.fd

%files latex-listings
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/listings
%{texmf}/tex/latex/listings/listings.cfg
%{texmf}/tex/latex/listings/listings.sty
%{texmf}/tex/latex/listings/lstdoc.sty
%{texmf}/tex/latex/listings/lstlang1.sty
%{texmf}/tex/latex/listings/lstlang2.sty
%{texmf}/tex/latex/listings/lstlang3.sty
%{texmf}/tex/latex/listings/lstmisc.sty
%{texmf}/tex/latex/listings/lstpatch.sty

%files latex-labels
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/labels
%{texmf}/tex/latex/labels/labels.sty
%{texmf}/tex/latex/labels/olabels.sty

%files latex-koma-script
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/koma-script
%dir %{texmf}/tex/latex/koma-script
%{texmf}/tex/latex/koma-script/scraddr.sty
%{texmf}/tex/latex/koma-script/scrartcl.cls
%{texmf}/tex/latex/koma-script/scrbook.cls
%{texmf}/tex/latex/koma-script/scrdate.sty
%{texmf}/tex/latex/koma-script/script_l.sty
%{texmf}/tex/latex/koma-script/script_s.sty
%{texmf}/tex/latex/koma-script/script.sty
%{texmf}/tex/latex/koma-script/scrlettr.cls
%{texmf}/tex/latex/koma-script/scrpage2.sty
%{texmf}/tex/latex/koma-script/scrpage.sty
%{texmf}/tex/latex/koma-script/scrreprt.cls
%{texmf}/tex/latex/koma-script/scrtime.sty
%{texmf}/tex/latex/koma-script/typearea.sty

%files latex-jknappen
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/jknappen
%dir %{texmf}/tex/latex/jknappen
%{texmf}/tex/latex/jknappen/greekctr.sty
%{texmf}/tex/latex/jknappen/latin1jk.def
%{texmf}/tex/latex/jknappen/latin2jk.def
%{texmf}/tex/latex/jknappen/latin3jk.def
%{texmf}/tex/latex/jknappen/mathbbol.sty
%{texmf}/tex/latex/jknappen/mathrsfs.sty
%{texmf}/tex/latex/jknappen/ubbold.fd
%{texmf}/tex/latex/jknappen/ursfs.fd

%files latex-hyperref
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/hyperref
%dir %{texmf}/tex/latex/hyperref
%{texmf}/tex/latex/hyperref/backref.sty
%{texmf}/tex/latex/hyperref/hdvipdfm.def
%{texmf}/tex/latex/hyperref/hdvips.def
%{texmf}/tex/latex/hyperref/hdvipson.def
%{texmf}/tex/latex/hyperref/hdviwind.def
%{texmf}/tex/latex/hyperref/hpdftex.def
%{texmf}/tex/latex/hyperref/htex4ht.cfg
%{texmf}/tex/latex/hyperref/htex4ht.def
%{texmf}/tex/latex/hyperref/htexture.def
%{texmf}/tex/latex/hyperref/hvtex.def
%{texmf}/tex/latex/hyperref/hvtexhtm.def
%{texmf}/tex/latex/hyperref/hvtexmrk.def
%{texmf}/tex/latex/hyperref/hycheck.tex
%{texmf}/tex/latex/hyperref/hylatex.ltx
%{texmf}/tex/latex/hyperref/hyperref.sty
%{texmf}/tex/latex/hyperref/hypertex.def
%{texmf}/tex/latex/hyperref/minitoc-hyper.sty
%{texmf}/tex/latex/hyperref/nameref.sty
%{texmf}/tex/latex/hyperref/nohyperref.sty
%{texmf}/tex/latex/hyperref/ntheorem-hyper.sty
%{texmf}/tex/latex/hyperref/pd1enc.def
%{texmf}/tex/latex/hyperref/pdfmark.def
%{texmf}/tex/latex/hyperref/puenc.def
%{texmf}/tex/latex/hyperref/xr-hyper.sty

%files latex-graphics
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/graphics
%dir %{texmf}/tex/latex/graphics
%{texmf}/tex/latex/graphics/color.sty
%{texmf}/tex/latex/graphics/dvipdf.def
%{texmf}/tex/latex/graphics/dvipdfm.def
%{texmf}/tex/latex/graphics/dvips.def
%{texmf}/tex/latex/graphics/dvipsnam.def
%{texmf}/tex/latex/graphics/dvipsone.def
%{texmf}/tex/latex/graphics/dviwin.def
%{texmf}/tex/latex/graphics/emtex.def
%{texmf}/tex/latex/graphics/epsfig.sty
%{texmf}/tex/latex/graphics/graphics.sty
%{texmf}/tex/latex/graphics/graphicx.sty
%{texmf}/tex/latex/graphics/keyval.sty
%{texmf}/tex/latex/graphics/lscape.sty
%{texmf}/tex/latex/graphics/pctex32.def
%{texmf}/tex/latex/graphics/pctexhp.def
%{texmf}/tex/latex/graphics/pctexps.def
%{texmf}/tex/latex/graphics/pctexwin.def
%{texmf}/tex/latex/graphics/pdftex.def
%{texmf}/tex/latex/graphics/pstcol.sty
%{texmf}/tex/latex/graphics/tcidvi.def
%{texmf}/tex/latex/graphics/textures.def
%{texmf}/tex/latex/graphics/trig.sty
%{texmf}/tex/latex/graphics/truetex.def
%{texmf}/tex/latex/graphics/vtex.def

%files latex-g-brief
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/g-brief
%dir %{texmf}/tex/latex/g-brief
%{texmf}/tex/latex/g-brief/g-brief.cls
%{texmf}/tex/latex/g-brief/g-brief.sty

%files latex-fp
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/fp
%{texmf}/tex/latex/fp/defpattern.sty
%{texmf}/tex/latex/fp/fp-addons.sty
%{texmf}/tex/latex/fp/fp-basic.sty
%{texmf}/tex/latex/fp/fp-eqn.sty
%{texmf}/tex/latex/fp/fp-eval.sty
%{texmf}/tex/latex/fp/fp-exp.sty
%{texmf}/tex/latex/fp/fp-pas.sty
%{texmf}/tex/latex/fp/fp-random.sty
%{texmf}/tex/latex/fp/fp-snap.sty
%{texmf}/tex/latex/fp/fp.sty
%{texmf}/tex/latex/fp/fp.tex
%{texmf}/tex/latex/fp/fp-trigo.sty
%{texmf}/tex/latex/fp/fp-upn.sty
%{texmf}/tex/latex/fp/lfp.sty

%files latex-fancyvrb
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/fancyvrb
%dir %{texmf}/tex/latex/fancyvrb
%{texmf}/tex/latex/fancyvrb/fancyvrb.sty
%{texmf}/tex/latex/fancyvrb/fvrb-ex.sty
%{texmf}/tex/latex/fancyvrb/hbaw.sty
%{texmf}/tex/latex/fancyvrb/hcolor.sty

%files latex-fancyheadings
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/fancyhdr
%dir %{texmf}/tex/latex/fancyheadings
%{texmf}/tex/latex/fancyheadings/fancyheadings.sty
%{texmf}/tex/latex/fancyheadings/lastpage209.sty

%files latex-fancyhdr
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/fancyhdr
%{texmf}/tex/latex/fancyhdr/extramarks.sty
%{texmf}/tex/latex/fancyhdr/fancyhdr.sty
%{texmf}/tex/latex/fancyhdr/fixmarks.sty

%files latex-endfloat
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/endfloat
%{texmf}/tex/latex/endfloat/efxmpl.cfg
%{texmf}/tex/latex/endfloat/endfloat.sty

%files latex-eepic
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/eepic
%dir %{texmf}/tex/latex/eepic
%{texmf}/tex/latex/eepic/eepicemu.sty
%{texmf}/tex/latex/eepic/eepic.sty
%{texmf}/tex/latex/eepic/epic.sty

%files latex-dvilj
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/dvilj
%{texmf}/tex/latex/dvilj/cgalbertus.sty
%{texmf}/tex/latex/dvilj/cgantiqueolive.sty
%{texmf}/tex/latex/dvilj/cgcourier.sty
%{texmf}/tex/latex/dvilj/cggothic.sty
%{texmf}/tex/latex/dvilj/cgtimes.sty
%{texmf}/tex/latex/dvilj/cgunivers.sty
%{texmf}/tex/latex/dvilj/graybox.sty
%{texmf}/tex/latex/dvilj/hpfonts.sty

%files latex-dstroke
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/dstroke
%{texmf}/tex/latex/dstroke/dsfont.sty
%{texmf}/tex/latex/dstroke/Udsrom.fd
%{texmf}/tex/latex/dstroke/Udsss.fd

%files latex-draftcopy
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/draftcopy
%{texmf}/tex/latex/draftcopy/draftcopy.sty

%files latex-dinbrief
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/dinbrief
%dir %{texmf}/tex/latex/dinbrief
%{texmf}/tex/latex/dinbrief/dinbrief.cls
%{texmf}/tex/latex/dinbrief/dinbrief.sty

%files latex-cyrillic
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/cyrillic
%dir %{texmf}/tex/latex/cyrillic
%{texmf}/tex/latex/cyrillic/cp1251.def
%{texmf}/tex/latex/cyrillic/cp855.def
%{texmf}/tex/latex/cyrillic/cp866av.def
%{texmf}/tex/latex/cyrillic/cp866.def
%{texmf}/tex/latex/cyrillic/cp866mav.def
%{texmf}/tex/latex/cyrillic/cp866nav.def
%{texmf}/tex/latex/cyrillic/cp866tat.def
%{texmf}/tex/latex/cyrillic/ctt.def
%{texmf}/tex/latex/cyrillic/dbk.def
%{texmf}/tex/latex/cyrillic/iso88595.def
%{texmf}/tex/latex/cyrillic/isoir111.def
%{texmf}/tex/latex/cyrillic/koi8-r.def
%{texmf}/tex/latex/cyrillic/koi8-ru.def
%{texmf}/tex/latex/cyrillic/koi8-u.def
%{texmf}/tex/latex/cyrillic/lcycmdh.fd
%{texmf}/tex/latex/cyrillic/lcycmfib.fd
%{texmf}/tex/latex/cyrillic/lcycmfr.fd
%{texmf}/tex/latex/cyrillic/lcycmr.fd
%{texmf}/tex/latex/cyrillic/lcycmss.fd
%{texmf}/tex/latex/cyrillic/lcycmtt.fd
%{texmf}/tex/latex/cyrillic/lcycmvtt.fd
%{texmf}/tex/latex/cyrillic/lcydefs.tex
%{texmf}/tex/latex/cyrillic/lcyenc.def
%{texmf}/tex/latex/cyrillic/lcylcmss.fd
%{texmf}/tex/latex/cyrillic/lcylcmtt.fd
%{texmf}/tex/latex/cyrillic/lcy.sty
%{texmf}/tex/latex/cyrillic/maccyr.def
%{texmf}/tex/latex/cyrillic/macukr.def
%{texmf}/tex/latex/cyrillic/mik.def
%{texmf}/tex/latex/cyrillic/mls.def
%{texmf}/tex/latex/cyrillic/mnk.def
%{texmf}/tex/latex/cyrillic/mos.def
%{texmf}/tex/latex/cyrillic/ncc.def
%{texmf}/tex/latex/cyrillic/ot2cmdh.fd
%{texmf}/tex/latex/cyrillic/ot2cmfib.fd
%{texmf}/tex/latex/cyrillic/ot2cmfr.fd
%{texmf}/tex/latex/cyrillic/ot2cmr.fd
%{texmf}/tex/latex/cyrillic/ot2cmss.fd
%{texmf}/tex/latex/cyrillic/ot2cmtt.fd
%{texmf}/tex/latex/cyrillic/ot2cmvtt.fd
%{texmf}/tex/latex/cyrillic/ot2enc.def
%{texmf}/tex/latex/cyrillic/ot2lcmss.fd
%{texmf}/tex/latex/cyrillic/ot2lcmtt.fd
%{texmf}/tex/latex/cyrillic/ot2wncyr.fd
%{texmf}/tex/latex/cyrillic/ot2wncyss.fd
%{texmf}/tex/latex/cyrillic/pt154.def
%{texmf}/tex/latex/cyrillic/pt254.def
%{texmf}/tex/latex/cyrillic/t2acmdh.fd
%{texmf}/tex/latex/cyrillic/t2acmfib.fd
%{texmf}/tex/latex/cyrillic/t2acmfr.fd
%{texmf}/tex/latex/cyrillic/t2acmr.fd
%{texmf}/tex/latex/cyrillic/t2acmss.fd
%{texmf}/tex/latex/cyrillic/t2acmtt.fd
%{texmf}/tex/latex/cyrillic/t2acmvtt.fd
%{texmf}/tex/latex/cyrillic/t2aenc.def
%{texmf}/tex/latex/cyrillic/t2alcmss.fd
%{texmf}/tex/latex/cyrillic/t2alcmtt.fd
%{texmf}/tex/latex/cyrillic/t2bcmdh.fd
%{texmf}/tex/latex/cyrillic/t2bcmfib.fd
%{texmf}/tex/latex/cyrillic/t2bcmfr.fd
%{texmf}/tex/latex/cyrillic/t2bcmr.fd
%{texmf}/tex/latex/cyrillic/t2bcmss.fd
%{texmf}/tex/latex/cyrillic/t2bcmtt.fd
%{texmf}/tex/latex/cyrillic/t2bcmvtt.fd
%{texmf}/tex/latex/cyrillic/t2benc.def
%{texmf}/tex/latex/cyrillic/t2blcmss.fd
%{texmf}/tex/latex/cyrillic/t2blcmtt.fd
%{texmf}/tex/latex/cyrillic/t2ccmdh.fd
%{texmf}/tex/latex/cyrillic/t2ccmfib.fd
%{texmf}/tex/latex/cyrillic/t2ccmfr.fd
%{texmf}/tex/latex/cyrillic/t2ccmr.fd
%{texmf}/tex/latex/cyrillic/t2ccmss.fd
%{texmf}/tex/latex/cyrillic/t2ccmtt.fd
%{texmf}/tex/latex/cyrillic/t2ccmvtt.fd
%{texmf}/tex/latex/cyrillic/t2cenc.def
%{texmf}/tex/latex/cyrillic/t2clcmss.fd
%{texmf}/tex/latex/cyrillic/t2clcmtt.fd
%{texmf}/tex/latex/cyrillic/x2cmdh.fd
%{texmf}/tex/latex/cyrillic/x2cmfib.fd
%{texmf}/tex/latex/cyrillic/x2cmfr.fd
%{texmf}/tex/latex/cyrillic/x2cmr.fd
%{texmf}/tex/latex/cyrillic/x2cmss.fd
%{texmf}/tex/latex/cyrillic/x2cmtt.fd
%{texmf}/tex/latex/cyrillic/x2cmvtt.fd
%{texmf}/tex/latex/cyrillic/x2enc.def
%{texmf}/tex/latex/cyrillic/x2lcmss.fd
%{texmf}/tex/latex/cyrillic/x2lcmtt.fd

%files latex-custom-bib
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/custom-bib
%dir %{texmf}/tex/latex/custom-bib
%{texmf}/tex/latex/custom-bib/catalan.mbs
%{texmf}/tex/latex/custom-bib/dansk.mbs
%{texmf}/tex/latex/custom-bib/dutch.mbs
%{texmf}/tex/latex/custom-bib/english.mbs
%{texmf}/tex/latex/custom-bib/esperant.mbs
%{texmf}/tex/latex/custom-bib/finnish.mbs
%{texmf}/tex/latex/custom-bib/french.mbs
%{texmf}/tex/latex/custom-bib/geojour.mbs
%{texmf}/tex/latex/custom-bib/german.mbs
%{texmf}/tex/latex/custom-bib/italian.mbs
%{texmf}/tex/latex/custom-bib/makebst.tex
%{texmf}/tex/latex/custom-bib/merlin.mbs
%{texmf}/tex/latex/custom-bib/norsk.mbs
%{texmf}/tex/latex/custom-bib/photjour.mbs
%{texmf}/tex/latex/custom-bib/physjour.mbs
%{texmf}/tex/latex/custom-bib/polski.mbs
%{texmf}/tex/latex/custom-bib/portuges.mbs
%{texmf}/tex/latex/custom-bib/spanish.mbs
%{texmf}/tex/latex/custom-bib/suppjour.mbs

%files latex-curves
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/curves
%{texmf}/tex/latex/curves/curvesls.sty
%{texmf}/tex/latex/curves/curves.sty

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

%files latex-context
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/context
%{texmf}/tex/latex/context/m-ch-de.sty
%{texmf}/tex/latex/context/m-ch-en.sty
%{texmf}/tex/latex/context/m-ch-nl.sty
%{texmf}/tex/latex/context/m-metapo.sty
%{texmf}/tex/latex/context/m-pictex.sty

%files format-latex
%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/latex.fmt

%files latex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/general
%doc %{texmf}/doc/latex/base
%{_infodir}/latex.info*
%lang(fi) %{_mandir}/fi/man1/latex.1*
%lang(pl) %{_mandir}/pl/man1/latex.1*
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pslatex.1*
%dir %{texmf}/tex/latex/config
%dir %{_datadir}/texmf/tex/latex
%{texmf}/tex/latex/config/color.cfg
%{texmf}/tex/latex/config/draftcopy.cfg
%{texmf}/tex/latex/config/geometry.cfg
%{texmf}/tex/latex/config/graphics.cfg
%{texmf}/tex/latex/config/latex209.cfg
%{texmf}/tex/latex/config/latex.ini
%{texmf}/tex/latex/config/ltxdoc.cfg
%{texmf}/tex/latex/config/ltxguide.cfg
%{texmf}/tex/latex/config/seminar.con
%{texmf}/tex/latex/config/SIunits.cfg
%{texmf}/tex/latex/config/texsys.cfg
%dir %{texmf}/tex/latex/base
%{texmf}/tex/latex/base/alltt.sty
%{texmf}/tex/latex/base/ansinew.def
%{texmf}/tex/latex/base/applemac.def
%{texmf}/tex/latex/base/article.cls
%{texmf}/tex/latex/base/article.sty
%{texmf}/tex/latex/base/ascii.def
%{texmf}/tex/latex/base/bezier.sty
%{texmf}/tex/latex/base/bk10.clo
%{texmf}/tex/latex/base/bk11.clo
%{texmf}/tex/latex/base/bk12.clo
%{texmf}/tex/latex/base/book.cls
%{texmf}/tex/latex/base/book.sty
%{texmf}/tex/latex/base/cp1250.def
%{texmf}/tex/latex/base/cp1252.def
%{texmf}/tex/latex/base/cp437de.def
%{texmf}/tex/latex/base/cp437.def
%{texmf}/tex/latex/base/cp850.def
%{texmf}/tex/latex/base/cp852.def
%{texmf}/tex/latex/base/cp865.def
%{texmf}/tex/latex/base/decmulti.def
%{texmf}/tex/latex/base/docstrip.tex
%{texmf}/tex/latex/base/doc.sty
%{texmf}/tex/latex/base/exscale.sty
%{texmf}/tex/latex/base/fixltx2e.sty
%{texmf}/tex/latex/base/flafter.sty
%{texmf}/tex/latex/base/fleqn.clo
%{texmf}/tex/latex/base/fleqn.sty
%{texmf}/tex/latex/base/fontenc.sty
%{texmf}/tex/latex/base/fontmath.ltx
%{texmf}/tex/latex/base/fonttext.ltx
%{texmf}/tex/latex/base/graphpap.sty
%{texmf}/tex/latex/base/hyphen.ltx
%{texmf}/tex/latex/base/idx.tex
%{texmf}/tex/latex/base/ifthen.sty
%{texmf}/tex/latex/base/inputenc.sty
%{texmf}/tex/latex/base/lablst.tex
%{texmf}/tex/latex/base/latex209.def
%{texmf}/tex/latex/base/latexbug.tex
%{texmf}/tex/latex/base/latex.ltx
%{texmf}/tex/latex/base/latexsym.sty
%{texmf}/tex/latex/base/latin1.def
%{texmf}/tex/latex/base/latin2.def
%{texmf}/tex/latex/base/latin3.def
%{texmf}/tex/latex/base/latin4.def
%{texmf}/tex/latex/base/latin5.def
%{texmf}/tex/latex/base/latin9.def
%{texmf}/tex/latex/base/leqno.clo
%{texmf}/tex/latex/base/leqno.sty
%{texmf}/tex/latex/base/letter.cls
%{texmf}/tex/latex/base/letter.sty
%{texmf}/tex/latex/base/ltnews.cls
%{texmf}/tex/latex/base/ltpatch.ltx
%{texmf}/tex/latex/base/ltxcheck.tex
%{texmf}/tex/latex/base/ltxdoc.cls
%{texmf}/tex/latex/base/ltxguide.cls
%{texmf}/tex/latex/base/makeidx.sty
%{texmf}/tex/latex/base/minimal.cls
%{texmf}/tex/latex/base/newlfont.sty
%{texmf}/tex/latex/base/next.def
%{texmf}/tex/latex/base/nfssfont.tex
%{texmf}/tex/latex/base/oldlfont.sty
%{texmf}/tex/latex/base/omlcmm.fd
%{texmf}/tex/latex/base/omlcmr.fd
%{texmf}/tex/latex/base/omlenc.def
%{texmf}/tex/latex/base/omllcmm.fd
%{texmf}/tex/latex/base/omscmr.fd
%{texmf}/tex/latex/base/omscmsy.fd
%{texmf}/tex/latex/base/omsenc.def
%{texmf}/tex/latex/base/omslcmsy.fd
%{texmf}/tex/latex/base/omxcmex.fd
%{texmf}/tex/latex/base/omxlcmex.fd
%{texmf}/tex/latex/base/openbib.sty
%{texmf}/tex/latex/base/ot1cmdh.fd
%{texmf}/tex/latex/base/ot1cmfib.fd
%{texmf}/tex/latex/base/ot1cmfr.fd
%{texmf}/tex/latex/base/ot1cmr.fd
%{texmf}/tex/latex/base/ot1cmss.fd
%{texmf}/tex/latex/base/ot1cmtt.fd
%{texmf}/tex/latex/base/ot1cmvtt.fd
%{texmf}/tex/latex/base/ot1enc.def
%{texmf}/tex/latex/base/ot1lcmss.fd
%{texmf}/tex/latex/base/ot1lcmtt.fd
%{texmf}/tex/latex/base/ot4enc.def
%{texmf}/tex/latex/base/pict2e.sty
%{texmf}/tex/latex/base/preload.ltx
%{texmf}/tex/latex/base/proc.cls
%{texmf}/tex/latex/base/proc.sty
%{texmf}/tex/latex/base/report.cls
%{texmf}/tex/latex/base/report.sty
%{texmf}/tex/latex/base/sample2e.tex
%{texmf}/tex/latex/base/sfonts.def
%{texmf}/tex/latex/base/shortvrb.sty
%{texmf}/tex/latex/base/showidx.sty
%{texmf}/tex/latex/base/size10.clo
%{texmf}/tex/latex/base/size11.clo
%{texmf}/tex/latex/base/size12.clo
%{texmf}/tex/latex/base/slides.cls
%{texmf}/tex/latex/base/slides.def
%{texmf}/tex/latex/base/slides.sty
%{texmf}/tex/latex/base/small2e.tex
%{texmf}/tex/latex/base/syntonly.sty
%{texmf}/tex/latex/base/t1cmdh.fd
%{texmf}/tex/latex/base/t1cmfib.fd
%{texmf}/tex/latex/base/t1cmfr.fd
%{texmf}/tex/latex/base/t1cmr.fd
%{texmf}/tex/latex/base/t1cmss.fd
%{texmf}/tex/latex/base/t1cmtt.fd
%{texmf}/tex/latex/base/t1cmvtt.fd
%{texmf}/tex/latex/base/t1enc.def
%{texmf}/tex/latex/base/t1enc.sty
%{texmf}/tex/latex/base/t1lcmss.fd
%{texmf}/tex/latex/base/t1lcmtt.fd
%{texmf}/tex/latex/base/testpage.tex
%{texmf}/tex/latex/base/textcomp.sty
%{texmf}/tex/latex/base/tracefnt.sty
%{texmf}/tex/latex/base/ts1cmr.fd
%{texmf}/tex/latex/base/ts1cmss.fd
%{texmf}/tex/latex/base/ts1cmtt.fd
%{texmf}/tex/latex/base/ts1cmvtt.fd
%{texmf}/tex/latex/base/ts1enc.def
%{texmf}/tex/latex/base/ucmr.fd
%{texmf}/tex/latex/base/ucmss.fd
%{texmf}/tex/latex/base/ucmtt.fd
%{texmf}/tex/latex/base/ulasy.fd
%{texmf}/tex/latex/base/ullasy.fd

%files latex-concmath
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/concmath
%{texmf}/tex/latex/concmath/concmath.sty
%{texmf}/tex/latex/concmath/omlccm.fd
%{texmf}/tex/latex/concmath/omlccr.fd
%{texmf}/tex/latex/concmath/omsccr.fd
%{texmf}/tex/latex/concmath/omsccsy.fd
%{texmf}/tex/latex/concmath/omxccex.fd
%{texmf}/tex/latex/concmath/ot1ccr.fd
%{texmf}/tex/latex/concmath/ucca.fd
%{texmf}/tex/latex/concmath/uccb.fd

%files latex-cite
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/cite
%{texmf}/tex/latex/cite/chapterbib.sty
%{texmf}/tex/latex/cite/cite.sty
%{texmf}/tex/latex/cite/drftcite.sty
%{texmf}/tex/latex/cite/overcite.sty

%files latex-ccfonts
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/ccfonts
%dir %{texmf}/tex/latex/ccfonts
%{texmf}/tex/latex/ccfonts/ccfonts.sty
%{texmf}/tex/latex/ccfonts/omlxcm.fd
%{texmf}/tex/latex/ccfonts/omsxcsy.fd
%{texmf}/tex/latex/ccfonts/omxxcex.fd
%{texmf}/tex/latex/ccfonts/t1ccr.fd
%{texmf}/tex/latex/ccfonts/ts1ccr.fd

%files latex-carlisle
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/carlisle
%dir %{texmf}/tex/latex/carlisle
%{texmf}/tex/latex/carlisle/blkarray.sty
%{texmf}/tex/latex/carlisle/colortbl.sty
%{texmf}/tex/latex/carlisle/comma.sty
%{texmf}/tex/latex/carlisle/dotlessj.sty
%{texmf}/tex/latex/carlisle/fix2col.sty
%{texmf}/tex/latex/carlisle/ltxtable.sty
%{texmf}/tex/latex/carlisle/ltxtable.tex
%{texmf}/tex/latex/carlisle/mylatex.ltx
%{texmf}/tex/latex/carlisle/nopageno.sty
%{texmf}/tex/latex/carlisle/plain.sty
%{texmf}/tex/latex/carlisle/pspicture.sty
%{texmf}/tex/latex/carlisle/remreset.sty
%{texmf}/tex/latex/carlisle/scalefnt.sty
%{texmf}/tex/latex/carlisle/textcase.sty
%{texmf}/tex/latex/carlisle/typehtml.sty

%files latex-caption
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/caption
%dir %{texmf}/tex/latex/caption
%{texmf}/tex/latex/caption/caption2.sty
%{texmf}/tex/latex/caption/caption.sty

%files latex-bbm
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/bbm
%{texmf}/tex/latex/bbm/bbm.sty
%{texmf}/tex/latex/bbm/ubbm.fd
%{texmf}/tex/latex/bbm/ubbmss.fd
%{texmf}/tex/latex/bbm/ubbmtt.fd

%files latex-antt
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/antt
%{texmf}/tex/latex/antt/antyktor.sty
%{texmf}/tex/latex/antt/ot1antt.fd
%{texmf}/tex/latex/antt/ot4antt.fd
%{texmf}/tex/latex/antt/qxantt.fd

%files latex-antp
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/antp
%{texmf}/tex/latex/antp/antpolt.sty
%{texmf}/tex/latex/antp/lqxantp.fd
%{texmf}/tex/latex/antp/ot4antp.fd
%{texmf}/tex/latex/antp/qxantp.fd

%files latex-amsmath
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/amsmath
%dir %{texmf}/tex/latex/amsmath
%{texmf}/tex/latex/amsmath/amsbsy.sty
%{texmf}/tex/latex/amsmath/amscd.sty
%{texmf}/tex/latex/amsmath/amsgen.sty
%{texmf}/tex/latex/amsmath/amsmath.sty
%{texmf}/tex/latex/amsmath/amsopn.sty
%{texmf}/tex/latex/amsmath/amstex.sty
%{texmf}/tex/latex/amsmath/amstext.sty
%{texmf}/tex/latex/amsmath/amsxtra.sty

%files latex-amsfonts
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/amsfonts
%{texmf}/tex/latex/amsfonts/amsfonts.sty
%{texmf}/tex/latex/amsfonts/amssymb.sty
%{texmf}/tex/latex/amsfonts/cmmib57.sty
%{texmf}/tex/latex/amsfonts/eucal.sty
%{texmf}/tex/latex/amsfonts/eufrak.sty
%{texmf}/tex/latex/amsfonts/euscript.sty
%{texmf}/tex/latex/amsfonts/ueuex57.fd
%{texmf}/tex/latex/amsfonts/ueuex.fd
%{texmf}/tex/latex/amsfonts/ueuf57.fd
%{texmf}/tex/latex/amsfonts/ueuf.fd
%{texmf}/tex/latex/amsfonts/ueur57.fd
%{texmf}/tex/latex/amsfonts/ueur.fd
%{texmf}/tex/latex/amsfonts/ueus57.fd
%{texmf}/tex/latex/amsfonts/ueus.fd
%{texmf}/tex/latex/amsfonts/umsa57.fd
%{texmf}/tex/latex/amsfonts/umsa.fd
%{texmf}/tex/latex/amsfonts/umsb57.fd
%{texmf}/tex/latex/amsfonts/umsb.fd

%files latex-amscls
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/amscls
%dir %{texmf}/tex/latex/amscls
%{texmf}/tex/latex/amscls/amsart.cls
%{texmf}/tex/latex/amscls/amsbook.cls
%{texmf}/tex/latex/amscls/amsdtx.cls
%{texmf}/tex/latex/amscls/amsldoc.cls
%{texmf}/tex/latex/amscls/amsproc.cls
%{texmf}/tex/latex/amscls/amsthm.sty
%{texmf}/tex/latex/amscls/upref.sty

%files latex-algorith
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/algorith
%{texmf}/tex/latex/algorith/algorithmic.sty
%{texmf}/tex/latex/algorith/algorithm.sty

%files latex-ae
%defattr(644,root,root,755)
%dir %{texmf}/tex/latex/ae
%{texmf}/tex/latex/ae/aecompl.sty
%{texmf}/tex/latex/ae/ae.sty
%{texmf}/tex/latex/ae/omlaer.fd
%{texmf}/tex/latex/ae/omsaer.fd
%{texmf}/tex/latex/ae/ot1aer.fd
%{texmf}/tex/latex/ae/ot1aess.fd
%{texmf}/tex/latex/ae/ot1aett.fd
%{texmf}/tex/latex/ae/ot1laess.fd
%{texmf}/tex/latex/ae/ot1laett.fd
%{texmf}/tex/latex/ae/t1aer.fd
%{texmf}/tex/latex/ae/t1aess.fd
%{texmf}/tex/latex/ae/t1aett.fd
%{texmf}/tex/latex/ae/t1laess.fd
%{texmf}/tex/latex/ae/t1laett.fd

%files eplain
%defattr(644,root,root,755)
# mo¿e texmf/etex do jakiego¶ wspólnego pakietu?
%attr(755,root,root) %{_bindir}/etex
%attr(755,root,root) %{_bindir}/evirtex
%attr(755,root,root) %{_bindir}/einitex
%attr(755,root,root) %{_bindir}/eplain
%{_mandir}/man1/einitex.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{_mandir}/man1/evirtex.1*
%dir %{texmf}/etex
%doc %{texmf}/doc/etex
%doc %{texmf}/doc/eplain
%dir %{texmf}/etex/plain
%dir %{texmf}/etex/plain/base
%{texmf}/etex/plain/base/etexdefs.lib
%{texmf}/etex/plain/base/etex.src
%dir %{texmf}/etex/plain/config
%{texmf}/etex/plain/config/etex.ini
%{texmf}/etex/plain/config/language.def
%{texmf}/tex/eplain
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/etex.efmt
%{_datadir}/texmf/web2c/etex.pool
%{_datadir}/texmf/web2c/etex-pl.pool


%files format-elatex
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/elatex
%{_mandir}/man1/elatex.1*
%dir %{texmf}/etex/latex
%dir %{texmf}/etex/latex/config
%{texmf}/etex/latex/config/elatex.ini
%dir %{texmf}/etex/latex/misc
%{texmf}/etex/latex/misc/etex.sty
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/elatex.efmt

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
%config(noreplace) %verify(not size md5 mtime) %{texmf}/web2c/bplain.fmt

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
%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvips
%attr(755,root,root) %{_bindir}/odvitype

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
