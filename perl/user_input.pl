#!/bin/perl
use warnings;
use strict;


print "Enter first number:\n > ";
my $x = <STDIN>;
chomp $x;

print "Enter second number:\n > ";
my $y = <STDIN>;
chomp $y;

printf "%d + %d = %d", $x, $y, ($x + $y)