
%define		tetex_ver	beta-20020208
%define		texmf_ver	beta-20020207
%define		texmfsrc_ver	beta-20020207

Summary:	TeX typesetting system and MetaFont font formatter
Summary(de):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr):	Systéme de compostion TeX et formatteur de MetaFontes
Summary(pl):	System sk³adu publikacji TeX oraz formater fontów MetaFont
Summary(pt_BR):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr):	TeX dizgi sistemi ve MetaFont yazýtipi biçimlendiricisi
Name:		tetex
Version:	1.0.7.%(echo %{tetex_ver}|tr -- - _)
Release:	0.1
License:	distributable
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
# Release sources at ftp://sunsite.informatik.rwth-aachen.de/pub/comp/tex/teTeX/1.0/distrib/sources/
Source0:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX-beta/teTeX-src-%{tetex_ver}.tar.gz
Source1:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX-beta/teTeX-texmf-%{texmf_ver}.tar.gz
#Source2:	ftp://ftp.dante.de/tex-archive/systems/unix/teTeX-beta/teTeX-texmfsrc-%{texmfsrc_ver}.tar.gz
Source3:	%{name}-non-english-man-pages.tar.bz2
Source4:	%{name}.cron
Source5:	xdvi.desktop
Source6:	teTeX-hugelatex.cnf
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
URL:		http://www.tug.org/teTeX/
Requires:	tmpwatch
Requires:	dialog
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
Obsoletes:	tetex-texmf-src
Obsoletes:	tetex-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package latex
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(es):	Paquete de macros LaTeX
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makro-pakiet LaTeX
Summary(pt_BR):	Pacote de macros LaTeX
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}
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
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
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
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
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

%package afm
Summary:	afm (Adobe Font Metrics) fonts and utilities
Summary(de):	Fonts und Dienstprogramme für afm (Adobe Font Metrics)
Summary(es):	Fuentes afm (Adobe Font Metrics) y utilitarios relacionados
Summary(fr):	Fontes afm (Adobe Font Metrics) et utilitaires
Summary(pl):	afm (Adobe Font Metrics) czcionki i narzêdzia
Summary(pt_BR):	Fontes afm (Adobe Font Metrics) e utilitários relacionados
Summary(tr):	afm yazýtipleri ve yardýmcý programlarý
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description afm
tetex-afm provides afm2tfm, a converter for PostScript font metric
files. PostScript fonts are accompanied by .afm font metric files
which describe the characteristics of each font. To use PostScript
fonts with TeX, TeX needs .tfm files that contain similar information.
Afm2tfm will convert .afm files to .tfm files.

%description afm -l de
PostScript-Fonts werden (oder sollten) von Font-Metric-Dateien (z.B.
Times-Roman.afm) begleitet, die die Eigenschaften des Fonts (hier:
Times-Roman) beschreiben. Um solche Fonts mit TeX verwenden zu können,
werden TFM-Dateien benötigt, die ähnliche Informationen

%description afm -l es
Fuentes PostScript son (o deberían ser) acompañadas de archivos de
métrica de fuentes como Times Roman. Afm, que describen las
características de la fuente Times-Roman. Para usar estas fuentes con
TeX, necesitamos de archivos TFM que contiene información similar.
Afm2tfm hace esta conversión.

%description afm -l fr
Les fontes PostScript sont (ou devraient être) accompagnées de fontes
métriques comme Times-Roman.afm qui décrivent les caractéristiques des
fontes appelées Times-Roman. pour utiliser ces fontes avec TeX, nous
avons besoin de TFM, des fichiers qui contiennent des informations
similaires. afm2tfm réalise cette conversion.

%description afm -l pl
Fonty PostScriptowe s± (powinny byæ) dostarczane wraz z metrykami
takimi jak np. Times-Roman.afm, opisuj±cymi charakterystykê znaków.
Aby u¿ywaæ takich fontów z TeXem potrzebne s± metryki zrozumia³e dla
TeXa (pliki *.TFM). afm2tfm konwertuje pomiêdzy tymi dwoma rodzajami
metryk.

%description afm -l pt_BR
Fontes PostScript são (ou deveriam ser) acompanhadas por arquivos de
métrica de fontes como Times-Roman.afm, que descrevem as
características da fonte Times-Roman. Para usar tais fontes com o TeX,
precisamos de arquivos TFM que contém informações similares. afm2tfm
faz esta conversão.

%description afm -l tr
PostScript yazýtipleri, yazýtipi ölçüt dosyalarý ile beraber
daðýtýlýrlar. Örneðin Times-Roman.afm, Times-Roman yazýtipinin
karakteristik özelliklerini tanýmlar. Bu türde yazýtiplerini TeX ile
kullanabilmek için, benzer bilgileri taþýyan TFM dosyalarý gerekir.
afm2tfm bu gerekli dönüþümü yapar.

%package ams
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makra dla LaTeX
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description ams
American Mathematics Society macros for plainTeX and LaTeX.

%description ams -l pl
Makra American Mathematics Society do sk³adania publikacji
matematycznych.

%package bibtex
Summary:	LaTeX macro package
Summary(pl):	Dodatkowe makra dla LaTeXa
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
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
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description etex
e-TeX: a 100%-compatible successor to TeX.

%description etex -l pl
e-TeX -- Pierwsza przymiarka do New Typesetting System.

%package omega
Summary:	extended unicode TeX
Summary(pl):	Rozszerzony unicode TeX
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description omega
Omega is extended unicode TeX.

%description omega -l pl
Omega -- TeX ze wsparciem dla Unicode.

%package oxdvi
Summary:	xdvi viewer for Omega
Summary(pl):	Przegl±darka xdvi dla Omegi
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}

%description oxdvi
xdvi viewer for Omega - extended unicode TeX.

%description oxdvi -l pl
Przegl±darka xdvi dla Omegi -- TeXa ze wsparciem dla Unicode.

%package pdftex
Summary:	PDFtex
Summary(pl):	PDFtex
Group:		Applications/Publishing/TeX
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
Requires:	%{name} = %{version}

%description pdftex
TeX generating PDFs instead DVI.

%description pdftex -l pl
PDFTeX generuje pliki PDF na podstawie plików DVI.

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
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
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
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
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
Group(de):	Applikationen/Publizieren/TeX
Group(es):	Aplicaciones/Editoración/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Group(pt_BR):	Aplicações/Editoração/TeX
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
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	òÁÚÒÁÂÏÔËÁ/âÉÂÌÉÏÔÅËÉ
Group(uk):	òÏÚÒÏÂËÁ/â¦ÂÌ¦ÏÔÅËÉ
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

%prep
%setup  -q -n teTeX-src-%{tetex_ver}
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
	-e "s|\.\./\.\./texmf|$RPM_BUILD_ROOT%{_datadir}/texmf|g;" \
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
	texmf=$RPM_BUILD_ROOT%{_datadir}/texmf

#%{__make} -C texk/tetex install \
#	prefix=$RPM_BUILD_ROOT%{_prefix} \
#	bindir=$RPM_BUILD_ROOT%{_bindir} \
#	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
#	libdir=$RPM_BUILD_ROOT%{_libdir} \
#	datadir=$RPM_BUILD_ROOT%{_datadir} \
#	infodir=$RPM_BUILD_ROOT%{_infodir} \
#	includedir=$RPM_BUILD_ROOT%{_includedir} \
#	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
#	texmf=$RPM_BUILD_ROOT%{_datadir}/texmf


#%{__make} -C texk/ps2pkm install \
#	prefix=$RPM_BUILD_ROOT%{_prefix} \
#	bindir=$RPM_BUILD_ROOT%{_bindir} \
#	mandir=$RPM_BUILD_ROOT%{_mandir}/man1 \
#	libdir=$RPM_BUILD_ROOT%{_libdir} \
#	datadir=$RPM_BUILD_ROOT%{_datadir} \
#	infodir=$RPM_BUILD_ROOT%{_infodir} \
#	includedir=$RPM_BUILD_ROOT%{_includedir} \
#	sbindir=$RPM_BUILD_ROOT%{_sbindir} \
#	texmf=$RPM_BUILD_ROOT%{_datadir}/texmf

#install texk/tetex/texconfig $RPM_BUILD_ROOT%{_bindir}

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
	texmf=$RPM_BUILD_ROOT%{_datadir}/texmf

perl -pi \
	-e "s|$RPM_BUILD_ROOT||g;" \
	$RPM_BUILD_ROOT%{_datadir}/texmf/web2c/texmf.cnf
## temporary fix
# prepare conf file to build hugelatex
# (required to build jadetex)
# I don't know how to make it better now :( /klakier
#cat %{SOURCE6} >> $RPM_BUILD_ROOT%{_datadir}/texmf/web2c/texmf.cnf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily/tetex

# temporary fix
#ln -sf libkpathsea.so.3.3.7 $RPM_BUILD_ROOT%{_libdir}/libkpathsea.so

install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers
bzip2 -dc %{SOURCE3} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

# remove all *.dvi ? why ? /wiget
#find $RPM_BUILD_ROOT%{_datadir}/texmf -name \*.dvi -exec rm -f {} \;

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
/sbin/ldconfig
/usr/bin/fmtutil --all >/dev/null 2>&1

