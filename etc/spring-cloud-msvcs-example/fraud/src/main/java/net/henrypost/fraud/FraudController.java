package net.henrypost.fraud;

import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import net.henrypost.fraud.model.rest.FraudCheckResponse;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/v1/fraud-check")
@Slf4j
@AllArgsConstructor
public class FraudController {

    private final FraudCheckService fraudCheckService;

    @GetMapping(path = "{customerId}")
    public FraudCheckResponse isFraudster(
            @PathVariable("customerId") Integer customerId) {

        boolean b = fraudCheckService.isFraudster(customerId);

        FraudController.log.info("fraud check request for customer {}",customerId);

        return new FraudCheckResponse(b);

    }
}
