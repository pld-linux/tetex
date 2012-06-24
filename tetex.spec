
%define		_ver	beta-20020208
%define		texmf_ver	beta-20020207

Summary:	TeX typesetting system and MetaFont font formatter
Summary(de):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(es):	Sistema de typesetting TeX y formateador de fuentes MetaFont
Summary(fr):	Syst�me de compostion TeX et formatteur de MetaFontes
Summary(pl):	System sk�adu publikacji TeX oraz formater font�w MetaFont
Summary(pt_BR):	Sistema de typesetting TeX e formatador de fontes MetaFont
Summary(tr):	TeX dizgi sistemi ve MetaFont yaz�tipi bi�imlendiricisi
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

%define		texmf	%{_datadir}/texmf

%description
teTeX is an implementation of TeX for Linux or UNIX systems. TeX takes
a text file and a set of formatting commands as input and creates a
typesetter independent .dvi (DeVice Independent) file as output.
Usually, TeX is used in conjunction with a higher level formatting
package like LaTeX or PlainTeX, since TeX by itself is not very
user-friendly.

%description -l es
Tex formata archivos de texto y �rdenes para una salida independiente
de dispositivo (que se llama DVI - DeVice Independent). En The TeXbook
de Knut se describen las capacidades y el lenguaje TeX.

%description -l de
TeX formatiert eine Datei, die abwechselnd Text und Befehle enth�lt
und gibt eine ger�teunabh�ngige Datei aus (DVI genannt, Abk. f�r
DeVice Independent). Die Funktionen und Sprache von TeX werden in The
TeXbook von Knuth beschrieben.

%description -l fr
TeX formate un fichier de commandes et de texte m�land�s, et produit
un fichier de ind�pendant de toute plate-forme (appel� DVI, qui est un
raccourci pour Device Independant). Les possibilit�s de TeX et son
langage sont d�crites dans l'ouvrage TeXbook, de Knuth.

%description -l pl
TeX formatuje przygotowany tekst oraz komendy i produkuje niezale�ny
od urz�dzenia plik wynikowy (tzw. DVI -- skr�t od DeVice Independent).
Mo�liwo�ci TeXa, oraz jego j�zyk zosta�y opisane w ,,The TeXbook''
Donalda E. Knutha.

%description -l pt_BR
Tex formata arquivos de texto e comandos para uma sa�da independente
de dispositivo (chamado DVI - DeVice Independent). As capacidades e a
linguagem TeX s�o descritas no The TeXbook, de Knuth.

%description -l tr
TeX, i�inde metin ve komutlar�n yer ald��� bir dosyay� okur ve dizgi
ayg�t�ndan ba��ms�z bir ��kt� (DeVice Independent - DVI) olu�turur.
TeX'in becerileri ve dizgi dili, dili geli�tiren Knuth'un 'The
TeXbook' ba�l�kl� kitab�nda anlat�lmaktad�r.

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
PreReq:		%{_bindir}/texhash

%description latex
LaTeX is a front end for the TeX text formatting system. Easier to use
than TeX, LaTeX is essentially a set of TeX macros which provide
convenient, predefined document formats for users.

%description latex -l de
LaTeX ist ein TeX-Makropaket. Die LaTeX-Makros regen den Autor an,
�ber den Inhalt - und nicht die Form - ihrer Dokumente nachzudenken.
Ideal, wenn auch schwer zu realisieren, w�re ein Dokument, das
keinerlei Formatierungsbefehle (von der Art 'Kursiv ein/aus' oder
'Zeilenabstand um 2 Pica vergr��ern') enthielte. Stattdessen w�rde all
dies durch spezifische 'redaktionelle' Instruktionen ersetzt
('auszeichnen', 'neues Kapitel starten').

%description latex -l es
LaTeX es un paquete de macros TeX. Las macros LaTeX impulsionan
escritores a pensar sobre el contenido de sus documentos, y no en su
forma. Lo ideal, muy dif�cil de realizar, es no tener ning�n comando
de fomatear (como ''switch to italic'' 0 ''skip 2 points'') en el
documento; en lugar de esto, todo se hace especificando instrucciones
de marcado: : ''emphasize'', ''start la section''.

