package net.henrypost.fraud;

import lombok.AllArgsConstructor;
import net.henrypost.fraud.model.jpa.FraudCheckHistory;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
@AllArgsConstructor
public class FraudCheckService {

    private final FraudCheckHistoryRepository fraudCheckHistoryRepository;

    public boolean isFraudster(Integer customerID) {

        fraudCheckHistoryRepository.save(
                FraudCheckHistory
                        .builder()
                        .created(LocalDateTime.now())
                        .id(customerID)
                        .isFraudster(false)
                        .build()
        );

        return false;
    }
}
