#
# spec file for package perl-TOML
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name TOML
Name:           perl-TOML
Version:        0.92
Release:        0
License:        CHECK(Artistic-1.0 or GPL-1.0-or-later)
Summary:        Parser for Tom's Obvious, Minimal Language
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        TOML-1399992340.24e1541.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(TOML::Parser)
Requires:       perl(TOML::Parser)
%{perl_requires}

%description
'TOML' implements a parser for Tom's Obvious, Minimal Language, as defined
at https://github.com/mojombo/toml. 'TOML' exports two subroutines,
'from_toml' and 'to_toml',

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changelog README
%license COPYING

%changelog
