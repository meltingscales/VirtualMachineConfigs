package net.henrypost.customer.service;

import net.henrypost.customer.model.Customer;
import net.henrypost.customer.model.CustomerRegistrationRequest;
import org.springframework.stereotype.Service;

@Service
public record CustomerService() {
    public void registerCustomer(CustomerRegistrationRequest customerRegistrationRequest) {
        Customer customer = Customer.builder()
                .firstName(customerRegistrationRequest.firstName())
                .lastName(customerRegistrationRequest.lastName())
                .email(customerRegistrationRequest.email())
                .build();

        //todo: valid email
        //todo: email unique
        //todo: store customer
    }
}
