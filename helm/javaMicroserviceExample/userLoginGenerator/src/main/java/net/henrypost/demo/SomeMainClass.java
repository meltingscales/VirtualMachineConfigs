package net.henrypost.demo;

import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.core.env.Environment;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

import net.henrypost.demo.model.UserPOJO;

@SpringBootApplication
@EnableScheduling
public class SomeMainClass {
	@Autowired
	Environment environment;

	@Scheduled(cron = "*/5 * * * * *") // every 5 seconds
	public void periodicallyCreateNewUser() throws Exception {

		System.out.println("periodicallyCreateNewUser :3c");

		String uri = environment.getProperty("target.url") +
				environment.getProperty("target.endpoint");

		String response = WebClient.builder().build()
				.post()
				.uri(uri)
				.body(BodyInserters.fromValue(UserPOJO.newRandomUser()))
				.retrieve()
				.bodyToMono(String.class)
				.block();

		System.out.println(response);

	}

	@Scheduled(cron = "*/12 * * * * *")
	public void cronJobGetSomeRandomStuff() throws Exception {

		System.out.println("cronJobGetSomeRandomStuff :3c");

		String response = WebClient.builder().build()
				.get()
				.uri("%s/api/someRandomStuff".formatted(
						environment.getProperty("target.url")))
				.retrieve()
				.bodyToMono(String.class)
				.block();

		System.out.println(response);

	}

	public static void main(String[] args) {
		SpringApplication.run(SomeMainClass.class, args);
	}

}
