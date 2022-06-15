package net.henrypost.customer;

public record CustomerRegistrationRequest(
        String firstName,
        String lastName,
        String email
) {
}