%description latex -l fr
LaTeX est un paquetage de macros TeX. Les macros LaTeX permettent aux
auteurs de se concentrer sur le contenu des leurs documents, plut�t
que sur la forme. L'id�al, tr�s difficile � r�aliser, est de n'avoir
aucune commande de formatage (comme � mettre en italique �, ou �
sauter 2 picas �) dans le document ; au lieu de cela, tout est fait
par des balises : � d�but de section �, � gras �.

%description latex -l pl
LaTeX jest zestawem makr TeXowych. Makra LaTeXa u�atwiaj� pisz�cym
my�lenie o zawarto�ci dokumentu, zamiast o jego wygl�dzie. Idealny,
bardzo trudny do implementacji system nie powinien posiada� komend
formatuj�cych (takich jak ,,pisz kursyw�'', czy prze��cz na font 8
punktowy) a jedynie polecenia znakuj�ce takie jak np. podkre�l, czy
zacznij sekcj�. LaTeX powoli zbli�a si� do tego idea�u, nie odrzucaj�c
mo�liwo�ci ingerencji w wygl�d dokumentu.

%description latex -l pt_BR
LaTeX � um pacote de macros TeX. Os macros LaTeX encorajam escritores
a pensar sobre o conte�do de seus documentos, e n�o na forma. O ideal,
muito dif�cil de realizar, � n�o ter nenhum comando de formata��o
(como ``switch to italic'' ou ``skip 2 picas'') no documento; no lugar
disto, tudo � feito especificando instru��es de marca��o:
``emphasize'', ``start a section''.

%description latex -l tr
LaTeX bir TeX makro paketidir. LaTeX makrolar�, yazarlar� belgelerinin
bi�imlerinden �ok i�erikleri �zerinde yo�unla�mlar�na �zendirir.
�dealde, ger�ekle�tirilmesi �ok zor olsa da, hi� bi�imlendirme
komutuna yer vermeksizin (``2 birim aral�k b�rak'' gibi), yaln�zca
�zel i�aretleme y�nergeleri ile (``yeni bir kesime ge�'' gibi) bunu
ba�armaya �al���r.

%package dvips
Summary:	dvi to postscript convertor
Summary(de):	dvi-Postscript-Konvertierungsprogramm
Summary(es):	Convertidor dvi para postscript
Summary(fr):	Convertisseur dvi vers PostScript
Summary(pl):	Konwerter dvi do postscriptu
Summary(pt_BR):	Conversor dvi para postscript
Summary(tr):	dvi'dan postscript'e d�n��t�r�c�
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
enviando el resultado directamente a la impresora l�ser.

%description dvips -l fr
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le r�sultat directement sur une imprimante Laser.

%description dvips -l pl
Program dvips bierze plik DVI wygenerowany przez TeXa (lub jaki� inny
program, jak na przyk�ad GFtoDVI) i konwertuje go do PostScriptu.
Domy�lnie wynik jest wysy�any bezpo�rednio do drukarki.

%description dvips -l pt_BR
O programa dvips toma um arquivo DVI (.dvi) produzido pelo TeX (ou por
outro processador como o GFtoDVI) e o converte para PostScript,
normalmente enviando o resultado diretamente para a impressora laser.

%description dvips -l tr
dvips program�, dvi bi�iminde bir girdi dosyas� al�r ve onu
PostScript'e d�n��t�r�r. Kaynak dosya TeX taraf�ndan olu�turulmu�
olabilece�i gibi ba�ka i�leyiciler taraf�ndan da (GFtoDVI gibi)
�retilmi� olabilir.

%package dvilj
Summary:	dvi to laserjet convertor
Summary(de):	Ein dvi-->Laserjet-Konvertierer
Summary(es):	Convertidor dvi para laserjet
Summary(fr):	convertisseur dvi vers laserjet.
Summary(pl):	Konwerter dvi do laserjet
Summary(pt_BR):	Conversor dvi para laserjet
Summary(tr):	dvi'dan laserjet'e d�n��t�r�c�
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
Dvilj und Gebr�der konvertieren TeX-Ausgabe-.dvi-Dateien in HP PCL (HP
Printer Control Language) Befehle zum Drucken auf HP LaserJet+, HP
LaserJet IIP (mit dvilj2p), HP LaserJet 4 (mit dvilj4) und vollst�ndig
kompatiblen Druckern.

