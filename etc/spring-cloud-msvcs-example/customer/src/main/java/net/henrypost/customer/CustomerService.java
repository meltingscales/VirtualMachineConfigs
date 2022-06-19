package net.henrypost.customer;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import net.henrypost.customer.model.jpa.Customer;
import net.henrypost.customer.model.rest.CustomerRegistrationRequest;
import net.henrypost.customer.model.rest.FraudCheckResponse;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
@AllArgsConstructor
public class CustomerService {

    private final CustomerRepository customerRepository;
    private final RestTemplate restTemplate;
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
        this.customerRepository.saveAndFlush(customer);

        //we must flush (commit) so we can access the customer ID and be certain that it is not null...
        //this is related to the entity lifecycle

        //check if fraudster
        FraudCheckResponse fraudCheckResponse = this.restTemplate.getForObject(
                "http://localhost:8081/api/v1/fraud-check/{cid}",
                FraudCheckResponse.class,
                customer.getId()
        );

        assert fraudCheckResponse != null;
        if(fraudCheckResponse.isFraudster()){
            throw  new IllegalStateException("fraudster: "+customer.toString());
        }

        //todo send notification

        return customer;
    }
}
