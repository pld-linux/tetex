%define		texmf_ver	1.0
Summary:	TeX typesetting system and MetaFont font formatter
Summary(de):	TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(fr):	Syst�me de compostion TeX et formatteur de MetaFontes.
Summary(pl):	System sk�adu publikacji TeX oraz formater font�w MetaFont 
Summary(tr):	TeX dizgi sistemi ve MetaFont yaz�tipi bi�imlendiricisi
Name:		tetex
Version:	1.0.6
Release:	0.1
Copyright:	distributable
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Source0:	ftp://sunsite.informatik.rwth-aachen.de/pub/comp/tex/teTeX/1.0/distrib/sources/teTeX-src-%{version}.tar.gz
Source1:	ftp://sunsite.informatik.rwth-aachen.de/pub/comp/tex/teTeX/1.0/distrib/sources/teTeX-texmf-%{texmf_ver}.tar.gz
Source2:	ftp://sunsite.informatik.rwth-aachen.de/pub/comp/tex/teTeX/1.0/distrib/sources/teTeX-texmfsrc-%{texmf_ver}.tar.gz
Source3:	dvi-to-ps.fpi
Source4:	tetex.cron
Patch0:		teTeX-rhconfig.patch  
Patch1:		teTeX-buildr.patch
Patch2:		teTeX-manpages.patch
Patch3:		teTeX-arm.patch
Patch4:		teTeX-info.patch
Patch5:		teTeX-klibtool.patch
Patch6:		teTeX-texi2html.patch
URL:		http://www.tug.org/teTeX/
Requires:	tmpwatch
Requires:	dialog
Prereq:		/sbin/ldconfig
Prereq:		/sbin/install-info
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	XFree86-devel
BuildRequires:	ed
Obsoletes:	tetex-texmf-src
Obsoletes:	tetex-doc
BuildRoot:	/tmp/%{name}-%{version}-root

%description
TeX formats a file of interspersed text and commands and outputs a
typesetter independent file (called DVI, which is short for DeVice
Independent). TeX capabilities and language are described in The TeXbook, by
Knuth.

%description -l de
TeX formatiert eine Datei, die abwechselnd Text und Befehle enth�lt und gibt
eine ger�teunabh�ngige Datei aus (DVI genannt, Abk. f�r DeVice Independent).
Die Funktionen und Sprache von TeX werden in The TeXbook von Knuth
beschrieben.

%description -l fr
TeX formate un fichier de commandes et de texte m�land�s, et produit un
fichier de ind�pendant de toute plate-forme (appel� DVI, qui est un
raccourci pour Device Independant). Les possibilit�s de TeX et son langage
sont d�crites dans l'ouvrage TeXbook, de Knuth.

%description -l pl 
TeX formatuje przygotowany tekst oraz komendy i produkuje niezale�ny od
urz�dzenia plik wynikowy (tzw. DVI -- skr�t od DeVice Independent). 
Mo�liwo�ci TeXa, oraz jego j�zyk zosta�y opisane w
,,The TeXbook'' Donalda E. Knutha.

%description -l tr
TeX, i�inde metin ve komutlar�n yer ald��� bir dosyay� okur ve dizgi
ayg�t�ndan ba��ms�z bir ��kt� (DeVice Independent - DVI) olu�turur. TeX'in
becerileri ve dizgi dili, dili geli�tiren Knuth'un 'The TeXbook' ba�l�kl�
kitab�nda anlat�lmaktad�r.

%package latex
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makro-pakiet LaTeX
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}
Prereq:		/sbin/install-info

%description latex
LaTeX is a TeX macro package. The LaTeX macros encourage writers to think
about the content of their documents, rather than the form.  The ideal, very
difficult to realize, is to have no formatting commands (like ``switch to
italic'' or ``skip 2 picas'') in the document at all; instead, everything is
done by specific markup instructions: ``emphasize'', ``start a section''.

%description -l de latex
LaTeX ist ein TeX-Makropaket. Die LaTeX-Makros regen den Autor an, �ber den
Inhalt - und nicht die Form - ihrer Dokumente nachzudenken.  Ideal, wenn
auch schwer zu realisieren, w�re ein Dokument, das keinerlei
Formatierungsbefehle (von der Art 'Kursiv ein/aus' oder 'Zeilenabstand um 2
Pica vergr��ern') enthielte. Stattdessen w�rde all dies durch spezifische
'redaktionelle' Instruktionen ersetzt ('auszeichnen', 'neues Kapitel
starten').

%description -l fr latex
LaTeX est un paquetage de macros TeX. Les macros LaTeX permettent aux
auteurs de se concentrer sur le contenu des leurs documents, plut�t que sur
la forme. L'id�al, tr�s difficile � r�aliser, est de n'avoir aucune commande
de formatage (comme � mettre en italique �, ou � sauter 2 picas �) dans le
document ; au lieu de cela, tout est fait par des balises : � d�but de
section �, � gras �.

%description -l pl latex
LaTeX jest zestawem makr TeXowych. Makra LaTeX macros u�atwiaj� pisz�cym
my�lenie o zawarto�ci dokumentu, zamiast o jego wygl�dzie.  Idealny, bardzo
trudny do implementacji system nie powinien posiada� komend formatuj�cych
(takich jak ,,pisz kursyw�'', czy prze��cz na font 8 punktowy) a jedynie
polecenia znakuj�ce takie jak np. podkre�l, czy zacznij sekcj�. LaTeX powoli
zbli�a si� do tego idea�u, nie odrzucaj�c mo�liwo�ci ingerencji w wygl�d
dokumentu.

%description -l tr latex
LaTeX bir TeX makro paketidir. LaTeX makrolar�, yazarlar� belgelerinin
bi�imlerinden �ok i�erikleri �zerinde yo�unla�mlar�na �zendirir. �dealde,
ger�ekle�tirilmesi �ok zor olsa da, hi� bi�imlendirme komutuna yer
vermeksizin (``2 birim aral�k b�rak'' gibi), yaln�zca �zel i�aretleme
y�nergeleri ile (``yeni bir kesime ge�'' gibi) bunu ba�armaya �al���r.

%package dvips
Summary:	dvi to postscript convertor
Summary(de):	dvi-Postscript-Konvertierungsprogramm
Summary(fr):	Convertisseur dvi vers PostScript
Summary(pl):	Konwerter dvi do postscriptu
Summary(tr):	dvi'dan postscript'e d�n��t�r�c�
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}
Prereq:		/sbin/install-info

%description dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by some
other processor such as GFtoDVI) and converts it to PostScript, normally
sending the result directly to the laserprinter.

