Summary:	Sequel: The Database Toolkit for Ruby
Summary(pl.UTF-8):	Sequel - zestaw narzędzi bazodanowych dla języka Ruby
Name:		ruby-sequel
Version:	2.11.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/sequel-%{version}.gem
# Source0-md5:	736c1577ea9d738d22b8f3eb110074ba
Patch0:		%{name}-rubygems.patch
URL:		http://sequel.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.4.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sequel: The Database Toolkit for Ruby.

%description -l pl.UTF-8
Sequel - zestaw narzędzi bazodanowych dla języka Ruby.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/sequel
%{ruby_rubylibdir}/sequel*
