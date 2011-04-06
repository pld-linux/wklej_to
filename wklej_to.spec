Summary:	wklej.to service client
Summary(pl.UTF-8):	Klient serwisu wklej.to
Name:		wklej_to
Version:	1
Release:	1
License:	GPL
Group:		Applications
Source0:	%{name}.tar.gz
# Source0-md5:	9cebe9808faf64ee3bd3ea88577d77d6
URL:		http://wklej.to/page/klienty
Requires:	python-PyQt4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Written in python, works on any operating system wklej.to service
client in text version. Fully opened source code (GPL), full
funcionality of service implemented.

%description -l pl.UTF-8
Napisany w pythonie, działający pod dowolnym systemem operacyjnym
klient serwisu wklej.to w wersji tekstowej. Kod w całości otwarty
(GPL), zaimplementowana w nim jest pełna funkcjonalność serwisu.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
