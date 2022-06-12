package net.henrypost.customer.controller;

import lombok.extern.slf4j.Slf4j;
import net.henrypost.customer.model.CustomerRegistrationRequest;
import net.henrypost.customer.service.CustomerService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("api/v1/customer/")
public record CustomerController(CustomerService customerService) {
    @PostMapping
    public void registerCustomer(@RequestBody CustomerRegistrationRequest customerRegistrationRequest) {
        log.info("new customer registered {}", customerRegistrationRequest);
        customerService.registerCustomer(customerRegistrationRequest);
    }
}
