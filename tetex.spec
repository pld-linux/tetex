Summary:     TeX typesetting system and MetaFont font formatter
Name:        tetex
Version:     0.9
Release:     6.2d
Copyright:   distributable
Group:       Applications/Publishing/TeX
#######      ftp://ftp.rrzn.uni-hannover.de/pub/local/misc/teTeX-beta
Source:      teTeX-src-%{version}.tar.gz
Source1:     teTeX-texmf-%{version}.tar.gz
Source2:     dvi-to-ps.fpi
Source10:    tetex.cron
Patch0:      teTeX-0.9-rhconfig.patch  
Patch1:      teTeX-0.9-buildr.patch
Patch2:      %{name}-%{version}-manpages.patch
Url:         http://www.tug.org/teTeX/
Requires:    tmpwatch
Requires:    dialog
Prereq:      /sbin/install-info
Obsoletes:   tetex-texmf-src
Obsoletes:   tetex-doc
Buildroot:   /tmp/%{name}-%{version}-buildroot
Summary(de): TeX-Satzherstellungssystem und MetaFont-Formatierung
Summary(fr): Systéme de compostion TeX et formatteur de MetaFontes.
Summary(tr): TeX dizgi sistemi ve MetaFont yazýtipi biçimlendiricisi
Summary(pl): System sk³adu publikacji TeX oraz formater fontów MetaFont 

%description
TeX formats a file of interspersed text and commands and outputs a
typesetter independent file (called DVI, which is short for DeVice
Independent).  TeX capabilities and language are described in The
TeXbook, by Knuth.

%package latex
Summary:     LaTeX macro package
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(de): LaTeX-Makropaket
Summary(fr): Package de macros pour LaTeX
Summary(tr): LaTeX makro paketi
Summary(pl): Makro-pakiet LaTeX

%description latex
LaTeX is a TeX macro package. The LaTeX macros encourage writers to
think about the content of their documents, rather than the form.  The
ideal, very difficult to realize, is to have no formatting commands
(like ``switch to italic'' or ``skip 2 picas'') in the document at
all; instead, everything is done by specific markup instructions:
``emphasize'', ``start a section''.

%package xdvi
Summary:     X11 previewer
Group:       Applications/Publishing/TeX
Summary(de): X11-Previewer 
Summary(fr): Prévisualisateur X11
Summary(tr): X11 öngörüntüleyici
Summary(pl): Przegl±darka DVI dla X11 

%description xdvi
xdvi is a program which runs under the X window system. It is used to
preview dvi files, such as are produced by tex and latex.

%package dvips
Summary:     dvi to postscript convertor
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(de): dvi-Postscript-Konvertierungsprogramm
Summary(fr): Convertisseur dvi vers PostScript
Summary(tr): dvi'dan postscript'e dönüþtürücü
Summary(pl): Konwerter dvi do postscriptu

%description dvips
The program dvips takes a DVI file file[.dvi] produced by TeX (or by
some other processor such as GFtoDVI) and converts it to PostScript,
normally sending the result directly to the laserprinter.

%package dvilj
Summary:     dvi to laserjet convertor
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(de): Ein dvi-->Laserjet-Konvertierer
Summary(fr): convertisseur dvi vers laserjet.
Summary(tr): dvi'dan laserjet'e dönüþtürücü
Summary(pl): Konwerter dvi do laserjet

%description dvilj
Dvilj and siblings convert TeX-output .dvi files into HP PCL (i.e.  HP
Printer Control Language) commands suitable for printing on a HP
LaserJet+, HP LaserJet IIP (using dvilj2p), HP LaserJet 4 (using
dvilj4), and fully compatible printers.

%package afm
Summary:     afm (Adobe Font Metrics) fonts and utilities
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(de): Fonts und Dienstprogramme für afm (Adobe Font Metrics)
Summary(fr): Fontes afm (Adobe Font Metrics) et utilitaires
Summary(tr): afm yazýtipleri ve yardýmcý programlarý
Summary(pl): afm (Adobe Font Metrics) fonty i u¿ytki

%description afm
PostScript fonts are (or should be) accompanied by font metric files
such as Times-Roman.afm, which describes the characteristics of the
font called Times-Roman.  To use such fonts with TeX, we need TFM
files that contain similar information.  afm2tfm does that conversion.

%package ams
Summary:     LaTeX macro package
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(de): LaTeX-Makropaket
Summary(fr): Package de macros pour LaTeX
Summary(tr): LaTeX makro paketi
Summary(pl): Makra dla LaTeX 

%description ams
American Mathematics Society macros for plainTeX and LaTeX. 

%package bibtex 
Summary:     LaTeX macro package
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(pl): Dodatkowe makra dla LaTeX

%description bibtex 
LaTeX macro package

%package etex
Summary:     e-TeX 
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(pl): e-TeX 

%description etex
e-TeX: a 100%-compatible successor to TeX

%package omega
Summary:     extended unicode TeX
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(pl): Rozszerzony unicode TeX

%description omega
Omega is extended unicode TeX. 

%package pdftex
Summary:     PDFtex 
Group:       Applications/Publishing/TeX
Requires:    %{name} = %{version}
Summary(pl): PDFtex 

%description pdftex
TeX generating PDFs instead DVI

%description -l de latex
LaTeX ist ein TeX-Makropaket. Die LaTeX-Makros regen den Autor an, 
über den Inhalt - und nicht die Form - ihrer Dokumente nachzudenken. 
Ideal, wenn auch schwer zu realisieren, wäre ein Dokument, das 
keinerlei Formatierungsbefehle (von der Art 'Kursiv ein/aus' 
oder 'Zeilenabstand um 2 Pica vergrößern') enthielte. Stattdessen  
würde all dies durch spezifische 'redaktionelle' Instruktionen ersetzt 
('auszeichnen', 'neues Kapitel starten'). 

