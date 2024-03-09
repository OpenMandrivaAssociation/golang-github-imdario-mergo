# Run tests in check section
%bcond_without check

# https://github.com/imdario/mergo
%global goipath		github.com/imdario/mergo
%global forgeurl	https://github.com/imdario/mergo
Version:		0.3.16

%gometa

Summary:	Merging Go structs and maps
Name:		golang-github-imdario-mergo

Release:	1
Source0:	https://github.com/imdario/mergo/archive/v%{version}/mergo-%{version}.tar.gz
URL:		https://github.com/imdario/mergo
License:	BSD
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with check}
BuildRequires:	golang(gopkg.in/yaml.v3)
%endif
BuildArch:	noarch

%description
A helper to merge structs and maps in Golang. Useful for
configuration default values, avoiding messy if-statements.

Mergo merges same-type structs and maps by setting default
values in zero-value fields. Mergo won't merge unexported
(private) fields. It will do recursively any exported one.
It also won't merge structs inside maps (because they are
not addressable using Go reflection).

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n mergo-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

