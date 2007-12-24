#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	AIO
Summary:	IO::AIO - Perl Asynchronous Input/Output
Summary(pl.UTF-8):	IO::AIO - asynchroniczne wejście/wyjście w Perlu
Name:		perl-IO-AIO
Version:	2.51
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a9051ad1eca00a083f9880014fb17c0a
URL:		http://search.cpan.org/dist/IO-AIO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements asynchronous I/O using whatever means your
operating system supports.

%description -l pl.UTF-8
Ten moduł implementuje asynchroniczne we/wy przy użyciu dowolnych
metod obsługiwanych przez system operacyjny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/IO/AIO.pm
%dir %{perl_vendorarch}/auto/IO/AIO
%{perl_vendorarch}/auto/IO/AIO/AIO.bs
%attr(755,root,root) %{perl_vendorarch}/auto/IO/AIO/AIO.so
%{_mandir}/man3/*
