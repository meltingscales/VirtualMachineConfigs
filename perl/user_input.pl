#!/bin/perl
use warnings;
use strict;
use Scalar::Util qw(looks_like_number);

my $x = "";
my $y = "";

until (looks_like_number($x)) {
    print "Enter first number:\n > ";
    $x = <STDIN>;
    chomp $x;
}

until (looks_like_number($y)) {
    print "Enter second number:\n > ";
    $y = <STDIN>;
    chomp $y;
}

printf("%d + %d = %d", $x, $y, ($x + $y))