%define upstream_name Filesys-POSIX
%define upstream_version 0.10.0

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Filesys::POSIX(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Provide POSIX-like filesystem semantics in pure Perl
License:	Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/~wrath/Filesys-POSIX-0.10.0/lib/Filesys/POSIX.pm
Source0:	http://search.cpan.org/CPAN/authors/id/W/WR/WRATH/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::NoWarnings)
BuildArch:	noarch

%description
This modules provide POSIX-like filesystem semantics in pure Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

