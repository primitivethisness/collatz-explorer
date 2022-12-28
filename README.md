# collatz-explorer

A small python project that extracts statistics from the orbits of natural
numbers under the Collatz map:

$$
\mathrm{Col}(x) = 
    \begin{cases}
    3x+1 & \text{if $x$ is odd} \\
    x/2 & \text{if $x$ is even}
    \end{cases}
$$

More specifically, for any natural number $n$ we can consider its orbit
under the Collatz map $O(n) = \{n, \mathrm{Col}(n), \mathrm{Col}^2(n), ...\}$; for
each of these orbits, this project aims to extract its maximum value, its mean value and 
its length (assuming that the orbit ends when the value 1 is attained). 

The motivation for this project does not come from a practical necessity; 
it's just intended as a fun little side project to improve my computing
skills. So far, the functions in this project can compute this statistics for numbers
between 1 and $10^8$, but I intend to improve this by using different libraries (so far,
only numpy is involved).

Thank you for your interest and let me know if I can help you with anything!
