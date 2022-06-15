package net.henrypost.customer.model.rest;

import lombok.Builder;

@Builder
public record CustomerRegistrationRequest(
        String firstName,
        String lastName,
        String email
) {
}
