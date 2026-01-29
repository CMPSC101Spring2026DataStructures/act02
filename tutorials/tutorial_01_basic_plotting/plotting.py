"""
Tutorial 1: Basic Data Visualization with Lists
================================================

This program demonstrates creating data using Python lists and range() functions,
then visualizing that data using matplotlib, pandas, and plotly.

Learning Objectives:
- Use range() to generate sequences of numbers
- Store data in Python lists
- Create various types of plots to visualize data
- Understand how package managers (UV) help manage project dependencies

Instructions:
- Complete all To-Do sections below
- Run the program using: uv run plotting.py
- Observe how your data appears in different plot types
"""

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def generate_linear_data():
    """
    Generate simple linear data using range() and for loops.
    
    Returns:
        tuple: (x_values, y_values) as lists
    """
    # TODO: Create a list of x values from 0 to 49 using range()
    # Hint: x_values = list(range(...))
    x_values = []  # Replace this line
    
    # TODO: Create a list of y values where y = 2*x + 5 for each x
    # Hint: Use a for loop to iterate through x_values
    #       For each x, calculate y = 2*x + 5 and append to y_values
    y_values = []  # Add your loop here
    
    return x_values, y_values


def generate_quadratic_data():
    """
    Generate quadratic data for more interesting visualizations.
    
    Returns:
        tuple: (x_values, y_values) as lists
    """
    # TODO: Create a list of x values from -20 to 20 using range()
    x_values = []  # Replace this line
    
    # TODO: Create y values using the formula y = x^2 - 10
    # Hint: Use a for loop to iterate through x_values
    #       For each x, calculate y = x**2 - 10 and append to y_values
    y_values = []  # Add your loop here
    
    return x_values, y_values


def generate_categorical_data():
    """
    Generate categorical data for bar chart visualization.
    
    Returns:
        tuple: (categories, values) as lists
    """
    # Categories are provided
    categories = ['Python', 'Java', 'JavaScript', 'C++', 'Go', 'Rust']
    
    # TODO: Create a list of 6 popularity scores (integers between 50 and 100)
    # These represent fictional popularity scores for each programming language
    # Hint: You can manually create a list like [85, 72, ...]
    values = []  # Replace this line
    
    return categories, values


def plot_linear_with_matplotlib(x_values, y_values):
    """
    Create a line plot using matplotlib.
    This code is provided - no changes needed.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'b-', linewidth=2, label='y = 2x + 5')
    plt.xlabel('X Values', fontsize=12)
    plt.ylabel('Y Values', fontsize=12)
    plt.title('Linear Relationship Visualization', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('linear_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Saved linear_plot.png")
    plt.close()


def plot_quadratic_with_pandas(x_values, y_values):
    """
    Create a scatter plot using pandas and matplotlib.
    This code is provided - no changes needed.
    """
    # Create a DataFrame using pandas
    df = pd.DataFrame({
        'x': x_values,
        'y': y_values
    })
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot.scatter(x='x', y='y', c='y', cmap='viridis', 
                     s=50, alpha=0.6, ax=ax, colorbar=True)
    ax.set_xlabel('X Values', fontsize=12)
    ax.set_ylabel('Y Values', fontsize=12)
    ax.set_title('Quadratic Distribution (y = x² - 10)', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('quadratic_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Saved quadratic_plot.png")
    plt.close()


def plot_categorical_with_plotly(categories, values):
    """
    Create an interactive bar chart using plotly.
    This code is provided - no changes needed.
    """
    # Create a bar chart with color gradient
    fig = go.Figure(data=[
        go.Bar(
            x=categories,
            y=values,
            marker=dict(
                color=values,
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Score")
            ),
            text=values,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title={
            'text': 'Programming Language Popularity Scores',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'weight': 'bold'}
        },
        xaxis_title='Programming Language',
        yaxis_title='Popularity Score',
        template='plotly_white',
        height=500,
        showlegend=False
    )
    
    fig.write_html('categorical_plot.html')
    print("✓ Saved categorical_plot.html (open in web browser)")


def create_combined_visualization():
    """
    Create a multi-panel visualization combining different plot types.
    This code is provided - no changes needed.
    """
    # Generate all data
    x_linear, y_linear = generate_linear_data()
    x_quad, y_quad = generate_quadratic_data()
    categories, values = generate_categorical_data()
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(15, 5))
    
    # Subplot 1: Linear
    ax1 = fig.add_subplot(131)
    ax1.plot(x_linear, y_linear, 'r-', linewidth=2)
    ax1.set_title('Linear Function', fontweight='bold')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.grid(True, alpha=0.3)
    
    # Subplot 2: Quadratic
    ax2 = fig.add_subplot(132)
    scatter = ax2.scatter(x_quad, y_quad, c=y_quad, cmap='plasma', s=30, alpha=0.7)
    ax2.set_title('Quadratic Function', fontweight='bold')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.grid(True, alpha=0.3)
    plt.colorbar(scatter, ax=ax2)
    
    # Subplot 3: Categorical
    ax3 = fig.add_subplot(133)
    bars = ax3.bar(categories, values, color='steelblue', alpha=0.7)
    ax3.set_title('Categorical Data', fontweight='bold')
    ax3.set_xlabel('Category')
    ax3.set_ylabel('Value')
    ax3.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('combined_visualization.png', dpi=300, bbox_inches='tight')
    print("✓ Saved combined_visualization.png")
    plt.close()


def main():
    """
    Main function to run all visualizations.
    """
    print("\n" + "="*60)
    print("Tutorial 1: Basic Data Visualization")
    print("="*60)
    
    # Generate data
    print("\n[Step 1] Generating linear data...")
    x_linear, y_linear = generate_linear_data()
    print(f"  Created {len(x_linear)} data points")
    
    print("\n[Step 2] Generating quadratic data...")
    x_quad, y_quad = generate_quadratic_data()
    print(f"  Created {len(x_quad)} data points")
    
    print("\n[Step 3] Generating categorical data...")
    categories, values = generate_categorical_data()
    print(f"  Created {len(categories)} categories")
    
    # Create visualizations
    print("\n[Step 4] Creating visualizations...")
    plot_linear_with_matplotlib(x_linear, y_linear)
    plot_quadratic_with_pandas(x_quad, y_quad)
    plot_categorical_with_plotly(categories, values)
    
    print("\n[Step 5] Creating combined visualization...")
    create_combined_visualization()
    
    print("\n" + "="*60)
    print("All visualizations created successfully!")
    print("="*60)
    print("\nOutput files created:")
    print("  - linear_plot.png")
    print("  - quadratic_plot.png")
    print("  - categorical_plot.html (open in browser for interactive plot)")
    print("  - combined_visualization.png")
    print("\n")


if __name__ == "__main__":
    main()
