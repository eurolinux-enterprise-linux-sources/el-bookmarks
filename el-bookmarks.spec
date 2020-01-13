Name:           el-bookmarks
Version:        6
Release:        2.1.el6
Summary:        EuroLinux bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://www.euro-linux.com/
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks


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
* Tue Sep 15 2015 Aleksander Baranowski <aleksander.baranowski@euro-linux.com>
- Updated bookmarks, rebranded for EL.

* Mon Apr 2 2012 Pat Riehecky <riehecky@fnal.gov> 6-2.el6
- Updated bookmarks, added links to useful external resources

* Fri Nov 12 2010 Troy Dawson <dawson@fnal.gov> 6-1.el6
- Updated to final SL 6 release

* Wed Jul 14 2010 Troy Dawson <dawson@fnal.gov> 6-0.el6
- Changed the bookmarks to be SL's bookmarks

* Fri Jan 29 2010 Christopher Aillon <caillon@redhat.com> 6-0
- Initial SRPM

