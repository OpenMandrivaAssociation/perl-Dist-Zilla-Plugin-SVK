%define upstream_name    Dist-Zilla-Plugin-SVK
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Provide the allow_dirty & changelog attributes
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(Cwd)
BuildRequires: perl(DateTime)
BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Role::AfterRelease)
BuildRequires: perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(Dist::Zilla::Tester)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Temp)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Moose::Role)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(Path::Class)
BuildRequires: perl(SVK)
BuildRequires: perl(SVK::Util)
BuildRequires: perl(SVK::XD)
BuildRequires: perl(SVN::Repos)
BuildRequires: perl(String::Formatter)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This set of plugins for the Dist::Zilla manpage can do interesting things
for module authors using http://svk.bestpractical.com to track their work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


