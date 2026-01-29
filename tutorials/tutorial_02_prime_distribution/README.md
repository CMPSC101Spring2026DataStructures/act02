# Tutorial 2: Prime Number Distribution Analysis

This tutorial explores prime numbers and their mathematical properties through data analysis and visualization.

## Setup Instructions

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_02_prime_distribution
   ```

2. Initialize the UV project (if not already done):
   ```bash
   uv init
   ```

3. Add required dependencies:
   ```bash
   uv add matplotlib pandas plotly numpy
   ```

4. Run the program:
   ```bash
   uv run primes.py
   ```

## What You'll Learn

- Implementing algorithms to find prime numbers
- Using loops to build data structures from mathematical sequences
- Analyzing the Prime Number Theorem: π(n) ≈ n/ln(n)
- Exploring twin prime patterns and distributions
- Creating complex mathematical visualizations

## Mathematical Concepts

### Prime Number Theorem
The Prime Number Theorem states that the number of primes less than or equal to n is approximately n/ln(n). Your code will verify this relationship!

### Twin Primes
Twin primes are pairs of prime numbers that differ by 2:
- (3, 5), (5, 7), (11, 13), (17, 19), (29, 31), ...
- The Twin Prime Conjecture suggests there are infinitely many twin primes

## Tasks

Complete all `TODO` sections in `primes.py`:

1. **generate_primes_up_to()**: Loop through numbers and identify primes
2. **find_twin_primes()**: Identify prime pairs that differ by 2
3. **analyze_twin_prime_gaps()**: Calculate spacing between twin prime pairs

## Expected Output

When complete, the program will generate:
- `prime_theorem_analysis.png` - Comparison of actual vs theoretical prime counts
- `twin_primes_distribution.png` - Visualization of twin prime patterns
- `prime_density_grid.html` - Interactive heatmap of prime distribution
- Statistical report printed to console

## Tips

- The `is_prime()` function is already provided - use it to check primality
- Use `range()` for loops: `for n in range(start, end, step)`
- Use list methods: `append()`, `len()`
- Use `math.log()` for natural logarithm (ln)
- Test incrementally: complete one function at a time
- Start with small limits for testing, then increase

## Challenges (Optional)

If you finish early, try modifying the code to:
- Analyze Sophie Germain primes (p where 2p+1 is also prime)
- Investigate prime gaps larger than 2
- Explore the Goldbach conjecture for even numbers
