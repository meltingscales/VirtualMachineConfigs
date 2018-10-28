#!/bin/perl
use warnings;
use strict;

my %people = (
  "jack", "alive",
  "jill", 0,
  "john", "dead",
  "janet", "alive",
);

for (;;) {
  print("Enter name:\n > ");

  my $in=<STDIN>;
  chomp($in);

  if(exists $people{$in}) {
    printf("%s is %s.\n", $in, $people{$in});    
  } else {
    printf("%s doesn't exist. However, these people do:\n", $in);
    print((join ';', keys %people)."\n");
  }
  print("\n")
  
}
