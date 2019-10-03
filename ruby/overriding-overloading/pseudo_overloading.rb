# Ruby doesn't support true overloading, but you can accept varargs to get around this.
# Thanks Ruby and Python. Bro >:(

class Line
  def initialize(*args)
    if args.size < 4 || args.size > 5
      raise 'You must specify 4 or 5 args.'
    end

    if args.size == 4
      puts "Creates a line with (x1,y1),(x2,y2) coords."
    elsif args.size == 5
      puts "Creates a line with (x1,y1), slope, offset, length."
    end

  end

end

Line.new(0, 0, 2, 2)
Line.new(0, 0, 0.75, 0, 5)

Line.new(1, 2)