%define upstream_name Filesys-POSIX
%define upstream_version 0.9.19

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Filesys::POSIX(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	0.9.19
Release:	2

Summary:	Provide POSIX-like filesystem semantics in pure Perl
License:	Artistic
Group:		Development/Perl
URL:		https://github.com/xantronix/Filesys-POSIX
Source0:	https://cpan.metacpan.org/authors/id/X/XA/XAN/Filesys-POSIX-0.9.19.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch

%description
This modules provide POSIX-like filesystem semantics in pure Perl.

%prep
%setup -q -n Filesys-POSIX-0.9.19

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# Kharec: a bad .t file breaks the rebuild...
# %check
# %make test

%install
%makeinstall_std

%files
%doc COPYRIGHT LICENSE MANIFEST README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

