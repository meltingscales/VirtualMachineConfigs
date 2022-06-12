package net.henrypost.customer.model;

import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class Customer {

    Integer id;
    String firstName;
    String lastName;
    String email;
}
