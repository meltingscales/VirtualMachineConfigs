@ECHO OFF

REM Q: What the heck is this file? Ew, batch is ugly.

REM A: Yeah, batch is pretty ugly.

REM It converts my `MD` files into `DOCX` files. Thanks `Pandoc`!
REM Cool, huh?

REM Take that, nonexistent UNC path support! Ha!
REM (This command allows UNC paths in `CMD.EXE` scripts)
@pushd %~dp0


FOR %%A IN (*.md) DO (
	ECHO "%%A" "->" "%%~nA".docx
	
	pandoc -s %%A -o %%~nA.docx --toc
)

@popd