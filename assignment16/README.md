# Employee RDD Processing Using PySpark and Docker

## Objective
Process employee data using PySpark RDD operations and containerize the application using Docker.

## Dataset
employees.csv contains:
- Employee ID
- Name
- Department
- Salary

## Operations Performed

1. Read CSV into RDD
2. Sort employees by salary in descending order
3. Calculate department-wise total salary
4. Find top 3 highest-paid employees
5. Save top 3 employees to a text file

## Project Structure

employee-pyspark-docker/
├── app/
│ └── employee_processing.py
├── data/
│ └── employees.csv
├── output/
│ └── top_3_employees.txt
├── Dockerfile
├── requirements.txt
└── README.md

## Build

```bash
docker build -t employee-pyspark .
```

## Run

```bash
docker run --name employee-container employee-pyspark
```

## Copy Output

```bash
docker cp employee-container:/app/output/top_3_employees.txt .
```

## Technologies Used
- Python 3.12
- Apache Spark (PySpark)
- RDD API
- Docker