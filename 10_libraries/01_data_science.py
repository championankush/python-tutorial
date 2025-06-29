# Data Science Libraries in Python
# NumPy, Pandas, and Matplotlib examples

# ==========================================
# 1. NumPy - Numerical Computing
# ==========================================

print("=== NumPy - Numerical Computing ===")

# Note: In a real environment, you would install these with:
# pip install numpy pandas matplotlib seaborn

try:
    import numpy as np
    print("NumPy imported successfully!")
    
    # Creating arrays
    print("\n--- Creating Arrays ---")
    
    # 1D array
    arr1d = np.array([1, 2, 3, 4, 5])
    print(f"1D array: {arr1d}")
    print(f"Shape: {arr1d.shape}")
    print(f"Data type: {arr1d.dtype}")
    
    # 2D array (matrix)
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"\n2D array:\n{arr2d}")
    print(f"Shape: {arr2d.shape}")
    
    # Array creation functions
    zeros = np.zeros((3, 4))
    ones = np.ones((2, 3))
    random_array = np.random.rand(3, 3)
    
    print(f"\nZeros array:\n{zeros}")
    print(f"Ones array:\n{ones}")
    print(f"Random array:\n{random_array}")
    
    # Array operations
    print("\n--- Array Operations ---")
    
    # Basic arithmetic
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a ** 2 = {a ** 2}")
    
    # Statistical operations
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"\nData: {data}")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard deviation: {np.std(data)}")
    print(f"Variance: {np.var(data)}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    
    # Reshaping arrays
    print("\n--- Reshaping Arrays ---")
    
    arr = np.arange(12)
    print(f"Original array: {arr}")
    
    reshaped = arr.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    
    transposed = reshaped.T
    print(f"Transposed:\n{transposed}")
    
    # Boolean indexing
    print("\n--- Boolean Indexing ---")
    
    numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    even_mask = numbers % 2 == 0
    print(f"Numbers: {numbers}")
    print(f"Even mask: {even_mask}")
    print(f"Even numbers: {numbers[even_mask]}")
    
    # Filtering
    greater_than_5 = numbers[numbers > 5]
    print(f"Numbers > 5: {greater_than_5}")
    
except ImportError:
    print("NumPy not installed. Install with: pip install numpy")

# ==========================================
# 2. Pandas - Data Manipulation
# ==========================================

print("\n=== Pandas - Data Manipulation ===")

try:
    import pandas as pd
    print("Pandas imported successfully!")
    
    # Creating DataFrames
    print("\n--- Creating DataFrames ---")
    
    # From dictionary
    data_dict = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Boston'],
        'Salary': [50000, 60000, 70000, 55000]
    }
    
    df = pd.DataFrame(data_dict)
    print("DataFrame from dictionary:")
    print(df)
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Data types:\n{df.dtypes}")
    
    # From list of lists
    data_list = [
        ['Alice', 25, 'New York', 50000],
        ['Bob', 30, 'Los Angeles', 60000],
        ['Charlie', 35, 'Chicago', 70000],
        ['Diana', 28, 'Boston', 55000]
    ]
    
    df2 = pd.DataFrame(data_list, columns=['Name', 'Age', 'City', 'Salary'])
    print("\nDataFrame from list:")
    print(df2)
    
    # Basic operations
    print("\n--- Basic Operations ---")
    
    # Selecting columns
    print("Names column:")
    print(df['Name'])
    
    print("\nAge and Salary columns:")
    print(df[['Age', 'Salary']])
    
    # Selecting rows
    print("\nFirst 2 rows:")
    print(df.head(2))
    
    print("\nLast 2 rows:")
    print(df.tail(2))
    
    # Filtering
    print("\n--- Filtering ---")
    
    high_salary = df[df['Salary'] > 55000]
    print("People with salary > 55000:")
    print(high_salary)
    
    young_people = df[df['Age'] < 30]
    print("\nPeople under 30:")
    print(young_people)
    
    # Multiple conditions
    young_high_salary = df[(df['Age'] < 30) & (df['Salary'] > 55000)]
    print("\nYoung people with high salary:")
    print(young_high_salary)
    
    # Sorting
    print("\n--- Sorting ---")
    
    sorted_by_age = df.sort_values('Age')
    print("Sorted by age:")
    print(sorted_by_age)
    
    sorted_by_salary_desc = df.sort_values('Salary', ascending=False)
    print("\nSorted by salary (descending):")
    print(sorted_by_salary_desc)
    
    # Statistical operations
    print("\n--- Statistical Operations ---")
    
    print(f"Age statistics:\n{df['Age'].describe()}")
    print(f"\nSalary statistics:\n{df['Salary'].describe()}")
    
    print(f"\nAverage age: {df['Age'].mean()}")
    print(f"Average salary: {df['Salary'].mean()}")
    print(f"Total salary: {df['Salary'].sum()}")
    
    # Grouping
    print("\n--- Grouping ---")
    
    # Group by city and calculate average salary
    city_salary = df.groupby('City')['Salary'].mean()
    print("Average salary by city:")
    print(city_salary)
    
    # Group by city and get multiple statistics
    city_stats = df.groupby('City').agg({
        'Age': ['mean', 'min', 'max'],
        'Salary': ['mean', 'sum', 'count']
    })
    print("\nCity statistics:")
    print(city_stats)
    
    # Adding new columns
    print("\n--- Adding New Columns ---")
    
    df['Salary_K'] = df['Salary'] / 1000
    df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Adult')
    
    print("DataFrame with new columns:")
    print(df)
    
    # Handling missing data
    print("\n--- Handling Missing Data ---")
    
    # Create DataFrame with missing values
    df_missing = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, None, 28, 35],
        'Salary': [50000, None, 70000, 55000, None],
        'City': ['New York', 'Los Angeles', 'Chicago', None, 'Boston']
    })
    
    print("DataFrame with missing values:")
    print(df_missing)
    
    print(f"\nMissing values:\n{df_missing.isnull().sum()}")
    
    # Fill missing values
    df_filled = df_missing.fillna({
        'Age': df_missing['Age'].mean(),
        'Salary': df_missing['Salary'].median(),
        'City': 'Unknown'
    })
    
    print("\nDataFrame with filled missing values:")
    print(df_filled)
    
