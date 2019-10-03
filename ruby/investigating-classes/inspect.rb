class Foo
  @@count = 0

  def initialize(m, c)
    @m = m
    @c = c
  end

  def calc
    puts @m * @c ** 2
  end

  def test
    @@count += 1
  end
end


bar = Foo.new(1, 186000)

puts bar.inspect
gets

puts bar.object_id
gets

puts bar.methods.sort
gets

puts bar.public_methods.sort
