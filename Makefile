NULL=
MODULES=\
	aifc \
	asynchat \
	asyncore \
	audioop \
	binhex \
	cgi \
	chunk \
	colorsys \
	crypt \
	fileinput \
	formatter \
	imghdr \
	msilib \
	nntplib \
	pipes \
	smtpd \
	sndhdr \
	sunau \
	uu \
	xdrlib \
	legacytest \
	$(NULL)

SKIPPED_MODULES=\
	nis \
	ossaudiodev \
	spwd \
	$(NULL)

.PHONY=all
all: dist
	for module in $(MODULES); do \
		pushd $${module}; \
		rm -f ../dist/$${module}*; \
		python3 setup.py check --strict --metadata || exit 1; \
		python3 setup.py sdist -d ../dist/ || exit 1; \
		python3 setup.py bdist_wheel -d ../dist/ || exit 1; \
		popd; \
	done

dist:
	mkdir $@
