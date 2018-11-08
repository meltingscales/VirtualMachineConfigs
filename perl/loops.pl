#!/bin/perl
use warnings;
use strict;

my $in = 'Y';
my $x = 0;

my $pat = m/[yY]/;

while($in =~ $pat) { # While they enter 'Y' or 'y'...
  
  printf("Whee! We've looped %d times!\n", $x);
  
  $x++;
  
  printf("Continue? (Y/N)\n > ");
  
  $in = <STDIN>;
  chomp $in;
}
