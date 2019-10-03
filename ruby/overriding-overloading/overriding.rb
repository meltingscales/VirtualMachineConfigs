class Mammal
  def breathe
    puts "AAAAAAAAAAAAAAAAAA I HAVE LUNGS"
  end

  def speak
    puts "hi"
  end
end


class Dog < Mammal
  def speak
    puts "wan wan"
  end
end

dalton = Dog.new
dalton.breathe
dalton.speak