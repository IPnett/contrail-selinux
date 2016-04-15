VERSION ?= 1.0.0
BUILD_NUMBER ?= 1
TOPDIR = /tmp/contrail-selinux-rpm
PWD = $(shell pwd)


rpm: build
	@rpmbuild -v -bb \
			--define "_sourcedir $(PWD)" \
			--define "_rpmdir $(PWD)" \
			--define "_topdir $(TOPDIR)" \
			--define "version $(VERSION)" \
			--define "build_number $(BUILD_NUMBER)" \
			contrail-selinux.spec
	@rpmbuild -v -bb \
			--define "_sourcedir $(PWD)" \
			--define "_rpmdir $(PWD)" \
			--define "_topdir $(TOPDIR)" \
			--define "version $(VERSION)" \
			--define "build_number $(BUILD_NUMBER)" \
			irond-selinux.spec
	mv $(OUTPUTDIR)/*.rpm .

build:
	@make -C ./contrail-policy -f /usr/share/selinux/devel/Makefile
	@mv ./contrail-policy/contrail.pp .
	@make -C ./irond-policy -f /usr/share/selinux/devel/Makefile
	@mv ./irond-policy/irond.pp .


clean:
	@make -C ./contrail-policy -f /usr/share/selinux/devel/Makefile clean
	@make -C ./irond-policy -f /usr/share/selinux/devel/Makefile clean
	@rm -rf $(TOPDIR)
	@rm -rf *.pp
	@rm -rf noarch
