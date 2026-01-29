"""
Tutorial 2: Prime Number Distribution Analysis
================================================

This program explores the fascinating world of prime numbers through data analysis
and visualization. You'll implement algorithms to find primes and analyze their
mathematical properties.

Learning Objectives:
- Implement loops to identify prime numbers
- Analyze mathematical relationships in prime distributions
- Explore the Prime Number Theorem: π(n) ≈ n/ln(n)
- Investigate twin prime patterns
- Create sophisticated visualizations of mathematical data

Mathematical Background:
- Prime numbers are natural numbers greater than 1 that have no positive divisors 
  other than 1 and themselves
- The Prime Number Theorem describes the asymptotic distribution of primes
- Twin primes are pairs of primes that differ by 2 (e.g., 11 and 13)

Instructions:
- Complete all To-Do sections below
- Run the program using: uv run primes.py
- Observe the mathematical patterns in your visualizations
"""

import math
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import numpy as np


def is_prime(n):
    """
    Check if a number is prime.
    This function is provided - no changes needed.
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_primes_up_to(limit):
    """
    Generate all prime numbers up to a given limit.
    
    Args:
        limit (int): Upper bound for prime generation
    
    Returns:
        list: List of prime numbers up to limit
    """
    # TODO: Create an empty list to store prime numbers
    primes = []
    
    # TODO: Use a for loop to check each number from 2 to limit
    # Hint: for num in range(2, limit + 1):
    #           if is_prime(num):
    #               primes.append(num)
    # Write your loop here (approximately 3-4 lines)
    
    return primes


def count_primes_in_ranges(max_n, step):
    """
    Count how many primes exist up to various values of n.
    This helps us analyze the Prime Number Theorem.
    
    Args:
        max_n (int): Maximum value to analyze
        step (int): Step size for creating ranges
    
    Returns:
        tuple: (n_values, prime_counts, theoretical_counts)
    """
    n_values = []
    prime_counts = []
    theoretical_counts = []
    
    # SOLUTION: Create a loop that iterates from step to max_n with step increments
    for n in range(step, max_n + 1, step):
        # 1. Generate primes up to n using generate_primes_up_to(n)
        primes = generate_primes_up_to(n)
        
        # 2. Count how many primes exist: len(primes)
        actual_count = len(primes)
        
        # 3. Calculate theoretical count: n / ln(n)
        theoretical_count = n / math.log(n)
        
        # 4. Append n to n_values list
        n_values.append(n)
        
        # 5. Append actual count to prime_counts list
        prime_counts.append(actual_count)
        
        # 6. Append theoretical count to theoretical_counts list
        theoretical_counts.append(theoretical_count)
    
    return n_values, prime_counts, theoretical_counts


def find_twin_primes(limit):
    """
    Find all twin prime pairs up to a given limit.
    Twin primes are pairs of primes that differ by 2.
    
    Args:
        limit (int): Upper bound for twin prime search
    
    Returns:
        list: List of tuples containing twin prime pairs
    """
    primes = generate_primes_up_to(limit)
    twin_primes = []
    
    # TODO: Loop through the primes list to find twin prime pairs
    # Hint: for i in range(len(primes) - 1):
    # Check if primes[i+1] - primes[i] == 2
    # If yes, append the pair (primes[i], primes[i+1]) to twin_primes 
    # Note: You can add two items together; twin_primes.append((primes[i], primes[i + 1]))
    
    return twin_primes


def analyze_twin_prime_gaps(limit):
    """
    Analyze the distribution of twin primes by looking at gaps between them.
    
    Args:
        limit (int): Upper bound for analysis
    
    Returns:
        tuple: (twin_prime_positions, gaps_between_twin_pairs)
    """
    twin_pairs = find_twin_primes(limit)
    
    # Get the first number of each twin pair
    positions = [pair[0] for pair in twin_pairs]
    
    # TODO: Calculate gaps between consecutive twin prime pairs
    # Hint: Create an empty list called gaps
    #       Use a for loop: for i in range(len(positions) - 1):
    #           gap = positions[i+1] - positions[i]
    #           gaps.append(gap)
    gaps = []
    
    # Write your loop here (approximately 3-4 lines)
    
    return positions, gaps


def plot_prime_counting_function(n_values, prime_counts, theoretical_counts):
    """
    Visualize the Prime Number Theorem: π(n) vs n/ln(n)
    This code is provided - no changes needed.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Actual vs Theoretical counts
    ax1.plot(n_values, prime_counts, 'b-', linewidth=2, 
             label='π(n) - Actual prime count', alpha=0.8)
    ax1.plot(n_values, theoretical_counts, 'r--', linewidth=2, 
             label='n/ln(n) - Theoretical estimate', alpha=0.8)
    ax1.set_xlabel('n', fontsize=12)
    ax1.set_ylabel('Number of Primes', fontsize=12)
    ax1.set_title('Prime Number Theorem: π(n) ≈ n/ln(n)', 
                  fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Ratio of actual to theoretical
    ratios = [actual / theoretical if theoretical > 0 else 0 
              for actual, theoretical in zip(prime_counts, theoretical_counts)]
    ax2.plot(n_values, ratios, 'g-', linewidth=2)
    ax2.axhline(y=1.0, color='k', linestyle='--', alpha=0.5, 
                label='Perfect agreement (ratio = 1)')
    ax2.set_xlabel('n', fontsize=12)
    ax2.set_ylabel('Ratio: π(n) / (n/ln(n))', fontsize=12)
    ax2.set_title('Accuracy of Prime Number Theorem Approximation', 
                  fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('prime_theorem_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Saved prime_theorem_analysis.png")
    plt.close()


def plot_twin_primes_distribution(positions, gaps):
    """
    Visualize the distribution and gaps of twin primes.
    This code is provided - no changes needed.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Plot 1: Twin prime positions
    ax1.scatter(range(len(positions)), positions, c=positions, 
                cmap='viridis', s=30, alpha=0.6)
    ax1.set_xlabel('Twin Prime Pair Index', fontsize=12)
    ax1.set_ylabel('Position (First Prime in Pair)', fontsize=12)
    ax1.set_title('Distribution of Twin Prime Pairs', 
                  fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Gaps between twin prime pairs
    if len(gaps) > 0:
        ax2.hist(gaps, bins=30, color='steelblue', alpha=0.7, edgecolor='black')
        ax2.set_xlabel('Gap Size', fontsize=12)
        ax2.set_ylabel('Frequency', fontsize=12)
        ax2.set_title('Distribution of Gaps Between Consecutive Twin Prime Pairs', 
                      fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add statistics
        mean_gap = np.mean(gaps)
        median_gap = np.median(gaps)
        ax2.axvline(mean_gap, color='red', linestyle='--', linewidth=2, 
                    label=f'Mean: {mean_gap:.1f}')
        ax2.axvline(median_gap, color='orange', linestyle='--', linewidth=2, 
                    label=f'Median: {median_gap:.1f}')
        ax2.legend()
    
    plt.tight_layout()
    plt.savefig('twin_primes_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved twin_primes_distribution.png")
    plt.close()


def create_interactive_prime_visualization(limit):
    """
    Create an interactive visualization of prime density.
    This code is provided - no changes needed.
    """
    # Generate primes
    primes = generate_primes_up_to(limit)
    
    # Create a grid showing which numbers are prime
    numbers = list(range(2, limit + 1))
    is_prime_list = [1 if num in primes else 0 for num in numbers]
    
    # Reshape into a grid for visualization (e.g., 50 columns)
    cols = 50
    rows = len(numbers) // cols + 1
    
    # Pad the list to make it fit the grid
    padded_list = is_prime_list + [0] * (rows * cols - len(is_prime_list))
    grid = np.array(padded_list).reshape(rows, cols)
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=grid,
        colorscale=[[0, 'lightgray'], [1, 'darkblue']],
        showscale=False,
        hovertemplate='Position: %{x}, %{y}<br>Value: %{z}<extra></extra>'
    ))
    
    fig.update_layout(
        title={
            'text': f'Prime Number Distribution (2 to {limit})<br>' + 
                    f'<sub>Blue = Prime, Gray = Composite | Total Primes: {len(primes)}</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        xaxis_title='Column',
        yaxis_title='Row',
        height=600,
        width=1000
    )
    
    fig.write_html('prime_density_grid.html')
    print("✓ Saved prime_density_grid.html (open in web browser)")


def display_prime_statistics(limit):
    """
    Display interesting statistics about primes.
    This code is provided - no changes needed.
    """
    primes = generate_primes_up_to(limit)
    twin_pairs = find_twin_primes(limit)
    
    print("\n" + "="*60)
    print("PRIME NUMBER STATISTICS")
    print("="*60)
    print(f"Range analyzed: 2 to {limit}")
    print(f"Total primes found: {len(primes)}")
    print(f"Theoretical estimate (n/ln(n)): {limit / math.log(limit):.2f}")
    print(f"Density of primes: {len(primes) / limit * 100:.2f}%")
    print(f"\nFirst 10 primes: {primes[:10]}")
    print(f"Last 10 primes: {primes[-10:]}")
    print(f"\nTwin prime pairs found: {len(twin_pairs)}")
    print(f"First 5 twin pairs: {twin_pairs[:5]}")
    print(f"Last 5 twin pairs: {twin_pairs[-5:]}")
    print("="*60 + "\n")


def main():
    """
    Main function to run all prime number analyses.
    """
    print("\n" + "="*60)
    print("Tutorial 2: Prime Number Distribution Analysis")
    print("="*60)
    
    # Configuration
    PRIME_LIMIT = 5000  # Find primes up to this number
    ANALYSIS_MAX = 5000  # Analyze Prime Number Theorem up to this
    ANALYSIS_STEP = 500  # Step size for analysis
    
    print("\n[Step 1] Generating prime numbers...")
    primes = generate_primes_up_to(PRIME_LIMIT)
    print(f"  Found {len(primes)} primes up to {PRIME_LIMIT}")
    
    print("\n[Step 2] Analyzing Prime Number Theorem...")
    n_vals, actual_counts, theoretical_counts = count_primes_in_ranges(
        ANALYSIS_MAX, ANALYSIS_STEP)
    print(f"  Analyzed {len(n_vals)} data points")
    
    print("\n[Step 3] Finding twin primes...")
    twin_pairs = find_twin_primes(PRIME_LIMIT)
    print(f"  Found {len(twin_pairs)} twin prime pairs")
    
    print("\n[Step 4] Analyzing twin prime gaps...")
    positions, gaps = analyze_twin_prime_gaps(PRIME_LIMIT)
    print(f"  Calculated {len(gaps)} gap measurements")
    
    print("\n[Step 5] Creating visualizations...")
    plot_prime_counting_function(n_vals, actual_counts, theoretical_counts)
    plot_twin_primes_distribution(positions, gaps)
    create_interactive_prime_visualization(PRIME_LIMIT)
    
    print("\n[Step 6] Generating statistics report...")
    display_prime_statistics(PRIME_LIMIT)
    
    print("="*60)
    print("All analyses completed successfully!")
    print("="*60)
    print("\nOutput files created:")
    print("  - prime_theorem_analysis.png")
    print("  - twin_primes_distribution.png")
    print("  - prime_density_grid.html (open in browser for interactive view)")
    print("\n")


if __name__ == "__main__":
    main()
