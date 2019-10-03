# noinspection RubyClassVariableUsageInspection,RubyParenthesesAfterMethodCallInspection
class Sphere
  PI = 3.14
  @@count = 0

  def initialize()

  end

  def vol(r)
    inc_calcs()

    puts @@count


    return (1.333 * PI * r ** 3).round(3)

  end

  def inc_calcs
    @@count += 1
  end

  private :inc_calcs


end

foo = Sphere.new()

puts foo.vol(1)
puts foo.vol(1)
puts foo.vol(10)

# Can't access this from outside the class. Will error.
foo.inc_calcs