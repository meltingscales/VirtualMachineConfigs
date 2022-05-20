package net.henrypost.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.reactive.function.client.WebClient;

@SpringBootApplication
@EnableScheduling
public class SomeMainClass {

	@Scheduled(cron = "*/5 * * * * *")
	public void cronJobSch() throws Exception {

		System.out.println("wow its a phucking cron job :3c");

		String response = WebClient.builder().build()
				.get()
				.uri("http://localhost:8080/api/someresource")
				.retrieve()
				.bodyToMono(String.class)
				.block();

		System.out.println(response);

	}

	public static void main(String[] args) {
		SpringApplication.run(SomeMainClass.class, args);
	}

}
