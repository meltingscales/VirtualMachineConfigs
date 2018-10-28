#!/bin/perl
use warnings;
use strict;

my @foods = qw(broccoli pizza artichoke dumplings REMOVEME);

sub print_foods {
  for (my $i = 0; $i < @foods; $i++) {
    printf("%dth item is %s.\n", $i, $foods[$i])
  } 
}

print("All foods:\n");
print_foods();
printf("\n");

for(;;) { # Infinite loop.
  
  printf("Enter a food:\n > ");

  my $in = <STDIN>;
  chomp($in);

  push(@foods, $in); # This appends $in to $foods.
  
  unshift(@foods, pop(@foods)); # This will move the last element to the beginning. 
  push(@foods, shift(@foods)); # This will move the first element to the end.
  # Fun fact: The above two statements undo eachother. Cool, huh?
  
  print($foods[0]." and ".$foods[-1]." are the first and last items.\n");
  
  printf("Array has ".scalar(@foods)." items.\n\n");
  
  print_foods();
  
  printf("\n")
  
}
