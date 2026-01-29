# Tutorial 1: Basic Plotting

This tutorial introduces data visualization with Python using lists generated from `range()` loops.

## Setup Instructions

1. Navigate to this directory:
   ```bash
   cd tutorials/tutorial_01_basic_plotting
   ```

2. Initialize the UV project (if not already done):
   ```bash
   uv init
   ```

3. Add required dependencies:
   ```bash
   uv add matplotlib pandas plotly
   ```

4. Run the program:
   ```bash
   uv run plotting.py
   ```

## What You'll Learn

- Creating lists using `range()` and for loops
- Generating different types of data (linear, quadratic, categorical)
- Using matplotlib for static plots
- Using pandas for data manipulation and plotting
- Using plotly for interactive visualizations

## Tasks
There is already a lot of code written for you but you are still to add some "finishing touches" to the code before it can be successfully executed. Please complete all `TODO` sections in `plotting.py` to determine what still needs completing.

1. **generate_linear_data()**: Create x and y lists for linear data
2. **generate_quadratic_data()**: Create x and y lists for quadratic data
3. **generate_categorical_data()**: Create a list of values for categories

## Expected Output

When complete, the program will generate:
- `linear_plot.png` - Line plot of linear relationship
- `quadratic_plot.png` - Scatter plot of quadratic function
- `categorical_plot.html` - Interactive bar chart
- `combined_visualization.png` - All three plots together

## Tips

- Use `list(range(start, stop))` to create sequences
- Use for loops to build lists: `for item in source_list:`
- For squaring: use `x**2` or `x * x`
- Use `.append()` to add items to a list
- Test your code frequently with `uv run plotting.py`
