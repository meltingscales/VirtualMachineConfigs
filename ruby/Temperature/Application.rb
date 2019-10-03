$LOAD_PATH << '.'
require "TemperatureLib"


class Convert
  include Temp
end

c=Convert.new

puts "Temperature in f:"
f=gets.chomp.to_i
puts "Temperature in c = #{c.farenheit_to_c(f).round(2)}"