%description dvilj -l es
Dvilj y semejantes convierten archivos de salida TeX.dvi en comandos
HP PCL (i.e. Lenguaje de Control de Impresoras HP) adecuados a
impresi�n de impresoras HP LaserJEt+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) y compatibles.

%description dvilj -l fr
dvilj et ses cousins convertissent les fichiers dvi en commandes HPPCL
(le langage des imprimantes HP) pour les imprimer sur HP LaserJet+, HP
LaserJet IIP (avec dvilj2p), HP LaserJet 4 (avec dvilj4), et autres
imprimantes totalement compatibles.

%description dvilj -l pt_BR
Dvilj e semelhantes convertem arquivos de sa�da TeX .dvi em comandos
HP PCL (i.e. Linguagem de Controle de Impressoras HP) adequados para
impress�o em impressoras HP LaserJet+, HP LaserJet IIP (usando
dvilj2p), HP LaserJet 4 (usando dvilj4) e compat�veis.

%description dvilj -l tr
TeX ��kt�s� dvi dosyalar�n� HP PCL (HP'nin geli�tirdi�i bir yaz�c�
denetim dili) komutlar�na �evirir ve b�ylece bir LaserJet+, HP
LaserJet IIP (dvilj2p ile), HP LaserJet4 (dvilj4 ile) ve tam
uyumlular�ndan yaz�c� ��kt�s� al�nabilir.

%package amstex
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makra dla LaTeX
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description amstex
American Mathematics Society macros for plainTeX.

%description amstex -l pl
Makra American Mathematics Society do sk�adania publikacji
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

%package omega
Summary:	extended unicode TeX
Summary(pl):	Rozszerzony unicode TeX
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}
PreReq:		%{_bindir}/texhash

%description omega
Omega is extended unicode TeX.

%description omega -l pl
Omega -- TeX ze wsparciem dla Unicode.

%package oxdvi
Summary:	xdvi viewer for Omega
Summary(pl):	Przegl�darka xdvi dla Omegi
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}

%description oxdvi
xdvi viewer for Omega - extended unicode TeX.

%description oxdvi -l pl
Przegl�darka xdvi dla Omegi -- TeXa ze wsparciem dla Unicode.

%package pdftex
Summary:	PDFtex
Summary(pl):	PDFtex
Group:		Applications/Publishing/TeX
Requires:	%{name} = %{version}

%description pdftex
TeX generating PDFs instead DVI.

%description pdftex -l pl
PDFTeX generuje pliki PDF na podstawie plik�w DVI.

%package -n xdvi
Summary:	X11 previewer
Summary(de):	X11-Previewer
Summary(es):	Visualizador TeX X11
Summary(fr):	Pr�visualisateur X11
Summary(pl):	Przegl�darka DVI dla X11
Summary(pt_BR):	Visualizador TeX X11
Summary(tr):	X11 �ng�r�nt�leyici
Requires:	%{name} = %{version}
Group:		Applications/Publishing/TeX
Obsoletes:	tetex-xdvi

%description -n xdvi
xdvi is a program which runs under the X window system. It is used to
preview dvi files, such as are produced by tex and latex.

%description -n xdvi -l de
xdvi ist ein Programm, das unter dem X-Window-System l�uft und gewohnt
ist, dvi-Dateien als Vorschau anzuzeigen, etwa solche, die von tex und
latex erzeugt wurden.

%description -n xdvi -l es
xdvi es un programa que se ejecuta en el sistema X Window. Se usa para
visualizar archivos dvi, como los producidos por tex y latex.

%description -n xdvi -l fr
xdvi est un programme s'ex�cutant sous le syst�me X Window. Il sert �
visualiser les fichiers dvi tels que ceux produits par tex et latex.

