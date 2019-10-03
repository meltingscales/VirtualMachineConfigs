class Person
  def initialize(name, role)
    @name = name
    @role = role
  end

  def set_salary(s)
    @salary = s
  end

  def name
    @name
  end

  def role
    @role
  end

  def salary
    @salary
  end

end

me = Person.new("henry", "employee")
me.set_salary(70000)

puts "#{me.name} is a #{me.role} and makes #{me.salary} per year."