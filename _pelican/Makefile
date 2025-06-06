PY?=
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/..
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=main
GITHUB_PAGES_COMMIT_MESSAGE=Generate Pelican site


DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make clean                          remove the generated files         '
	@echo '   make publish                        generate using production settings '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make github                         upload the web site                '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

clean:
	rm -rf "$(OUTPUTDIR)"/feeds
	rm -rf "$(OUTPUTDIR)"/theme
	rm -rf "$(OUTPUTDIR)"/author
	rm -rf "$(OUTPUTDIR)"/category
	rm -rf "$(OUTPUTDIR)"/pages
	rm -rf "$(OUTPUTDIR)"/**.html

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

github: clean publish
	git add -A
	git commit -m "mise à jour"
	git push origin $(GITHUB_PAGES_BRANCH)


.PHONY: help clean devserver publish github
