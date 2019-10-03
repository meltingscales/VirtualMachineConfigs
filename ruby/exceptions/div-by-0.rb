# noinspection RubyUnnecessaryReturnStatement
class Test
  def div(x)
    raise ZeroDivisionError, "division by zero: Cannot divide #{x} by 0." if x == 0
    return 8 / x
  end
end

t = Test.new

puts t.div(2)

puts t.div(0)