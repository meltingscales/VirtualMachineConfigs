package net.henrypost.customer;

import net.henrypost.customer.Customer;
import net.henrypost.customer.CustomerRegistrationRequest;
import net.henrypost.customer.CustomerRepository;
import org.springframework.stereotype.Service;

@Service
public record CustomerService(CustomerRepository customerRepository) {
    public void registerCustomer(CustomerRegistrationRequest customerRegistrationRequest) {
        Customer customer = Customer
                .builder()
                .firstName(customerRegistrationRequest.firstName())
                .lastName(customerRegistrationRequest.lastName())
                .email(customerRegistrationRequest.email())
                .build();

        //todo: valid email
        //todo: email unique

        //store customer
        customerRepository.save(customer);
    }
}
