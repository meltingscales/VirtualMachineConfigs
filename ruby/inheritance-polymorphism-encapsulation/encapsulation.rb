class Person
  def initialize(first, last)
    @first = first
    @last = last
  end

  def name
    "#{@first.capitalize} #{@last.capitalize}"
  end
end

person = Person.new('henry', 'post')

puts person.name