%description -l de dvips
Das dvips-Programm nimmt eine dvi-Datei ([.dvi]), die von TeX
bzw. durch einen anderen Prozessor wie GFtoDVI) erzeugt wurde, und
konvertiert diese in PostScript, wobei das Ergebnis in der Regel direkt
an einen Laserdrucker gesandt wird.

%description -l de afm
PostScript-Fonts werden (oder sollten) von Font-Metric-Dateien
(z.B. Times-Roman.afm) begleitet, die die Eigenschaften des Fonts
(hier: Times-Roman) beschreiben. Um solche Fonts mit TeX verwenden
zu können, werden TFM-Dateien benötigt, die ähnliche Informationen

%description -l de xdvi
xdvi ist ein Programm, das unter dem X-Window-System läuft und gewohnt 
ist, dvi-Dateien als Vorschau anzuzeigen, etwa solche, die von tex und 
latex erzeugt wurden. 

%description -l de dvilj
Dvilj und Gebrüder konvertieren TeX-Ausgabe-.dvi-Dateien in HP PCL 
 (HP Printer Control Language) Befehle zum Drucken auf HP LaserJet+, 
HP LaserJet IIP (mit dvilj2p), HP LaserJet 4 (mit
 dvilj4) und 
vollständig kompatiblen Druckern. 

%description -l de
TeX formatiert eine Datei, die abwechselnd Text und Befehle enthält und
gibt eine geräteunabhängige Datei aus (DVI genannt, Abk. für DeVice
Independent). Die Funktionen und Sprache von TeX werden in The
TeXbook von Knuth beschrieben.

%description -l fr latex
LaTeX est un paquetage de macros TeX. Les macros LaTeX permettent aux
auteurs de se concentrer sur le contenu des leurs documents, plutôt que
sur la forme. L'idéal, très difficile à réaliser, est de n'avoir aucune
commande de formatage (comme « mettre en italique », ou « sauter 2 picas »)
dans le document ; au lieu de cela, tout est fait par des balises :
« début de section », « gras ».

%description -l fr dvips
Le programme dvips convertit les fichiers DVI en PostScript, en
envoyant normalement le résultat directement sur une imprimante Laser.

%description -l fr afm
Les fontes PostScript sont (ou devraient être) accompagnées de
fontes métriques comme Times-Roman.afm qui décrivent les caractéristiques
des fontes appelées Times-Roman. pour utiliser ces fontes avec TeX, nous
avons besoin de TFM, des fichiers qui contiennent des informations
similaires. afm2tfm réalise cette conversion.

%description -l fr xdvi
xdvi est un programme s'exécutant sous le système X Window. Il sert à
visualiser les fichiers dvi tels que ceux produits par tex et latex.

%description -l fr dvilj
dvilj et ses cousins convertissent les fichiers dvi en commandes HPPCL
(le langage des imprimantes HP) pour les imprimer sur HP LaserJet+,
HP LaserJet IIP (avec dvilj2p), HP LaserJet 4 (avec dvilj4), et autres
imprimantes totalement compatibles.  

%description -l fr
TeX formate un fichier de commandes et de texte mélandés, et produit un
fichier de indépendant de toute plate-forme (appelé DVI, qui est
un raccourci pour Device Independant). Les possibilités de TeX et son
langage sont décrites dans l'ouvrage TeXbook, de Knuth.

%description -l tr latex
LaTeX bir TeX makro paketidir. LaTeX makrolarý, yazarlarý belgelerinin
biçimlerinden çok içerikleri üzerinde yoðunlaþmlarýna özendirir. Ýdealde,
gerçekleþtirilmesi çok zor olsa da, hiç biçimlendirme komutuna yer
vermeksizin (``2 birim aralýk býrak'' gibi), yalnýzca özel iþaretleme
yönergeleri ile (``yeni bir kesime geç'' gibi) bunu baþarmaya çalýþýr.

%description -l tr dvips
dvips programý, dvi biçiminde bir girdi dosyasý alýr ve onu PostScript'e
dönüþtürür. Kaynak dosya TeX tarafýndan oluþturulmuþ olabileceði gibi baþka
iþleyiciler tarafýndan da (GFtoDVI gibi) üretilmiþ olabilir.

%description -l tr afm
PostScript yazýtipleri, yazýtipi ölçüt dosyalarý ile beraber daðýtýlýrlar.
Örneðin Times-Roman.afm, Times-Roman yazýtipinin karakteristik özelliklerini
tanýmlar. Bu türde yazýtiplerini TeX ile kullanabilmek için, benzer
bilgileri taþýyan TFM dosyalarý gerekir. afm2tfm bu gerekli dönüþümü yapar.

%description -l tr xdvi
xdvi X Windows sistemi altýnda çalýþan bir programdýr. TeX ya da LaTeX
tarafýndan oluþturulmuþ olan dvi dosyalarýnýn görüntülenmesi amacýyla
kullanýlýr.

%description -l tr dvilj
TeX çýktýsý dvi dosyalarýný HP PCL (HP'nin geliþtirdiði bir yazýcý denetim
dili) komutlarýna çevirir ve böylece bir LaserJet+, HP LaserJet IIP (dvilj2p
ile), HP LaserJet4 (dvilj4 ile) ve tam uyumlularýndan yazýcý çýktýsý
alýnabilir.

%description -l tr
TeX, içinde metin ve komutlarýn yer aldýðý bir dosyayý okur ve dizgi
aygýtýndan baðýmsýz bir çýktý (DeVice Independent - DVI) oluþturur.
TeX'in becerileri ve dizgi dili, dili geliþtiren Knuth'un 'The TeXbook'
baþlýklý kitabýnda anlatýlmaktadýr.