%description -l de dvips
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX bzw. durch
einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und konvertiert diese in
PostScript, wobei das Ergebnis in der Regel direkt an einen Laserdrucker
gesandt wird.

%description -l fr dvips
Le programme dvips convertit les fichiers DVI en PostScript, en envoyant
normalement le r�sultat directement sur une imprimante Laser.

%description -l tr dvips
dvips program�, dvi bi�iminde bir girdi dosyas� al�r ve onu PostScript'e
d�n��t�r�r. Kaynak dosya TeX taraf�ndan olu�turulmu� olabilece�i gibi ba�ka
i�leyiciler taraf�ndan da (GFtoDVI gibi) �retilmi� olabilir.

%package dvilj
Summary:	dvi to laserjet convertor
Summary(de):	Ein dvi-->Laserjet-Konvertierer
Summary(fr):	convertisseur dvi vers laserjet.
Summary(pl):	Konwerter dvi do laserjet
Summary(tr):	dvi'dan laserjet'e d�n��t�r�c�
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description dvilj
Dvilj and siblings convert TeX-output .dvi files into HP PCL (i.e. HP
Printer Control Language) commands suitable for printing on a HP LaserJet+,
HP LaserJet IIP (using dvilj2p), HP LaserJet 4 (using dvilj4), and fully
compatible printers.

%description -l de dvilj
Dvilj und Gebr�der konvertieren TeX-Ausgabe-.dvi-Dateien in HP PCL (HP
Printer Control Language) Befehle zum Drucken auf HP LaserJet+, HP LaserJet
IIP (mit dvilj2p), HP LaserJet 4 (mit dvilj4) und vollst�ndig kompatiblen
Druckern.

%description -l fr dvilj
dvilj et ses cousins convertissent les fichiers dvi en commandes HPPCL (le
langage des imprimantes HP) pour les imprimer sur HP LaserJet+, HP LaserJet
IIP (avec dvilj2p), HP LaserJet 4 (avec dvilj4), et autres imprimantes
totalement compatibles.

%description -l tr dvilj
TeX ��kt�s� dvi dosyalar�n� HP PCL (HP'nin geli�tirdi�i bir yaz�c� denetim
dili) komutlar�na �evirir ve b�ylece bir LaserJet+, HP LaserJet IIP (dvilj2p
ile), HP LaserJet4 (dvilj4 ile) ve tam uyumlular�ndan yaz�c� ��kt�s�
al�nabilir.

%package afm
Summary:	afm (Adobe Font Metrics) fonts and utilities
Summary(de):	Fonts und Dienstprogramme f�r afm (Adobe Font Metrics)
Summary(fr):	Fontes afm (Adobe Font Metrics) et utilitaires
Summary(pl):	afm (Adobe Font Metrics) czcionki i narz�dzia
Summary(tr):	afm yaz�tipleri ve yard�mc� programlar�
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description afm
PostScript fonts are (or should be) accompanied by font metric files such as
Times-Roman.afm, which describes the characteristics of the font called
Times-Roman. To use such fonts with TeX, we need TFM files that contain
similar information. afm2tfm does that conversion.

%description -l de afm
PostScript-Fonts werden (oder sollten) von Font-Metric-Dateien (z.B.
Times-Roman.afm) begleitet, die die Eigenschaften des Fonts (hier:
Times-Roman) beschreiben. Um solche Fonts mit TeX verwenden zu k�nnen,
werden TFM-Dateien ben�tigt, die �hnliche Informationen

%description -l fr afm
Les fontes PostScript sont (ou devraient �tre) accompagn�es de fontes
m�triques comme Times-Roman.afm qui d�crivent les caract�ristiques des
fontes appel�es Times-Roman. pour utiliser ces fontes avec TeX, nous avons
besoin de TFM, des fichiers qui contiennent des informations similaires.
afm2tfm r�alise cette conversion.

%description -l pl afm
Fonty PostScriptowe s� (powinny by�) dostarczane wraz z metrykami takimi jak
np. Times-Roman.afm, opisuj�cymi charakterystyk� znak�w.  Aby u�ywa� takich
font�w z TeXem potrzebne s� metryki zrozumia�e dla TeXa (pliki *.TFM).
afm2tfm konwertuje pomi�dzy tymi dwoma rodzajami metryk.

%description -l tr afm
PostScript yaz�tipleri, yaz�tipi �l��t dosyalar� ile beraber da��t�l�rlar.
�rne�in Times-Roman.afm, Times-Roman yaz�tipinin karakteristik �zelliklerini
tan�mlar. Bu t�rde yaz�tiplerini TeX ile kullanabilmek i�in, benzer
bilgileri ta��yan TFM dosyalar� gerekir. afm2tfm bu gerekli d�n���m� yapar.

