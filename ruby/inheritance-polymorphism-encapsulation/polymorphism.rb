
class Animal
  def speak
    puts "<animal noises>"
  end
  def hunger
    puts "I, a #{self.class.name}, am hungy. FEED ME."
  end
end

class Dog < Animal
  def speak
    puts "WAN WAN"
  end
end

class Cat < Animal
  def speak
    puts "lasaga."
  end
end

[Animal.new, Dog.new, Cat.new].each do |animal|
  animal.speak
  animal.hunger
  puts
end