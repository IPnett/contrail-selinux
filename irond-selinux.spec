%define _prefix   /

Name:		irond-selinux	
Version:	1.0.0
Release:	1%{?dist}
Summary:	SELinux Policy for irond

Group:		System Environment/Base
BuildArch:	noarch
License:	GPLv2
Requires:		policycoreutils, libselinux-utils
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):	policycoreutils
BuildRequires:		selinux-policy selinux-policy-devel
Source0: 		./selinux/irond.pp


%description
SELinux Policy module for use with irond


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/irond/irond.pp

%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/irond/
%attr(0600, root, root) /usr/share/selinux/packages/irond/irond.pp

%post
	/usr/sbin/semodule -i /usr/share/selinux/packages/irond/irond.pp 
	if [ -f /usr/lib/systemd/system/contrail-ifmap-server.service ]; then
		/usr/sbin/restorecon /usr/lib/systemd/system/contrail-ifmap-server.service
	fi
	if [ -f /usr/bin/ifmap-server ]; then
		/usr/sbin/restorecon /usr/bin/ifmap-server
	fi
	if [ -d /etc/ifmap-server ]; then
		/usr/sbin/restorecon  -R /etc/ifmap-server
	fi
	if [ -d /var/log/ifmap-server ]; then
		/usr/sbin/restorecon  -R /etc/ifmap-server
	fi


%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/semodule -r irond
	if [ -f /usr/lib/systemd/system/contrail-ifmap-server.service ]; then
		/usr/sbin/restorecon /usr/lib/systemd/system/contrail-ifmap-server.service
	fi
	if [ -f /usr/bin/ifmap-server ]; then
		/usr/sbin/restorecon /usr/bin/ifmap-server
	fi
	if [ -d /etc/ifmap-server ]; then
		/usr/sbin/restorecon  -R /etc/ifmap-server
	fi
	if [ -d /var/log/ifmap-server ]; then
		/usr/sbin/restorecon  -R /etc/ifmap-server
	fi

fi


%changelog

