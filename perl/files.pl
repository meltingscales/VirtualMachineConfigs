#!/bin/perl
use warnings;
use strict;

my $FILEPATH = "./coolfile.txt";

my $JACKS = 0;
my $JILLS = 0;

open(my $filehandle, $FILEPATH) # Open file.
  or die("Could not open '$FILEPATH'!");

while(my $row = <$filehandle>) { # Loop through lines of file.
  chomp($row); # Remove whitespace
  
  my @arr = split(/:/, $row); # Split string by colons
  
  printf("%s has %d melons.\n", $arr[0], $arr[1]);
  
  if($arr[0] eq 'jack') {
    $JACKS++;
  } elsif($arr[0] eq 'jill') {
    $JILLS++;
  }
  
}

printf("%d jacks, %d jills.", $JACKS, $JILLS);


close($filehandle) or die("Could not close '$FILEPATH'!")