except ImportError:
    print("Pandas not installed. Install with: pip install pandas")

# ==========================================
# 3. Matplotlib - Data Visualization
# ==========================================

print("\n=== Matplotlib - Data Visualization ===")

try:
    import matplotlib.pyplot as plt
    print("Matplotlib imported successfully!")
    
    # Create sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Line plot
    print("\n--- Creating Line Plot ---")
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
    plt.plot(x, y2, label='cos(x)', color='red', linewidth=2)
    plt.title('Sine and Cosine Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('sine_cosine_plot.png')
    print("Line plot saved as 'sine_cosine_plot.png'")
    plt.close()
    
    # Scatter plot
    print("\n--- Creating Scatter Plot ---")
    np.random.seed(42)
    x_scatter = np.random.randn(50)
    y_scatter = 2 * x_scatter + np.random.randn(50) * 0.5
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x_scatter, y_scatter, alpha=0.6, color='green')
    plt.title('Scatter Plot Example')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.grid(True, alpha=0.3)
    plt.savefig('scatter_plot.png')
    print("Scatter plot saved as 'scatter_plot.png'")
    plt.close()
    
    # Bar plot
    print("\n--- Creating Bar Plot ---")
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values, color='skyblue', edgecolor='black')
    plt.title('Bar Plot Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.savefig('bar_plot.png')
    print("Bar plot saved as 'bar_plot.png'")
    plt.close()
    
    # Histogram
    print("\n--- Creating Histogram ---")
    data_hist = np.random.normal(0, 1, 1000)
    
    plt.figure(figsize=(8, 6))
    plt.hist(data_hist, bins=30, alpha=0.7, color='orange', edgecolor='black')
    plt.title('Histogram Example')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.savefig('histogram.png')
    print("Histogram saved as 'histogram.png'")
    plt.close()
    
    # Subplots
    print("\n--- Creating Subplots ---")
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subplot 1: Line plot
    axes[0, 0].plot(x, y1)
    axes[0, 0].set_title('Sine Function')
    axes[0, 0].grid(True)
    
    # Subplot 2: Scatter plot
    axes[0, 1].scatter(x_scatter, y_scatter, alpha=0.6)
    axes[0, 1].set_title('Scatter Plot')
    axes[0, 1].grid(True)
    
    # Subplot 3: Bar plot
    axes[1, 0].bar(categories, values)
    axes[1, 0].set_title('Bar Plot')
    
    # Subplot 4: Histogram
    axes[1, 1].hist(data_hist, bins=30, alpha=0.7)
    axes[1, 1].set_title('Histogram')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig('subplots.png')
    print("Subplots saved as 'subplots.png'")
    plt.close()
    
except ImportError:
    print("Matplotlib not installed. Install with: pip install matplotlib")

# ==========================================
# 4. Seaborn - Statistical Visualization
# ==========================================

print("\n=== Seaborn - Statistical Visualization ===")

try:
    import seaborn as sns
    print("Seaborn imported successfully!")
    
    # Set style
    sns.set_style("whitegrid")
    
    # Create sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    # Scatter plot with regression line
    print("\n--- Creating Seaborn Scatter Plot ---")
    plt.figure(figsize=(8, 6))
    sns.regplot(data=data, x='x', y='y', scatter_kws={'alpha': 0.6})
    plt.title('Seaborn Scatter Plot with Regression Line')
    plt.savefig('seaborn_scatter.png')
    print("Seaborn scatter plot saved as 'seaborn_scatter.png'")
    plt.close()
    
    # Box plot
    print("\n--- Creating Box Plot ---")
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, x='category', y='y')
    plt.title('Box Plot by Category')
    plt.savefig('box_plot.png')
    print("Box plot saved as 'box_plot.png'")
    plt.close()
    
    # Violin plot
    print("\n--- Creating Violin Plot ---")
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=data, x='category', y='y')
    plt.title('Violin Plot by Category')
    plt.savefig('violin_plot.png')
    print("Violin plot saved as 'violin_plot.png'")
    plt.close()
    
    # Heatmap
    print("\n--- Creating Heatmap ---")
    correlation_matrix = data[['x', 'y']].corr()
    
    plt.figure(figsize=(6, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.savefig('heatmap.png')
    print("Heatmap saved as 'heatmap.png'")
    plt.close()
    
except ImportError:
    print("Seaborn not installed. Install with: pip install seaborn")

# ==========================================
# 5. Practical Example: Data Analysis
# ==========================================

print("\n=== Practical Example: Data Analysis ===")

try:
    # Create a realistic dataset
    np.random.seed(42)
    n_samples = 1000
    
    # Generate synthetic sales data
    sales_data = pd.DataFrame({
        'date': pd.date_range('2023-01-01', periods=n_samples, freq='D'),
        'product_id': np.random.randint(1, 11, n_samples),
        'quantity': np.random.poisson(5, n_samples),
        'price': np.random.uniform(10, 100, n_samples),
        'customer_id': np.random.randint(1, 101, n_samples),
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_samples)
    })
    
    # Calculate total sales
    sales_data['total_sales'] = sales_data['quantity'] * sales_data['price']
    
    print("Sales Data Overview:")
    print(f"Shape: {sales_data.shape}")
    print(f"Date range: {sales_data['date'].min()} to {sales_data['date'].max()}")
    print(f"Total sales: ${sales_data['total_sales'].sum():,.2f}")
    
    # Basic statistics
    print("\n--- Sales Statistics ---")
    print(f"Average quantity: {sales_data['quantity'].mean():.2f}")
    print(f"Average price: ${sales_data['price'].mean():.2f}")
    print(f"Average total sales: ${sales_data['total_sales'].mean():.2f}")
    
    # Sales by region
    print("\n--- Sales by Region ---")
    region_sales = sales_data.groupby('region')['total_sales'].agg(['sum', 'mean', 'count'])
    print(region_sales)
    
    # Top products
    print("\n--- Top 5 Products by Sales ---")
    product_sales = sales_data.groupby('product_id')['total_sales'].sum().sort_values(ascending=False)
    print(product_sales.head())
    
    # Time series analysis
    print("\n--- Daily Sales Trend ---")
    daily_sales = sales_data.groupby('date')['total_sales'].sum()
    print(f"Average daily sales: ${daily_sales.mean():,.2f}")
    print(f"Best day: {daily_sales.idxmax()} with ${daily_sales.max():,.2f}")
    print(f"Worst day: {daily_sales.idxmin()} with ${daily_sales.min():,.2f}")
    
    # Create visualizations
    plt.figure(figsize=(15, 10))
    
    # Subplot 1: Daily sales trend
    plt.subplot(2, 2, 1)
    daily_sales.plot(kind='line')
    plt.title('Daily Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    
    # Subplot 2: Sales by region
    plt.subplot(2, 2, 2)
    region_sales['sum'].plot(kind='bar')
    plt.title('Total Sales by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    
    # Subplot 3: Product sales distribution
    plt.subplot(2, 2, 3)
    product_sales.head(10).plot(kind='bar')
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Product ID')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    
    # Subplot 4: Price vs Quantity scatter
    plt.subplot(2, 2, 4)
    plt.scatter(sales_data['price'], sales_data['quantity'], alpha=0.5)
    plt.title('Price vs Quantity')
    plt.xlabel('Price ($)')
    plt.ylabel('Quantity')
    
    plt.tight_layout()
    plt.savefig('sales_analysis.png')
    print("\nSales analysis visualization saved as 'sales_analysis.png'")
    plt.close()
    
except Exception as e:
    print(f"Error in practical example: {e}")

print("\n=== End of Data Science Libraries ===")
print("You've learned the basics of NumPy, Pandas, and Matplotlib! 📊") 