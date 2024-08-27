Name: nodejs-picocolors
Version: 1.0.1
Release: 1
Source0: https://github.com/alexeyraspopov/picocolors/archive/refs/tags/v%{version}.tar.gz
Summary: Node.js library for terminal output formatting with ANSI colors
URL: https://github.com/alexeyraspopov/picocolors
License: ISC
Group: Development/Other
BuildRequires: nodejs
BuildRequires: nodejs-packaging
BuildRequires: rsync
BuildArch: noarch

%description
Node.js library for terminal output formatting with ANSI colors

%prep
%autosetup -p1 -n picocolors-%{version}

%build

%install
npm -g --omit=dev --prefix=/tmp/INSTROOT.$$%{_prefix} install
# Using rsync to dereference symlinks
rsync -rptgoDLk /tmp/INSTROOT.$$/ %{buildroot}
rm -rf /tmp/INSTROOT.$$

%files
%{nodejs_sitelib}/picocolors
