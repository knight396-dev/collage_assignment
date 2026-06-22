from pyspark import SparkContext

sc = SparkContext(appName="EmployeeRDDProcessing")

# Read CSV file
rdd = sc.textFile("/app/data/employees.csv")

# Remove header
header = rdd.first()
data = rdd.filter(lambda x: x != header)

# Convert each row into tuple
employees = data.map(
    lambda x: x.split(",")
).map(
    lambda x: (
        int(x[0]),      # id
        x[1],           # name
        x[2],           # department
        int(x[3])       # salary
    )
)

# ---------------------------------------------------
# 1. Sort employees by salary in descending order
# ---------------------------------------------------
sorted_emp = employees.sortBy(lambda x: x[3], ascending=False)

print("\n===== Employees Sorted By Salary =====")
for emp in sorted_emp.collect():
    print(emp)

# ---------------------------------------------------
# 2. Department-wise total salary
# ---------------------------------------------------
dept_salary = (
    employees
    .map(lambda x: (x[2], x[3]))
    .reduceByKey(lambda a, b: a + b)
)

print("\n===== Department Wise Total Salary =====")
for dept in dept_salary.collect():
    print(f"{dept[0]} : {dept[1]}")

# ---------------------------------------------------
# 3. Top 3 highest-paid employees
# ---------------------------------------------------
top_three = sorted_emp.take(3)

output = open("/app/output/top_3_employees.txt", "w")

output.write("Top 3 Highest Paid Employees\n")
output.write("---------------------------------\n")

for emp in top_three:
    line = (
        f"ID: {emp[0]}, "
        f"Name: {emp[1]}, "
        f"Department: {emp[2]}, "
        f"Salary: {emp[3]}"
    )
    output.write(line + "\n")

output.close()

print("\nTop 3 employees saved successfully.")

sc.stop()