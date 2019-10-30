UUID=$(shell date "+%Y%m%d%H%M%S")-$(shell uuid)

list:
	@grep '^[^#[:space:]].*:' Makefile

all: format backup_src compile

clean: # Remove temporary files.
	rm -rf bak/

backup_src: # Backup the source code.
	mkdir -p bak/
	cp -r "src/" "bak/src-${UUID}"

format: # Format the source code.
	elm-format --yes src/*

compile: # Compile the source code.
	elm make src/*

reactor: # Run the elm dashboard
	elm reactor

show:
	xdg-open index.html