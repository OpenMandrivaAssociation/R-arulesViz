%global packname  arulesViz
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1_4
Release:          1
Summary:          arulesViz - Visualizing Association Rules and Frequent Itemsets
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-4.tar.gz
Requires:         R-arules R-MASS R-scatterplot3d R-vcd R-seriation R-igraph
Requires:         R-iplots R-Rgraphviz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-arules
BuildRequires:    R-MASS R-scatterplot3d R-vcd R-seriation R-igraph
BuildRequires:    R-iplots R-Rgraphviz

%description
Various visualization techniques for association rules and itemsets. The
packages also includes several interactive visualizations for rule
exploration. This package extends package arules.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
