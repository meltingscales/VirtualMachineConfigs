package net.henrypost.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.reactive.function.client.WebClient;

@SpringBootApplication
@EnableScheduling
public class DemoApplication {

	@Bean
	public WebClient.Builder getWebClientBuilder() {
		return WebClient.builder();
	}

	@Autowired
	private WebClient.Builder webClientBuilder;

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	// every 5 seconds
	@Scheduled(cron = "*/5 * * * * *")
	public void cronJobSch() throws Exception {
		System.out.println("wow its a phucking cron job :3c");

		 product = webClientBuilder.build()
            .get()
            .uri("http://localhost:8080/api/products")
            .retrieve();
			

	}

}
