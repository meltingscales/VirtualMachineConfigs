import java.util.Scanner;

/**
 * Program to simulate voting.
 */
public class Voting {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ask them for how many precincts we have.
        System.out.print("Enter number of precincts to be tallied: ");
        int numberPrecincts = scanner.nextInt();

        // An empty array, counting votes per precinct for each candidate, that is as long as how many precincts we have.
        int[] votesCandidate1 = new int[numberPrecincts];
        int[] votesCandidate2 = new int[numberPrecincts];

        // Integers that will store the total amount of votes for each candidate.
        int votesTotalCandidate1 = 0;
        int votesTotalCandidate2 = 0;

        // Ask them for the candidate names.
        System.out.print("Candidate 1: ");
        String nameCandidate1 = scanner.next();

        System.out.print("Candidate 2: ");
        String nameCandidate2 = scanner.next();

        // Now, we must tally up all votes in all precincts!
        for (int i = 0; i < numberPrecincts; i++) {

            // Get the votes for each candidate in each precinct.

            // Candidate 1.
            System.out.println("How many votes did " + nameCandidate1 + " win in precinct " + (i + 1) + "? "); // Ask them for the votes.
            int votesCandidate1temp = scanner.nextInt(); // Read it in from them.

            votesCandidate1[i] = votesCandidate1temp; // Store our per-precinct result for this candidate.
            votesTotalCandidate1 += votesCandidate1temp; // Add our result to the total for the candidate.

            // Candidate 2.
            System.out.println("How many votes did " + nameCandidate2 + " win in precinct " + (i + 1) + "? ");// Ask them for the votes.
            int votesCandidate2temp = scanner.nextInt(); // Read it in from them.

            votesCandidate2[i] = votesCandidate2temp; // Store our per-precinct result for this candidate.
            votesTotalCandidate2 += votesCandidate2temp; // Add our result to the total for the candidate.


            // Show who's in the lead!
            if (votesTotalCandidate1 > votesTotalCandidate2) { // If candidate 1 is winning,
                // Show the difference.
                System.out.println(nameCandidate1 + " is in the lead by " + (votesTotalCandidate1 - votesTotalCandidate2) + ".");

            } else if (votesTotalCandidate2 > votesTotalCandidate1) { // If candidate 2 is winning,
                // Show the difference.
                System.out.println(nameCandidate2 + " is in the lead by " + (votesTotalCandidate2 - votesTotalCandidate1) + ".");

            } else { // They're tied!
                System.out.println("Both candidates are tied!");
            }
        }

        // Show the total!

        // Total votes.
        int totalVotes = votesTotalCandidate1 + votesTotalCandidate2;

        // Percentages of votes per candidate out of all votes. This will be a number between zero and 100.
        double percentCandidate1 = ((float) votesTotalCandidate1 / totalVotes);
        double percentCandidate2 = ((float) votesTotalCandidate2 / totalVotes);

        // Convert that number to out of 100, and remove any decimal point.
        percentCandidate1 = (int)(percentCandidate1 * 100);
        percentCandidate2 = (int)(percentCandidate2 * 100);

        // Print it all out.
        System.out.println("Total votes tallied: " + totalVotes);
        System.out.println(nameCandidate1 + ": " + votesTotalCandidate1 + " votes (" + percentCandidate1 + ")");
        System.out.println(nameCandidate2 + ": " + votesTotalCandidate2 + " votes (" + percentCandidate2 + ")");

    }
}
