package net.henrypost.fraud;

import lombok.AllArgsConstructor;
import net.henrypost.fraud.model.rest.FraudCheckResponse;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api/v1/fraud-check")
@AllArgsConstructor
public class FraudController {

    private final FraudCheckService fraudCheckService;

    @GetMapping(path = "{customerId}")
    public FraudCheckResponse isFraudster(@PathVariable("customerId") Integer customerId) {

        boolean b = fraudCheckService.isFraudster(customerId);

        return new FraudCheckResponse(b);

    }
}
