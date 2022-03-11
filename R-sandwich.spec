#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sandwich
Version  : 3.0.1
Release  : 66
URL      : https://cran.r-project.org/src/contrib/sandwich_3.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sandwich_3.0-1.tar.gz
Summary  : Robust Covariance Matrix Estimators
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-zoo
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
## Robust Covariance Matrix Estimators
Model-robust standard error estimators for cross-sectional, time series,
clustered, panel, and longitudinal data. Modular object-oriented
implementation with support for many model objects, including: `lm`,
`glm`, `survreg`, `coxph`, `mlogit`, `polr`, `hurdle`, `zeroinfl`, and
beyond.

%prep
%setup -q -c -n sandwich
cd %{_builddir}/sandwich

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641118576

%install
export SOURCE_DATE_EPOCH=1641118576
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sandwich
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sandwich
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sandwich
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sandwich || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sandwich/CITATION
/usr/lib64/R/library/sandwich/DESCRIPTION
/usr/lib64/R/library/sandwich/INDEX
/usr/lib64/R/library/sandwich/Meta/Rd.rds
/usr/lib64/R/library/sandwich/Meta/data.rds
/usr/lib64/R/library/sandwich/Meta/features.rds
/usr/lib64/R/library/sandwich/Meta/hsearch.rds
/usr/lib64/R/library/sandwich/Meta/links.rds
/usr/lib64/R/library/sandwich/Meta/nsInfo.rds
/usr/lib64/R/library/sandwich/Meta/package.rds
/usr/lib64/R/library/sandwich/Meta/vignette.rds
/usr/lib64/R/library/sandwich/NAMESPACE
/usr/lib64/R/library/sandwich/NEWS.md
/usr/lib64/R/library/sandwich/R/sandwich
/usr/lib64/R/library/sandwich/R/sandwich.rdb
/usr/lib64/R/library/sandwich/R/sandwich.rdx
/usr/lib64/R/library/sandwich/data/InstInnovation.rda
/usr/lib64/R/library/sandwich/data/Investment.rda
/usr/lib64/R/library/sandwich/data/PetersenCL.rda
/usr/lib64/R/library/sandwich/data/PublicSchools.rda
/usr/lib64/R/library/sandwich/doc/index.html
/usr/lib64/R/library/sandwich/doc/sandwich-CL.R
/usr/lib64/R/library/sandwich/doc/sandwich-CL.Rnw
/usr/lib64/R/library/sandwich/doc/sandwich-CL.pdf
/usr/lib64/R/library/sandwich/doc/sandwich-OOP.R
/usr/lib64/R/library/sandwich/doc/sandwich-OOP.Rnw
/usr/lib64/R/library/sandwich/doc/sandwich-OOP.pdf
/usr/lib64/R/library/sandwich/doc/sandwich.R
/usr/lib64/R/library/sandwich/doc/sandwich.Rnw
/usr/lib64/R/library/sandwich/doc/sandwich.pdf
/usr/lib64/R/library/sandwich/doc/sim-CL.R
/usr/lib64/R/library/sandwich/doc/sim-CL.rda
/usr/lib64/R/library/sandwich/help/AnIndex
/usr/lib64/R/library/sandwich/help/aliases.rds
/usr/lib64/R/library/sandwich/help/figures/README-sandwich.svg
/usr/lib64/R/library/sandwich/help/paths.rds
/usr/lib64/R/library/sandwich/help/sandwich.rdb
/usr/lib64/R/library/sandwich/help/sandwich.rdx
/usr/lib64/R/library/sandwich/html/00Index.html
/usr/lib64/R/library/sandwich/html/R.css
/usr/lib64/R/library/sandwich/tests/Examples/sandwich-Ex.Rout.save
/usr/lib64/R/library/sandwich/tests/vcovCL.R
/usr/lib64/R/library/sandwich/tests/vcovCL.Rout.save
/usr/lib64/R/library/sandwich/tests/vcovPC.R
/usr/lib64/R/library/sandwich/tests/vcovPC.Rout.save
/usr/lib64/R/library/sandwich/tests/vcovPL.R
/usr/lib64/R/library/sandwich/tests/vcovPL.Rout.save
