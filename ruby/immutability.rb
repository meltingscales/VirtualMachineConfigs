str = "    hi mom :)     "

puts str

str.freeze

# This will error because `str` is frozen... Try commenting it out.
str.strip!


str = "new string"

puts "is str frozen? #{str.frozen?}"

str << " with extra stuff"

puts str