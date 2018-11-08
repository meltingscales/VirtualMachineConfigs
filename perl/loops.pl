#!/bin/perl
use warnings;
use strict;

my $in = 'Y';
my $x = 0;

while($in =~ /^[yY]/) { # While they enter 'Y' or 'y'...
  
  printf("Whee! We've looped %d times!\n", $x);
  $x++;
  
  printf("Continue? (Y/N)\n > ");
  
  $in = <STDIN>;
  chomp $in;
}

printf("Bye!\n");