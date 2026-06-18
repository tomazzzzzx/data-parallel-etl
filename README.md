# Data Parallel Etl

GPU-accelerated ETL pipeline for processing petabyte-scale datasets.

## Features
- RAPIDS cuDF for GPU DataFrames
- Automatic CPU/GPU fallback
- Distributed processing with Dask
- Schema validation and data quality checks

## Performance
| Operation | GPU (cuDF) | CPU (pandas) | Speedup |
|-----------|-----------|-------------|--------|
| GroupBy 1B rows | 1.2s | 45s | 37x |
| Join 500M x 100M | 3.8s | 180s | 47x |

## License
MIT
