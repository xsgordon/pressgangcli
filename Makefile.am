SKYNET_SHELL_TOOLS_CACHE_DIR	?= $(HOME)/skynet-shell-tools-cache

EXTRA_DIST = \
	pressgangcli.spec \
	pressgangcli.spec.in \
	scripts/pressgang-edit \
	scripts/pressgang-get.py \
	scripts/pressgang-put.py \
	scripts/pressgang-config.py \
	scripts/topic.py \
	scripts/config.py 

DISTCLEANFILES = $(PACKAGE)-$(VERSION).tar.gz

rpms: dist
	rpmbuild $(RPM_FLAGS) -ta $(distdir).tar.gz

srpms: dist
	rpmbuild $(RPM_FLAGS) -ts $(distdir).tar.gz

publish: rpms
	mkdir -p $(SKYNET_SHEEL_TOOLS_CACHE_DIR)
	rsync -aq $(shell rpm --eval '%{_rpmdir}')/ $(SKYNET_SHELL_TOOLS_CACHE_DIR)/skynet/
	rsync -aq $(shell rpm --eval '%{_srcrpmdir}')/ $(SKYNET_SHELL_TOOLS_CACHE_DIR)/skynet/src
	createrepo $(SKYNET_SHELL_TOOLS_CACHE_DIR)/skynet

.PHONY: rpms publish srpms

