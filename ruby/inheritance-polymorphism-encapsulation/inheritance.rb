class Mammal
  def breathe
    puts "WHOOOSH I GOT LUNGS BRO WOOOOOOOOOOOOOOOOOOOOOO"
  end
end


class Dog < Mammal
  def bark
    puts "wan wan"
  end
end

dalton = Dog.new
dalton.breathe
dalton.bark

okapi = Mammal.new
okapi.breathe
okapi.bark # Won't work, it cannot. It's just a mammal.