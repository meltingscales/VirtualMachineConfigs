package net.henrypost.customer.model.rest;

import lombok.Builder;
import net.henrypost.customer.model.pojo.Customer;

@Builder
public record CustomerRegistrationResponse(
        Customer customer,
        int code
) {
}