%package ams
Summary:	LaTeX macro package
Summary(de):	LaTeX-Makropaket
Summary(fr):	Package de macros pour LaTeX
Summary(pl):	Makra dla LaTeX 
Summary(tr):	LaTeX makro paketi
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description ams
American Mathematics Society macros for plainTeX and LaTeX. 

%description -l pl ams
Makra American Mathematics Society do sk�adania z publikacji matematycznych.

%package bibtex 
Summary:	LaTeX macro package
Summary(pl):	Dodatkowe makra dla LaTeX
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description bibtex 
LaTeX macro package.

%package etex
Summary:	e-TeX 
Summary(pl):	e-TeX 
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description etex
e-TeX: a 100%-compatible successor to TeX.

%description -l pl etex
e-TeX -- Pierwsza przymiarka do New Typesetting System...

%package omega
Summary:	extended unicode TeX
Summary(pl):	Rozszerzony unicode TeX
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description omega
Omega is extended unicode TeX. 

%description -l pl omega
Omega -- TeX ze wsprciem dla Unicode.

%package pdftex
Summary:	PDFtex 
Summary(pl):	PDFtex 
Group:		Applications/Publishing/TeX
Group(pl):	Aplikacje/Publikowanie/TeX
Requires:	%{name} = %{version}

%description pdftex
TeX generating PDFs instead DVI.

%description -l pl pdftex
pdfTeX generuje zamiast DVI pliki PDF.

%prep
%setup -q -n teTeX-%{texmf_ver}
%patch  -p1 
%patch1 -p1 

install -d texk/share/texmf
tar xzf %{SOURCE1} -C texk/share/texmf
tar xzf %{SOURCE2} -C texk/share/texmf

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
sh ./reautoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-system-ncurses \
	--with-system-zlib \
	--with-system-pnglib \
	--disable-multiplatform \
	--without-dialog \
	--with-texinfo \
	--with-fonts-dir=/var/cache/fonts \
	--with-texmf-dir=../share/texmf \
	--with-ncurses \
	--enable-shared \
	--disable-static

make
cd texk 
make
cd ..

cd texk/tetex
make
cd ../..

cd texk/dvipsk
makeinfo dvips.texi
cd ../..

cd texk/kpathsea
makeinfo kpathsea.texi
cd ../..

cd texk/web2c/doc
makeinfo web2c.texi
cd ../../..

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir} \
	$RPM_BUILD_ROOT/var/cache/fonts \
	$RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters \
	$RPM_BUILD_ROOT/etc/cron.daily

perl -pi \
	-e "s|\.\./share/texmf|$RPM_BUILD_ROOT%{_datadir}/texmf|g;" \
	-e "s|/var/cache/fonts|$RPM_BUILD_ROOT/var/cache/fonts|g;" \
	texk/share/texmf/web2c/texmf.cnf

cp -a texk/share/texmf  $RPM_BUILD_ROOT%{_datadir}/texmf

LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}; export LD_LIBRARY_PATH

make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT/%{_libdir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir} \
	includedir=$RPM_BUILD_ROOT/%{_includedir} \
	sbindir=$RPM_BUILD_ROOT/%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{_datadir}/texmf

cd texk/tetex
make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT/%{_libdir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir} \
	includedir=$RPM_BUILD_ROOT/%{_includedir} \
	sbindir=$RPM_BUILD_ROOT/%{_sbindir} \
        texmf=$RPM_BUILD_ROOT%{_datadir}/texmf
cd ../..

cd texk/ps2pkm 
make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT/%{_libdir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir} \
	includedir=$RPM_BUILD_ROOT/%{_includedir} \
	sbindir=$RPM_BUILD_ROOT/%{_sbindir} \
        texmf=$RPM_BUILD_ROOT%{_datadir}/texmf
cd ../..

install texk/tetex/texconfig $RPM_BUILD_ROOT%{_bindir}

make init \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT/%{_bindir} \
	mandir=$RPM_BUILD_ROOT/%{_mandir}/man1 \
	libdir=$RPM_BUILD_ROOT/%{_libdir} \
	datadir=$RPM_BUILD_ROOT/%{_datadir} \
	infodir=$RPM_BUILD_ROOT/%{_infodir} \
	includedir=$RPM_BUILD_ROOT/%{_includedir} \
	sbindir=$RPM_BUILD_ROOT/%{_sbindir} \
	texmf=$RPM_BUILD_ROOT%{_datadir}/texmf

perl -pi \
	-e "s|\.\./share/texmf|%{_datadir}/texmf|g;" \
	-e "s|$RPM_BUILD_ROOT/var/cache/fonts|/var/cache/fonts|g;" \
	$RPM_BUILD_ROOT%{_datadir}/texmf/web2c/texmf.cnf

# install the new magic print filter for converting dvi to ps
install %{SOURCE3} $RPM_BUILD_ROOT%{_libdir}/rhs/rhs-printfilters

install %{SOURCE4} $RPM_BUILD_ROOT/etc/cron.daily

