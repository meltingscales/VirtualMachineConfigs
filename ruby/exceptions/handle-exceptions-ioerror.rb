# noinspection RubyDeadCode,RubyArgCount
class Test

  def raise_rescue
    begin
      raise IOError, "Your hard disk exploded. Sorry."
    rescue IOError => e
      puts e.message

      e.backtrace.each do |x|
        puts x
      end

    end
  end

  def throw
    raise_rescue
  end

end

t = Test.new
t.throw