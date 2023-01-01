"""
Compute statistics of the orbits of natural numbers
under the Collatz map.

Currently, the statistics that are supported are:
    - Maximum of each orbit.

To execute the script, modify the parameters `num_elements`
and `num_iterations` in the main loop and specify the output
directory via the `output_dir` variable.
"""

import os
import sys
from typing import Tuple

import dask.array as da
import dask.dataframe as dd


# Set recursion limit
RECURSION_LIMIT = 2000
sys.setrecursionlimit(RECURSION_LIMIT)


def collatz(array: da.Array) -> da.Array:
    """
    Apply the Collatz transformation to an array of numbers.

    The Collatz transformation is applied element-wise and
    only to entries of the array that are different from one.

    Args:
        array: The array to which the Collatz transformation
            is applied.

    Returns:
        The result of applying the Collatz transformation to
        the array passed as a parameter element-wise.
    """
    ones = array == 1
    return da.where((array%2==1) & ~ones,
                    (3*array+1)/2,
                    da.where(ones,
                            array,
                            array/2)
                   )

def find_max(first_array: da.Array, 
             second_array: da.Array) -> da.Array:
    """
    Find the element-wise maximum between the input arrays.

    Example:
        The maximum of [2, 3, 7] and [1, 5, 3] is:
        the array [2, 5, 7], because:

            2  1  ->  2
            3  5  ->  5
            7  3  ->  7

    Args:
        first_array: The first input array.
        second_array: The second input array.

    Returns:
        An array that is equal to the element-wise
        maximum of the input arrays.
    """
    return (da
            .vstack([first_array, second_array])
            .max(axis=0)
            )

def collatz_iterator(state_array: da.Array,
                     max_array: da.Array,
                     num_iterations: int) -> Tuple[da.Array, da.Array]:
    """
    Return the state and maximum arrays after iterating the Collatz map.

    Args:
        state_array: The array representing the initial state of the system.
        max_array: The array representing the maximum of each orbit under
            the Collatz map.
        num_iterations: The number of times that the Collatz map will be
            applied.

    Returns:
        A tuple where:
            - the first element represents the state of the system after
                applying the Collatz map num_iterations times.
            - the second element represents the maximum value attained in
                each orbit after applying the Collatz map
                num_iterations times.
    """
    if num_iterations == 0:
        return state_array, max_array
    else:
        next_state = collatz(state_array)
        next_max = find_max(max_array, next_state)
        return collatz_iterator(next_state,
                                next_max,
                                num_iterations-1)


if __name__ == "__main__":
    # Input parameters
    num_elements = 10**9
    num_iterations = 10**3
    output_dir = os.path.join("..",
                              "data",
                              f"collatz_stats_{num_elements}_part_*.csv")

    # Generate input values
    initial_state = da.arange(1, num_elements+1)
    initial_max = initial_state.copy()
    
    final_state, final_max = collatz_iterator(initial_state, 
                                             initial_max,
                                             num_iterations)
     
    # Prepare output to be written into disk 
    output_array = da.vstack([initial_state, final_max]).T

    ddf = dd.from_dask_array(output_array,
                             columns=["seed", "max"])

    # Write CSV to disk
    ddf.to_csv(os.path.join(output_dir),
               sep="|",
               header=True,
               index=False)
