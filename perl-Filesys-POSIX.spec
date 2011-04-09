%define upstream_name Filesys-POSIX
%define upstream_version 0.10.0

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Provide POSIX-like filesystem semantics in pure Perl
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/~wrath/Filesys-POSIX-0.10.0/lib/Filesys/POSIX.pm
Source0:	http://search.cpan.org/CPAN/authors/id/W/WR/WRATH/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Test::Exception)
BuildRequires:  perl(Test::NoWarnings)
BuildArch: noarch

%description
This modules provide POSIX-like filesystem semantics in pure Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc COPYRIGHT LICENSE MANIFEST README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*

