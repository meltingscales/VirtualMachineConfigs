package net.henrypost.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

import net.henrypost.demo.model.UserPOJO;

@SpringBootApplication
@EnableScheduling
public class SomeMainClass {

	@Scheduled(cron = "*/5 * * * * *")
	public void periodicallyCreateNewUser() throws Exception {

		System.out.println("periodicallyCreateNewUser :3c");

		String response = WebClient.builder().build()
				.post()
				.uri("http://localhost:8080/api/user/create")
				.body(BodyInserters.fromValue(new UserPOJO()))
				.retrieve()
				.bodyToMono(String.class)
				.block();


				// .exchangeToMono((arg0) -> sysou)
				// .retrieve()
				// .bodyToMono(String.class)
				// .block();

		System.out.println(response);

	}

	@Scheduled(cron = "*/12 * * * * *")
	public void cronJobGetSomeRandomStuff() throws Exception {

		System.out.println("cronJobGetSomeRandomStuff :3c");

		String response = WebClient.builder().build()
				.get()
				.uri("http://localhost:8080/api/someRandomStuff")
				.retrieve()
				.bodyToMono(String.class)
				.block();

		System.out.println(response);

	}


	public static void main(String[] args) {
		SpringApplication.run(SomeMainClass.class, args);
	}

}
