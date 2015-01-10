#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Parse
%define		pnam	RPM-Spec
%include	/usr/lib/rpm/macros.perl
Summary:	Parse::RPM::Spec - Perl extension to parse RPM spec files
Name:		perl-Parse-RPM-Spec
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parse/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	247aadd8017bbd5f058e79fe3d43302c
URL:		http://search.cpan.org/dist/Parse-RPM-Spec/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Moose)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RPM is the package management system used on Linux distributions based
on Red Hat Linux. These days that includes Fedora, Red Hat Enterprise
Linux, Centos, SUSE, Mandriva and many more.

RPMs are build from the source of a packages along with a spec file.
The spec file controls how the RPM is built.

This module creates Perl objects which module spec files. Currently it
gives you simple access to various pieces of information from the spec
file.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Parse/RPM
%{perl_vendorlib}/Parse/RPM/Spec.pm
%{_mandir}/man3/Parse::RPM::Spec.3pm*
