# gear-mechanism-func

The functions included in this codebase for calculating various parameters related to gear mechanisms. Each function serves a specific purpose in the context of gearing systems.

## Functions

### `calc_GR(gear_list1, gear_list2)`
Calculates the gear ratio of a gearing mechanism based on the gear lists provided as inputs. The gear ratio is computed by dividing the last gear in `gear_list1` by the first gear and multiplying it with the ratio of the last gear in `gear_list2` to the first gear.

### `calc_PD(gear_list, module)`
Computes the pitch diameter (in millimeters) for each gear in the gear list provided, using the specified module. The pitch diameter for each gear is calculated by multiplying the gear value with the module.

### `calc_CD(pitch_diameter_list)`
Determines the center distance (in millimeters) between the input and output gears for a set of gears. It sums up all the pitch diameters in the provided list and subtracts half of the first and last pitch diameters to find the center distance.

### `verify_center_distance(first_lvl, forefinger, thumb)`
Verifies the calculated center distances for three different gear configurations: `first_lvl`, `forefinger`, and `thumb`. The expected center distances are predefined as constants (`first_lvl_CD`, `forefinger_CD`, `thumb_CD`). The function calculates the center distance for each configuration using `calc_CD()` and compares it with the expected values, returning a list of boolean results indicating whether the calculated center distances match the expected values.
