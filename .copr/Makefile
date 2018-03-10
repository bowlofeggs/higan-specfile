srpm:
	dnf -y install rpmdevtools fedpkg
	spectool -g higan.spec
	fedpkg srpm
	cp *.src.rpm $(outdir)