%description -l pl 
TeX formatuje przygotowany tekst oraz komendy i produkuje niezale¿ny 
od urz±dzenia plik wynikowy  (tzw. DVI -- skrót od  DeVice Independent).  
Mo¿liwo¶ci TeXa, oraz jego jêzyk zosta³y opisane  w 
,,The TeXbook'' Donalda E. Knutha.

%description -l pl latex
LaTeX jest zestawem makr TeXowych. Makra LaTeX macros u³atwiaj± pisz±cym 
my¶lenie o zawarto¶ci dokumentu, zamiast o jego wygl±dzie. 
Idealny, bardzo trudny do implementacji system nie powinien posiadaæ 
komend formatuj±cych (takich jak ,,pisz kursyw±'', czy prze³±cz na font
8 punktowy) a jedynie polecenia znakuj±ce takie jak np. podkre¶l, 
czy zacznij sekcjê. LaTeX powoli zbli¿a siê do tego idea³u, nie odrzucaj±c
mo¿liwo¶ci ingerencji w wygl±d dokumentu. 

%description -l pl xdvi
xdvi jest programem (dzia³aj±cym w X Window System) do przegl±dania plików DVI, 
produkowanych przez TeXa i LaTeXa.

%description -l afm
Fonty PostScriptowe s± (powinny byæ) dostarczane wraz z metrykami 
takimi jak np. Times-Roman.afm, opisuj±cymi charakterystykê znaków. 
Aby u¿ywaæ takich fontów z TeXem potrzebne s± metryki zrozumia³e dla 
TeXa (pliki *.TFM). afm2tfm konwertuje pomiêdzy tymi dwoma rodzajami metryk. 

%description ams
Makra American Mathematics Society do sk³adania z publikacji 
matematycznych. 

%description -l pl etex
e-TeX -- Pierwsza przymiarka do New Typesetting System... 

%description -l pl omega
Omega -- TeX ze wsprciem dla Unicode 

%description -l pl pdftex
pdfTeX generuje zamiast DVI pliki PDF

%prep
%setup -q -n teTeX-%{version}
%patch  -p1 
%patch1 -p1 

install -d texk/share/texmf
tar xzf %{SOURCE1} -C texk/share/texmf

%patch2 -p1

%build
sh ./reautoconf
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s ./configure --prefix=/usr \
	--with-system-ncurses --with-system-zlib --with-system-pnglib \
	--disable-multiplatform --without-dialog --with-texinfo \
	--with-fonts-dir=/var/lib/texmf \
	--with-texmf-dir=../share/texmf --with-ncurses \
	 %{buildarch}-pld-`echo %{buildos} | tr A-Z a-z`
make

cd texk 
make 

cd tetex 
make 

cd ../ps2pkm 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/share
install -d $RPM_BUILD_ROOT/var/lib/texmf

perl -pi \
	-e "s|\.\./share/texmf|$RPM_BUILD_ROOT/usr/share/texmf|g;" \
	-e "s|/var/lib/texmf|$RPM_BUILD_ROOT/var/lib/texmf|g;" \
	texk/share/texmf/web2c/texmf.cnf

cp -a texk/share/texmf  $RPM_BUILD_ROOT/usr/share/texmf

make install prefix=$RPM_BUILD_ROOT/usr \
	texmf=$RPM_BUILD_ROOT/usr/share/texmf

cd texk/tetex
make install prefix=$RPM_BUILD_ROOT/usr \
        texmf=$RPM_BUILD_ROOT/usr/share/texmf

cd ../ps2pkm 
make install prefix=$RPM_BUILD_ROOT/usr \
        texmf=$RPM_BUILD_ROOT/usr/share/texmf

cd ../..
install $RPM_BUILD_DIR/teTeX-0.9/texk/tetex/texconfig $RPM_BUILD_ROOT/usr/bin	

make init prefix=$RPM_BUILD_ROOT/usr \
	texmf=$RPM_BUILD_ROOT/usr/share/texmf

perl -pi \
	-e "s|\.\./share/texmf|/usr/share/texmf|g;" \
	-e "s|$RPM_BUILD_ROOT/var/lib/texmf|/var/lib/texmf|g;" \
	$RPM_BUILD_ROOT/usr/share/texmf/web2c/texmf.cnf

rm -f $RPM_BUILD_ROOT/usr/info/dir

