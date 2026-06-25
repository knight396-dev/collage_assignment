# PySpark Sales Analysis Using Docker

## Objective
Read a sales dataset using PySpark DataFrame and perform:

1. Sort products by sales in descending order.
2. Display top 3 products by sales.
3. Filter products with sales > 80,000.
4. Save filtered records as CSV.

## Technologies Used

- Python 3.12
- Apache Spark 3.5.1
- PySpark
- Docker

## Build Docker Image

```bash
docker build -t sales-analysis .
```

## Run Container

```bash
docker run --name sales-container sales-analysis
```

## Expected Output

### Sorted Products

| Product | Sales |
|----------|---------|
| Laptop | 150000 |
| TV | 120000 |
| Mobile | 95000 |
| Bed | 90000 |
| Sofa | 80000 |
| Table | 45000 |
| Chair | 30000 |
| Headphones | 25000 |

### Top 3 Products

- Laptop
- TV
- Mobile

### Filtered Products (Sales > 80000)

- Laptop
- Mobile
- TV
- Bed

The filtered output is saved in the output directory.