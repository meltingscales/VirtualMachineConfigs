#!/bin/perl
use warnings;
use strict;
use English qw( -no_match_vars ); # This is so we can use $OSNAME.

system("clear");

printf("Your OS is '%s'.\n", $OSNAME);

if($OSNAME =~ "MSWin32") {

	printf("Hello, Windows user.\n");
	
	printf("Output from 'dir' command:\n");
	
	my $filelist = `dir`;
	
	print($filelist);

} elsif($OSNAME =~ "unix") {

	printf("Hello, Unix user.\n");
	
	printf("Output from 'ls' command:\n");
	
	my $filelist = `ls`;
	
	print($filelist)

} elsif($OSNAME =~ "darwin") {

	printf("appel :>)")

} else {
	printf("What OS u got??? %s aint no OS I ever heard of? They speak English in %s?\n",$OSNAME,$OSNAME);
}