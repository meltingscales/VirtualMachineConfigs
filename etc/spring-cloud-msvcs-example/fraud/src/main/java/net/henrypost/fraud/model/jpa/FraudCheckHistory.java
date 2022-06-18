package net.henrypost.fraud.model.jpa;

import lombok.*;
import org.hibernate.Hibernate;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.Objects;

@Getter
@Setter
@ToString
@RequiredArgsConstructor
@AllArgsConstructor
@Builder
@Entity
public class FraudCheckHistory {
    @Id
    @SequenceGenerator(
            name = "fraud_id_seq",
            sequenceName = "fraud_id_seq")
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "fraud_id_seq")
    private Integer id;

    private Integer customerId;

    private boolean isFraudster;

    private LocalDateTime created;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || Hibernate.getClass(this) != Hibernate.getClass(o)) return false;
        FraudCheckHistory that = (FraudCheckHistory) o;
        return id != null && Objects.equals(id, that.id);
    }

    @Override
    public int hashCode() {
        return getClass().hashCode();
    }
}
