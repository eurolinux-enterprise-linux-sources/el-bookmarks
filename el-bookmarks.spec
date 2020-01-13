Name:           el-bookmarks
Version:        7
Release:        7.el7
Summary:        EuroLinux bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://www.euro-linux.com
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks
Provides:       redhat-bookmarks
Provides:       sl-bookmarks


%description
This package contains the default bookmarks for EuroLinux

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Mon Dec 23 2019 Aleksander Baranowski <aleksander.baranowski@euro-linux.com> 7.7
- Version up for new build system.

* Fri Jul 10 2015 Aleksander Baranowski <aleksander.baranowski@euro-linux.com>  7.1
- Rebranding from SL to EL 

* Tue May  6 2015 Pat Riehecky <riehecky@fnal.gov.com> 7-0
- Initial package