%description -n xdvi -l pl
Xdvi jest programem (dzia�aj�cym w X Window System) do przegl�dania
plik�w DVI, produkowanych przez TeXa i LaTeXa.

%description -n xdvi -l pt_BR
xdvi � um programa que roda no sistema X Window. � usado para
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
Pakiet tetex-fonts zawiera czcionki u�ywane przez TeXa oraz Xdvi.
Je�eli chcesz korzysta� z kt�rego� z tych program�w, musisz
zainstalowa� ten pakiet.

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
Dokumentacja do TeXa. Je�eli chcesz korzysta� z TeXa to powiniene�
zainstalowa� ten pakiet.

%package -n kpathsea-devel
Summary:	Kpathsea library filename lookup header files and documentation
Summary(es):	Bibliotecas y archivos de inclusi�n para desarrollo TeX
Summary(pl):	Pliki nag��wkowe oraz dokumetacja kpathsea
Summary(pt_BR):	Bibliotecas e headers para desenvolvimento TeX
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description -n kpathsea-devel
Kpathsea library filename lookup header files and documentation.

%description -n kpathsea-devel -l es
Bibliotecas, archivos de inclusi�n, etc, para que puedas desarrollar
aplicaciones TeX.

%description -n kpathsea-devel -l pl
Pliki nag��wkowe oraz dokumentacja biblioteki kpathsea.

%description -n kpathsea-devel -l pt_BR
Bibliotecas, headers e outros componentes que podem ser utilizados
para desenvolver aplica��es TeX.

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
Requires:	%{name} = %{version}

%description fonts-bitstrea
fonts-bitstrea

%package fonts-antp
Summary:	fonts-antp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-antp
fonts-antp

%package fonts-antt
Summary:	fonts-antt
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-antt
fonts-antt

%package fonts-marvosym
Summary:	fonts-marvosym
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-marvosym
fonts-marvosym

%package fonts-omega
Summary:	fonts-omega
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-omega
fonts-omega

%package fonts-qfonts
Summary:	fonts-qfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-qfonts
fonts-qfonts

%package fonts-xypic
Summary:	fonts-xypic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-xypic
fonts-xypic

%package fonts-urw
Summary:	fonts-urw
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-urw
fonts-urw

%package fonts-yandy
Summary:	fonts-yandy
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-yandy
fonts-yandy

%package fonts-ams
Summary:	fonts-ams
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-ams
fonts-ams

%package fonts-jknappen
Summary:	fonts-jknappen
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-jknappen
fonts-jknappen

%package fonts-lh
Summary:	fonts-lh
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-lh
fonts-lh

%package fonts-bbm
Summary:	fonts-bbm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-bbm
fonts-bbm

%package fonts-bbold
Summary:	fonts-bbold
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-bbold
fonts-bbold

%package fonts-cbgreek
Summary:	fonts-cbgreek
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cbgreek
fonts-cbgreek

%package fonts-cc-pl
Summary:	fonts-cc-pl
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cc-pl
fonts-cc-pl

%package fonts-cm
Summary:	fonts-cm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cm
fonts-cm

%package fonts-cmcyr
Summary:	fonts-cmcyr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cmcyr
fonts-cmcyr

%package fonts-cm-bold
Summary:	fonts-cm-bold
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cm-bold
fonts-cm-bold

%package fonts-cmextra
Summary:	fonts-cmextra
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cmextra
fonts-cmextra

%package fonts-concmath
Summary:	fonts-concmath
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-concmath
fonts-concmath

%package fonts-concrete
Summary:	fonts-concrete
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-concrete
fonts-concrete

%package fonts-cs
Summary:	fonts-cs
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cs
fonts-cs

%package fonts-dstroke
Summary:	fonts-dstroke
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-dstroke
fonts-dstroke

%package fonts-ecc
Summary:	fonts-ecc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-ecc
fonts-ecc

%package fonts-euxm
Summary:	fonts-euxm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-euxm
fonts-euxm

%package fonts-gothic
Summary:	fonts-gothic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-gothic
fonts-gothic

