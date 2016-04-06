# contrail-selinux
SELinux policy for opencontrail

Contrail-selinux is a selinux policy module tested for use with contrail 3 and EL7. 

The policy may look a bit strange at first inspection, but keep in mind that most contrail
appliations needs to execute system binaries to work, often in a sub shell. 

In addition, many of the ports used by contrail are already labeled with other names, or
not labeled at all. Thus the connect/bind statements may be harder to read than desirable.

Currently, this policy covers config, control, analytics and vrouter-agent. 

To get rpms, simply clone this and type "make"


Notes:

    - vrouter-agent
        - cap sys_module 
        - needs to exec virsh (domain transistion)
        - needs to exec ps, gawk, bash.
        - need external types (virsh_exec_t, virsh_t)

    - contrail-named
        - need external types (named_var_run_t)

    