# temporary fix
ln -sf libkpathsea.so.3.3.1 $RPM_BUILD_ROOT%{_libdir}/libkpathsea.so

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man1/*}

%post
/sbin/install-info %{_infodir}/web2c.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/kpathsea.info.gz /etc/info-dir
/sbin/ldconfig

/usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/kpathsea.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/web2c.info.gz /etc/info-dir
fi

%postun
/sbin/ldconfig

[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%post latex
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
/sbin/install-info %{_infodir}/latex.info.gz /etc/info-dir
exit 0

%preun latex
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/latex.info.gz /etc/info-dir
fi

%postun latex
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%post dvips
/sbin/install-info %{_infodir}/dvips.info.gz /etc/info-dir
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%preun dvips
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/dvips.info.gz /etc/info-dir
fi

%postun dvips
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%post dvilj
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%postun dvilj
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%post afm
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%postun afm
[ -x %{_bindir}/texhash ] && /usr/bin/env - /usr/bin/texhash 1>&2
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

%attr(1777,root,root) %dir /var/cache/fonts

%attr(750,root,root) %config /etc/cron.daily/tetex.cron
#%config %{_datadir}/texmf/web2c/mktex.cnf
#%config %{_datadir}/texmf/web2c/texmf.cnf

%attr(755,root,root) %{_bindir}/MakeTeXPK
%attr(755,root,root) %{_bindir}/access
%attr(755,root,root) %{_bindir}/all*
%attr(755,root,root) %{_bindir}/cont-de
%attr(755,root,root) %{_bindir}/cont-en
%attr(755,root,root) %{_bindir}/cont-nl
%attr(755,root,root) %{_bindir}/dmp
%attr(755,root,root) %{_bindir}/dvi2fax
%attr(755,root,root) %{_bindir}/dvicopy
%attr(755,root,root) %{_bindir}/dvihp
%attr(755,root,root) %{_bindir}/dvired
%attr(755,root,root) %{_bindir}/dvitomp
%attr(755,root,root) %{_bindir}/dvitype
%attr(755,root,root) %{_bindir}/fontexport
%attr(755,root,root) %{_bindir}/fontimport
%attr(755,root,root) %{_bindir}/fontinst
%attr(755,root,root) %{_bindir}/gftodvi
%attr(755,root,root) %{_bindir}/gftopk
%attr(755,root,root) %{_bindir}/gftype
%attr(755,root,root) %{_bindir}/gsftopk
%attr(755,root,root) %{_bindir}/inimf
%attr(755,root,root) %{_bindir}/inimpost
%attr(755,root,root) %{_bindir}/initex
%attr(755,root,root) %{_bindir}/kpsepath
%attr(755,root,root) %{_bindir}/kpsestat
%attr(755,root,root) %{_bindir}/kpsetool
%attr(755,root,root) %{_bindir}/kpsewhich
%attr(755,root,root) %{_bindir}/kpsexpand
%attr(755,root,root) %{_bindir}/lambda
%attr(755,root,root) %{_bindir}/mag
%attr(755,root,root) %{_bindir}/makeindex
%attr(755,root,root) %{_bindir}/makempx
%attr(755,root,root) %{_bindir}/mf
%attr(755,root,root) %{_bindir}/mft
%attr(755,root,root) %{_bindir}/mkfontdesc
%attr(755,root,root) %{_bindir}/mkindex
%attr(755,root,root) %{_bindir}/mkocp
%attr(755,root,root) %{_bindir}/mkofm
%attr(755,root,root) %{_bindir}/mktexlsr
%attr(755,root,root) %{_bindir}/mktexmf
%attr(755,root,root) %{_bindir}/mktexpk
%attr(755,root,root) %{_bindir}/mktextfm
%attr(755,root,root) %{_bindir}/mpost
%attr(755,root,root) %{_bindir}/mpto
%attr(755,root,root) %{_bindir}/newer
%attr(755,root,root) %{_bindir}/odvicopy
%attr(755,root,root) %{_bindir}/odvitype
%attr(755,root,root) %{_bindir}/ofm2opl
%attr(755,root,root) %{_bindir}/opl2ofm
%attr(755,root,root) %{_bindir}/otangle
%attr(755,root,root) %{_bindir}/otp2ocp
%attr(755,root,root) %{_bindir}/outocp
%attr(755,root,root) %{_bindir}/ovf2ovp
%attr(755,root,root) %{_bindir}/ovp2ovf
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
%attr(755,root,root) %{_bindir}/tangle
%attr(755,root,root) %{_bindir}/tex
%attr(755,root,root) %{_bindir}/texconfig
%attr(755,root,root) %{_bindir}/texhash
%attr(755,root,root) %{_bindir}/texi2html
%attr(755,root,root) %{_bindir}/texi2pdf
%attr(755,root,root) %{_bindir}/tftopl
%attr(755,root,root) %{_bindir}/tie
%attr(755,root,root) %{_bindir}/vftovp
%attr(755,root,root) %{_bindir}/virmf
%attr(755,root,root) %{_bindir}/virmpost
%attr(755,root,root) %{_bindir}/virtex
%attr(755,root,root) %{_bindir}/vptovf
%attr(755,root,root) %{_bindir}/weave
%attr(755,root,root) %{_bindir}/fmtutil
%attr(755,root,root) %{_bindir}/mfw
%attr(755,root,root) %{_bindir}/rubibtex
%attr(755,root,root) %{_bindir}/rumakeindex
%attr(755,root,root) %{_bindir}/texdoc
%attr(755,root,root) %{_bindir}/texexec
%attr(755,root,root) %{_bindir}/texlinks
%attr(755,root,root) %{_bindir}/texshow
%attr(755,root,root) %{_bindir}/texutil
%attr(755,root,root) %{_bindir}/ttf2afm

%{_includedir}/kpathsea

%{_infodir}/kpathsea.info*
%{_infodir}/web2c.info*

%attr(755,root,root) %{_libdir}/lib*.so*

%{_mandir}/man1/MakeTeXPK.1*
%{_mandir}/man1/access.1*
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*

%lang(de) %{_mandir}/man1/cont-de.1*
%lang(en) %{_mandir}/man1/cont-en.1*
%lang(nl) %{_mandir}/man1/cont-nl.1*

%{_mandir}/man1/dmp.1*
%{_mandir}/man1/dvicopy.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/fontexport.1*
%{_mandir}/man1/fontimport.1*
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/gsftopk.1*
%{_mandir}/man1/inimf.1*
%{_mandir}/man1/inimpost.1*
%{_mandir}/man1/initex.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/lambda.1*
%{_mandir}/man1/mag.1*
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/makempx.1*
%{_mandir}/man1/mf.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/mpost.1*
%{_mandir}/man1/mpto.1*
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
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/tex.1*
%{_mandir}/man1/texconfig.1*
%{_mandir}/man1/texhash.1*
%{_mandir}/man1/texi2html.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/tie.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/virmf.1*
%{_mandir}/man1/virmpost.1*
%{_mandir}/man1/virtex.1*
%{_mandir}/man1/vptovf.1*
%{_mandir}/man1/weave.1*

%doc %{_datadir}/texmf/ChangeLog
%config %{_datadir}/texmf/aliases

%config %{_datadir}/texmf/context/config/texexec.ini
%lang(de) %{_datadir}/texmf/context/data/cont-de.tws
%lang(en) %{_datadir}/texmf/context/data/cont-en.tws
%lang(nl) %{_datadir}/texmf/context/data/cont-nl.tws

%{_datadir}/texmf/etex/plain/base/*
%{_datadir}/texmf/etex/plain/config/*
%{_datadir}/texmf/fontname/*

%{_datadir}/texmf/fonts/pfm/public/xypic/*
%{_datadir}/texmf/fonts/source/jknappen
%{_datadir}/texmf/fonts/source/lh/base/*
%{_datadir}/texmf/fonts/source/lh/lh-lcy
%{_datadir}/texmf/fonts/source/lh/lh-ot2
%{_datadir}/texmf/fonts/source/lh/lh-t2a
%{_datadir}/texmf/fonts/source/lh/lh-t2b
%{_datadir}/texmf/fonts/source/lh/lh-t2c
%{_datadir}/texmf/fonts/source/lh/lh-x2
%{_datadir}/texmf/fonts/source/lh/nont2
%{_datadir}/texmf/fonts/source/public/bbm
%{_datadir}/texmf/fonts/source/public/bbold
%{_datadir}/texmf/fonts/source/public/cbgreek
%{_datadir}/texmf/fonts/source/public/cc-pl
%{_datadir}/texmf/fonts/source/public/cm/*.mf
%{_datadir}/texmf/fonts/source/public/cmbright
%{_datadir}/texmf/fonts/source/public/cmextra
%{_datadir}/texmf/fonts/source/public/concmath
%{_datadir}/texmf/fonts/source/public/concrete
%{_datadir}/texmf/fonts/source/public/dstroke
%{_datadir}/texmf/fonts/source/public/ecc
%{_datadir}/texmf/fonts/source/public/euxm
%{_datadir}/texmf/fonts/source/public/gothic
%{_datadir}/texmf/fonts/source/public/mflogo
%{_datadir}/texmf/fonts/source/public/misc
%{_datadir}/texmf/fonts/source/public/pandora
%{_datadir}/texmf/fonts/source/public/pl
%dir %{_datadir}/texmf/fonts/source/public/rsfs
%{_datadir}/texmf/fonts/source/public/rsfs/*.mf
%dir %{_datadir}/texmf/fonts/source/public/stmaryrd
%{_datadir}/texmf/fonts/source/public/stmaryrd/*.mf
%dir %{_datadir}/texmf/fonts/source/public/wasy/
%{_datadir}/texmf/fonts/source/public/wasy/*.mf
%dir %{_datadir}/texmf/fonts/source/public/xypic
%{_datadir}/texmf/fonts/source/public/xypic/*.mf
%dir %{_datadir}/texmf/fonts/source/yandy/mathtime
%{_datadir}/texmf/fonts/source/yandy/mathtime/*

%{_datadir}/texmf/fonts/tfm/bh
%{_datadir}/texmf/fonts/tfm/cg
%{_datadir}/texmf/fonts/tfm/hoekwater
%{_datadir}/texmf/fonts/tfm/monotype
%{_datadir}/texmf/fonts/tfm/public/ae
%{_datadir}/texmf/fonts/tfm/public/bbm
%{_datadir}/texmf/fonts/tfm/public/bbold
%{_datadir}/texmf/fonts/tfm/public/cc-pl
%{_datadir}/texmf/fonts/tfm/public/cm
%{_datadir}/texmf/fonts/tfm/public/cmcyr
%{_datadir}/texmf/fonts/tfm/public/cmbright
%{_datadir}/texmf/fonts/tfm/public/cmextra
%{_datadir}/texmf/fonts/tfm/public/concmath
%{_datadir}/texmf/fonts/tfm/public/concrete
%{_datadir}/texmf/fonts/tfm/public/euxm
%{_datadir}/texmf/fonts/tfm/public/gothic
%{_datadir}/texmf/fonts/tfm/public/marvosym
%{_datadir}/texmf/fonts/tfm/public/mathpple
%{_datadir}/texmf/fonts/tfm/public/mflogo
%{_datadir}/texmf/fonts/tfm/public/misc
%{_datadir}/texmf/fonts/tfm/public/pandora
%{_datadir}/texmf/fonts/tfm/public/pl
%{_datadir}/texmf/fonts/tfm/public/rsfs
%{_datadir}/texmf/fonts/tfm/public/stmaryrd
%{_datadir}/texmf/fonts/tfm/public/wasy
%{_datadir}/texmf/fonts/tfm/public/xypic
%{_datadir}/texmf/fonts/tfm/yandy/courier
%{_datadir}/texmf/fonts/tfm/yandy/lubright
%{_datadir}/texmf/fonts/tfm/yandy/lucida
%{_datadir}/texmf/fonts/tfm/yandy/lucidfax
%{_datadir}/texmf/fonts/tfm/yandy/lucsans
%{_datadir}/texmf/fonts/tfm/yandy/lumath
%{_datadir}/texmf/fonts/tfm/yandy/mathpi
%{_datadir}/texmf/fonts/tfm/yandy/mathplus
%{_datadir}/texmf/fonts/tfm/yandy/mathtime
%{_datadir}/texmf/fonts/tfm/yandy/symbol
%{_datadir}/texmf/fonts/tfm/yandy/times
%{_datadir}/texmf/fonts/tfm/yandy/zapfding

%{_datadir}/texmf/fonts/type1/adobe/utopia
%{_datadir}/texmf/fonts/type1/bitstrea/charter
%{_datadir}/texmf/fonts/type1/bluesky/cm
%{_datadir}/texmf/fonts/type1/bluesky/cmextra
%{_datadir}/texmf/fonts/type1/bluesky/cyrillic
%{_datadir}/texmf/fonts/type1/bluesky/euler
%{_datadir}/texmf/fonts/type1/bluesky/symbols
%{_datadir}/texmf/fonts/type1/hoekwater/context
%{_datadir}/texmf/fonts/type1/hoekwater/mflogo
%{_datadir}/texmf/fonts/type1/hoekwater/misc
%{_datadir}/texmf/fonts/type1/hoekwater/rsfs
%{_datadir}/texmf/fonts/type1/hoekwater/stmaryrd
%{_datadir}/texmf/fonts/type1/hoekwater/wasy
%{_datadir}/texmf/fonts/type1/public/cmcyr
%{_datadir}/texmf/fonts/type1/public/marvosym
%{_datadir}/texmf/fonts/type1/public/pl
%{_datadir}/texmf/fonts/type1/public/xypic
%{_datadir}/texmf/fonts/type1/urw/avantgar
%{_datadir}/texmf/fonts/type1/urw/bookman
%{_datadir}/texmf/fonts/type1/urw/courier
%{_datadir}/texmf/fonts/type1/urw/helvetic
%{_datadir}/texmf/fonts/type1/urw/ncntrsbk
%{_datadir}/texmf/fonts/type1/urw/palatino
%{_datadir}/texmf/fonts/type1/urw/symbol
%{_datadir}/texmf/fonts/type1/urw/times
%{_datadir}/texmf/fonts/type1/urw/zapfchan
%{_datadir}/texmf/fonts/type1/urw/zapfding

%{_datadir}/texmf/fonts/vf/adobe/avantgar
%{_datadir}/texmf/fonts/vf/adobe/bookman
%{_datadir}/texmf/fonts/vf/adobe/courier
%{_datadir}/texmf/fonts/vf/adobe/helvetic
%{_datadir}/texmf/fonts/vf/adobe/mathppl
%{_datadir}/texmf/fonts/vf/adobe/mathptm
%{_datadir}/texmf/fonts/vf/adobe/mathptmx
%{_datadir}/texmf/fonts/vf/adobe/ncntrsbk
%{_datadir}/texmf/fonts/vf/adobe/palatino
%{_datadir}/texmf/fonts/vf/adobe/pslatex
%{_datadir}/texmf/fonts/vf/adobe/times
%{_datadir}/texmf/fonts/vf/adobe/utopia
%{_datadir}/texmf/fonts/vf/adobe/zapfchan
%{_datadir}/texmf/fonts/vf/bitstrea/charter
%{_datadir}/texmf/fonts/vf/bh/lubright
%{_datadir}/texmf/fonts/vf/bh/lucida
%{_datadir}/texmf/fonts/vf/bh/lucidfax
%{_datadir}/texmf/fonts/vf/bh/lucsans
%{_datadir}/texmf/fonts/vf/cg/albertus
%{_datadir}/texmf/fonts/vf/cg/atqolive
%{_datadir}/texmf/fonts/vf/cg/clarendo
%{_datadir}/texmf/fonts/vf/cg/coronet
%{_datadir}/texmf/fonts/vf/cg/courier
%{_datadir}/texmf/fonts/vf/cg/garamond
%{_datadir}/texmf/fonts/vf/cg/lettrgth
%{_datadir}/texmf/fonts/vf/cg/marigold
%{_datadir}/texmf/fonts/vf/cg/optima
%{_datadir}/texmf/fonts/vf/cg/times
%{_datadir}/texmf/fonts/vf/cg/univers
%{_datadir}/texmf/fonts/vf/monotype/helvetic
%{_datadir}/texmf/fonts/vf/monotype/timesnew
%{_datadir}/texmf/fonts/vf/public/ae
%{_datadir}/texmf/fonts/vf/public/cmcyr
%{_datadir}/texmf/fonts/vf/public/mathpple
%{_datadir}/texmf/fonts/vf/yandy/mathplus
%{_datadir}/texmf/fonts/vf/yandy/mathtime
%{_datadir}/texmf/fonts/vf/yandy/times

%{_datadir}/texmf/ls-R
%{_datadir}/texmf/makeindex

%{_datadir}/texmf/metafont/base
%{_datadir}/texmf/metafont/config
%{_datadir}/texmf/metafont/misc

%{_datadir}/texmf/metapost/base
%{_datadir}/texmf/metapost/config
%{_datadir}/texmf/metapost/context
%{_datadir}/texmf/metapost/misc

%{_datadir}/texmf/mft

%{_datadir}/texmf/tex/context/base
%{_datadir}/texmf/tex/context/config

%{_datadir}/texmf/tex/fontinst/base

%attr(-,root,root) %{_datadir}/texmf/tex/generic

%{_datadir}/texmf/tex/plain/base
%{_datadir}/texmf/tex/plain/config
%{_datadir}/texmf/tex/plain/mathtime
%{_datadir}/texmf/tex/plain/misc

%{_datadir}/texmf/tex/cyrplain/base
%config %{_datadir}/texmf/tex/cyrplain/config/*.ini
%{_datadir}/texmf/tex/mex/base
%config %{_datadir}/texmf/tex/mex/config/mex.ini
%config %{_datadir}/texmf/tex/mex/config/mexconf.tex

%{_datadir}/texmf/tex/texinfo

%doc %{_datadir}/texmf/texconfig/README

%{_datadir}/texmf/texconfig/g*
%{_datadir}/texmf/texconfig/v*
%{_datadir}/texmf/texconfig/x*

%{_datadir}/texmf/updates.dat

%dir %{_datadir}/texmf/web2c
%{_datadir}/texmf/web2c/*.tcx

# nie wiem do czego te pliki
%{_datadir}/texmf/web2c/*.pool 
%{_datadir}/texmf/web2c/*.opt
%{_datadir}/texmf/web2c/mpost.mem

%attr(755,root,root) %{_datadir}/texmf/web2c/mktexdir
%attr(755,root,root) %{_datadir}/texmf/web2c/mktexnam
%attr(755,root,root) %{_datadir}/texmf/web2c/mktexupd
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/fmtutil.cnf
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/mktex.cnf
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/tex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/texmf.cnf
%{_datadir}/texmf/web2c/mf.base
%{_datadir}/texmf/web2c/mfw.base
%{_datadir}/texmf/web2c/plain.*

# do rozrzucenia po pakietach
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/elatex.efmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/etex.efmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/lambda.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/latex.fmt
#%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/mex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/omega.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfelatex.efmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdflatex.fmt
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/texmf/web2c/pdfetex.efmt

%doc %{_datadir}/texmf/doc/Makefile
%doc %{_datadir}/texmf/doc/README
%doc %{_datadir}/texmf/doc/context
%doc %{_datadir}/texmf/doc/e*
%doc %{_datadir}/texmf/doc/mkhtml.nawk
%doc %{_datadir}/texmf/doc/tetex.gif
%doc %{_datadir}/texmf/doc/mex

%doc %{_datadir}/texmf/doc/fonts/c*
%doc %{_datadir}/texmf/doc/fonts/ec*
%doc %{_datadir}/texmf/doc/fonts/pl
%doc %{_datadir}/texmf/doc/fonts/bluesky
%doc %{_datadir}/texmf/doc/fonts/dstroke
%doc %{_datadir}/texmf/doc/fonts/hoekwater
%doc %{_datadir}/texmf/doc/fonts/lucidabr
%doc %{_datadir}/texmf/doc/fonts/marvosym
%doc %{_datadir}/texmf/doc/fonts/fontname
%doc %{_datadir}/texmf/doc/fonts/oldgerman
%doc %{_datadir}/texmf/doc/generic
%doc %{_datadir}/texmf/doc/help*
%doc %{_datadir}/texmf/doc/images
%doc %{_datadir}/texmf/doc/index.html
%doc %{_datadir}/texmf/doc/makeindex
%doc %{_datadir}/texmf/doc/metapost
%doc %{_datadir}/texmf/doc/mkhtml
%doc %{_datadir}/texmf/doc/newhelpindex.html
%doc %{_datadir}/texmf/doc/programs
%doc %{_datadir}/texmf/doc/tetex

%doc %{_datadir}/texmf/source/README
%{_datadir}/texmf/source/generic

%files latex 
%defattr(644,root,root,755)

%{_datadir}/texmf/etex/latex/misc/etex.sty
%{_datadir}/texmf/fonts/source/public/latex
%{_datadir}/texmf/fonts/tfm/public/latex
%{_datadir}/texmf/tex/generic/pictex/latexpicobjs.tex
%{_datadir}/texmf/tex/generic/xypic/xylatex.ini
%{_datadir}/texmf/tex/latex

%attr(755,root,root) %{_bindir}/latex
%attr(755,root,root) %{_bindir}/pslatex

%{_mandir}/man1/latex.1*
%{_mandir}/man1/pdflatex.1*

%{_infodir}/latex.info*

%doc %{_datadir}/texmf/doc/latex
%attr(755,root,root) %{_bindir}/bibtex
%{_mandir}/man1/bibtex.1*

%{_datadir}/texmf/bibtex/bib
%{_datadir}/texmf/bibtex/bst/base
%{_datadir}/texmf/bibtex/bst/germbib
%{_datadir}/texmf/bibtex/bst/koma-script
%{_datadir}/texmf/bibtex/bst/misc
%{_datadir}/texmf/bibtex/bst/natbib

%doc %{_datadir}/texmf/doc/bibtex/

%{_datadir}/texmf/source/latex

%{_datadir}/texmf/tex/platex/base
%config %{_datadir}/texmf/tex/platex/config

%files etex
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/elatex
%{_mandir}/man1/elatex.1*

%attr(755,root,root) %{_bindir}/einitex
%attr(755,root,root) %{_bindir}/eplain
%attr(755,root,root) %{_bindir}/etex
%attr(755,root,root) %{_bindir}/evirtex

%{_mandir}/man1/einitex.1*
%{_mandir}/man1/eplain.1*
%{_mandir}/man1/etex.1*
%{_mandir}/man1/evirtex.1*

%{_datadir}/texmf/tex/eplain

%config %{_datadir}/texmf/etex/latex/config/elatex.ini

%files omega 
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/iniomega
%attr(755,root,root) %{_bindir}/omega
%attr(755,root,root) %{_bindir}/viromega
%{_mandir}/man1/iniomega.1*
%{_mandir}/man1/omega.1*
%{_mandir}/man1/viromega.1*

%{_datadir}/texmf/fonts/ofm/public/omega
%{_datadir}/texmf/fonts/tfm/public/omega
%{_datadir}/texmf/fonts/ovf/public/omega
%{_datadir}/texmf/fonts/ovp/public/omega
%{_datadir}/texmf/fonts/type1/public/omega

%{_datadir}/texmf/omega/otp/omega
%{_datadir}/texmf/omega/plain/config
%{_datadir}/texmf/omega/plain/base
%{_datadir}/texmf/omega/lambda
%{_datadir}/texmf/omega/ocp/char2uni
%{_datadir}/texmf/omega/ocp/misc
%{_datadir}/texmf/omega/ocp/omega
%{_datadir}/texmf/omega/ocp/uni2char
%{_datadir}/texmf/omega/otp/char2uni
%{_datadir}/texmf/omega/otp/uni2char
%{_datadir}/texmf/omega/otp/misc

%doc %{_datadir}/texmf/doc/omega

%attr(755,root,root) %{_bindir}/odvips
%attr(755,root,root) %{_bindir}/oxdvi
%attr(755,root,root) %{_bindir}/oxdvi.bin

%files pdftex 
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/pdfinitex
%attr(755,root,root) %{_bindir}/pdftex
%attr(755,root,root) %{_bindir}/pdfvirtex
%attr(755,root,root) %{_bindir}/pdfeinitex
%attr(755,root,root) %{_bindir}/pdfelatex
%attr(755,root,root) %{_bindir}/pdfetex
%attr(755,root,root) %{_bindir}/pdfevirtex
%attr(755,root,root) %{_bindir}/thumbpdf
%attr(755,root,root) %{_bindir}/e2pall
%attr(755,root,root) %{_bindir}/epstopdf

%{_mandir}/man1/pdfinitex.1*
%{_mandir}/man1/pdftex.1*
%{_mandir}/man1/pdfvirtex.1*

%{_datadir}/texmf/pdftex/config
%{_datadir}/texmf/pdftex/plain/misc
%{_datadir}/texmf/pdftex/texinfo

%config %{_datadir}/texmf/pdftex/latex/config/pdflatex.ini
%config %{_datadir}/texmf/pdftex/mex/config/pdfmex.ini
%config %{_datadir}/texmf/pdftex/plain/config/pdftex.ini

%config %{_datadir}/texmf/pdfetex/latex/config/pdfelatex.ini
%config %{_datadir}/texmf/pdfetex/tex/config/pdfetex.ini

%attr(755,root,root) %{_bindir}/pdflatex 
%doc %{_datadir}/texmf/doc/pdftex

%{_datadir}/texmf/source/pdftex

%files dvips 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/rhs/rhs-printfilters/dvi-to-ps.fpi

%attr(-,root,root) %{_datadir}/texmf/dvips

%{_datadir}/texmf/tex/generic/pstricks/dvipsone.con
%{_datadir}/texmf/tex/generic/xypic/xydvips.tex
%{_datadir}/texmf/tex/plain/dvips
%{_datadir}/texmf/tex/latex/graphics/*.def
%{_datadir}/texmf/tex/latex/hyperref/*.def

%attr(755,root,root) %{_bindir}/dvips
%{_mandir}/man1/dvips.1*

%{_infodir}/dvips.info*

%files dvilj 
%defattr(644,root,root,755)
%{_datadir}/texmf/tex/latex/dvilj/*.sty

%attr(755,root,root) %{_bindir}/dvilj
%attr(755,root,root) %{_bindir}/dvilj2p
%attr(755,root,root) %{_bindir}/dvilj4
%attr(755,root,root) %{_bindir}/dvilj4l
%attr(755,root,root) %{_bindir}/dvilj6
%{_mandir}/man1/dvilj.1*

%files afm 
%defattr(644,root,root,755)
%{_datadir}/texmf/fonts/afm

%attr(755,root,root) %{_bindir}/afm2tfm
%{_mandir}/man1/afm2tfm.1*

%files ams 
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/amstex
%{_mandir}/man1/amstex.1*

%{_datadir}/texmf/fonts/source/ams/cmextra
%{_datadir}/texmf/fonts/source/ams/cyrillic
%{_datadir}/texmf/fonts/source/ams/euler
%{_datadir}/texmf/fonts/source/ams/symbols
%{_datadir}/texmf/fonts/tfm/ams

%{_datadir}/texmf/tex/amstex/base
%{_datadir}/texmf/tex/amstex/config
%{_datadir}/texmf/tex/plain/amsfonts
%{_datadir}/texmf/bibtex/bst/amslatex

%{_datadir}/texmf/source/amstex

%doc %{_datadir}/texmf/doc/amstex
%doc %{_datadir}/texmf/doc/latex/amslatex
%doc %{_datadir}/texmf/doc/fonts/amsfonts
