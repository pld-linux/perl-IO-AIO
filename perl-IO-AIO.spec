#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	IO
%define		pnam	AIO
Summary:	IO::AIO - Perl Asynchronous Input/Output
Summary(pl):	IO::AIO - asynchroniczne wej¶cie/wyj¶cie w Perlu
Name:		perl-IO-AIO
Version:	1.71
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c256b5e48e40a60e90aa7562abbcd70f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements asynchronous I/O using whatever means your
operating system supports.

%description -l pl
Ten modu³ implementuje asynchroniczne we/wy przy u¿yciu dowolnych
metod obs³ugiwanych przez system operacyjny.

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
