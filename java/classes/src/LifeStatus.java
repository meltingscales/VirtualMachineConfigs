/**
 * This enum stores two unique states available to organisms: ALIVE and DEAD.
 * <p>
 * <p>
 * This is a decent use of enums, because we're replacing "TRUE" and "FALSE" with a special datatype that can only be
 * interpreted as "ALIVE" or "DEAD", to prevent ambiguity in our code.
 * <p>
 * <p>
 * Having an enum that stored days of the week is also a good example, as "MONDAY", "TUESDAY", etc, have no intrinsic
 * ordering (Does Monday start first? Sunday? Saturday?), but with Enumerations, we don't have to think about that.
 * <p>
 * <p>
 * The only thing that matters is that they're <b>unique</b>!
 */
public enum LifeStatus {
    ALIVE,
    DEAD,
}
