package net.henrypost.customer;

import lombok.extern.slf4j.Slf4j;
import net.henrypost.customer.model.pojo.Customer;
import net.henrypost.customer.model.rest.CustomerRegistrationRequest;
import net.henrypost.customer.model.rest.CustomerRegistrationResponse;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("api/v1/customer/")
public record CustomerController(CustomerService customerService) {
    @PostMapping
    public CustomerRegistrationResponse registerCustomer(@RequestBody CustomerRegistrationRequest customerRegistrationRequest) {

        log.info("new customer registered {}", customerRegistrationRequest);

        Customer c = customerService.registerCustomer(customerRegistrationRequest);

        return CustomerRegistrationResponse
                .builder()
                .customer(c)
                .code(200)
                .build();

    }
}
