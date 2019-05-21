PYTHON=python3
NULL=
MODULES=\
	aifc \
	asynchat \
	asyncore \
	audioop \
	binhex \
	cgi \
	cgitb \
	chunk \
	colorsys \
	crypt \
	fileinput \
	formatter \
	imghdr \
	msilib \
	nis \
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
	ossaudiodev \
	spwd \
	$(NULL)

.PHONY=all
all: $(MODULES)

$(MODULES): dist FORCE
	rm -f $(CURDIR)/dist/$@*
	cd $@; $(PYTHON) setup.py check --strict --metadata
	cd $@; $(PYTHON) setup.py sdist -d $(CURDIR)/dist/
	cd $@; $(PYTHON) setup.py bdist_wheel -d $(CURDIR)/dist/

FORCE:

dist:
	mkdir $@

.PHONY=clean
clean:
	rm -rf $(CURDIR)/dist
	find $(CURDIR) -name build -and -type d | xargs rm -rf
	find $(CURDIR) -name __pycache__ -and -type d | xargs rm -rf