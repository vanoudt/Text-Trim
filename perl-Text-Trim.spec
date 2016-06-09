Name:           perl-Text-Trim
Version:        1.02
Release:        1%{?dist}
Summary:        Remove leading and/or trailing whitespace from strings
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Trim/
Source0:        http://www.cpan.org/authors/id/M/MA/MATTLAW/Text-Trim-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides functions for removing leading and/or trailing
whitespace from strings. It is basically a wrapper around some simple
regexes with a flexible context-based interface.

%prep
%setup -q -n Text-Trim-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 1.02-1
- Specfile autogenerated by cpanspec 1.78.
