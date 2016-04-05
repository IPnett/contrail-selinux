%define _prefix   /

Name:		contrail-selinux	
Version:	1.0.0
Release:	1%{?dist}
Summary:	SELinux Policy for contrail

Group:		System Environment/Base
BuildArch:	noarch
License:	GPLv2
Requires:		policycoreutils, libselinux-utils
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):	policycoreutils
BuildRequires:		selinux-policy selinux-policy-devel
Source0: 		./selinux/contrail.pp


%description
SELinux Policy module for use with contrail


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/contrail/contrail.pp

%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/contrail/
%attr(0600, root, root) /usr/share/selinux/packages/contrail/contrail.pp

%post
	/usr/sbin/semodule -i /usr/share/selinux/packages/contrail/contrail.pp 
	/usr/sbin/restorecon -R /usr/bin/
        if [ -d /var/log/contrail ]; then
	 /usr/sbin/restorecon -R /var/log/contrail 
	fi
	if [ -d /var/run/contrail ]; then
	 /usr/sbin/restorecon -R /var/run/contrail 
	fi
	if [ -d /var/lib/contrail ]; then
	 /usr/sbin/restorecon -R /var/lib/contrail
	fi
	if [ -d /etc/contrail ]; then
	 /usr/sbin/restorecon -R /etc/contrail 
	fi
	if [ -d /usr/lib/systemd/system ]; then
	 /usr/sbin/restorecon -R /usr/lib/systemd/system 
	fi


%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/semodule -r contrail
	/usr/sbin/restorecon -R /usr/bin/ 
        if [ -d /var/log/contrail ]; then
	 /usr/sbin/restorecon -R /var/log/contrail 
	fi
	if [ -d /var/run/contrail ]; then
	 /usr/sbin/restorecon -R /var/run/contrail 
	fi
	if [ -d /var/lib/contrail ]; then
	 /usr/sbin/restorecon -R /var/lib/contrail
	fi
	if [ -d /etc/contrail ]; then
	 /usr/sbin/restorecon -R /etc/contrail 
	fi
	if [ -d /usr/lib/systemd/system ]; then
	 /usr/sbin/restorecon -R /usr/lib/systemd/system 
	fi

fi


%changelog

