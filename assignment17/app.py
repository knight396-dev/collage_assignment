from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

# Read CSV file
df = spark.read.csv("sales.csv", header=True, inferSchema=True)

print("\n=== Original Data ===")
df.show()

# Sort products by sales in descending order
print("\n=== Products Sorted by Sales (Descending) ===")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

# Display Top 3 Products
print("\n=== Top 3 Products by Sales ===")
top3_df = sorted_df.limit(3)
top3_df.show()

# Filter products with sales > 80000
print("\n=== Products with Sales > 80000 ===")
filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

# Save filtered data as CSV
filtered_df.coalesce(1).write.mode("overwrite") \
    .option("header", "true") \
    .csv("output")

print("Filtered data saved to output folder.")

spark.stop()