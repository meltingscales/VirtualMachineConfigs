$LOAD_PATH << "."
require "measure"

m = Measure.new
puts "Radius: "
r = gets.chomp.to_i

puts "Area: #{m.area(r).round(2)}"
puts "Perimeter: #{m.perim(r).round(2)}"

# Can also use class methods. Must comment 'extend' in 'measure.rb'.
# puts "Area: #{Measure.area(r).round(2)}"
# puts "Perimeter: #{Measure.perim(r).round(2)}"