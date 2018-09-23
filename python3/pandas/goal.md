NOTE: All removed rows should be placed into a separate DataFrame.

1.  Combine `A` and `B` into `C` by concatenation.

  Example:
  
|   a   |   b   |   c   |
| -----:| -----:| -----:|
|   a   |   b   |  ab   |
|   z   |   x   |  zx   |
-------------------------
  
2.  Count all the duplicates of `C` and store them in `D`.

Example:
  
|   c   |   d   |
| -----:| -----:|
|  ab   |   1   |
|  zx   |   2   |
|  zx   |   2   |
-----------------

3. Ignore all rows where `D` is `1`.

Example:

|   c   |   d   | ignored |
| -----:| -----:| ------:|
|  ab   |   1   |  YES   |
|  zx   |   2   |        |
|  zx   |   2   |        |
--------------------------

4.  Delete all rows where `F` is `CANCELLED` and `D` is NOT `1`.

5.  If any value in `G` is over `100`, and any other row with the same `C`'s `G`
 is less than `16`, then delete the row with the value less than `16`.
 
