Summary:	Sequel: The Database Toolkit for Ruby
Name:		ruby-sequel
Version:	2.4.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/sequel-%{version}.gem
# Source0-md5:	6f496df294eae4b6f8c8d5ec89c0c93d
URL:		http://sequel.rubyforge.org/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sequel: The Database Toolkit for Ruby.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/sequel*
