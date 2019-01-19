import java.time.Instant;
import java.time.LocalDate;
import java.time.ZoneId;

public class Organism {

    /**
     * How many organisms have ever existed?
     */
    public static long totalOrganisms = 0;

    /**
     * Which one are we?
     */
    public long organismNumber = 0;

    /**
     * When this Organism was born.
     * <p>
     * Defaults to when you instantiated the Organism object.
     */
    public Instant birth = Instant.now();

    /**
     * If this Organism is alive or dead.
     */
    public LifeStatus lifeStatus = LifeStatus.ALIVE;

    /**
     * How much nutrition an Organism has access to.
     * <p>
     * You can think of this like how much food an Organism has eaten.
     **/
    public long calories = 1000;

    /**
     * This is a default constructor. It takes no arguments.
     * <p>
     * For now, let's just mark down that we've made a new Organism, and record which organism we are.
     */
    public Organism() {
        totalOrganisms++; // One more living Organism!
        organismNumber = totalOrganisms;
    }

    /**
     * This is a constructor for Organisms that allows you to pass a date string.
     *
     * @param birth A date string of format "YYYY-MM-DD", i.e. "1990-01-20".
     */
    public Organism(String birth) {
        // Call our default constructor to show we've made a new Organism.
        this();

        // Ignore this.
        // This just makes the date start at Chicago's time, 12:00AM midnight.
        this.birth = LocalDate.parse(birth).atStartOfDay(ZoneId.of(("America/Chicago"))).toInstant();
    }

    /**
     * @return If we are dead.
     */
    public Boolean isDead() {
        return this.lifeStatus == LifeStatus.DEAD;
    }

    /**
     * @return If we are alive.
     */
    public Boolean isAlive() {
        return this.lifeStatus == LifeStatus.ALIVE;
    }

    /**
     * Attempt to eat another organism and consume its calories.
     * <p>
     * This will kill the victim and strip it of calories.
     * <p>
     * You are allowed to eat a dead Organism, and also one with zero calories.
     *
     * @param victim The victim being eaten.
     */
    public void eat(Organism victim) throws Exception {

        // If we are dead,
        if (this.isDead()) {

            // Stop eating and give an error!
            throw new Exception("Dead organisms cannot eat!");
        }

        // The victim dies,
        victim.lifeStatus = LifeStatus.DEAD;

        // We add their calories to ours,
        this.calories = this.calories + victim.calories;

        // And set theirs to zero.
        victim.calories = 0;
    }

    @Override
    public String toString() {
        return String.format("Organism #%d\nBirth: %s\nCalories: %d\nAlive: %s",
                this.organismNumber, this.birth.toString(), this.calories, this.isAlive().toString());
    }
}
