Name:		openshift-origin-cartridge-moodle
Version:	3.0.0
Release:	1%{?dist}
Summary:	Provides Moodle cartridge to OpenShift. (Cartridge Format V2)

Group:		Development/Languages
License:	GPLv3
URL:		https://moodle.org
Source0:	openshift-origin-cartridge-moodle.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	openshift-origin-node-util
Requires:   php54
Requires:   php54-php-gd
Requires:   php54-php-mbstring
Requires:   php54-php-soap
Requires:   php54-php-xmlrpc

%description
Moodle is a learning platform designed to provide educators, administrators and learners with a single robust, secure and integrated system to create personalised learning environments. You can download the software onto your own web server or ask one of our knowledgable Moodle Partners to assist you.

Moodle is built by the Moodle project which is led and coordinated by Moodle HQ, an Australian company of 30 developers which is financially supported by a network of 60 Moodle Partner service companies worldwide


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog

