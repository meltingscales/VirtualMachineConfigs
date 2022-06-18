package net.henrypost.customer;

import net.henrypost.customer.model.jpa.Customer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CustomerRepository extends JpaRepository<Customer, Integer> {
}
