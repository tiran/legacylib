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
	ossaudiodev \
	pipes \
	smtpd \
	sndhdr \
	spwd \
	sunau \
	uu \
	xdrlib \
	legacytest \
	$(NULL)

SKIPPED_MODULES=\
	msilib \
	$(NULL)

.PHONY=all
all: $(MODULES) docs

FORCE:

$(MODULES): dist FORCE
	rm -f $(CURDIR)/dist/$@*
	cd $@; $(PYTHON) setup.py check --strict --metadata
	cd $@; $(PYTHON) setup.py sdist -d $(CURDIR)/dist/
	cd $@; $(PYTHON) setup.py bdist_wheel -d $(CURDIR)/dist/

dist:
	mkdir $@

docs: FORCE
	$(MAKE) -C docs html

.PHONY=clean
clean:
	rm -rf $(CURDIR)/dist
	rm -rf $(CURDIR)/*/build
	find $(CURDIR) -name __pycache__ -and -type d | xargs rm -rf