gzip $RPM_BUILD_ROOT/usr/info/*info*

# install the new magic print filter for converting dvi to ps
install -d $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters
install %{SOURCE2} $RPM_BUILD_ROOT/usr/lib/rhs/rhs-printfilters

install -d $RPM_BUILD_ROOT/etc/cron.daily
install %{SOURCE10} $RPM_BUILD_ROOT/etc/cron.daily

#wmconfig things
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdvi <<EOF
xdvi name "XDvi"
xdvi icon "text.xpm"
xdvi mini-icon "mini-doc1.xpm"
xdvi exec "xdvi &"
xdvi group "Graphics/Viewers"
EOF

bzip2 -9 $RPM_BUILD_ROOT/usr/man/man1/*

%clean
[ -d /usr/share/texmf.TeX.build ] && {
    rm -rf /usr/share/texmf
    mv -f /usr/share/texmf.TeX.build /usr/share/texmf
}
rm -rf $RPM_BUILD_ROOT

# make sure ls-R used by tetex is updated after an install

%post
/sbin/install-info /usr/info/web2c.info.gz /usr/info/dir
/sbin/install-info /usr/info/kpathsea.info.gz /usr/info/dir
/usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
/sbin/install-info /usr/info/latex.info.gz /usr/info/dir
exit 0

%post xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post dvips
/sbin/install-info /usr/info/dvips.info.gz /usr/info/dir
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%post afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun latex
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun xdvi
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun dvips
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun dvilj
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun afm
[ -x /usr/bin/texhash ] && /usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%preun
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/kpathsea.info.gz /usr/info/dir
	/sbin/install-info --delete /usr/info/web2c.info.gz /usr/info/dir
fi

%preun dvips
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/dvips.info.gz /usr/info/dir
fi

%preun latex
if [ "$1" = 0 ]; then
	/sbin/install-info --delete /usr/info/latex.info.gz /usr/info/dir
fi

%files 
%defattr(644,root,root,755)

%attr(1777,root,root) %dir /var/lib/texmf

%attr(750,root,root) %config /etc/cron.daily/tetex.cron
#%config /usr/share/texmf/web2c/mktex.cnf
#%config /usr/share/texmf/web2c/texmf.cnf

%attr(755,root,root) /usr/bin/MakeTeXPK
%attr(711,root,root) /usr/bin/access
%attr(755,root,root) /usr/bin/all*
%attr(755,root,root) /usr/bin/cont-de
%attr(755,root,root) /usr/bin/cont-en
%attr(755,root,root) /usr/bin/cont-nl
%attr(711,root,root) /usr/bin/dmp
%attr(755,root,root) /usr/bin/dvi2fax
%attr(711,root,root) /usr/bin/dvicopy
%attr(755,root,root) /usr/bin/dvihp
%attr(755,root,root) /usr/bin/dvired
%attr(711,root,root) /usr/bin/dvitomp
%attr(711,root,root) /usr/bin/dvitype
%attr(755,root,root) /usr/bin/fontexport
%attr(755,root,root) /usr/bin/fontimport
%attr(755,root,root) /usr/bin/fontinst
%attr(711,root,root) /usr/bin/gftodvi
%attr(711,root,root) /usr/bin/gftopk
%attr(711,root,root) /usr/bin/gftype
%attr(711,root,root) /usr/bin/gsftopk
%attr(755,root,root) /usr/bin/inimf
%attr(755,root,root) /usr/bin/inimpost
%attr(755,root,root) /usr/bin/initex
%attr(755,root,root) /usr/bin/kpsepath
%attr(711,root,root) /usr/bin/kpsestat
%attr(755,root,root) /usr/bin/kpsetool
%attr(711,root,root) /usr/bin/kpsewhich
%attr(755,root,root) /usr/bin/kpsexpand
%attr(755,root,root) /usr/bin/lambda
%attr(711,root,root) /usr/bin/mag
%attr(711,root,root) /usr/bin/makeindex
%attr(755,root,root) /usr/bin/makempx
%attr(711,root,root) /usr/bin/mf
%attr(711,root,root) /usr/bin/mft
%attr(755,root,root) /usr/bin/mkfontdesc
%attr(755,root,root) /usr/bin/mkindex
%attr(755,root,root) /usr/bin/mkocp
%attr(755,root,root) /usr/bin/mkofm
%attr(755,root,root) /usr/bin/mktexlsr
%attr(755,root,root) /usr/bin/mktexmf
%attr(755,root,root) /usr/bin/mktexpk
%attr(755,root,root) /usr/bin/mktextfm
%attr(711,root,root) /usr/bin/mpost
%attr(711,root,root) /usr/bin/mpto
%attr(711,root,root) /usr/bin/newer
%attr(711,root,root) /usr/bin/odvicopy
%attr(711,root,root) /usr/bin/odvitype
%attr(711,root,root) /usr/bin/ofm2opl
%attr(711,root,root) /usr/bin/opl2ofm
%attr(711,root,root) /usr/bin/otangle
%attr(711,root,root) /usr/bin/otp2ocp
%attr(711,root,root) /usr/bin/outocp
%attr(711,root,root) /usr/bin/ovf2ovp
%attr(711,root,root) /usr/bin/ovp2ovf
%attr(711,root,root) /usr/bin/patgen
%attr(711,root,root) /usr/bin/pfb2pfa
%attr(711,root,root) /usr/bin/pk2bm
%attr(711,root,root) /usr/bin/pktogf
%attr(711,root,root) /usr/bin/pktype
%attr(711,root,root) /usr/bin/pltotf
%attr(711,root,root) /usr/bin/pooltype
%attr(755,root,root) /usr/bin/ps2frag
%attr(711,root,root) /usr/bin/ps2pk
%attr(711,root,root) /usr/bin/readlink
%attr(711,root,root) /usr/bin/tangle
%attr(711,root,root) /usr/bin/tex
%attr(755,root,root) /usr/bin/texconfig
%attr(755,root,root) /usr/bin/texhash
%attr(755,root,root) /usr/bin/texi2html
%attr(755,root,root) /usr/bin/texi2pdf
%attr(711,root,root) /usr/bin/tftopl
%attr(711,root,root) /usr/bin/tie
%attr(711,root,root) /usr/bin/vftovp
%attr(755,root,root) /usr/bin/virmf
%attr(755,root,root) /usr/bin/virmpost
%attr(755,root,root) /usr/bin/virtex
%attr(711,root,root) /usr/bin/vptovf
%attr(711,root,root) /usr/bin/weave

/usr/include/kpathsea/*

/usr/info/kpathsea.info*
/usr/info/web2c.info*

/usr/lib/libkpathsea.a

%attr(755,root,root) /usr/lib/rhs/rhs-printfilters/dvi-to-ps.fpi

%attr(644,root, man) /usr/man/man1/MakeTeXPK.1.bz2
%attr(644,root, man) /usr/man/man1/access.1.bz2
%attr(644,root, man) /usr/man/man1/allcm.1.bz2
%attr(644,root, man) /usr/man/man1/allec.1.bz2
%attr(644,root, man) /usr/man/man1/allneeded.1.bz2

%lang(de) %attr(644,root,man) /usr/man/man1/cont-de.1.bz2
%lang(en) %attr(644,root,man) /usr/man/man1/cont-en.1.bz2
%lang(nl) %attr(644,root,man) /usr/man/man1/cont-nl.1.bz2

%attr(644,root, man) /usr/man/man1/dmp.1.bz2
%attr(644,root, man) /usr/man/man1/dvicopy.1.bz2
%attr(644,root, man) /usr/man/man1/dvired.1.bz2
%attr(644,root, man) /usr/man/man1/dvitype.1.bz2
%attr(644,root, man) /usr/man/man1/fontexport.1.bz2
%attr(644,root, man) /usr/man/man1/fontimport.1.bz2
%attr(644,root, man) /usr/man/man1/gftodvi.1.bz2
%attr(644,root, man) /usr/man/man1/gftopk.1.bz2
%attr(644,root, man) /usr/man/man1/gftype.1.bz2
%attr(644,root, man) /usr/man/man1/gsftopk.1.bz2
%attr(644,root, man) /usr/man/man1/inimf.1.bz2
%attr(644,root, man) /usr/man/man1/inimpost.1.bz2
%attr(644,root, man) /usr/man/man1/initex.1.bz2
%attr(644,root, man) /usr/man/man1/kpsestat.1.bz2
%attr(644,root, man) /usr/man/man1/kpsewhich.1.bz2
%attr(644,root, man) /usr/man/man1/lambda.1.bz2
%attr(644,root, man) /usr/man/man1/mag.1.bz2
%attr(644,root, man) /usr/man/man1/makeindex.1.bz2
%attr(644,root, man) /usr/man/man1/makempx.1.bz2
%attr(644,root, man) /usr/man/man1/mf.1.bz2
%attr(644,root, man) /usr/man/man1/mft.1.bz2
%attr(644,root, man) /usr/man/man1/mktexlsr.1.bz2
%attr(644,root, man) /usr/man/man1/mktexmf.1.bz2
%attr(644,root, man) /usr/man/man1/mktexpk.1.bz2
%attr(644,root, man) /usr/man/man1/mktextfm.1.bz2
%attr(644,root, man) /usr/man/man1/mpost.1.bz2
%attr(644,root, man) /usr/man/man1/mpto.1.bz2
%attr(644,root, man) /usr/man/man1/newer.1.bz2
%attr(644,root, man) /usr/man/man1/patgen.1.bz2
%attr(644,root, man) /usr/man/man1/pfb2pfa.1.bz2
%attr(644,root, man) /usr/man/man1/pk2bm.1.bz2
%attr(644,root, man) /usr/man/man1/pktogf.1.bz2
%attr(644,root, man) /usr/man/man1/pktype.1.bz2
%attr(644,root, man) /usr/man/man1/pltotf.1.bz2
%attr(644,root, man) /usr/man/man1/pooltype.1.bz2
%attr(644,root, man) /usr/man/man1/ps2frag.1.bz2
%attr(644,root, man) /usr/man/man1/ps2pk.1.bz2
%attr(644,root, man) /usr/man/man1/readlink.1.bz2
%attr(644,root, man) /usr/man/man1/tangle.1.bz2
%attr(644,root, man) /usr/man/man1/tex.1.bz2
%attr(644,root, man) /usr/man/man1/texconfig.1.bz2
%attr(644,root, man) /usr/man/man1/texhash.1.bz2
%attr(644,root, man) /usr/man/man1/texi2html.1.bz2
%attr(644,root, man) /usr/man/man1/tftopl.1.bz2
%attr(644,root, man) /usr/man/man1/tie.1.bz2
%attr(644,root, man) /usr/man/man1/vftovp.1.bz2
%attr(644,root, man) /usr/man/man1/virmf.1.bz2
%attr(644,root, man) /usr/man/man1/virmpost.1.bz2
%attr(644,root, man) /usr/man/man1/virtex.1.bz2
%attr(644,root, man) /usr/man/man1/vptovf.1.bz2
%attr(644,root, man) /usr/man/man1/weave.1.bz2

%doc /usr/share/texmf/ChangeLog
%config /usr/share/texmf/aliases

/usr/share/texmf/etex/plain/base/*
/usr/share/texmf/etex/plain/config/*
/usr/share/texmf/fontname/*

%attr(-,root,root) /usr/share/texmf/fonts/fontdesc

/usr/share/texmf/fonts/pfm/public/xypic/*
/usr/share/texmf/fonts/source/jknappen/ec/*
/usr/share/texmf/fonts/source/jknappen/sauter/*
/usr/share/texmf/fonts/source/jknappen/tc/*
/usr/share/texmf/fonts/source/public/bbm/*
/usr/share/texmf/fonts/source/public/bbold/*
/usr/share/texmf/fonts/source/public/cm/*.mf

%doc /usr/share/texmf/fonts/source/public/cm/README

/usr/share/texmf/fonts/source/public/cmbright/*
/usr/share/texmf/fonts/source/public/cmextra/*
/usr/share/texmf/fonts/source/public/concmath/*
/usr/share/texmf/fonts/source/public/concrete/*
/usr/share/texmf/fonts/source/public/ecc/*
/usr/share/texmf/fonts/source/public/euxm/*
/usr/share/texmf/fonts/source/public/gothic/*
/usr/share/texmf/fonts/source/public/mflogo/*
/usr/share/texmf/fonts/source/public/misc/*
/usr/share/texmf/fonts/source/public/pandora/*
/usr/share/texmf/fonts/source/public/rsfs/*.mf
/usr/share/texmf/fonts/source/public/stmary/*.mf
/usr/share/texmf/fonts/source/public/wasy/*.mf
/usr/share/texmf/fonts/source/public/xypic/*.mf

/usr/share/texmf/fonts/tfm/adobe/avantgar/*.tfm
/usr/share/texmf/fonts/tfm/adobe/bookman/*.tfm
/usr/share/texmf/fonts/tfm/adobe/courier/*.tfm
/usr/share/texmf/fonts/tfm/adobe/helvetic/*.tfm
/usr/share/texmf/fonts/tfm/adobe/mathppl/*.tfm
/usr/share/texmf/fonts/tfm/adobe/mathptm/*.tfm
/usr/share/texmf/fonts/tfm/adobe/mathptmx/*.tfm
/usr/share/texmf/fonts/tfm/adobe/ncntrsbk/*.tfm
/usr/share/texmf/fonts/tfm/adobe/palatino/*.tfm
/usr/share/texmf/fonts/tfm/adobe/symbol/*.tfm
/usr/share/texmf/fonts/tfm/adobe/times/*.tfm
/usr/share/texmf/fonts/tfm/adobe/utopia/*.tfm
/usr/share/texmf/fonts/tfm/adobe/zapfding/*.tfm
/usr/share/texmf/fonts/tfm/bitstrea/charter/*.tfm
/usr/share/texmf/fonts/tfm/jknappen/ec/*.tfm
/usr/share/texmf/fonts/tfm/public/bbm/*.tfm
/usr/share/texmf/fonts/tfm/public/bbold/*.tfm
/usr/share/texmf/fonts/tfm/public/cm/*.tfm
/usr/share/texmf/fonts/tfm/public/cmbright/*.tfm
/usr/share/texmf/fonts/tfm/public/cmextra/*.tfm
/usr/share/texmf/fonts/tfm/public/concmath/*.tfm
/usr/share/texmf/fonts/tfm/public/concrete/*.tfm
/usr/share/texmf/fonts/tfm/public/ecc/*.tfm
/usr/share/texmf/fonts/tfm/public/euxm/*.tfm
/usr/share/texmf/fonts/tfm/public/gothic/*.tfm
/usr/share/texmf/fonts/tfm/public/mflogo/*.tfm
/usr/share/texmf/fonts/tfm/public/misc/*.tfm
/usr/share/texmf/fonts/tfm/public/pandora/*.tfm
/usr/share/texmf/fonts/tfm/public/rsfs/*
/usr/share/texmf/fonts/tfm/public/stmary/*
/usr/share/texmf/fonts/tfm/public/wasy/*
/usr/share/texmf/fonts/tfm/public/xypic/*

/usr/share/texmf/fonts/type1/adobe/utopia/*
/usr/share/texmf/fonts/type1/bitstrea/charter/*
/usr/share/texmf/fonts/type1/bluesky/cm/*
/usr/share/texmf/fonts/type1/hoekwater/cm/*
/usr/share/texmf/fonts/type1/hoekwater/rsfs/*
/usr/share/texmf/fonts/type1/hoekwater/stmary/*
/usr/share/texmf/fonts/type1/hoekwater/wasy/*
/usr/share/texmf/fonts/type1/public/xypic/*
/usr/share/texmf/fonts/type1/urw/avantgar/*
/usr/share/texmf/fonts/type1/urw/bookman/*
/usr/share/texmf/fonts/type1/urw/courier/*
/usr/share/texmf/fonts/type1/urw/helvetic/*

/usr/share/texmf/fonts/vf/adobe/avantgar/*
/usr/share/texmf/fonts/vf/adobe/bookman/*
/usr/share/texmf/fonts/vf/adobe/courier/*
/usr/share/texmf/fonts/vf/adobe/helvetic/*
/usr/share/texmf/fonts/vf/adobe/mathppl/*
/usr/share/texmf/fonts/vf/adobe/mathptm/*
/usr/share/texmf/fonts/vf/adobe/mathptmx/*
/usr/share/texmf/fonts/vf/adobe/ncntrsbk/*
/usr/share/texmf/fonts/vf/adobe/palatino/*
/usr/share/texmf/fonts/vf/adobe/times/*
/usr/share/texmf/fonts/vf/adobe/utopia/*
/usr/share/texmf/fonts/vf/adobe/zapfchan/*
/usr/share/texmf/fonts/vf/bitstrea/charter/*

%doc /usr/share/texmf/lists/bibtex
%doc /usr/share/texmf/lists/bibtex-doc
%doc /usr/share/texmf/lists/fonts-doc
%doc /usr/share/texmf/lists/general-doc
%doc /usr/share/texmf/lists/generic-doc
%doc /usr/share/texmf/lists/makeindex-doc
%doc /usr/share/texmf/lists/metapost
%doc /usr/share/texmf/lists/metapost-doc
%doc /usr/share/texmf/lists/misc-fonts
%doc /usr/share/texmf/lists/pictex
%doc /usr/share/texmf/lists/postscript-fonts
%doc /usr/share/texmf/lists/programs-doc
%doc /usr/share/texmf/lists/pstricks
%doc /usr/share/texmf/lists/sauter-fonts
%doc /usr/share/texmf/lists/tetex-base
%doc /usr/share/texmf/lists/texdraw
%doc /usr/share/texmf/lists/xypic

/usr/share/texmf/ls-R
/usr/share/texmf/makeindex/*

/usr/share/texmf/metafont/base/*
/usr/share/texmf/metafont/config/*
/usr/share/texmf/metafont/misc/*

/usr/share/texmf/metapost/base/*
/usr/share/texmf/metapost/config/*
/usr/share/texmf/metapost/misc/*

/usr/share/texmf/mft/*

/usr/share/texmf/tex/context/base/*
/usr/share/texmf/tex/context/config/*
/usr/share/texmf/tex/context/modules/*
/usr/share/texmf/tex/context/ppchtex/*

/usr/share/texmf/tex/fontinst/etx/*
/usr/share/texmf/tex/fontinst/mtx/*
/usr/share/texmf/tex/fontinst/tex/*

/usr/share/texmf/tex/french/base/*
/usr/share/texmf/tex/french/config/*

%attr(-,root,root) /usr/share/texmf/tex/generic

/usr/share/texmf/tex/plain/base/*
/usr/share/texmf/tex/plain/config/*
/usr/share/texmf/tex/plain/misc/*

/usr/share/texmf/tex/texinfo/*

%doc /usr/share/texmf/texconfig/README

/usr/share/texmf/texconfig/g*
/usr/share/texmf/texconfig/v*
/usr/share/texmf/texconfig/x*

/usr/share/texmf/updates.dat

%attr(-,root,root) /usr/share/texmf/web2c

%doc /usr/share/texmf/doc/Makefile
%doc /usr/share/texmf/doc/README
%doc /usr/share/texmf/doc/context
%doc /usr/share/texmf/doc/e*

%doc /usr/share/texmf/doc/fonts/c*
%doc /usr/share/texmf/doc/fonts/ec*
%doc /usr/share/texmf/doc/fonts/fontname
%doc /usr/share/texmf/doc/fonts/oldgerman
%doc %lang(fr) /usr/share/texmf/doc/french
%doc /usr/share/texmf/doc/generic
%doc /usr/share/texmf/doc/help*
%doc /usr/share/texmf/doc/images
%doc /usr/share/texmf/doc/index.html
%doc /usr/share/texmf/doc/makeindex
%doc /usr/share/texmf/doc/metapost
%doc /usr/share/texmf/doc/mkhtml
%doc /usr/share/texmf/doc/newhelpindex.html
%doc /usr/share/texmf/doc/programs
%doc /usr/share/texmf/doc/tetex

%files latex 
%defattr(644,root,root,755)

/usr/share/texmf/etex/latex/misc/etex.sty
/usr/share/texmf/fonts/source/public/latex/*
/usr/share/texmf/fonts/tfm/public/latex/*
/usr/share/texmf/lists/latex-doc
/usr/share/texmf/lists/latex-extra
/usr/share/texmf/tex/generic/pictex/latexpicobjs.tex
/usr/share/texmf/tex/generic/xypic/xylatex.ini
/usr/share/texmf/tex/latex/*

%attr(755,root,root) /usr/bin/latex
%attr(755,root,root) /usr/bin/pslatex

%attr(644,root, man) /usr/man/man1/latex.1.bz2
%attr(644,root, man) /usr/man/man1/pdflatex.1.bz2

/usr/info/latex.info*

%doc /usr/share/texmf/doc/latex
%attr(711,root,root) /usr/bin/bibtex
%attr(644,root, man) /usr/man/man1/bibtex.1.bz2

/usr/share/texmf/bibtex/bib/*
/usr/share/texmf/bibtex/bst/base/*
/usr/share/texmf/bibtex/bst/germbib/*
/usr/share/texmf/bibtex/bst/komascr/*
/usr/share/texmf/bibtex/bst/natbib/*

%doc /usr/share/texmf/doc/bibtex/

%files etex
%defattr(644,root,root,755)

%attr(711,root,root) /usr/bin/elatex
%attr(644,root, man) /usr/man/man1/elatex.1.bz2

%attr(755,root,root) /usr/bin/einitex
%attr(755,root,root) /usr/bin/eplain
%attr(711,root,root) /usr/bin/etex
%attr(755,root,root) /usr/bin/evirtex

%attr(644,root, man) /usr/man/man1/einitex.1.bz2
%attr(644,root, man) /usr/man/man1/eplain.1.bz2
%attr(644,root, man) /usr/man/man1/etex.1.bz2
%attr(644,root, man) /usr/man/man1/evirtex.1.bz2

%doc /usr/share/texmf/lists/eplain
%doc /usr/share/texmf/lists/eplain-doc
/usr/share/texmf/tex/eplain/*

%files omega 
%defattr(644,root,root,755)

%attr(711,root,root) /usr/bin/iniomega
%attr(711,root,root) /usr/bin/omega
%attr(711,root,root) /usr/bin/viromega
%attr(644,root, man) /usr/man/man1/iniomega.1.bz2
%attr(644,root, man) /usr/man/man1/omega.1.bz2
%attr(644,root, man) /usr/man/man1/viromega.1.bz2

/usr/share/texmf/fonts/ofm/public/omega/*
/usr/share/texmf/fonts/tfm/public/omega/*.tfm
/usr/share/texmf/fonts/type1/public/omega/*

/usr/share/texmf/omega/otp/omega/*
/usr/share/texmf/omega/plain/config/*
/usr/share/texmf/omega/latex/*
/usr/share/texmf/omega/ocp/char2uni/*
/usr/share/texmf/omega/ocp/misc/*
/usr/share/texmf/omega/otp/char2uni/*
/usr/share/texmf/omega/otp/misc/*

%doc /usr/share/texmf/doc/omega

%attr(711,root,root) /usr/bin/odvips
%attr(755,root,root) /usr/bin/oxdvi
%attr(711,root,root) /usr/bin/oxdvi.bin

%files pdftex 
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/pdfinitex
%attr(711,root,root) /usr/bin/pdftex
%attr(755,root,root) /usr/bin/pdfvirtex
%attr(644,root, man) /usr/man/man1/pdfinitex.1.bz2
%attr(644,root, man) /usr/man/man1/pdftex.1.bz2
%attr(644,root, man) /usr/man/man1/pdfvirtex.1.bz2

/usr/share/texmf/pdftex/base/*
/usr/share/texmf/pdftex/config/*
/usr/share/texmf/pdftex/plain/misc/*
/usr/share/texmf/pdftex/texinfo/*

%config /usr/share/texmf/pdftex/latex/config/pdflatex.ini

%attr(755,root,root) /usr/bin/pdflatex 
%doc /usr/share/texmf/doc/pdftex

%files xdvi 
%defattr(644,root,root,755)

%config /etc/X11/wmconfig/xdvi

%attr(711,root,root) /usr/bin/xdvi.bin
%attr(755,root,root) /usr/bin/xdvi

%attr(644,root, man) /usr/man/man1/xdvi.1.bz2
/usr/share/texmf/tex/generic/xypic/xyxdvi.tex
/usr/share/texmf/xdvi/XDvi

%files dvips 
%defattr(644,root,root,755)

%attr(755,root,root) /usr/lib/rhs/rhs-printfilters/dvi-to-ps.fpi

%attr(-,root,root) /usr/share/texmf/dvips

/usr/share/texmf/tex/generic/pstricks/dvipsone.con
/usr/share/texmf/tex/generic/xypic/xydvips.tex
/usr/share/texmf/tex/plain/dvips/*
/usr/share/texmf/tex/latex/graphics/*.def
/usr/share/texmf/tex/latex/hyperref/*.def
/usr/share/texmf/tex/latex/dvips/*.sty

%doc /usr/share/texmf/tex/latex/dvips/README

%attr(711,root,root) /usr/bin/dvips
%attr(644,root, man) /usr/man/man1/dvips.1.bz2

/usr/info/dvips.info*

%files dvilj 
%defattr(644,root,root,755)
/usr/share/texmf/tex/latex/dvilj/*.sty

%attr(711,root,root) /usr/bin/dvilj
%attr(711,root,root) /usr/bin/dvilj2p
%attr(711,root,root) /usr/bin/dvilj4
%attr(711,root,root) /usr/bin/dvilj4l
%attr(644,root, man) /usr/man/man1/dvilj.1.bz2

%files afm 
%defattr(644,root,root,755)

/usr/share/texmf/fonts/afm/*

%attr(711,root,root) /usr/bin/afm2tfm
%attr(644,root, man) /usr/man/man1/afm2tfm.1.bz2

%files ams 
%defattr(644,root,root,755)

%attr(755,root,root) /usr/bin/amstex
%attr(644,root, man) /usr/man/man1/amstex.1.bz2

/usr/share/texmf/fonts/source/ams/cmextra/*
/usr/share/texmf/fonts/source/ams/cyrillic/*
/usr/share/texmf/fonts/source/ams/euler/*
/usr/share/texmf/fonts/source/ams/symbols/*
/usr/share/texmf/fonts/tfm/ams/cmextra/*.tfm
/usr/share/texmf/fonts/tfm/ams/cyrillic/*.tfm
/usr/share/texmf/fonts/tfm/ams/euler/*.tfm
/usr/share/texmf/fonts/tfm/ams/symbols/*.tfm
/usr/share/texmf/fonts/type1/bluesky/ams/*

%doc /usr/share/texmf/lists/ams-doc
%doc /usr/share/texmf/lists/ams-fonts
%doc /usr/share/texmf/lists/amstex

/usr/share/texmf/tex/amstex/base/*
/usr/share/texmf/tex/amstex/config/*
/usr/share/texmf/bibtex/bst/ams/*

%doc /usr/share/texmf/doc/ams
%doc /usr/share/texmf/doc/latex/amsfonts
%doc /usr/share/texmf/doc/latex/amslatex
%doc /usr/share/texmf/doc/fonts/ams

%changelog
* Sun Dec 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
[0.9-6.2d]
- added missing files... 

* Tue Dec  8 1998 Ziemek Borowski <zmb@faq-bot.ziembor.waw.pl>
[0.9-6d]
- added tetex-pdftex subpackage 
- removed doc subpackage 

* Sun Oct 11 1998 <ziembor@faq-bot.ziembor.waw.pl>
[0.9-5]
- filelist move to spec 
- more informative %files (added %doc, %attr for binaries)

* Thu Sep 24 1998 Cristian Gafton <gafton@redhat.com>
- credted the doc subpackage
- fully buildroot
- require dialog in the main package
- add support for wmconfig in for the xdvi package

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- upgrade to 0.9
- texmf-src package is gone
- use /var/lib/texmf instead of /var/tmp/texmf

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- make sub-packages depend on tetex (problem #214)

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- eliminate environment when running texhash (problem #849)

* Mon Aug 17 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Feb  5 1998 Otto Hammersmith <otto@redhat.com>
- added install-info support (dvips, fontname and kpathsea)
- combined the two changelogs in the spec file.

* Tue Oct 14 1997 Michael Fulbright <msf@redhat.com>
- Fixed dvi-to-ps.fpi to create temp files more safely.

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Apr  8 1997 Michael Fulbright <msf@redhat.com>
- Removed afmdoit from file list (mistakenly added in release 3 rpm)

* Mon Mar 24 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to tetex-lib to 0.4pl8 and fixed cron tmpwatch entry to not
  delete /var/lib/texmf/fonts and /var/lib/texmf/texfonts

* Fri Mar 07 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.4pl7.

* Mon Feb 17 1997 Michael Fulbright <msf@redhat.com>
- Upgraded to 0.4pl6, and fixed file permissions on /var/lib/texmf/texfonts
  so normal users could create fonts on demand.
