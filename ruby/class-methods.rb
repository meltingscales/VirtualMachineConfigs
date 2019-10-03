class Invoice

  @@total = 0

  def initialize(customer, amount)
    @customer = customer
    @amount = amount

    @@total += amount
  end

  def self.total()
    puts "The total amount billed is #{@@total}"
  end

  def customer
    @customer
  end

  def amount
    @amount
  end

end

inv1 = Invoice.new("Customer1", 10000)
inv2 = Invoice.new("Customer2", 7500)

Invoice.total

puts "The invoice for #{inv2.customer} is #{inv2.amount}."