%package fonts-latex
Summary:	fonts-latex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-latex
fonts-latex

%package fonts-mflogo
Summary:	fonts-mflogo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-mflogo
fonts-mflogo

%package fonts-misc
Summary:	fonts-misc
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-misc
fonts-misc

%package fonts-pandora
Summary:	fonts-pandora
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-pandora
fonts-pandora

%package fonts-pl
Summary:	fonts-pl
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-pl
fonts-pl

%package fonts-rsfs
Summary:	fonts-rsfs
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-rsfs
fonts-rsfs

%package fonts-stmaryrd
Summary:	fonts-stmaryrd
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-stmaryrd
fonts-stmaryrd

%package fonts-vnr
Summary:	fonts-vnr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-vnr
fonts-vnr

%package fonts-wasy
Summary:	fonts-wasy
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-wasy
fonts-wasy

%package fonts-bh
Summary:	fonts-bh
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-bh
fonts-bh

%package fonts-cg
Summary:	fonts-cg
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-cg
fonts-cg

%package fonts-hoekwater
Summary:	fonts-hoekwater
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-hoekwater
fonts-hoekwater

%package fonts-monotype
Summary:	fonts-monotype
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-monotype
fonts-monotype

%package fonts-ae
Summary:	fonts-ae
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-ae
fonts-ae

%package fonts-mathpple
Summary:	fonts-mathpple
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-mathpple
fonts-mathpple

%package fonts-pazo
Summary:	fonts-pazo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-pazo
fonts-pazo

%package fonts-vcm
Summary:	fonts-vcm
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-vcm
fonts-vcm

%package fonts-type1-adobe
Summary:	fonts-type1-adobe
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-adobe
fonts-type1-adobe

%package fonts-type1-bitstrea
Summary:	fonts-type1-bitstrea
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-bitstrea
fonts-type1-bitstrea

%package fonts-type1-bluesky
Summary:	fonts-type1-bluesky
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-bluesky
fonts-type1-bluesky

%package fonts-type1-hoekwater
Summary:	fonts-type1-hoekwater
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-hoekwater
fonts-type1-hoekwater

%package fonts-type1-antp
Summary:	fonts-type1-antp
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-antp
fonts-type1-antp

%package fonts-type1-antt
Summary:	fonts-type1-antt
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-antt
fonts-type1-antt

%package fonts-type1-belleek
Summary:	fonts-type1-belleek
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-belleek
fonts-type1-belleek

%package fonts-type1-cmcyr
Summary:	fonts-type1-cmcyr
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-cmcyr
fonts-type1-cmcyr

%package fonts-type1-cs
Summary:	fonts-type1-cs
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-cs
fonts-type1-cs

%package fonts-type1-marvosym
Summary:	fonts-type1-marvosym
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-marvosym
fonts-type1-marvosym

%package fonts-type1-mathpazo
Summary:	fonts-type1-mathpazo
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-mathpazo
fonts-type1-mathpazo

%package fonts-type1-omega
Summary:	fonts-type1-omega
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-omega
fonts-type1-omega

%package fonts-type1-pl
Summary:	fonts-type1-pl
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-pl
fonts-type1-pl

%package fonts-type1-qfonts
Summary:	fonts-type1-qfonts
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-qfonts
fonts-type1-qfonts

%package fonts-type1-xypic
Summary:	fonts-type1-xypic
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description fonts-type1-xypic
fonts-type1-xypic

%package fonts-type1-urw
Summary:	fonts-type1-urw
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

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

%package omega-lambda
Summary:	omega-lambda
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description omega-lambda
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

%package pdfetex
Summary:	pdfetex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfetex
pdfetex

%package pdfelatex
Summary:	pdfelatex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfelatex
pdfelatex

%package pdfemex
Summary:	pdfemex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfemex
pdfemex

%package pdftex-amstex
Summary:	pdftex-amstex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdftex-amstex
pdftex-amstex

%package pdftex-context
Summary:	pdftex-context
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdftex-context
pdftex-context

%package pdflatex
Summary:	pdflatex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdflatex
pdflatex

%package pdfmex
Summary:	pdfmex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfmex
pdfmex

