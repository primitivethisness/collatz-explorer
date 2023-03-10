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
under the Collatz map $\mathcal{O}(n) = (n, \mathrm{Col}(n), \mathrm{Col}^2(n), ...)$; for
each of these orbits, this project aims to extract its maximum value, its mean value and 
its length (assuming that the orbit ends when the value 1 is attained). 

Thank you for your interest and let me know if I can help you with anything!
