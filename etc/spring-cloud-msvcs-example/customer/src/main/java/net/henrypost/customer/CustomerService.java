package net.henrypost.customer;

import net.henrypost.customer.model.pojo.Customer;
import net.henrypost.customer.model.rest.CustomerRegistrationRequest;
 import org.springframework.stereotype.Service;

@Service
public record CustomerService(CustomerRepository customerRepository) {
    public Customer registerCustomer(CustomerRegistrationRequest customerRegistrationRequest) {

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

        return customer;
    }
}