%package pdfplatex
Summary:	pdfplatex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description pdfplatex
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

%package context
Summary:	context
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description context
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
Summary:	platex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description platex
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

%package elatex
Summary:	elatex
Group:		Applications/Publishing/TeX
Requires(post):	/usr/bin/texhash
Requires(postun):	/usr/bin/texhash
Requires:	%{name} = %{version}

%description elatex
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

%post amstex
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 1>&2
exit 0

%postun amstex
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

%files
%defattr(644,root,root,755)
%{_datadir}/info/web2c.info*

%files -n kpathsea-devel
%defattr(644,root,root,755)
%{_includedir}/kpathsea
%{_libdir}/libkpathsea.so
%{_infodir}/kpathsea.info*

%files -n kpathsea
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/kpathsea.dvi
%doc %{texmf}/doc/programs/kpathsea.pdf
%{_libdir}/libkpathsea.so.3.3.7

%files dvips
%defattr(644,root,root,755)
%doc %{texmf}/doc/programs/dvips.dvi
%attr(755,root,root) %{_bindir}/dvips
%{_infodir}/dvips.info*
%lang(fi) %{_mandir}/fi/man1/dvips.1*
%{_mandir}/man1/dvips.1*
%dir %{texmf}/dvips

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
# hmm, mo�e jeszcze rozpisa�?
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
%{texmf}/makeindex

%files metafont
%defattr(644,root,root,755)
%{texmf}/metafont

%files matapost
%defattr(644,root,root,755)
%doc %{texmf}/doc/metapost
%dir %{texmf}/metapost
%{texmf}/metapost/base
%{texmf}/metapost/config
%{texmf}/metapost/mfpic
%{texmf}/metapost/misc
#%files metapost-context
%{texmf}/metapost/context

%files omega
%defattr(644,root,root,755)
%doc %{texmf}/doc/omega
%dir %{texmf}/omega
%{texmf}/omega/encodings
#%files omega-plain
%dir %{texmf}/omega/plain
%{texmf}/omega/plain/base
%{texmf}/omega/plain/config

%files omega-lambda
%defattr(644,root,root,755)
%dir %{texmf}/omega/lambda
%{texmf}/omega/lambda/base
%{texmf}/omega/lambda/config
%{texmf}/omega/lambda/misc

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

%files pdfetex
%defattr(644,root,root,755)
%dir %{texmf}/pdfetex
%dir %{texmf}/pdfetex/tex
%{texmf}/pdfetex/tex/config

%files pdfelatex
%defattr(644,root,root,755)
%dir %{texmf}/pdfetex/latex
%{texmf}/pdfetex/latex/config

%files pdfemex
%defattr(644,root,root,755)
%dir %{texmf}/pdfetex/mex
%{texmf}/pdfetex/mex/config

%files pdftex
%defattr(644,root,root,755)
%doc %{texmf}/doc/pdftex
%dir %{texmf}/pdftex
%dir %{texmf}/pdftex/config
%{texmf}/pdftex/config/cmttf.map
%{texmf}/pdftex/config/pdftex.cfg
%dir %{texmf}/pdftex/plain
%{texmf}/pdftex/plain/config
%{texmf}/pdftex/plain/misc

%files pdftex-amstex
%defattr(644,root,root,755)
%doc %{texmf}/doc/amstex
%dir %{texmf}/pdftex/amstex
%{texmf}/pdftex/amstex/config

%files pdftex-context
%defattr(644,root,root,755)
# zferyfikowac pliki z fontami
%{texmf}/pdftex/config/context

%files pdflatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/latex
%{texmf}/pdftex/latex/config

%files pdfmex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/mex
%{texmf}/pdftex/mex/config

%files pdfplatex
%defattr(644,root,root,755)
%dir %{texmf}/pdftex/platex
%{texmf}/pdftex/platex/config

%files tex
%defattr(644,root,root,755)
%dir %{texmf}/tex
%dir %{texmf}/tex/generic
%dir %{texmf}/tex/generic/config
%{texmf}/tex/generic/config/fontmath.cfg
%{texmf}/tex/generic/config/fonttext.cfg
%{texmf}/tex/generic/config/language.dat
%{texmf}/tex/generic/config/preload.cfg

