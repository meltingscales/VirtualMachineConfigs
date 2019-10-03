class Test
  def raise_exception
    raise "Something ain't right..."
  end

  def throw
    raise_exception
  end
end


t = Test.new
t.throw

print("I'm the gingerbread man and will never be printed!")