[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post latex
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun latex
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post dvips
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun dvips
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post dvilj
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun dvilj
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post afm
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun afm
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post ams
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun ams
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post omega
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun omega
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%post fonts
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun fonts
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kpathsea-devel
/usr/include/kpathsea
/usr/lib/libkpathsea.so
/usr/share/info/kpathsea.info-1.gz
/usr/share/info/kpathsea.info-2.gz
/usr/share/info/kpathsea.info-3.gz
/usr/share/info/kpathsea.info-4.gz
/usr/share/info/kpathsea.info.gz

%files -n kpathsea
%doc /usr/share/texmf/doc/programs/kpathsea.dvi
%doc /usr/share/texmf/doc/programs/kpathsea.pdf
/usr/lib/libkpathsea.so.3.3.7

%files dvips
%doc /usr/share/texmf/doc/programs/dvips.dvi
/usr/bin/dvips
/usr/share/info/dvips.info*
%lang(fi) /usr/share/man/fi/man1/dvips.1*
/usr/share/man/man1/dvips.1*
%dir /usr/share/texmf/dvips

%files xdvi
/usr/share/man/man1/xdvi.1*
/usr/bin/xdvi
/usr/bin/xdvi.bin
/usr/X11R6/share/applnk/Graphics/Viewers/xdvi.desktop
%dir /usr/share/texmf/xdvi
/usr/share/texmf/xdvi/ps2pk.map
/usr/share/texmf/xdvi/XDvi
/usr/share/texmf/xdvi/xdvi.cfg

%files latex
%doc /usr/share/texmf/doc/latex/general
%doc /usr/share/texmf/doc/latex/base
/usr/share/info/latex.info*
%lang(fi) /usr/share/man/fi/man1/latex.1*
%lang(pl) /usr/share/man/pl/man1/latex.1*
/usr/share/man/man1/latex.1*
/usr/bin/latex

%files web2c
/usr/share/info/web2c.info*

%files bibtex
%dir /usr/share/texmf/doc/bibtex
%doc /usr/share/texmf/doc/bibtex/base
%dir /usr/share/texmf/bibtex
%dir /usr/share/texmf/bibtex/bib
/usr/share/texmf/bibtex/bib/base
%dir /usr/share/texmf/bibtex/bst
%doc /usr/share/texmf/bibtex/bib/README
/usr/share/texmf/bibtex/bst/base
/usr/share/texmf/bibtex/bst/misc

%files bibtex-ams
/usr/share/texmf/bibtex/bib/ams
/usr/share/texmf/bibtex/bst/ams

%files bibtex-plbib
/usr/share/texmf/bibtex/bib/plbib
/usr/share/texmf/bibtex/bst/plbib

%files bibtex-germbib
/usr/share/texmf/bibtex/bst/germbib

%files bibtex-koma-script
/usr/share/texmf/bibtex/bst/koma-script

%files bibtex-natbib
/usr/share/texmf/bibtex/bst/natbib

%files bibtex-revtex4
/usr/share/texmf/bibtex/bst/revtex4

%files fonts-adobe
/usr/share/texmf/fonts/afm/adobe
/usr/share/texmf/fonts/tfm/adobe
/usr/share/texmf/fonts/vf/adobe

%files fonts-bitstrea
/usr/share/texmf/fonts/afm/bitstrea
/usr/share/texmf/fonts/tfm/bitstrea
/usr/share/texmf/fonts/vf/bitstrea

%files fonts-antp
%doc /usr/share/texmf/doc/fonts/polish/antp
/usr/share/texmf/fonts/afm/public/antp
/usr/share/texmf/fonts/tfm/public/antp

%files fonts-antt
%doc /usr/share/texmf/doc/fonts/polish/antt
/usr/share/texmf/fonts/afm/public/antt
/usr/share/texmf/fonts/tfm/public/antt

%files fonts-marvosym
%doc /usr/share/texmf/doc/fonts/marvosym
/usr/share/texmf/fonts/afm/public/marvosym
/usr/share/texmf/fonts/tfm/public/marvosym

%files fonts-omega
/usr/share/texmf/fonts/afm/public/omega
/usr/share/texmf/fonts/ofm/public/omega
/usr/share/texmf/fonts/ovf/public/omega
/usr/share/texmf/fonts/ovp/public/omega
/usr/share/texmf/fonts/tfm/public/omega

%files fonts-qfonts
%doc /usr/share/texmf/doc/fonts/polish/qfonts
/usr/share/texmf/fonts/afm/public/qfonts
/usr/share/texmf/fonts/tfm/public/qfonts

%files fonts-xypic
/usr/share/texmf/fonts/afm/public/xypic
/usr/share/texmf/fonts/pfm/public/xypic
/usr/share/texmf/fonts/source/public/xypic
/usr/share/texmf/fonts/tfm/public/xypic

%files fonts-urw
/usr/share/texmf/fonts/afm/urw

%files fonts-yandy
/usr/share/texmf/fonts/afm/yandy
/usr/share/texmf/fonts/source/yandy
/usr/share/texmf/fonts/tfm/yandy
/usr/share/texmf/fonts/vf/yandy

%files fonts-ams
/usr/share/texmf/fonts/source/ams
/usr/share/texmf/fonts/tfm/ams
%doc /usr/share/texmf/doc/fonts/amsfonts

%files fonts-jknappen
/usr/share/texmf/fonts/source/jknappen
/usr/share/texmf/fonts/tfm/jknappen

%files fonts-lh
/usr/share/texmf/fonts/source/lh

%files fonts-bbm
/usr/share/texmf/fonts/source/public/bbm
/usr/share/texmf/fonts/tfm/public/bbm

%files fonts-bbold
/usr/share/texmf/fonts/source/public/bbold
/usr/share/texmf/fonts/tfm/public/bbold

%files fonts-cbgreek
%doc /usr/share/texmf/doc/fonts/cbgreek
/usr/share/texmf/fonts/source/public/cbgreek

%files fonts-cc-pl
%doc /usr/share/texmf/doc/fonts/polish/cc-pl
/usr/share/texmf/fonts/source/public/cc-pl
/usr/share/texmf/fonts/tfm/public/cc-pl

%files fonts-cm
%doc /usr/share/texmf/doc/fonts/cm
/usr/share/texmf/fonts/source/public/cm
/usr/share/texmf/fonts/tfm/public/cm

%files fonts-cmcyr
/usr/share/texmf/fonts/tfm/public/cmcyr
/usr/share/texmf/fonts/vf/public/cmcyr

%files fonts-cm-bold
/usr/share/texmf/fonts/source/public/cm-bold

%files fonts-cmextra
/usr/share/texmf/fonts/source/public/cmextra
/usr/share/texmf/fonts/tfm/public/cmextra

%files fonts-concmath
/usr/share/texmf/fonts/source/public/concmath
/usr/share/texmf/fonts/tfm/public/concmath

%files fonts-concrete
/usr/share/texmf/fonts/source/public/concrete
/usr/share/texmf/fonts/tfm/public/concrete

%files fonts-cs
/usr/share/texmf/fonts/source/public/cs
/usr/share/texmf/fonts/tfm/public/cs

%files fonts-dstroke
%doc /usr/share/texmf/doc/fonts/dstroke
/usr/share/texmf/fonts/source/public/dstroke

%files fonts-ecc
%doc /usr/share/texmf/doc/fonts/ecc
/usr/share/texmf/fonts/source/public/ecc
/usr/share/texmf/fonts/tfm/public/ecc

%files fonts-euxm
/usr/share/texmf/fonts/source/public/euxm
/usr/share/texmf/fonts/tfm/public/euxm

%files fonts-gothic
/usr/share/texmf/fonts/source/public/gothic
/usr/share/texmf/fonts/tfm/public/gothic

%files fonts-latex
/usr/share/texmf/fonts/source/public/latex
/usr/share/texmf/fonts/tfm/public/latex

%files fonts-mflogo
/usr/share/texmf/fonts/source/public/mflogo
/usr/share/texmf/fonts/tfm/public/mflogo

%files fonts-misc
/usr/share/texmf/fonts/source/public/misc
/usr/share/texmf/fonts/tfm/public/misc

%files fonts-pandora
/usr/share/texmf/fonts/source/public/pandora
/usr/share/texmf/fonts/tfm/public/pandora

%files fonts-pl
%doc /usr/share/texmf/doc/fonts/polish/pl
/usr/share/texmf/fonts/source/public/pl
/usr/share/texmf/fonts/afm/public/pl
/usr/share/texmf/fonts/tfm/public/pl

%files fonts-rsfs
/usr/share/texmf/fonts/source/public/rsfs
/usr/share/texmf/fonts/tfm/public/rsfs

%files fonts-stmaryrd
/usr/share/texmf/fonts/source/public/stmaryrd
/usr/share/texmf/fonts/tfm/public/stmaryrd

%files fonts-vnr
/usr/share/texmf/fonts/source/public/vnr
/usr/share/texmf/fonts/tfm/public/vnr

%files fonts-wasy
/usr/share/texmf/fonts/source/public/wasy
/usr/share/texmf/fonts/tfm/public/wasy

%files fonts-bh
/usr/share/texmf/fonts/tfm/bh
/usr/share/texmf/fonts/vf/bh

%files fonts-cg
/usr/share/texmf/fonts/tfm/cg
/usr/share/texmf/fonts/vf/cg

%files fonts-hoekwater
%doc /usr/share/texmf/doc/fonts/hoekwater
/usr/share/texmf/fonts/tfm/hoekwater

%files fonts-monotype
/usr/share/texmf/fonts/tfm/monotype
/usr/share/texmf/fonts/vf/monotype

%files fonts-ae
%doc /usr/share/texmf/doc/fonts/ae
/usr/share/texmf/fonts/tfm/public/ae
/usr/share/texmf/fonts/vf/public/ae

%files fonts-mathpple
/usr/share/texmf/fonts/tfm/public/mathpple
/usr/share/texmf/fonts/vf/public/mathpple

%files fonts-pazo
/usr/share/texmf/fonts/tfm/public/pazo
/usr/share/texmf/fonts/vf/public/pazo

%files fonts-vcm
/usr/share/texmf/fonts/tfm/public/vcm
/usr/share/texmf/fonts/vf/public/vcm

%files fonts-type1-adobe
/usr/share/texmf/fonts/type1/adobe

%files fonts-type1-bitstrea
/usr/share/texmf/fonts/type1/bitstrea

%files fonts-type1-bluesky
%doc /usr/share/texmf/doc/fonts/bluesky
/usr/share/texmf/fonts/type1/bluesky

%files fonts-type1-hoekwater
# hmm, mo¿e jeszcze rozpisaæ?
/usr/share/texmf/fonts/type1/hoekwater

%files fonts-type1-antp
/usr/share/texmf/fonts/type1/public/antp

%files fonts-type1-antt
/usr/share/texmf/fonts/type1/public/antt

%files fonts-type1-belleek
%doc /usr/share/texmf/doc/fonts/belleek
/usr/share/texmf/fonts/type1/public/belleek

%files fonts-type1-cmcyr
/usr/share/texmf/fonts/type1/public/cmcyr

%files fonts-type1-cs
/usr/share/texmf/fonts/type1/public/cs

%files fonts-type1-marvosym
/usr/share/texmf/fonts/type1/public/marvosym

%files fonts-type1-mathpazo
%doc /usr/share/texmf/doc/fonts/mathpazo
/usr/share/texmf/fonts/type1/public/mathpazo

%files fonts-type1-omega
/usr/share/texmf/fonts/type1/public/omega

%files fonts-type1-pl
/usr/share/texmf/fonts/type1/public/pl

%files fonts-type1-qfonts
/usr/share/texmf/fonts/type1/public/qfonts

%files fonts-type1-xypic
/usr/share/texmf/fonts/type1/public/xypic

%files fonts-type1-urw
/usr/share/texmf/fonts/type1/urw

%files makeindex
%doc /usr/share/texmf/doc/makeindex
/usr/share/texmf/makeindex

%files metafont
/usr/share/texmf/metafont

%files matapost
%doc /usr/share/texmf/doc/metapost
%dir /usr/share/texmf/metapost
/usr/share/texmf/metapost/base
/usr/share/texmf/metapost/config
/usr/share/texmf/metapost/mfpic
/usr/share/texmf/metapost/misc
#%files metapost-context
/usr/share/texmf/metapost/context

%files omega
%doc /usr/share/texmf/doc/omega
%dir /usr/share/texmf/omega
/usr/share/texmf/omega/encodings
#%files omega-plain
%dir /usr/share/texmf/omega/plain
/usr/share/texmf/omega/plain/base
/usr/share/texmf/omega/plain/config

%files omega-lambda
%dir /usr/share/texmf/omega/lambda
/usr/share/texmf/omega/lambda/base
/usr/share/texmf/omega/lambda/config
/usr/share/texmf/omega/lambda/misc

%files omega-ocp
%dir /usr/share/texmf/omega/ocp
/usr/share/texmf/omega/ocp/char2uni
/usr/share/texmf/omega/ocp/misc
/usr/share/texmf/omega/ocp/omega
/usr/share/texmf/omega/ocp/uni2char

%files omega-otp
%dir /usr/share/texmf/omega/otp
/usr/share/texmf/omega/otp/char2uni
/usr/share/texmf/omega/otp/misc
/usr/share/texmf/omega/otp/omega
/usr/share/texmf/omega/otp/uni2char

%files pdfetex
%dir /usr/share/texmf/pdfetex
%dir /usr/share/texmf/pdfetex/tex
/usr/share/texmf/pdfetex/tex/config

%files pdfelatex
%dir /usr/share/texmf/pdfetex/latex
/usr/share/texmf/pdfetex/latex/config

%files pdfemex
%dir /usr/share/texmf/pdfetex/mex
/usr/share/texmf/pdfetex/mex/config

%files pdftex
%doc /usr/share/texmf/doc/pdftex
%dir /usr/share/texmf/pdftex
%dir /usr/share/texmf/pdftex/config
/usr/share/texmf/pdftex/config/cmttf.map
/usr/share/texmf/pdftex/config/pdftex.cfg
%dir /usr/share/texmf/pdftex/plain
/usr/share/texmf/pdftex/plain/config
/usr/share/texmf/pdftex/plain/misc

%files pdftex-amstex
%doc /usr/share/texmf/doc/amstex
%dir /usr/share/texmf/pdftex/amstex
/usr/share/texmf/pdftex/amstex/config

%files pdftex-context
# zferyfikowac pliki z fontami
/usr/share/texmf/pdftex/config/context

%files pdflatex
%dir /usr/share/texmf/pdftex/latex
/usr/share/texmf/pdftex/latex/config

%files pdfmex
%dir /usr/share/texmf/pdftex/mex
/usr/share/texmf/pdftex/mex/config

%files pdfplatex
%dir /usr/share/texmf/pdftex/platex
/usr/share/texmf/pdftex/platex/config

%files tex
%dir /usr/share/texmf/tex
%dir /usr/share/texmf/tex/generic
%dir /usr/share/texmf/tex/generic/config
/usr/share/texmf/tex/generic/config/fontmath.cfg
/usr/share/texmf/tex/generic/config/fonttext.cfg
/usr/share/texmf/tex/generic/config/language.dat
/usr/share/texmf/tex/generic/config/preload.cfg

%files amstex
%dir /usr/share/texmf/tex/amstex
/usr/share/texmf/tex/amstex/base
/usr/share/texmf/tex/amstex/config
/usr/share/texmf/web2c/amstex.fmt
/usr/share/texmf/web2c/bamstex.fmt

%files texconfig
/usr/share/texmf/texconfig

%files context
%dir /usr/share/texmf/doc/context
%doc /usr/share/texmf/doc/context/base
%dir /usr/share/texmf/context
%dir /usr/share/texmf/context/config
/usr/share/texmf/context/config/texexec.ini
%dir /usr/share/texmf/context/data
/usr/share/texmf/context/data/conedt.ini
/usr/share/texmf/context/data/cont-cz.tws
/usr/share/texmf/context/data/cont-de.tws
/usr/share/texmf/context/data/cont-en.tws
/usr/share/texmf/context/data/cont-it.tws
/usr/share/texmf/context/data/cont-nl.tws
/usr/share/texmf/context/data/cont-ro.tws
/usr/share/texmf/context/data/type-buy.dat
/usr/share/texmf/context/data/type-tmf.dat
/usr/share/texmf/context/perltk
/usr/share/texmf/tex/generic/context


%dir /usr/share/texmf/tex/context
/usr/share/texmf/tex/context/base
%dir /usr/share/texmf/tex/context/config
/usr/share/texmf/tex/context/config/cont-cz.ini
/usr/share/texmf/tex/context/config/cont-de.ini
/usr/share/texmf/tex/context/config/cont-en.ini
/usr/share/texmf/tex/context/config/cont-it.ini
/usr/share/texmf/tex/context/config/cont-nl.ini
/usr/share/texmf/tex/context/config/cont-ro.ini
/usr/share/texmf/tex/context/config/cont-uk.ini
/usr/share/texmf/tex/context/config/cont-usr.tex
/usr/share/texmf/tex/context/extra
/usr/share/texmf/tex/context/sample
/usr/share/texmf/tex/context/user

%files csplain
%dir /usr/share/texmf/doc/cstex
%doc /usr/share/texmf/doc/cstex/cscorr.tab
%doc /usr/share/texmf/doc/cstex/cs-fonts.doc
%doc /usr/share/texmf/doc/cstex/csplain.doc
%doc /usr/share/texmf/doc/cstex/parpozn.tex
%doc /usr/share/texmf/doc/cstex/README-cspsfont
%doc /usr/share/texmf/doc/cstex/test8z.tex
%doc /usr/share/texmf/doc/cstex/testlat.tex

/usr/share/texmf/tex/csplain

%files cyrplain
%doc /usr/share/texmf/doc/cyrplain
%dir /usr/share/texmf/tex/cyrplain
/usr/share/texmf/tex/cyrplain/base
/usr/share/texmf/tex/cyrplain/config

%files texdoctk
%doc /usr/share/texmf/doc/texdoctk
/usr/share/texmf/texdoctk

%files fontinst
# zferyfikowaæ zawarto¶æ z tym co jest w pakietach z fontami
%doc /usr/share/texmf/doc/fontinst
%dir /usr/share/texmf/tex/fontinst
/usr/share/texmf/tex/fontinst/base

%files doc-Catalogue
/usr/share/texmf/doc/help/Catalogue

%files doc-de-tex-faq
/usr/share/texmf/doc/help/faq/de-tex-faq

%files doc-LaTeX-FAQ-francaise
/usr/share/texmf/doc/help/faq/LaTeX-FAQ-francaise

%files doc-uktug-faq
/usr/share/texmf/doc/help/faq/uktug-faq

%files doc-latex2e-html
/usr/share/texmf/doc/latex/latex2e-html

%files doc
/usr/share/texmf/doc/README
/usr/share/texmf/doc/tetex/teTeX-FAQ
/usr/share/texmf/doc/tetex
/usr/share/texmf/doc/tetex.gif
/usr/share/texmf/doc/tetex.png


%files platex
%doc /usr/share/texmf/doc/latex/platex
%dir /usr/share/texmf/tex/platex
%dir /usr/share/texmf/tex/platex/config
/usr/share/texmf/tex/platex/config/hyphen.cfg
/usr/share/texmf/tex/platex/config/language.dat
/usr/share/texmf/tex/platex/config/platex.ini
# a mo¿e jako¶ osobno to daæ?
%dir /usr/share/texmf/tex/latex/platex
/usr/share/texmf/tex/latex/platex/amigapl.def
/usr/share/texmf/tex/latex/platex/mazovia.def
/usr/share/texmf/tex/latex/platex/omlplcm.fd
/usr/share/texmf/tex/latex/platex/omlplm.fd
/usr/share/texmf/tex/latex/platex/omsplsy.fd
/usr/share/texmf/tex/latex/platex/omxplex.fd
/usr/share/texmf/tex/latex/platex/ot1patch.sty
/usr/share/texmf/tex/latex/platex/ot4ccr.fd
/usr/share/texmf/tex/latex/platex/ot4cmdh.fd
/usr/share/texmf/tex/latex/platex/ot4cmfib.fd
/usr/share/texmf/tex/latex/platex/ot4cmfr.fd
/usr/share/texmf/tex/latex/platex/ot4cmr.fd
/usr/share/texmf/tex/latex/platex/ot4cmss.fd
/usr/share/texmf/tex/latex/platex/ot4cmtt.fd
/usr/share/texmf/tex/latex/platex/plprefix.sty
/usr/share/texmf/tex/latex/platex/polski.sty
/usr/share/texmf/tex/latex/platex/qxenc.def

%files plain-misc
%dir /usr/share/texmf/tex/plain/misc
/usr/share/texmf/tex/plain/misc/arrow.tex
/usr/share/texmf/tex/plain/misc/btxmac.tex
/usr/share/texmf/tex/plain/misc/fontchart.tex
/usr/share/texmf/tex/plain/misc/idxmac.tex
/usr/share/texmf/tex/plain/misc/list.tex
/usr/share/texmf/tex/plain/misc/llist.tex
/usr/share/texmf/tex/plain/misc/mimulcol.tex
/usr/share/texmf/tex/plain/misc/mproof.tex
/usr/share/texmf/tex/plain/misc/scrload.tex
/usr/share/texmf/tex/plain/misc/verbatim.tex
/usr/share/texmf/tex/plain/misc/wasyfont.tex
/usr/share/texmf/tex/plain/misc/wlist.tex
/usr/share/texmf/tex/plain/misc/xepsf.tex

%files plain-plnfss
%dir /usr/share/texmf/tex/plain/plnfss
/usr/share/texmf/tex/plain/plnfss/ams.pfd
/usr/share/texmf/tex/plain/plnfss/il2cmr.pfd
/usr/share/texmf/tex/plain/plnfss/MIKmathf.tex
/usr/share/texmf/tex/plain/plnfss/ot1cmr.pfd
/usr/share/texmf/tex/plain/plnfss/plnfss.tex
/usr/share/texmf/tex/plain/plnfss/t5cmr.pfd
/usr/share/texmf/tex/plain/plnfss/t5vcmr.pfd

%files plain-mathtime
%doc /usr/share/texmf/doc/latex/mathtime
%dir /usr/share/texmf/tex/plain/mathtime
/usr/share/texmf/tex/plain/mathtime/ansiacce.tex
/usr/share/texmf/tex/plain/mathtime/chironmt.tex
/usr/share/texmf/tex/plain/mathtime/dcaccent.tex
/usr/share/texmf/tex/plain/mathtime/encodean.tex
/usr/share/texmf/tex/plain/mathtime/encodese.tex
/usr/share/texmf/tex/plain/mathtime/encode.tex
/usr/share/texmf/tex/plain/mathtime/encodetx.tex
/usr/share/texmf/tex/plain/mathtime/mtextra.tex
/usr/share/texmf/tex/plain/mathtime/mtmacs.tex
/usr/share/texmf/tex/plain/mathtime/mtplain.tex
/usr/share/texmf/tex/plain/mathtime/mtplainx.tex
/usr/share/texmf/tex/plain/mathtime/mtplus.tex
/usr/share/texmf/tex/plain/mathtime/plain-mt.tex
/usr/share/texmf/tex/plain/mathtime/stanacce.tex
/usr/share/texmf/tex/plain/mathtime/texnansi.tex

%files plain-dvips
/usr/share/texmf/tex/plain/dvips
/usr/share/texmf/tex/plain/dvips/blackdvi.tex
/usr/share/texmf/tex/plain/dvips/colordvi.tex
/usr/share/texmf/tex/plain/dvips/dvipsmac.tex
/usr/share/texmf/tex/plain/dvips/epsf.tex
/usr/share/texmf/tex/plain/dvips/rotate.tex
/usr/share/texmf/tex/plain/dvips/rotsample.tex

%files plain
%dir /usr/share/texmf/tex/plain/config
# bplain tu czy mo¿e gdzie¶ indziej?
/usr/share/texmf/tex/plain/config/bplain.ini
/usr/share/texmf/tex/plain/config/tex.ini
%dir /usr/share/texmf/tex/plain/base
/usr/share/texmf/tex/plain/base/gkpmac.tex
/usr/share/texmf/tex/plain/base/letter.tex
/usr/share/texmf/tex/plain/base/logmac.tex
/usr/share/texmf/tex/plain/base/manmac.tex
/usr/share/texmf/tex/plain/base/mftmac.tex
/usr/share/texmf/tex/plain/base/mptmac.tex
/usr/share/texmf/tex/plain/base/picmac.tex
/usr/share/texmf/tex/plain/base/plain.tex
/usr/share/texmf/tex/plain/base/story.tex
/usr/share/texmf/tex/plain/base/testfont.tex
/usr/share/texmf/tex/plain/base/webmac.tex
/usr/share/texmf/web2c/bplain.fmt

%files plain-amsfonts
%dir /usr/share/texmf/tex/plain
/usr/share/texmf/tex/plain/amsfonts
/usr/share/texmf/tex/plain/amsfonts/amssym.def
/usr/share/texmf/tex/plain/amsfonts/amssym.tex
/usr/share/texmf/tex/plain/amsfonts/cyracc.def

%files mex
%doc /usr/share/texmf/doc/polish/mex
%dir /usr/share/texmf/tex/mex
/usr/share/texmf/tex/mex/base
/usr/share/texmf/tex/mex/base/mex1.tex
/usr/share/texmf/tex/mex/base/mex2.tex
/usr/share/texmf/tex/mex/base/mex.tex
%dir /usr/share/texmf/tex/mex/config
/usr/share/texmf/tex/mex/config/mexconf.tex
/usr/share/texmf/tex/mex/config/mex.ini

%files latex-wasysym
%doc /usr/share/texmf/doc/latex/wasysym
%dir /usr/share/texmf/tex/latex/wasysym
/usr/share/texmf/tex/latex/wasysym/uwasy.fd
/usr/share/texmf/tex/latex/wasysym/wasysym.sty

%files latex-vnr
%dir /usr/share/texmf/tex/latex/vnr
/usr/share/texmf/tex/latex/vnr/t5cmdh.fd
/usr/share/texmf/tex/latex/vnr/t5cmfib.fd
/usr/share/texmf/tex/latex/vnr/t5cmfr.fd
/usr/share/texmf/tex/latex/vnr/t5cmr.fd
/usr/share/texmf/tex/latex/vnr/t5cmss.fd
/usr/share/texmf/tex/latex/vnr/t5cmtt.fd
/usr/share/texmf/tex/latex/vnr/t5cmvtt.fd

%files latex-vnps
%dir /usr/share/texmf/tex/latex/vnps
/usr/share/texmf/tex/latex/vnps/t5bch.fd
/usr/share/texmf/tex/latex/vnps/t5pag.fd
/usr/share/texmf/tex/latex/vnps/t5pbk.fd
/usr/share/texmf/tex/latex/vnps/t5pcr.fd
/usr/share/texmf/tex/latex/vnps/t5phv.fd
/usr/share/texmf/tex/latex/vnps/t5pnc.fd
/usr/share/texmf/tex/latex/vnps/t5ppl.fd
/usr/share/texmf/tex/latex/vnps/t5ptm.fd
/usr/share/texmf/tex/latex/vnps/t5put.fd
/usr/share/texmf/tex/latex/vnps/t5vcmdh.fd
/usr/share/texmf/tex/latex/vnps/t5vcmfib.fd
/usr/share/texmf/tex/latex/vnps/t5vcmfr.fd
/usr/share/texmf/tex/latex/vnps/t5vcmr.fd
/usr/share/texmf/tex/latex/vnps/t5vcmss.fd
/usr/share/texmf/tex/latex/vnps/t5vcmtt.fd
/usr/share/texmf/tex/latex/vnps/t5vcmvtt.fd

%files latex-units
%doc /usr/share/texmf/doc/latex/units
%dir /usr/share/texmf/tex/latex/units
/usr/share/texmf/tex/latex/units/nicefrac.sty
/usr/share/texmf/tex/latex/units/units.sty

%files latex-umlaute
%dir /usr/share/texmf/tex/latex/umlaute
/usr/share/texmf/tex/latex/umlaute/atari.def
/usr/share/texmf/tex/latex/umlaute/isolatin.def
/usr/share/texmf/tex/latex/umlaute/mac.def
/usr/share/texmf/tex/latex/umlaute/pc850.def
/usr/share/texmf/tex/latex/umlaute/roman8.def
/usr/share/texmf/tex/latex/umlaute/umlaute.sty
/usr/share/texmf/tex/latex/umlaute/umlaut.sty

%files latex-tools
%doc /usr/share/texmf/doc/latex/tools
%dir /usr/share/texmf/tex/latex/tools
/usr/share/texmf/tex/latex/tools/afterpage.sty
/usr/share/texmf/tex/latex/tools/array.sty
/usr/share/texmf/tex/latex/tools/bm.sty
/usr/share/texmf/tex/latex/tools/calc.sty
/usr/share/texmf/tex/latex/tools/dcolumn.sty
/usr/share/texmf/tex/latex/tools/delarray.sty
/usr/share/texmf/tex/latex/tools/enumerate.sty
/usr/share/texmf/tex/latex/tools/e.tex
/usr/share/texmf/tex/latex/tools/fontsmpl.sty
/usr/share/texmf/tex/latex/tools/fontsmpl.tex
/usr/share/texmf/tex/latex/tools/ftnright.sty
/usr/share/texmf/tex/latex/tools/hhline.sty
/usr/share/texmf/tex/latex/tools/h.tex
/usr/share/texmf/tex/latex/tools/indentfirst.sty
/usr/share/texmf/tex/latex/tools/layout.sty
/usr/share/texmf/tex/latex/tools/longtable.sty
/usr/share/texmf/tex/latex/tools/multicol.sty
/usr/share/texmf/tex/latex/tools/q.tex
/usr/share/texmf/tex/latex/tools/rawfonts.sty
/usr/share/texmf/tex/latex/tools/r.tex
/usr/share/texmf/tex/latex/tools/showkeys.sty
/usr/share/texmf/tex/latex/tools/somedefs.sty
/usr/share/texmf/tex/latex/tools/s.tex
/usr/share/texmf/tex/latex/tools/tabularx.sty
/usr/share/texmf/tex/latex/tools/.tex
/usr/share/texmf/tex/latex/tools/thb.sty
/usr/share/texmf/tex/latex/tools/thcb.sty
/usr/share/texmf/tex/latex/tools/thc.sty
/usr/share/texmf/tex/latex/tools/theorem.sty
/usr/share/texmf/tex/latex/tools/thmb.sty
/usr/share/texmf/tex/latex/tools/thm.sty
/usr/share/texmf/tex/latex/tools/thp.sty
/usr/share/texmf/tex/latex/tools/trace.sty
/usr/share/texmf/tex/latex/tools/varioref.sty
/usr/share/texmf/tex/latex/tools/verbatim.sty
/usr/share/texmf/tex/latex/tools/verbtest.tex
/usr/share/texmf/tex/latex/tools/xr.sty
/usr/share/texmf/tex/latex/tools/xspace.sty
/usr/share/texmf/tex/latex/tools/x.tex

%files latex-titlesec
%dir /usr/share/texmf/tex/latex/titlesec
/usr/share/texmf/tex/latex/titlesec/block.tss
/usr/share/texmf/tex/latex/titlesec/drop.tss
/usr/share/texmf/tex/latex/titlesec/frame.tss
/usr/share/texmf/tex/latex/titlesec/leftmargin.tss
/usr/share/texmf/tex/latex/titlesec/margin.tss
/usr/share/texmf/tex/latex/titlesec/page.tsk
/usr/share/texmf/tex/latex/titlesec/rightmargin.tss
/usr/share/texmf/tex/latex/titlesec/titlesec.new
/usr/share/texmf/tex/latex/titlesec/titlesec.sty
/usr/share/texmf/tex/latex/titlesec/titletoc.sty
/usr/share/texmf/tex/latex/titlesec/wrap.tss

%files latex-t2
/usr/share/texmf/tex/latex/t2
/usr/share/texmf/tex/latex/t2/citehack.sty
/usr/share/texmf/tex/latex/t2/mathtext.sty
/usr/share/texmf/tex/latex/t2/misccorr.sty

%files latex-SIunits
%doc /usr/share/texmf/doc/latex/SIunits
%dir /usr/share/texmf/tex/latex/SIunits
/usr/share/texmf/tex/latex/SIunits/binary.sty
/usr/share/texmf/tex/latex/SIunits/SIunits.sty

%files latex-seminar
%doc /usr/share/texmf/doc/latex/seminar
%dir /usr/share/texmf/tex/latex/seminar
/usr/share/texmf/tex/latex/seminar/2up.sty
/usr/share/texmf/tex/latex/seminar/2up.tex
/usr/share/texmf/tex/latex/seminar/npsfont.sty
/usr/share/texmf/tex/latex/seminar/sem-a4.sty
/usr/share/texmf/tex/latex/seminar/semcolor.sty
/usr/share/texmf/tex/latex/seminar/semhelv.sty
/usr/share/texmf/tex/latex/seminar/seminar.bg2
/usr/share/texmf/tex/latex/seminar/seminar.bug
/usr/share/texmf/tex/latex/seminar/seminar.cls
/usr/share/texmf/tex/latex/seminar/seminar.sty
/usr/share/texmf/tex/latex/seminar/semlayer.sty
/usr/share/texmf/tex/latex/seminar/semlcmss.sty
/usr/share/texmf/tex/latex/seminar/sem-page.sty
/usr/share/texmf/tex/latex/seminar/semrot.sty
/usr/share/texmf/tex/latex/seminar/slidesec.sty
/usr/share/texmf/tex/latex/seminar/xcomment.sty

%files latex-revtex4
%doc /usr/share/texmf/doc/latex/revtex4
/usr/share/texmf/tex/latex/revtex4
/usr/share/texmf/tex/latex/revtex4/10pt.rtx
/usr/share/texmf/tex/latex/revtex4/11pt.rtx
/usr/share/texmf/tex/latex/revtex4/12pt.rtx
/usr/share/texmf/tex/latex/revtex4/aps.rtx
/usr/share/texmf/tex/latex/revtex4/revsymb.sty
/usr/share/texmf/tex/latex/revtex4/revtex4.cls
/usr/share/texmf/tex/latex/revtex4/rmp.rtx

%files latex-qfonts
%dir /usr/share/texmf/tex/latex/qfonts
/usr/share/texmf/tex/latex/qfonts/ot1qbk.fd
/usr/share/texmf/tex/latex/qfonts/ot1qcr.fd
/usr/share/texmf/tex/latex/qfonts/ot1qhv.fd
/usr/share/texmf/tex/latex/qfonts/ot1qpl.fd
/usr/share/texmf/tex/latex/qfonts/ot1qtm.fd
/usr/share/texmf/tex/latex/qfonts/ot1qzc.fd
/usr/share/texmf/tex/latex/qfonts/ot4qbk.fd
/usr/share/texmf/tex/latex/qfonts/ot4qcr.fd
/usr/share/texmf/tex/latex/qfonts/ot4qhv.fd
/usr/share/texmf/tex/latex/qfonts/ot4qpl.fd
/usr/share/texmf/tex/latex/qfonts/ot4qtm.fd
/usr/share/texmf/tex/latex/qfonts/ot4qzc.fd
/usr/share/texmf/tex/latex/qfonts/qbookman.sty
/usr/share/texmf/tex/latex/qfonts/qcourier.sty
/usr/share/texmf/tex/latex/qfonts/qpalatin.sty
/usr/share/texmf/tex/latex/qfonts/qswiss.sty
/usr/share/texmf/tex/latex/qfonts/qtimes.sty
/usr/share/texmf/tex/latex/qfonts/qxqbk.fd
/usr/share/texmf/tex/latex/qfonts/qxqcr.fd
/usr/share/texmf/tex/latex/qfonts/qxqhv.fd
/usr/share/texmf/tex/latex/qfonts/qxqpl.fd
/usr/share/texmf/tex/latex/qfonts/qxqtm.fd
/usr/share/texmf/tex/latex/qfonts/qxqzc.fd
/usr/share/texmf/tex/latex/qfonts/qzapfcha.sty

%files latex-psnfss
%dir /usr/share/texmf/tex/latex/psnfss
/usr/share/texmf/tex/latex/psnfss/8rbch.fd
/usr/share/texmf/tex/latex/psnfss/8rpag.fd
/usr/share/texmf/tex/latex/psnfss/8rpbk.fd
/usr/share/texmf/tex/latex/psnfss/8rpcr.fd
/usr/share/texmf/tex/latex/psnfss/8rphv.fd
/usr/share/texmf/tex/latex/psnfss/8rpnc.fd
/usr/share/texmf/tex/latex/psnfss/8rppl.fd
/usr/share/texmf/tex/latex/psnfss/8rptm.fd
/usr/share/texmf/tex/latex/psnfss/8rput.fd
/usr/share/texmf/tex/latex/psnfss/8rpzc.fd
/usr/share/texmf/tex/latex/psnfss/8r.sty
/usr/share/texmf/tex/latex/psnfss/avant.sty
/usr/share/texmf/tex/latex/psnfss/bookman.sty
/usr/share/texmf/tex/latex/psnfss/chancery.sty
/usr/share/texmf/tex/latex/psnfss/charter.sty
/usr/share/texmf/tex/latex/psnfss/courier.sty
/usr/share/texmf/tex/latex/psnfss/helvet.sty
/usr/share/texmf/tex/latex/psnfss/mathpazo.sty
/usr/share/texmf/tex/latex/psnfss/mathpple.sty
/usr/share/texmf/tex/latex/psnfss/mathptm.sty
/usr/share/texmf/tex/latex/psnfss/mathptmx.sty
/usr/share/texmf/tex/latex/psnfss/newcent.sty
/usr/share/texmf/tex/latex/psnfss/omlbch.fd
/usr/share/texmf/tex/latex/psnfss/omlpag.fd
/usr/share/texmf/tex/latex/psnfss/omlpbk.fd
/usr/share/texmf/tex/latex/psnfss/omlpcr.fd
/usr/share/texmf/tex/latex/psnfss/omlphv.fd
/usr/share/texmf/tex/latex/psnfss/omlpnc.fd
/usr/share/texmf/tex/latex/psnfss/omlppl.fd
/usr/share/texmf/tex/latex/psnfss/omlptmcm.fd
/usr/share/texmf/tex/latex/psnfss/omlptm.fd
/usr/share/texmf/tex/latex/psnfss/omlput.fd
/usr/share/texmf/tex/latex/psnfss/omlpzc.fd
/usr/share/texmf/tex/latex/psnfss/omlzplm.fd
/usr/share/texmf/tex/latex/psnfss/omlzpple.fd
/usr/share/texmf/tex/latex/psnfss/omlztmcm.fd
/usr/share/texmf/tex/latex/psnfss/omsbch.fd
/usr/share/texmf/tex/latex/psnfss/omspag.fd
/usr/share/texmf/tex/latex/psnfss/omspbk.fd
/usr/share/texmf/tex/latex/psnfss/omspcr.fd
/usr/share/texmf/tex/latex/psnfss/omsphv.fd
/usr/share/texmf/tex/latex/psnfss/omspnc.fd
/usr/share/texmf/tex/latex/psnfss/omsppl.fd
/usr/share/texmf/tex/latex/psnfss/omsptm.fd
/usr/share/texmf/tex/latex/psnfss/omsput.fd
/usr/share/texmf/tex/latex/psnfss/omspzccm.fd
/usr/share/texmf/tex/latex/psnfss/omspzc.fd
/usr/share/texmf/tex/latex/psnfss/omszplm.fd
/usr/share/texmf/tex/latex/psnfss/omszpple.fd
/usr/share/texmf/tex/latex/psnfss/omsztmcm.fd
/usr/share/texmf/tex/latex/psnfss/omxpsycm.fd
/usr/share/texmf/tex/latex/psnfss/omxzplm.fd
/usr/share/texmf/tex/latex/psnfss/omxzpple.fd
/usr/share/texmf/tex/latex/psnfss/omxztmcm.fd
/usr/share/texmf/tex/latex/psnfss/ot1bch.fd
/usr/share/texmf/tex/latex/psnfss/ot1fplmbb.fd
/usr/share/texmf/tex/latex/psnfss/ot1pag.fd
/usr/share/texmf/tex/latex/psnfss/ot1pbk.fd
/usr/share/texmf/tex/latex/psnfss/ot1pcr.fd
/usr/share/texmf/tex/latex/psnfss/ot1phv.fd
/usr/share/texmf/tex/latex/psnfss/ot1pnc.fd
/usr/share/texmf/tex/latex/psnfss/ot1ppl.fd
/usr/share/texmf/tex/latex/psnfss/ot1ptmcm.fd
/usr/share/texmf/tex/latex/psnfss/ot1ptm.fd
/usr/share/texmf/tex/latex/psnfss/ot1put.fd
/usr/share/texmf/tex/latex/psnfss/ot1pzc.fd
/usr/share/texmf/tex/latex/psnfss/ot1zplm.fd
/usr/share/texmf/tex/latex/psnfss/ot1zpple.fd
/usr/share/texmf/tex/latex/psnfss/ot1ztmcm.fd
/usr/share/texmf/tex/latex/psnfss/palatino.sty
/usr/share/texmf/tex/latex/psnfss/pifont.sty
/usr/share/texmf/tex/latex/psnfss/t1bch.fd
/usr/share/texmf/tex/latex/psnfss/t1fplmbb.fd
/usr/share/texmf/tex/latex/psnfss/t1pag.fd
/usr/share/texmf/tex/latex/psnfss/t1pbk.fd
/usr/share/texmf/tex/latex/psnfss/t1pcr.fd
/usr/share/texmf/tex/latex/psnfss/t1phv.fd
/usr/share/texmf/tex/latex/psnfss/t1pnc.fd
/usr/share/texmf/tex/latex/psnfss/t1ppl.fd
/usr/share/texmf/tex/latex/psnfss/t1ptm.fd
/usr/share/texmf/tex/latex/psnfss/t1put.fd
/usr/share/texmf/tex/latex/psnfss/t1pzc.fd
/usr/share/texmf/tex/latex/psnfss/times.sty
/usr/share/texmf/tex/latex/psnfss/ts1bch.fd
/usr/share/texmf/tex/latex/psnfss/ts1pag.fd
/usr/share/texmf/tex/latex/psnfss/ts1pbk.fd
/usr/share/texmf/tex/latex/psnfss/ts1pcr.fd
/usr/share/texmf/tex/latex/psnfss/ts1phv.fd
/usr/share/texmf/tex/latex/psnfss/ts1pnc.fd
/usr/share/texmf/tex/latex/psnfss/ts1ppl.fd
/usr/share/texmf/tex/latex/psnfss/ts1ptm.fd
/usr/share/texmf/tex/latex/psnfss/ts1put.fd
/usr/share/texmf/tex/latex/psnfss/ts1pzc.fd
/usr/share/texmf/tex/latex/psnfss/ufplm.fd
/usr/share/texmf/tex/latex/psnfss/upsy.fd
/usr/share/texmf/tex/latex/psnfss/upzd.fd
/usr/share/texmf/tex/latex/psnfss/utopia.sty

%files latex-pb-diagram
%doc /usr/share/texmf/doc/latex/pb-diagram
%dir /usr/share/texmf/tex/latex/pb-diagram
/usr/share/texmf/tex/latex/pb-diagram/lamsarrow.sty
/usr/share/texmf/tex/latex/pb-diagram/pb-diagram.sty
/usr/share/texmf/tex/latex/pb-diagram/pb-lams.sty
/usr/share/texmf/tex/latex/pb-diagram/pb-xy.sty

%files latex-palatcm
%dir /usr/share/texmf/tex/latex/palatcm
/usr/share/texmf/tex/latex/palatcm/omlpplcm.fd
/usr/share/texmf/tex/latex/palatcm/omspplcm.fd
/usr/share/texmf/tex/latex/palatcm/omxpplcm.fd
/usr/share/texmf/tex/latex/palatcm/ot1pplcm.fd
/usr/share/texmf/tex/latex/palatcm/palatcm.sty

%files latex-oberdiek
%doc /usr/share/texmf/doc/latex/oberdiek
%dir /usr/share/texmf/tex/latex/oberdiek
/usr/share/texmf/tex/latex/oberdiek/alphalph.sty
/usr/share/texmf/tex/latex/oberdiek/chemarr.sty
/usr/share/texmf/tex/latex/oberdiek/dvipscol.sty
/usr/share/texmf/tex/latex/oberdiek/engord.sty
/usr/share/texmf/tex/latex/oberdiek/epstopdf.sty
/usr/share/texmf/tex/latex/oberdiek/hypbmsec.sty
/usr/share/texmf/tex/latex/oberdiek/hypcap.sty
/usr/share/texmf/tex/latex/oberdiek/ifpdf.sty
/usr/share/texmf/tex/latex/oberdiek/ifvtex.sty
/usr/share/texmf/tex/latex/oberdiek/pagesel.sty
/usr/share/texmf/tex/latex/oberdiek/pdfcolmk.sty
/usr/share/texmf/tex/latex/oberdiek/pdfcrypt.sty
/usr/share/texmf/tex/latex/oberdiek/pdflscape.sty
/usr/share/texmf/tex/latex/oberdiek/refcount.sty
/usr/share/texmf/tex/latex/oberdiek/settobox.sty
/usr/share/texmf/tex/latex/oberdiek/twoopt.sty
/usr/share/texmf/tex/latex/oberdiek/vpe.sty

%files latex-ntgclass
%doc /usr/share/texmf/doc/latex/ntgclass
%dir /usr/share/texmf/tex/latex/ntgclass
/usr/share/texmf/tex/latex/ntgclass/a4.sty
/usr/share/texmf/tex/latex/ntgclass/artikel1.cls
/usr/share/texmf/tex/latex/ntgclass/artikel2.cls
/usr/share/texmf/tex/latex/ntgclass/artikel3.cls
/usr/share/texmf/tex/latex/ntgclass/boek3.cls
/usr/share/texmf/tex/latex/ntgclass/boek.cls
/usr/share/texmf/tex/latex/ntgclass/brief.cls
/usr/share/texmf/tex/latex/ntgclass/ntg10.clo
/usr/share/texmf/tex/latex/ntgclass/ntg11.clo
/usr/share/texmf/tex/latex/ntgclass/ntg12.clo
/usr/share/texmf/tex/latex/ntgclass/rapport1.cls
/usr/share/texmf/tex/latex/ntgclass/rapport3.cls

%files latex-natbib
%doc /usr/share/texmf/doc/latex/natbib
%dir /usr/share/texmf/tex/latex/natbib
/usr/share/texmf/tex/latex/natbib/bibentry.sty
/usr/share/texmf/tex/latex/natbib/natbib.sty

%files latex-mwcls
%doc /usr/share/texmf/doc/latex/mwcls
%dir /usr/share/texmf/tex/latex/mwcls
/usr/share/texmf/tex/latex/mwcls/mw10.clo
/usr/share/texmf/tex/latex/mwcls/mw11.clo
/usr/share/texmf/tex/latex/mwcls/mw12.clo
/usr/share/texmf/tex/latex/mwcls/mwart.cls
/usr/share/texmf/tex/latex/mwcls/mwbk10.clo
/usr/share/texmf/tex/latex/mwcls/mwbk11.clo
/usr/share/texmf/tex/latex/mwcls/mwbk12.clo
/usr/share/texmf/tex/latex/mwcls/mwbk.cls
/usr/share/texmf/tex/latex/mwcls/mwrep.cls

%files latex-multirow
%dir /usr/share/texmf/tex/latex/multirow
/usr/share/texmf/tex/latex/multirow/bigdelim.sty
/usr/share/texmf/tex/latex/multirow/bigstrut.sty
/usr/share/texmf/tex/latex/multirow/multirow.sty

%files latex-ms
%doc /usr/share/texmf/doc/latex/ms
%dir /usr/share/texmf/tex/latex/ms
/usr/share/texmf/tex/latex/ms/count1to.sty
/usr/share/texmf/tex/latex/ms/eso-pic.sty
/usr/share/texmf/tex/latex/ms/everysel.sty
/usr/share/texmf/tex/latex/ms/everyshi.sty
/usr/share/texmf/tex/latex/ms/multitoc.sty
/usr/share/texmf/tex/latex/ms/prelim2e.sty
/usr/share/texmf/tex/latex/ms/ragged2e.sty

%files latex-mltex
%doc /usr/share/texmf/doc/latex/mltex
%dir /usr/share/texmf/tex/latex/mltex
/usr/share/texmf/tex/latex/mltex/lo1enc.def
/usr/share/texmf/tex/latex/mltex/mlltxchg.def
/usr/share/texmf/tex/latex/mltex/mltex.sty

%files latex-misc
%doc /usr/share/texmf/doc/latex/tocbibind
%doc /usr/share/texmf/doc/latex/xtab
%doc /usr/share/texmf/doc/latex/yfonts
%doc /usr/share/texmf/doc/latex/supertab
%doc /usr/share/texmf/doc/latex/sidecap
%doc /usr/share/texmf/doc/latex/showlabels
%doc /usr/share/texmf/doc/latex/scale
%doc /usr/share/texmf/doc/latex/rotfloat
%doc /usr/share/texmf/doc/latex/rotating
%doc /usr/share/texmf/doc/latex/leftidx
%doc /usr/share/texmf/doc/latex/geometry
%doc /usr/share/texmf/doc/latex/footmisc
%doc /usr/share/texmf/doc/latex/floatflt
%doc /usr/share/texmf/doc/latex/draftcopy
%doc /usr/share/texmf/doc/latex/changebar
%doc /usr/share/texmf/doc/latex/ccaption
%doc /usr/share/texmf/doc/latex/booktabs
%doc /usr/share/texmf/doc/latex/anysize
%doc /usr/share/texmf/doc/latex/aeguill
%doc /usr/share/texmf/doc/latex/acronym
%dir /usr/share/texmf/tex/latex/misc
/usr/share/texmf/tex/latex/misc/a4dutch.sty
/usr/share/texmf/tex/latex/misc/a4wide.sty
/usr/share/texmf/tex/latex/misc/acronym.sty
/usr/share/texmf/tex/latex/misc/aeguill.sty
/usr/share/texmf/tex/latex/misc/anysize.sty
/usr/share/texmf/tex/latex/misc/apalike.sty
/usr/share/texmf/tex/latex/misc/avantgar.sty
/usr/share/texmf/tex/latex/misc/bar.sty
/usr/share/texmf/tex/latex/misc/bbold.sty
/usr/share/texmf/tex/latex/misc/beton.sty
/usr/share/texmf/tex/latex/misc/bibgerm.sty
/usr/share/texmf/tex/latex/misc/bold-extra.sty
/usr/share/texmf/tex/latex/misc/booktabs.sty
/usr/share/texmf/tex/latex/misc/boxedminipage.sty
/usr/share/texmf/tex/latex/misc/cancel.sty
/usr/share/texmf/tex/latex/misc/capt-of.sty
/usr/share/texmf/tex/latex/misc/ccaption.sty
/usr/share/texmf/tex/latex/misc/changebar.sty
/usr/share/texmf/tex/latex/misc/chappg.sty
/usr/share/texmf/tex/latex/misc/citesort.sty
/usr/share/texmf/tex/latex/misc/comment.sty
/usr/share/texmf/tex/latex/misc/concrete.sty
/usr/share/texmf/tex/latex/misc/crop.sty
/usr/share/texmf/tex/latex/misc/doublespace.sty
/usr/share/texmf/tex/latex/misc/draftcopy.sty
/usr/share/texmf/tex/latex/misc/eclbip.sty
/usr/share/texmf/tex/latex/misc/ecltree.sty
/usr/share/texmf/tex/latex/misc/endnotes.sty
/usr/share/texmf/tex/latex/misc/euler.sty
/usr/share/texmf/tex/latex/misc/exam.cls
/usr/share/texmf/tex/latex/misc/example.sty
/usr/share/texmf/tex/latex/misc/fancybox.sty
/usr/share/texmf/tex/latex/misc/fguill.sty
/usr/share/texmf/tex/latex/misc/floatflt.sty
/usr/share/texmf/tex/latex/misc/float.sty
/usr/share/texmf/tex/latex/misc/fltpage.sty
/usr/share/texmf/tex/latex/misc/fnpara.sty
/usr/share/texmf/tex/latex/misc/footbib.sty
/usr/share/texmf/tex/latex/misc/footmisc.sty
/usr/share/texmf/tex/latex/misc/footnpag.sty
/usr/share/texmf/tex/latex/misc/framed.sty
/usr/share/texmf/tex/latex/misc/fullpage.sty
/usr/share/texmf/tex/latex/misc/geometry.sty
/usr/share/texmf/tex/latex/misc/gletter.sty
/usr/share/texmf/tex/latex/misc/hangcaption.sty
/usr/share/texmf/tex/latex/misc/helvetic.sty
/usr/share/texmf/tex/latex/misc/here.sty
/usr/share/texmf/tex/latex/misc/hyphenat.sty
/usr/share/texmf/tex/latex/misc/index.sty
/usr/share/texmf/tex/latex/misc/isolatin1.sty
/usr/share/texmf/tex/latex/misc/landscape.sty
/usr/share/texmf/tex/latex/misc/lastpage.sty
/usr/share/texmf/tex/latex/misc/layouts.sty
/usr/share/texmf/tex/latex/misc/leftidx.sty
/usr/share/texmf/tex/latex/misc/marvosym.sty
/usr/share/texmf/tex/latex/misc/mathcomp.sty
/usr/share/texmf/tex/latex/misc/moreverb.sty
/usr/share/texmf/tex/latex/misc/multibox.sty
/usr/share/texmf/tex/latex/misc/multind.sty
/usr/share/texmf/tex/latex/misc/ncntrsbk.sty
/usr/share/texmf/tex/latex/misc/nomencl.sty
/usr/share/texmf/tex/latex/misc/optional.sty
/usr/share/texmf/tex/latex/misc/overpic.sty
/usr/share/texmf/tex/latex/misc/paralist.sty
/usr/share/texmf/tex/latex/misc/parskip.sty
/usr/share/texmf/tex/latex/misc/pdfpages.sty
/usr/share/texmf/tex/latex/misc/picinpar.sty
/usr/share/texmf/tex/latex/misc/picins.sty
/usr/share/texmf/tex/latex/misc/placeins.sty
/usr/share/texmf/tex/latex/misc/portland.sty
/usr/share/texmf/tex/latex/misc/prettyref.sty
/usr/share/texmf/tex/latex/misc/program.sty
/usr/share/texmf/tex/latex/misc/psboxit.sty
/usr/share/texmf/tex/latex/misc/psfrag.sty
/usr/share/texmf/tex/latex/misc/pslatex.sty
/usr/share/texmf/tex/latex/misc/relsize.sty
/usr/share/texmf/tex/latex/misc/rotating.sty
/usr/share/texmf/tex/latex/misc/rotfloat.sty
/usr/share/texmf/tex/latex/misc/scale.sty
/usr/share/texmf/tex/latex/misc/sectsty.sty
/usr/share/texmf/tex/latex/misc/selectp.sty
/usr/share/texmf/tex/latex/misc/setspace.sty
/usr/share/texmf/tex/latex/misc/shadow.sty
/usr/share/texmf/tex/latex/misc/shapepar.sty
/usr/share/texmf/tex/latex/misc/showdim.sty
/usr/share/texmf/tex/latex/misc/showlabels.sty
/usr/share/texmf/tex/latex/misc/showtags.sty
/usr/share/texmf/tex/latex/misc/sidecap.sty
/usr/share/texmf/tex/latex/misc/SIunits.sty
/usr/share/texmf/tex/latex/misc/slashbox.sty
/usr/share/texmf/tex/latex/misc/soul.sty
/usr/share/texmf/tex/latex/misc/stdclsdv.sty
/usr/share/texmf/tex/latex/misc/stmaryrd.sty
/usr/share/texmf/tex/latex/misc/subfigure.sty
/usr/share/texmf/tex/latex/misc/supertabular.sty
/usr/share/texmf/tex/latex/misc/sz.sty
/usr/share/texmf/tex/latex/misc/tabls.sty
/usr/share/texmf/tex/latex/misc/textfit.sty
/usr/share/texmf/tex/latex/misc/threeparttable.sty
/usr/share/texmf/tex/latex/misc/tocbibind.sty
/usr/share/texmf/tex/latex/misc/tocloft.sty
/usr/share/texmf/tex/latex/misc/trees.sty
/usr/share/texmf/tex/latex/misc/type1cm.sty
/usr/share/texmf/tex/latex/misc/ulem.sty
/usr/share/texmf/tex/latex/misc/url.sty
/usr/share/texmf/tex/latex/misc/ustmry.fd
/usr/share/texmf/tex/latex/misc/version.sty
/usr/share/texmf/tex/latex/misc/vmargin.sty
/usr/share/texmf/tex/latex/misc/vpage.sty
/usr/share/texmf/tex/latex/misc/wrapfig.sty
/usr/share/texmf/tex/latex/misc/xtab.sty
/usr/share/texmf/tex/latex/misc/yfonts.sty
/usr/share/texmf/tex/latex/misc/zapfchan.sty

%files latex-minitoc
%doc /usr/share/texmf/doc/latex/minitoc
%dir /usr/share/texmf/tex/latex/minitoc
/usr/share/texmf/tex/latex/minitoc/afrikaan.mld
/usr/share/texmf/tex/latex/minitoc/afrikaans.mld
/usr/share/texmf/tex/latex/minitoc/american.mld
/usr/share/texmf/tex/latex/minitoc/arabic.mld
/usr/share/texmf/tex/latex/minitoc/arab.mld
/usr/share/texmf/tex/latex/minitoc/armenian.mld
/usr/share/texmf/tex/latex/minitoc/austrian.mld
/usr/share/texmf/tex/latex/minitoc/bahasa.mld
/usr/share/texmf/tex/latex/minitoc/basque.mld
/usr/share/texmf/tex/latex/minitoc/bicig.mld
/usr/share/texmf/tex/latex/minitoc/brazil.mld
/usr/share/texmf/tex/latex/minitoc/breton.mld
/usr/share/texmf/tex/latex/minitoc/buryat.mld
/usr/share/texmf/tex/latex/minitoc/catalan.mld
/usr/share/texmf/tex/latex/minitoc/croatian.mld
/usr/share/texmf/tex/latex/minitoc/czech.mld
/usr/share/texmf/tex/latex/minitoc/danish.mld
/usr/share/texmf/tex/latex/minitoc/dutch.mld
/usr/share/texmf/tex/latex/minitoc/english.mld
/usr/share/texmf/tex/latex/minitoc/esperant.mld
/usr/share/texmf/tex/latex/minitoc/esperanto.mld
/usr/share/texmf/tex/latex/minitoc/estonian.mld
/usr/share/texmf/tex/latex/minitoc/ethiopia.mld
/usr/share/texmf/tex/latex/minitoc/ethiopian.mld
/usr/share/texmf/tex/latex/minitoc/finnish.mld
/usr/share/texmf/tex/latex/minitoc/francais.mld
/usr/share/texmf/tex/latex/minitoc/french.mld
/usr/share/texmf/tex/latex/minitoc/galician.mld
/usr/share/texmf/tex/latex/minitoc/germanb.mld
/usr/share/texmf/tex/latex/minitoc/german.mld
/usr/share/texmf/tex/latex/minitoc/greek.mld
/usr/share/texmf/tex/latex/minitoc/hungarian.mld
/usr/share/texmf/tex/latex/minitoc/irish.mld
/usr/share/texmf/tex/latex/minitoc/italian.mld
/usr/share/texmf/tex/latex/minitoc/lithuanian.mld
/usr/share/texmf/tex/latex/minitoc/lsorbian.mld
/usr/share/texmf/tex/latex/minitoc/magyar.mld
/usr/share/texmf/tex/latex/minitoc/minitoc.sty
/usr/share/texmf/tex/latex/minitoc/mongol.mld
/usr/share/texmf/tex/latex/minitoc/mtcoff.sty
/usr/share/texmf/tex/latex/minitoc/ngermanb.mld
/usr/share/texmf/tex/latex/minitoc/norsk.mld
/usr/share/texmf/tex/latex/minitoc/nynorsk.mld
/usr/share/texmf/tex/latex/minitoc/polish.mld
/usr/share/texmf/tex/latex/minitoc/portuges.mld
/usr/share/texmf/tex/latex/minitoc/romanian.mld
/usr/share/texmf/tex/latex/minitoc/russianb.mld
/usr/share/texmf/tex/latex/minitoc/russianc.mld
/usr/share/texmf/tex/latex/minitoc/russian.mld
/usr/share/texmf/tex/latex/minitoc/scottish.mld
/usr/share/texmf/tex/latex/minitoc/serbian.mld
/usr/share/texmf/tex/latex/minitoc/slovak.mld
/usr/share/texmf/tex/latex/minitoc/slovene.mld
/usr/share/texmf/tex/latex/minitoc/spanish.mld
/usr/share/texmf/tex/latex/minitoc/swedish.mld
/usr/share/texmf/tex/latex/minitoc/turkish.mld
/usr/share/texmf/tex/latex/minitoc/ukraineb.mld
/usr/share/texmf/tex/latex/minitoc/usorbian.mld
/usr/share/texmf/tex/latex/minitoc/vietnamese.mld
/usr/share/texmf/tex/latex/minitoc/vietnam.mld
/usr/share/texmf/tex/latex/minitoc/welsh.mld

%files latex-mfnfss
%doc /usr/share/texmf/doc/latex/mfnfss
%dir /usr/share/texmf/tex/latex/mfnfss
/usr/share/texmf/tex/latex/mfnfss/oldgerm.sty
/usr/share/texmf/tex/latex/mfnfss/ot1panr.fd
/usr/share/texmf/tex/latex/mfnfss/ot1pss.fd
/usr/share/texmf/tex/latex/mfnfss/pandora.sty
/usr/share/texmf/tex/latex/mfnfss/uyfrak.fd
/usr/share/texmf/tex/latex/mfnfss/uygoth.fd
/usr/share/texmf/tex/latex/mfnfss/uyinit.fd
/usr/share/texmf/tex/latex/mfnfss/uyswab.fd

%files latex-mflogo
%dir /usr/share/texmf/tex/latex/mflogo
/usr/share/texmf/tex/latex/mflogo/mflogo.sty
/usr/share/texmf/tex/latex/mflogo/ulogo.fd

%files latex-mdwtools
%doc /usr/share/texmf/doc/latex/mdwtools
%dir /usr/share/texmf/tex/latex/mdwtools
/usr/share/texmf/tex/latex/mdwtools/at.sty
/usr/share/texmf/tex/latex/mdwtools/cmtt.sty
/usr/share/texmf/tex/latex/mdwtools/doafter.sty
/usr/share/texmf/tex/latex/mdwtools/doafter.tex
/usr/share/texmf/tex/latex/mdwtools/footnote.sty
/usr/share/texmf/tex/latex/mdwtools/mathenv.sty
/usr/share/texmf/tex/latex/mdwtools/mdwlist.sty
/usr/share/texmf/tex/latex/mdwtools/mdwmath.sty
/usr/share/texmf/tex/latex/mdwtools/mdwtab.sty
/usr/share/texmf/tex/latex/mdwtools/mTTcmtt.fd
/usr/share/texmf/tex/latex/mdwtools/mTTenc.def
/usr/share/texmf/tex/latex/mdwtools/sverb.sty
/usr/share/texmf/tex/latex/mdwtools/syntax.sty

%files latex-mathtime
%dir /usr/share/texmf/tex/latex/mathtime
/usr/share/texmf/tex/latex/mathtime/lfonts-m.tex
/usr/share/texmf/tex/latex/mathtime/lplain-m.tex
/usr/share/texmf/tex/latex/mathtime/mathpi.sty
/usr/share/texmf/tex/latex/mathtime/mathtime.sty
/usr/share/texmf/tex/latex/mathtime/mt11p.sty
/usr/share/texmf/tex/latex/mathtime/mtlatex.tex
/usr/share/texmf/tex/latex/mathtime/mtltplus.tex
/usr/share/texmf/tex/latex/mathtime/my1mtt.fd
/usr/share/texmf/tex/latex/mathtime/my2mtt.fd
/usr/share/texmf/tex/latex/mathtime/my3mtt.fd
/usr/share/texmf/tex/latex/mathtime/omslby.fd
/usr/share/texmf/tex/latex/mathtime/umh2.fd
/usr/share/texmf/tex/latex/mathtime/umh2scr.fd
/usr/share/texmf/tex/latex/mathtime/umh6.fd
/usr/share/texmf/tex/latex/mathtime/umtms.fd

%files latex-mathptmx
%dir /usr/share/texmf/tex/latex/mathptmx
/usr/share/texmf/tex/latex/mathptmx/mathptmx.sty
/usr/share/texmf/tex/latex/mathptmx/omlztmcm.fd
/usr/share/texmf/tex/latex/mathptmx/omsztmcm.fd
/usr/share/texmf/tex/latex/mathptmx/omxztmcm.fd
/usr/share/texmf/tex/latex/mathptmx/ot1ztmcm.fd

%files latex-mathptm
%dir /usr/share/texmf/tex/latex/mathptm
/usr/share/texmf/tex/latex/mathptm/mathptm.sty
/usr/share/texmf/tex/latex/mathptm/omlptmcm.fd
/usr/share/texmf/tex/latex/mathptm/omspzccm.fd
/usr/share/texmf/tex/latex/mathptm/omxpsycm.fd
/usr/share/texmf/tex/latex/mathptm/ot1ptmcm.fd

%files latex-mathpple
%dir /usr/share/texmf/tex/latex/mathpple
/usr/share/texmf/tex/latex/mathpple/mathpple.sty
/usr/share/texmf/tex/latex/mathpple/omlzpple.fd
/usr/share/texmf/tex/latex/mathpple/omszpple.fd
/usr/share/texmf/tex/latex/mathpple/omxzpple.fd
/usr/share/texmf/tex/latex/mathpple/ot1phvv.fd
/usr/share/texmf/tex/latex/mathpple/ot1zpple.fd
/usr/share/texmf/tex/latex/mathpple/t1phvv.fd
/usr/share/texmf/tex/latex/mathpple/ts1phvv.fd

%files latex-lucidabr
%dir /usr/share/texmf/tex/latex/lucidabr
/usr/share/texmf/tex/latex/lucidabr/8rhlce.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlcf.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlcn.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlct.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlcw.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlh.fd
/usr/share/texmf/tex/latex/lucidabr/8rhls.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlst.fd
/usr/share/texmf/tex/latex/lucidabr/8rhlx.fd
/usr/share/texmf/tex/latex/lucidabr/lmrhlcm.fd
/usr/share/texmf/tex/latex/lucidabr/lucbmath.sty
/usr/share/texmf/tex/latex/lucidabr/lucfont.tex
/usr/share/texmf/tex/latex/lucidabr/lucidabr.sty
/usr/share/texmf/tex/latex/lucidabr/lucidbrb.sty
/usr/share/texmf/tex/latex/lucidabr/lucidbry.sty
/usr/share/texmf/tex/latex/lucidabr/lucmin.sty
/usr/share/texmf/tex/latex/lucidabr/lucmtime.sty
/usr/share/texmf/tex/latex/lucidabr/ly1enc.def
/usr/share/texmf/tex/latex/lucidabr/ly1hlce.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlcf.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlcn.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlct.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlcw.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlh.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hls.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlst.fd
/usr/share/texmf/tex/latex/lucidabr/ly1hlx.fd
/usr/share/texmf/tex/latex/lucidabr/ly1pcr.fd
/usr/share/texmf/tex/latex/lucidabr/ly1phv.fd
/usr/share/texmf/tex/latex/lucidabr/ly1ptm.fd
/usr/share/texmf/tex/latex/lucidabr/omlhlcm.fd
/usr/share/texmf/tex/latex/lucidabr/omlhlh.fd
/usr/share/texmf/tex/latex/lucidabr/omshlcy.fd
/usr/share/texmf/tex/latex/lucidabr/omshlh.fd
/usr/share/texmf/tex/latex/lucidabr/omxhlcv.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlce.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlcf.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlcn.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlct.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlcw.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlh.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hls.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlst.fd
/usr/share/texmf/tex/latex/lucidabr/ot1hlx.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlce.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlcf.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlcn.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlct.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlcw.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlh.fd
/usr/share/texmf/tex/latex/lucidabr/t1hls.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlst.fd
/usr/share/texmf/tex/latex/lucidabr/t1hlx.fd
/usr/share/texmf/tex/latex/lucidabr/texnansi.sty
/usr/share/texmf/tex/latex/lucidabr/ts1hlce.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlcf.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlcn.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlct.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlcw.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlh.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hls.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlst.fd
/usr/share/texmf/tex/latex/lucidabr/ts1hlx.fd

%files latex-listings
%dir /usr/share/texmf/tex/latex/listings
/usr/share/texmf/tex/latex/listings/listings.cfg
/usr/share/texmf/tex/latex/listings/listings.sty
/usr/share/texmf/tex/latex/listings/lstdoc.sty
/usr/share/texmf/tex/latex/listings/lstlang1.sty
/usr/share/texmf/tex/latex/listings/lstlang2.sty
/usr/share/texmf/tex/latex/listings/lstlang3.sty
/usr/share/texmf/tex/latex/listings/lstmisc.sty
/usr/share/texmf/tex/latex/listings/lstpatch.sty

%files latex-labels
%dir /usr/share/texmf/tex/latex/labels
/usr/share/texmf/tex/latex/labels/labels.sty
/usr/share/texmf/tex/latex/labels/olabels.sty

%files latex-koma-script
%doc /usr/share/texmf/doc/latex/koma-script
%dir /usr/share/texmf/tex/latex/koma-script
/usr/share/texmf/tex/latex/koma-script/scraddr.sty
/usr/share/texmf/tex/latex/koma-script/scrartcl.cls
/usr/share/texmf/tex/latex/koma-script/scrbook.cls
/usr/share/texmf/tex/latex/koma-script/scrdate.sty
/usr/share/texmf/tex/latex/koma-script/script_l.sty
/usr/share/texmf/tex/latex/koma-script/script_s.sty
/usr/share/texmf/tex/latex/koma-script/script.sty
/usr/share/texmf/tex/latex/koma-script/scrlettr.cls
/usr/share/texmf/tex/latex/koma-script/scrpage2.sty
/usr/share/texmf/tex/latex/koma-script/scrpage.sty
/usr/share/texmf/tex/latex/koma-script/scrreprt.cls
/usr/share/texmf/tex/latex/koma-script/scrtime.sty
/usr/share/texmf/tex/latex/koma-script/typearea.sty

%files latex-jknappen
%doc /usr/share/texmf/doc/latex/jknappen
%dir /usr/share/texmf/tex/latex/jknappen
/usr/share/texmf/tex/latex/jknappen/greekctr.sty
/usr/share/texmf/tex/latex/jknappen/latin1jk.def
/usr/share/texmf/tex/latex/jknappen/latin2jk.def
/usr/share/texmf/tex/latex/jknappen/latin3jk.def
/usr/share/texmf/tex/latex/jknappen/mathbbol.sty
/usr/share/texmf/tex/latex/jknappen/mathrsfs.sty
/usr/share/texmf/tex/latex/jknappen/ubbold.fd
/usr/share/texmf/tex/latex/jknappen/ursfs.fd

%files latex-hyperref
%doc /usr/share/texmf/doc/latex/hyperref
%dir /usr/share/texmf/tex/latex/hyperref
/usr/share/texmf/tex/latex/hyperref/backref.sty
/usr/share/texmf/tex/latex/hyperref/hdvipdfm.def
/usr/share/texmf/tex/latex/hyperref/hdvips.def
/usr/share/texmf/tex/latex/hyperref/hdvipson.def
/usr/share/texmf/tex/latex/hyperref/hdviwind.def
/usr/share/texmf/tex/latex/hyperref/hpdftex.def
/usr/share/texmf/tex/latex/hyperref/htex4ht.cfg
/usr/share/texmf/tex/latex/hyperref/htex4ht.def
/usr/share/texmf/tex/latex/hyperref/htexture.def
/usr/share/texmf/tex/latex/hyperref/hvtex.def
/usr/share/texmf/tex/latex/hyperref/hvtexhtm.def
/usr/share/texmf/tex/latex/hyperref/hvtexmrk.def
/usr/share/texmf/tex/latex/hyperref/hycheck.tex
/usr/share/texmf/tex/latex/hyperref/hylatex.ltx
/usr/share/texmf/tex/latex/hyperref/hyperref.sty
/usr/share/texmf/tex/latex/hyperref/hypertex.def
/usr/share/texmf/tex/latex/hyperref/minitoc-hyper.sty
/usr/share/texmf/tex/latex/hyperref/nameref.sty
/usr/share/texmf/tex/latex/hyperref/nohyperref.sty
/usr/share/texmf/tex/latex/hyperref/ntheorem-hyper.sty
/usr/share/texmf/tex/latex/hyperref/pd1enc.def
/usr/share/texmf/tex/latex/hyperref/pdfmark.def
/usr/share/texmf/tex/latex/hyperref/puenc.def
/usr/share/texmf/tex/latex/hyperref/xr-hyper.sty

%files latex-graphics
%doc /usr/share/texmf/doc/latex/graphics
%dir /usr/share/texmf/tex/latex/graphics
/usr/share/texmf/tex/latex/graphics/color.sty
/usr/share/texmf/tex/latex/graphics/dvipdf.def
/usr/share/texmf/tex/latex/graphics/dvipdfm.def
/usr/share/texmf/tex/latex/graphics/dvips.def
/usr/share/texmf/tex/latex/graphics/dvipsnam.def
/usr/share/texmf/tex/latex/graphics/dvipsone.def
/usr/share/texmf/tex/latex/graphics/dviwin.def
/usr/share/texmf/tex/latex/graphics/emtex.def
/usr/share/texmf/tex/latex/graphics/epsfig.sty
/usr/share/texmf/tex/latex/graphics/graphics.sty
/usr/share/texmf/tex/latex/graphics/graphicx.sty
/usr/share/texmf/tex/latex/graphics/keyval.sty
/usr/share/texmf/tex/latex/graphics/lscape.sty
/usr/share/texmf/tex/latex/graphics/pctex32.def
/usr/share/texmf/tex/latex/graphics/pctexhp.def
/usr/share/texmf/tex/latex/graphics/pctexps.def
/usr/share/texmf/tex/latex/graphics/pctexwin.def
/usr/share/texmf/tex/latex/graphics/pdftex.def
/usr/share/texmf/tex/latex/graphics/pstcol.sty
/usr/share/texmf/tex/latex/graphics/tcidvi.def
/usr/share/texmf/tex/latex/graphics/textures.def
/usr/share/texmf/tex/latex/graphics/trig.sty
/usr/share/texmf/tex/latex/graphics/truetex.def
/usr/share/texmf/tex/latex/graphics/vtex.def

%files latex-g-brief
%doc /usr/share/texmf/doc/latex/g-brief
%dir /usr/share/texmf/tex/latex/g-brief
/usr/share/texmf/tex/latex/g-brief/g-brief.cls
/usr/share/texmf/tex/latex/g-brief/g-brief.sty

%files latex-fp
%dir /usr/share/texmf/tex/latex/fp
/usr/share/texmf/tex/latex/fp/defpattern.sty
/usr/share/texmf/tex/latex/fp/fp-addons.sty
/usr/share/texmf/tex/latex/fp/fp-basic.sty
/usr/share/texmf/tex/latex/fp/fp-eqn.sty
/usr/share/texmf/tex/latex/fp/fp-eval.sty
/usr/share/texmf/tex/latex/fp/fp-exp.sty
/usr/share/texmf/tex/latex/fp/fp-pas.sty
/usr/share/texmf/tex/latex/fp/fp-random.sty
/usr/share/texmf/tex/latex/fp/fp-snap.sty
/usr/share/texmf/tex/latex/fp/fp.sty
/usr/share/texmf/tex/latex/fp/fp.tex
/usr/share/texmf/tex/latex/fp/fp-trigo.sty
/usr/share/texmf/tex/latex/fp/fp-upn.sty
/usr/share/texmf/tex/latex/fp/lfp.sty

%files latex-fancyvrb
%doc /usr/share/texmf/doc/latex/fancyvrb
%dir /usr/share/texmf/tex/latex/fancyvrb
/usr/share/texmf/tex/latex/fancyvrb/fancyvrb.sty
/usr/share/texmf/tex/latex/fancyvrb/fvrb-ex.sty
/usr/share/texmf/tex/latex/fancyvrb/hbaw.sty
/usr/share/texmf/tex/latex/fancyvrb/hcolor.sty

%files latex-fancyheadings
%doc /usr/share/texmf/doc/latex/fancyhdr
%dir /usr/share/texmf/tex/latex/fancyheadings
/usr/share/texmf/tex/latex/fancyheadings/fancyheadings.sty
/usr/share/texmf/tex/latex/fancyheadings/lastpage209.sty

%files latex-fancyhdr
%dir /usr/share/texmf/tex/latex/fancyhdr
/usr/share/texmf/tex/latex/fancyhdr/extramarks.sty
/usr/share/texmf/tex/latex/fancyhdr/fancyhdr.sty
/usr/share/texmf/tex/latex/fancyhdr/fixmarks.sty

%files latex-endfloat
%dir /usr/share/texmf/tex/latex/endfloat
/usr/share/texmf/tex/latex/endfloat/efxmpl.cfg
/usr/share/texmf/tex/latex/endfloat/endfloat.sty

%files latex-eepic
%doc /usr/share/texmf/doc/latex/eepic
%dir /usr/share/texmf/tex/latex/eepic
/usr/share/texmf/tex/latex/eepic/eepicemu.sty
/usr/share/texmf/tex/latex/eepic/eepic.sty
/usr/share/texmf/tex/latex/eepic/epic.sty

%files latex-dvilj
%dir /usr/share/texmf/tex/latex/dvilj
/usr/share/texmf/tex/latex/dvilj/cgalbertus.sty
/usr/share/texmf/tex/latex/dvilj/cgantiqueolive.sty
/usr/share/texmf/tex/latex/dvilj/cgcourier.sty
/usr/share/texmf/tex/latex/dvilj/cggothic.sty
/usr/share/texmf/tex/latex/dvilj/cgtimes.sty
/usr/share/texmf/tex/latex/dvilj/cgunivers.sty
/usr/share/texmf/tex/latex/dvilj/graybox.sty
/usr/share/texmf/tex/latex/dvilj/hpfonts.sty

%files latex-dstroke
%dir /usr/share/texmf/tex/latex/dstroke
/usr/share/texmf/tex/latex/dstroke/dsfont.sty
/usr/share/texmf/tex/latex/dstroke/Udsrom.fd
/usr/share/texmf/tex/latex/dstroke/Udsss.fd

%files latex-draftcopy
%dir /usr/share/texmf/tex/latex/draftcopy
/usr/share/texmf/tex/latex/draftcopy/draftcopy.sty

%files latex-dinbrief
%doc /usr/share/texmf/doc/latex/dinbrief
%dir /usr/share/texmf/tex/latex/dinbrief
/usr/share/texmf/tex/latex/dinbrief/dinbrief.cls
/usr/share/texmf/tex/latex/dinbrief/dinbrief.sty

%files latex-cyrillic
%doc /usr/share/texmf/doc/latex/cyrillic
%dir /usr/share/texmf/tex/latex/cyrillic
/usr/share/texmf/tex/latex/cyrillic/cp1251.def
/usr/share/texmf/tex/latex/cyrillic/cp855.def
/usr/share/texmf/tex/latex/cyrillic/cp866av.def
/usr/share/texmf/tex/latex/cyrillic/cp866.def
/usr/share/texmf/tex/latex/cyrillic/cp866mav.def
/usr/share/texmf/tex/latex/cyrillic/cp866nav.def
/usr/share/texmf/tex/latex/cyrillic/cp866tat.def
/usr/share/texmf/tex/latex/cyrillic/ctt.def
/usr/share/texmf/tex/latex/cyrillic/dbk.def
/usr/share/texmf/tex/latex/cyrillic/iso88595.def
/usr/share/texmf/tex/latex/cyrillic/isoir111.def
/usr/share/texmf/tex/latex/cyrillic/koi8-r.def
/usr/share/texmf/tex/latex/cyrillic/koi8-ru.def
/usr/share/texmf/tex/latex/cyrillic/koi8-u.def
/usr/share/texmf/tex/latex/cyrillic/lcycmdh.fd
/usr/share/texmf/tex/latex/cyrillic/lcycmfib.fd
/usr/share/texmf/tex/latex/cyrillic/lcycmfr.fd
/usr/share/texmf/tex/latex/cyrillic/lcycmr.fd
/usr/share/texmf/tex/latex/cyrillic/lcycmss.fd
/usr/share/texmf/tex/latex/cyrillic/lcycmtt.fd
/usr/share/texmf/tex/latex/cyrillic/lcycmvtt.fd
/usr/share/texmf/tex/latex/cyrillic/lcydefs.tex
/usr/share/texmf/tex/latex/cyrillic/lcyenc.def
/usr/share/texmf/tex/latex/cyrillic/lcylcmss.fd
/usr/share/texmf/tex/latex/cyrillic/lcylcmtt.fd
/usr/share/texmf/tex/latex/cyrillic/lcy.sty
/usr/share/texmf/tex/latex/cyrillic/maccyr.def
/usr/share/texmf/tex/latex/cyrillic/macukr.def
/usr/share/texmf/tex/latex/cyrillic/mik.def
/usr/share/texmf/tex/latex/cyrillic/mls.def
/usr/share/texmf/tex/latex/cyrillic/mnk.def
/usr/share/texmf/tex/latex/cyrillic/mos.def
/usr/share/texmf/tex/latex/cyrillic/ncc.def
/usr/share/texmf/tex/latex/cyrillic/ot2cmdh.fd
/usr/share/texmf/tex/latex/cyrillic/ot2cmfib.fd
/usr/share/texmf/tex/latex/cyrillic/ot2cmfr.fd
/usr/share/texmf/tex/latex/cyrillic/ot2cmr.fd
/usr/share/texmf/tex/latex/cyrillic/ot2cmss.fd
/usr/share/texmf/tex/latex/cyrillic/ot2cmtt.fd
/usr/share/texmf/tex/latex/cyrillic/ot2cmvtt.fd
/usr/share/texmf/tex/latex/cyrillic/ot2enc.def
/usr/share/texmf/tex/latex/cyrillic/ot2lcmss.fd
/usr/share/texmf/tex/latex/cyrillic/ot2lcmtt.fd
/usr/share/texmf/tex/latex/cyrillic/ot2wncyr.fd
/usr/share/texmf/tex/latex/cyrillic/ot2wncyss.fd
/usr/share/texmf/tex/latex/cyrillic/pt154.def
/usr/share/texmf/tex/latex/cyrillic/pt254.def
/usr/share/texmf/tex/latex/cyrillic/t2acmdh.fd
/usr/share/texmf/tex/latex/cyrillic/t2acmfib.fd
/usr/share/texmf/tex/latex/cyrillic/t2acmfr.fd
/usr/share/texmf/tex/latex/cyrillic/t2acmr.fd
/usr/share/texmf/tex/latex/cyrillic/t2acmss.fd
/usr/share/texmf/tex/latex/cyrillic/t2acmtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2acmvtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2aenc.def
/usr/share/texmf/tex/latex/cyrillic/t2alcmss.fd
/usr/share/texmf/tex/latex/cyrillic/t2alcmtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmdh.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmfib.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmfr.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmr.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmss.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2bcmvtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2benc.def
/usr/share/texmf/tex/latex/cyrillic/t2blcmss.fd
/usr/share/texmf/tex/latex/cyrillic/t2blcmtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmdh.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmfib.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmfr.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmr.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmss.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2ccmvtt.fd
/usr/share/texmf/tex/latex/cyrillic/t2cenc.def
/usr/share/texmf/tex/latex/cyrillic/t2clcmss.fd
/usr/share/texmf/tex/latex/cyrillic/t2clcmtt.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmdh.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmfib.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmfr.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmr.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmss.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmtt.fd
/usr/share/texmf/tex/latex/cyrillic/x2cmvtt.fd
/usr/share/texmf/tex/latex/cyrillic/x2enc.def
/usr/share/texmf/tex/latex/cyrillic/x2lcmss.fd
/usr/share/texmf/tex/latex/cyrillic/x2lcmtt.fd

%files latex-custom-bib
%doc /usr/share/texmf/doc/latex/custom-bib
%dir /usr/share/texmf/tex/latex/custom-bib
/usr/share/texmf/tex/latex/custom-bib/catalan.mbs
/usr/share/texmf/tex/latex/custom-bib/dansk.mbs
/usr/share/texmf/tex/latex/custom-bib/dutch.mbs
/usr/share/texmf/tex/latex/custom-bib/english.mbs
/usr/share/texmf/tex/latex/custom-bib/esperant.mbs
/usr/share/texmf/tex/latex/custom-bib/finnish.mbs
/usr/share/texmf/tex/latex/custom-bib/french.mbs
/usr/share/texmf/tex/latex/custom-bib/geojour.mbs
/usr/share/texmf/tex/latex/custom-bib/german.mbs
/usr/share/texmf/tex/latex/custom-bib/italian.mbs
/usr/share/texmf/tex/latex/custom-bib/makebst.tex
/usr/share/texmf/tex/latex/custom-bib/merlin.mbs
/usr/share/texmf/tex/latex/custom-bib/norsk.mbs
/usr/share/texmf/tex/latex/custom-bib/photjour.mbs
/usr/share/texmf/tex/latex/custom-bib/physjour.mbs
/usr/share/texmf/tex/latex/custom-bib/polski.mbs
/usr/share/texmf/tex/latex/custom-bib/portuges.mbs
/usr/share/texmf/tex/latex/custom-bib/spanish.mbs
/usr/share/texmf/tex/latex/custom-bib/suppjour.mbs

%files latex-curves
%dir /usr/share/texmf/tex/latex/curves
/usr/share/texmf/tex/latex/curves/curvesls.sty
/usr/share/texmf/tex/latex/curves/curves.sty

%files cslatex
%doc /usr/share/texmf/doc/cstex/INSTALL.cslatex
%doc /usr/share/texmf/doc/cstex/README.cslatex
/usr/share/texmf/tex/cslatex
%dir /usr/share/texmf/tex/latex/cslatex
/usr/share/texmf/tex/latex/cslatex/cspsfont.il2
/usr/share/texmf/tex/latex/cslatex/cspsfont.tex
/usr/share/texmf/tex/latex/cslatex/cspsfont.xl2
/usr/share/texmf/tex/latex/cslatex/il2pag.fd
/usr/share/texmf/tex/latex/cslatex/il2pbk.fd
/usr/share/texmf/tex/latex/cslatex/il2pcr.fd
/usr/share/texmf/tex/latex/cslatex/il2phv.fd
/usr/share/texmf/tex/latex/cslatex/il2phvn.fd
/usr/share/texmf/tex/latex/cslatex/il2pnc.fd
/usr/share/texmf/tex/latex/cslatex/il2ppl.fd
/usr/share/texmf/tex/latex/cslatex/il2ptm.fd
/usr/share/texmf/tex/latex/cslatex/il2pzc.fd
/usr/share/texmf/tex/latex/cslatex/nhelvet.sty
/usr/share/texmf/tex/latex/cslatex/ntimes.sty
/usr/share/texmf/tex/latex/cslatex/xl2pag.fd
/usr/share/texmf/tex/latex/cslatex/xl2pbk.fd
/usr/share/texmf/tex/latex/cslatex/xl2pcr.fd
/usr/share/texmf/tex/latex/cslatex/xl2phv.fd
/usr/share/texmf/tex/latex/cslatex/xl2phvn.fd
/usr/share/texmf/tex/latex/cslatex/xl2pnc.fd
/usr/share/texmf/tex/latex/cslatex/xl2ppl.fd
/usr/share/texmf/tex/latex/cslatex/xl2ptm.fd
/usr/share/texmf/tex/latex/cslatex/xl2pzc.fd

%files latex-context
%dir /usr/share/texmf/tex/latex/context
/usr/share/texmf/tex/latex/context/m-ch-de.sty
/usr/share/texmf/tex/latex/context/m-ch-en.sty
/usr/share/texmf/tex/latex/context/m-ch-nl.sty
/usr/share/texmf/tex/latex/context/m-metapo.sty
/usr/share/texmf/tex/latex/context/m-pictex.sty

%files latex
%dir /usr/share/texmf/tex/latex/config
/usr/share/texmf/tex/latex/config/color.cfg
/usr/share/texmf/tex/latex/config/draftcopy.cfg
/usr/share/texmf/tex/latex/config/geometry.cfg
/usr/share/texmf/tex/latex/config/graphics.cfg
/usr/share/texmf/tex/latex/config/latex209.cfg
/usr/share/texmf/tex/latex/config/latex.ini
/usr/share/texmf/tex/latex/config/ltxdoc.cfg
/usr/share/texmf/tex/latex/config/ltxguide.cfg
/usr/share/texmf/tex/latex/config/seminar.con
/usr/share/texmf/tex/latex/config/SIunits.cfg
/usr/share/texmf/tex/latex/config/texsys.cfg
%dir /usr/share/texmf/tex/latex/base
/usr/share/texmf/tex/latex/base/alltt.sty
/usr/share/texmf/tex/latex/base/ansinew.def
/usr/share/texmf/tex/latex/base/applemac.def
/usr/share/texmf/tex/latex/base/article.cls
/usr/share/texmf/tex/latex/base/article.sty
/usr/share/texmf/tex/latex/base/ascii.def
/usr/share/texmf/tex/latex/base/bezier.sty
/usr/share/texmf/tex/latex/base/bk10.clo
/usr/share/texmf/tex/latex/base/bk11.clo
/usr/share/texmf/tex/latex/base/bk12.clo
/usr/share/texmf/tex/latex/base/book.cls
/usr/share/texmf/tex/latex/base/book.sty
/usr/share/texmf/tex/latex/base/cp1250.def
/usr/share/texmf/tex/latex/base/cp1252.def
/usr/share/texmf/tex/latex/base/cp437de.def
/usr/share/texmf/tex/latex/base/cp437.def
/usr/share/texmf/tex/latex/base/cp850.def
/usr/share/texmf/tex/latex/base/cp852.def
/usr/share/texmf/tex/latex/base/cp865.def
/usr/share/texmf/tex/latex/base/decmulti.def
/usr/share/texmf/tex/latex/base/docstrip.tex
/usr/share/texmf/tex/latex/base/doc.sty
/usr/share/texmf/tex/latex/base/exscale.sty
/usr/share/texmf/tex/latex/base/fixltx2e.sty
/usr/share/texmf/tex/latex/base/flafter.sty
/usr/share/texmf/tex/latex/base/fleqn.clo
/usr/share/texmf/tex/latex/base/fleqn.sty
/usr/share/texmf/tex/latex/base/fontenc.sty
/usr/share/texmf/tex/latex/base/fontmath.ltx
/usr/share/texmf/tex/latex/base/fonttext.ltx
/usr/share/texmf/tex/latex/base/graphpap.sty
/usr/share/texmf/tex/latex/base/hyphen.ltx
/usr/share/texmf/tex/latex/base/idx.tex
/usr/share/texmf/tex/latex/base/ifthen.sty
/usr/share/texmf/tex/latex/base/inputenc.sty
/usr/share/texmf/tex/latex/base/lablst.tex
/usr/share/texmf/tex/latex/base/latex209.def
/usr/share/texmf/tex/latex/base/latexbug.tex
/usr/share/texmf/tex/latex/base/latex.ltx
/usr/share/texmf/tex/latex/base/latexsym.sty
/usr/share/texmf/tex/latex/base/latin1.def
/usr/share/texmf/tex/latex/base/latin2.def
/usr/share/texmf/tex/latex/base/latin3.def
/usr/share/texmf/tex/latex/base/latin4.def
/usr/share/texmf/tex/latex/base/latin5.def
/usr/share/texmf/tex/latex/base/latin9.def
/usr/share/texmf/tex/latex/base/leqno.clo
/usr/share/texmf/tex/latex/base/leqno.sty
/usr/share/texmf/tex/latex/base/letter.cls
/usr/share/texmf/tex/latex/base/letter.sty
/usr/share/texmf/tex/latex/base/ltnews.cls
/usr/share/texmf/tex/latex/base/ltpatch.ltx
/usr/share/texmf/tex/latex/base/ltxcheck.tex
/usr/share/texmf/tex/latex/base/ltxdoc.cls
/usr/share/texmf/tex/latex/base/ltxguide.cls
/usr/share/texmf/tex/latex/base/makeidx.sty
/usr/share/texmf/tex/latex/base/minimal.cls
/usr/share/texmf/tex/latex/base/newlfont.sty
/usr/share/texmf/tex/latex/base/next.def
/usr/share/texmf/tex/latex/base/nfssfont.tex
/usr/share/texmf/tex/latex/base/oldlfont.sty
/usr/share/texmf/tex/latex/base/omlcmm.fd
/usr/share/texmf/tex/latex/base/omlcmr.fd
/usr/share/texmf/tex/latex/base/omlenc.def
/usr/share/texmf/tex/latex/base/omllcmm.fd
/usr/share/texmf/tex/latex/base/omscmr.fd
/usr/share/texmf/tex/latex/base/omscmsy.fd
/usr/share/texmf/tex/latex/base/omsenc.def
/usr/share/texmf/tex/latex/base/omslcmsy.fd
/usr/share/texmf/tex/latex/base/omxcmex.fd
/usr/share/texmf/tex/latex/base/omxlcmex.fd
/usr/share/texmf/tex/latex/base/openbib.sty
/usr/share/texmf/tex/latex/base/ot1cmdh.fd
/usr/share/texmf/tex/latex/base/ot1cmfib.fd
/usr/share/texmf/tex/latex/base/ot1cmfr.fd
/usr/share/texmf/tex/latex/base/ot1cmr.fd
/usr/share/texmf/tex/latex/base/ot1cmss.fd
/usr/share/texmf/tex/latex/base/ot1cmtt.fd
/usr/share/texmf/tex/latex/base/ot1cmvtt.fd
/usr/share/texmf/tex/latex/base/ot1enc.def
/usr/share/texmf/tex/latex/base/ot1lcmss.fd
/usr/share/texmf/tex/latex/base/ot1lcmtt.fd
/usr/share/texmf/tex/latex/base/ot4enc.def
/usr/share/texmf/tex/latex/base/pict2e.sty
/usr/share/texmf/tex/latex/base/preload.ltx
/usr/share/texmf/tex/latex/base/proc.cls
/usr/share/texmf/tex/latex/base/proc.sty
/usr/share/texmf/tex/latex/base/report.cls
/usr/share/texmf/tex/latex/base/report.sty
/usr/share/texmf/tex/latex/base/sample2e.tex
/usr/share/texmf/tex/latex/base/sfonts.def
/usr/share/texmf/tex/latex/base/shortvrb.sty
/usr/share/texmf/tex/latex/base/showidx.sty
/usr/share/texmf/tex/latex/base/size10.clo
/usr/share/texmf/tex/latex/base/size11.clo
/usr/share/texmf/tex/latex/base/size12.clo
/usr/share/texmf/tex/latex/base/slides.cls
/usr/share/texmf/tex/latex/base/slides.def
/usr/share/texmf/tex/latex/base/slides.sty
/usr/share/texmf/tex/latex/base/small2e.tex
/usr/share/texmf/tex/latex/base/syntonly.sty
/usr/share/texmf/tex/latex/base/t1cmdh.fd
/usr/share/texmf/tex/latex/base/t1cmfib.fd
/usr/share/texmf/tex/latex/base/t1cmfr.fd
/usr/share/texmf/tex/latex/base/t1cmr.fd
/usr/share/texmf/tex/latex/base/t1cmss.fd
/usr/share/texmf/tex/latex/base/t1cmtt.fd
/usr/share/texmf/tex/latex/base/t1cmvtt.fd
/usr/share/texmf/tex/latex/base/t1enc.def
/usr/share/texmf/tex/latex/base/t1enc.sty
/usr/share/texmf/tex/latex/base/t1lcmss.fd
/usr/share/texmf/tex/latex/base/t1lcmtt.fd
/usr/share/texmf/tex/latex/base/testpage.tex
/usr/share/texmf/tex/latex/base/textcomp.sty
/usr/share/texmf/tex/latex/base/tracefnt.sty
/usr/share/texmf/tex/latex/base/ts1cmr.fd
/usr/share/texmf/tex/latex/base/ts1cmss.fd
/usr/share/texmf/tex/latex/base/ts1cmtt.fd
/usr/share/texmf/tex/latex/base/ts1cmvtt.fd
/usr/share/texmf/tex/latex/base/ts1enc.def
/usr/share/texmf/tex/latex/base/ucmr.fd
/usr/share/texmf/tex/latex/base/ucmss.fd
/usr/share/texmf/tex/latex/base/ucmtt.fd
/usr/share/texmf/tex/latex/base/ulasy.fd
/usr/share/texmf/tex/latex/base/ullasy.fd

%files latex-concmath
%dir /usr/share/texmf/tex/latex/concmath
/usr/share/texmf/tex/latex/concmath/concmath.sty
/usr/share/texmf/tex/latex/concmath/omlccm.fd
/usr/share/texmf/tex/latex/concmath/omlccr.fd
/usr/share/texmf/tex/latex/concmath/omsccr.fd
/usr/share/texmf/tex/latex/concmath/omsccsy.fd
/usr/share/texmf/tex/latex/concmath/omxccex.fd
/usr/share/texmf/tex/latex/concmath/ot1ccr.fd
/usr/share/texmf/tex/latex/concmath/ucca.fd
/usr/share/texmf/tex/latex/concmath/uccb.fd

%files latex-cite
%dir /usr/share/texmf/tex/latex/cite
/usr/share/texmf/tex/latex/cite/chapterbib.sty
/usr/share/texmf/tex/latex/cite/cite.sty
/usr/share/texmf/tex/latex/cite/drftcite.sty
/usr/share/texmf/tex/latex/cite/overcite.sty

%files latex-ccfonts
%doc /usr/share/texmf/doc/latex/ccfonts
%dir /usr/share/texmf/tex/latex/ccfonts
/usr/share/texmf/tex/latex/ccfonts/ccfonts.sty
/usr/share/texmf/tex/latex/ccfonts/omlxcm.fd
/usr/share/texmf/tex/latex/ccfonts/omsxcsy.fd
/usr/share/texmf/tex/latex/ccfonts/omxxcex.fd
/usr/share/texmf/tex/latex/ccfonts/t1ccr.fd
/usr/share/texmf/tex/latex/ccfonts/ts1ccr.fd

%files latex-carlisle
%doc /usr/share/texmf/doc/latex/carlisle
%dir /usr/share/texmf/tex/latex/carlisle
/usr/share/texmf/tex/latex/carlisle/blkarray.sty
/usr/share/texmf/tex/latex/carlisle/colortbl.sty
/usr/share/texmf/tex/latex/carlisle/comma.sty
/usr/share/texmf/tex/latex/carlisle/dotlessj.sty
/usr/share/texmf/tex/latex/carlisle/fix2col.sty
/usr/share/texmf/tex/latex/carlisle/ltxtable.sty
/usr/share/texmf/tex/latex/carlisle/ltxtable.tex
/usr/share/texmf/tex/latex/carlisle/mylatex.ltx
/usr/share/texmf/tex/latex/carlisle/nopageno.sty
/usr/share/texmf/tex/latex/carlisle/plain.sty
/usr/share/texmf/tex/latex/carlisle/pspicture.sty
/usr/share/texmf/tex/latex/carlisle/remreset.sty
/usr/share/texmf/tex/latex/carlisle/scalefnt.sty
/usr/share/texmf/tex/latex/carlisle/textcase.sty
/usr/share/texmf/tex/latex/carlisle/typehtml.sty

%files latex-caption
%doc /usr/share/texmf/doc/latex/caption
%dir /usr/share/texmf/tex/latex/caption
/usr/share/texmf/tex/latex/caption/caption2.sty
/usr/share/texmf/tex/latex/caption/caption.sty

%files latex-bbm
%dir /usr/share/texmf/tex/latex/bbm
/usr/share/texmf/tex/latex/bbm/bbm.sty
/usr/share/texmf/tex/latex/bbm/ubbm.fd
/usr/share/texmf/tex/latex/bbm/ubbmss.fd
/usr/share/texmf/tex/latex/bbm/ubbmtt.fd

%files latex-antt
%dir /usr/share/texmf/tex/latex/antt
/usr/share/texmf/tex/latex/antt/antyktor.sty
/usr/share/texmf/tex/latex/antt/ot1antt.fd
/usr/share/texmf/tex/latex/antt/ot4antt.fd
/usr/share/texmf/tex/latex/antt/qxantt.fd

%files latex-antp
%dir /usr/share/texmf/tex/latex/antp
/usr/share/texmf/tex/latex/antp/antpolt.sty
/usr/share/texmf/tex/latex/antp/lqxantp.fd
/usr/share/texmf/tex/latex/antp/ot4antp.fd
/usr/share/texmf/tex/latex/antp/qxantp.fd

%files latex-amsmath
%doc /usr/share/texmf/doc/latex/amsmath
%dir /usr/share/texmf/tex/latex/amsmath
/usr/share/texmf/tex/latex/amsmath/amsbsy.sty
/usr/share/texmf/tex/latex/amsmath/amscd.sty
/usr/share/texmf/tex/latex/amsmath/amsgen.sty
/usr/share/texmf/tex/latex/amsmath/amsmath.sty
/usr/share/texmf/tex/latex/amsmath/amsopn.sty
/usr/share/texmf/tex/latex/amsmath/amstex.sty
/usr/share/texmf/tex/latex/amsmath/amstext.sty
/usr/share/texmf/tex/latex/amsmath/amsxtra.sty

%files latex-amsfonts
%dir /usr/share/texmf/tex/latex/amsfonts
/usr/share/texmf/tex/latex/amsfonts/amsfonts.sty
/usr/share/texmf/tex/latex/amsfonts/amssymb.sty
/usr/share/texmf/tex/latex/amsfonts/cmmib57.sty
/usr/share/texmf/tex/latex/amsfonts/eucal.sty
/usr/share/texmf/tex/latex/amsfonts/eufrak.sty
/usr/share/texmf/tex/latex/amsfonts/euscript.sty
/usr/share/texmf/tex/latex/amsfonts/ueuex57.fd
/usr/share/texmf/tex/latex/amsfonts/ueuex.fd
/usr/share/texmf/tex/latex/amsfonts/ueuf57.fd
/usr/share/texmf/tex/latex/amsfonts/ueuf.fd
/usr/share/texmf/tex/latex/amsfonts/ueur57.fd
/usr/share/texmf/tex/latex/amsfonts/ueur.fd
/usr/share/texmf/tex/latex/amsfonts/ueus57.fd
/usr/share/texmf/tex/latex/amsfonts/ueus.fd
/usr/share/texmf/tex/latex/amsfonts/umsa57.fd
/usr/share/texmf/tex/latex/amsfonts/umsa.fd
/usr/share/texmf/tex/latex/amsfonts/umsb57.fd
/usr/share/texmf/tex/latex/amsfonts/umsb.fd

%files latex-amscls
%doc /usr/share/texmf/doc/latex/amscls
%dir /usr/share/texmf/tex/latex/amscls
/usr/share/texmf/tex/latex/amscls/amsart.cls
/usr/share/texmf/tex/latex/amscls/amsbook.cls
/usr/share/texmf/tex/latex/amscls/amsdtx.cls
/usr/share/texmf/tex/latex/amscls/amsldoc.cls
/usr/share/texmf/tex/latex/amscls/amsproc.cls
/usr/share/texmf/tex/latex/amscls/amsthm.sty
/usr/share/texmf/tex/latex/amscls/upref.sty

%files latex-algorith
%dir /usr/share/texmf/tex/latex/algorith
/usr/share/texmf/tex/latex/algorith/algorithmic.sty
/usr/share/texmf/tex/latex/algorith/algorithm.sty

%files latex-ae
%dir /usr/share/texmf/tex/latex/ae
/usr/share/texmf/tex/latex/ae/aecompl.sty
/usr/share/texmf/tex/latex/ae/ae.sty
/usr/share/texmf/tex/latex/ae/omlaer.fd
/usr/share/texmf/tex/latex/ae/omsaer.fd
/usr/share/texmf/tex/latex/ae/ot1aer.fd
/usr/share/texmf/tex/latex/ae/ot1aess.fd
/usr/share/texmf/tex/latex/ae/ot1aett.fd
/usr/share/texmf/tex/latex/ae/ot1laess.fd
/usr/share/texmf/tex/latex/ae/ot1laett.fd
/usr/share/texmf/tex/latex/ae/t1aer.fd
/usr/share/texmf/tex/latex/ae/t1aess.fd
/usr/share/texmf/tex/latex/ae/t1aett.fd
/usr/share/texmf/tex/latex/ae/t1laess.fd
/usr/share/texmf/tex/latex/ae/t1laett.fd

%files eplain
# mo¿e texmf/etex do jakiego¶ wspólnego pakietu?
%dir /usr/share/texmf/etex
%doc /usr/share/texmf/doc/etex
%doc /usr/share/texmf/doc/eplain
%dir /usr/share/texmf/etex/plain
%dir /usr/share/texmf/etex/plain/base
/usr/share/texmf/etex/plain/base/etexdefs.lib
/usr/share/texmf/etex/plain/base/etex.src
%dir /usr/share/texmf/etex/plain/config
/usr/share/texmf/etex/plain/config/etex.ini
/usr/share/texmf/etex/plain/config/language.def
/usr/share/texmf/tex/eplain


%files elatex
%dir /usr/share/texmf/etex/latex
%dir /usr/share/texmf/etex/latex/config
/usr/share/texmf/etex/latex/config/elatex.ini
%dir /usr/share/texmf/etex/latex/misc
/usr/share/texmf/etex/latex/misc/etex.sty

%files fontname
# z dokumentacji wynika ¿e nie ma sensu tego rozdzielaæ po pakietach
%doc /usr/share/texmf/doc/fonts/fontname
%dir /usr/share/texmf/fontname
/usr/share/texmf/fontname/adobe.map
/usr/share/texmf/fontname/apple.map
/usr/share/texmf/fontname/bitstrea.map
/usr/share/texmf/fontname/dtc.map
/usr/share/texmf/fontname/itc.map
/usr/share/texmf/fontname/linot-cd.map
/usr/share/texmf/fontname/linotype.map
/usr/share/texmf/fontname/monotype.map
/usr/share/texmf/fontname/skey1250.map
/usr/share/texmf/fontname/skey1555.map
/usr/share/texmf/fontname/softkey.map
/usr/share/texmf/fontname/special.map
/usr/share/texmf/fontname/supplier.map
/usr/share/texmf/fontname/texfonts.map
/usr/share/texmf/fontname/typeface.map
/usr/share/texmf/fontname/urw.map
/usr/share/texmf/fontname/variant.map
/usr/share/texmf/fontname/weight.map
/usr/share/texmf/fontname/width.map
/usr/share/texmf/fontname/wolfram.map
/usr/share/texmf/fontname/yandy.map


%files babel
%doc /usr/share/texmf/doc/generic/babel
/usr/share/texmf/tex/generic/babel

%files tex-misc
%doc /usr/share/texmf/doc/generic/poligraf
%doc /usr/share/texmf/doc/generic/localloc
%doc /usr/share/texmf/doc/generic/cmyk-hax
%dir /usr/share/texmf/tex/generic/misc
/usr/share/texmf/tex/generic/misc/cmyk-hax.tex
/usr/share/texmf/tex/generic/misc/epsfx.tex
/usr/share/texmf/tex/generic/misc/letterspacing.tex
/usr/share/texmf/tex/generic/misc/localloc.sty
/usr/share/texmf/tex/generic/misc/null.tex
/usr/share/texmf/tex/generic/misc/path.sty
/usr/share/texmf/tex/generic/misc/poligraf.sty
/usr/share/texmf/tex/generic/misc/psfig.sty
/usr/share/texmf/tex/generic/misc/random.tex
/usr/share/texmf/tex/generic/misc/tap.tex
/usr/share/texmf/tex/generic/misc/texnames.sty
/usr/share/texmf/tex/generic/misc/trans.tex

%files tex-pstriks
%doc /usr/share/texmf/doc/generic/pstricks
/usr/share/texmf/tex/generic/pstricks

%files tex-pictex
/usr/share/texmf/tex/generic/pictex

%files tex-ruhyphen
%doc /usr/share/texmf/doc/generic/ruhyphen
/usr/share/texmf/tex/generic/ruhyphen

%files tex-spanishb
/usr/share/texmf/tex/generic/spanishb

%files tex-texdraw
%doc /usr/share/texmf/doc/generic/texdraw
/usr/share/texmf/tex/generic/texdraw

%files tex-thumbpdf
%doc /usr/share/texmf/doc/generic/thumbpdf
/usr/share/texmf/tex/generic/thumbpdf

%files tex-ukrhyph
%doc /usr/share/texmf/doc/generic/ukrhyph
/usr/share/texmf/tex/generic/ukrhyph

%files tex-vietnam
/usr/share/texmf/tex/generic/vietnam

%files tex-xypic
%doc /usr/share/texmf/doc/generic/xypic
/usr/share/texmf/tex/generic/xypic

%files tex-mfpic
%doc /usr/share/texmf/doc/generic/mfpic
/usr/share/texmf/tex/generic/mfpic

%files tex-hyphen
/usr/share/texmf/tex/generic/hyphen

%files tex-german
/usr/share/texmf/tex/generic/german

%files tex-eijkhout
/usr/share/texmf/tex/generic/eijkhout