%files amstex
%defattr(644,root,root,755)
%dir %{texmf}/tex/amstex
%{texmf}/tex/amstex/base
%{texmf}/tex/amstex/config
%{texmf}/web2c/amstex.fmt
%{texmf}/web2c/bamstex.fmt

%files texconfig
%defattr(644,root,root,755)
%{texmf}/texconfig

%files context
%defattr(644,root,root,755)
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

%{texmf}/tex/csplain

%files cyrplain
%defattr(644,root,root,755)
%doc %{texmf}/doc/cyrplain
%dir %{texmf}/tex/cyrplain
%{texmf}/tex/cyrplain/base
%{texmf}/tex/cyrplain/config

%files texdoctk
%defattr(644,root,root,755)
%doc %{texmf}/doc/texdoctk
%{texmf}/texdoctk

%files fontinst
%defattr(644,root,root,755)
# zferyfikowa� zawarto�� z tym co jest w pakietach z fontami
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
%{texmf}/doc/tetex
%{texmf}/doc/tetex.gif
%{texmf}/doc/tetex.png


%files platex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/platex
%dir %{texmf}/tex/platex
%dir %{texmf}/tex/platex/config
%{texmf}/tex/platex/config/hyphen.cfg
%{texmf}/tex/platex/config/language.dat
%{texmf}/tex/platex/config/platex.ini
# a mo�e jako� osobno to da�?
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
%{texmf}/tex/plain/dvips
%{texmf}/tex/plain/dvips/blackdvi.tex
%{texmf}/tex/plain/dvips/colordvi.tex
%{texmf}/tex/plain/dvips/dvipsmac.tex
%{texmf}/tex/plain/dvips/epsf.tex
%{texmf}/tex/plain/dvips/rotate.tex
%{texmf}/tex/plain/dvips/rotsample.tex

%files plain
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain/config
# bplain tu czy mo�e gdzie� indziej?
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
%{texmf}/web2c/bplain.fmt

%files plain-amsfonts
%defattr(644,root,root,755)
%dir %{texmf}/tex/plain
%{texmf}/tex/plain/amsfonts
%{texmf}/tex/plain/amsfonts/amssym.def
%{texmf}/tex/plain/amsfonts/amssym.tex
%{texmf}/tex/plain/amsfonts/cyracc.def

%files mex
%defattr(644,root,root,755)
%doc %{texmf}/doc/polish/mex
%dir %{texmf}/tex/mex
%{texmf}/tex/mex/base
%{texmf}/tex/mex/base/mex1.tex
%{texmf}/tex/mex/base/mex2.tex
%{texmf}/tex/mex/base/mex.tex
%dir %{texmf}/tex/mex/config
%{texmf}/tex/mex/config/mexconf.tex
%{texmf}/tex/mex/config/mex.ini

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
%{texmf}/tex/latex/t2
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
%{texmf}/tex/latex/revtex4
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

%files latex
%defattr(644,root,root,755)
%doc %{texmf}/doc/latex/general
%doc %{texmf}/doc/latex/base
%{_infodir}/latex.info*
%lang(fi) %{_mandir}/fi/man1/latex.1*
%lang(pl) %{_mandir}/pl/man1/latex.1*
%{_mandir}/man1/latex.1*
%attr(755,root,root) %{_bindir}/latex
%dir %{texmf}/tex/latex/config
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
# mo�e texmf/etex do jakiego� wsp�lnego pakietu?
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


%files elatex
%defattr(644,root,root,755)
%dir %{texmf}/etex/latex
%dir %{texmf}/etex/latex/config
%{texmf}/etex/latex/config/elatex.ini
%dir %{texmf}/etex/latex/misc
%{texmf}/etex/latex/misc/etex.sty

%files fontname
%defattr(644,root,root,755)
# z dokumentacji wynika �e nie ma sensu tego rozdziela� po pakietach
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
%{texmf}/tex/generic/thumbpdf

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
