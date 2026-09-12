# convert — developer notes

The app definition is `exemplar.card`, an L0 card. This document is not part of
the generation reference.

The card declares an amount, two unit names and a forward/reverse direction.
`sys.convert` owns the physical conversion coefficients and returns the validated `amount` and converted
`value`. Both display labels bind these runtime results.
The card has no factor, offset or arithmetic expression.

Supported pairs in either direction: km/mi, m/ft, cm/in, kg/lb, g/oz,
l/gal (US), km/h/mph and c/f. Unsupported pairs, including currencies, fail
without inventing a value. The requested amount seeds `amount` (default 1).
Unit names and the four display labels must agree. Swap changes direction;
preset chips select 1, 10 or 100. Render the result with `format: .ratio`.

Verification covers forward and reverse conversions, Celsius/Fahrenheit
offsets, unsupported pairs, non-finite input, and state changes updating the
runtime binding. A numeric keypad is outside this card's current controls.
