%define upstream_name    Dist-Zilla-Plugin-SVK
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Provide the allow_dirty & changelog attributes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://svn.openfoundry.org/dzilsvk
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DRBEAN/Dist-Zilla-Plugin-SVK-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Role::AfterRelease)
BuildRequires:	perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:	perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:	perl(Dist::Zilla::Tester)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Has::Sugar)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(SVK)
BuildRequires:	perl(SVK::Util)
BuildRequires:	perl(SVK::XD)
BuildRequires:	perl(SVN::Repos)
BuildRequires:	perl(String::Formatter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)

BuildArch:	noarch

%description
This set of plugins for the Dist::Zilla manpage can do interesting things
for module authors using http://svk.bestpractical.com to track their work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

