# noinspection RubyDeadCode,RubyArgCount
class Test2

  def raise_rescue
    begin

      puts "message before exception"
      raise "I don't feel so good, Mr Stark..."
      puts "I don't run :)"
    rescue
      puts "Just kidding Thanos dies."
    end
  end

  def raise
    raise_rescue
  end

end

t = Test2.new
t.raise