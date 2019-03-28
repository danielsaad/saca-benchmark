# saca-benchmark
Benchmark for Suffix Array Construction Algorithms


## Pre-requisites 

It is necessary to have
- CMake >= 2.8
- Aria2 
- Python3 with csv module installed
- 
## Running Benchmark

```sh
cd benchmark
./run_benchmark.sh
```

It will produce csv files containing the results for each Corpus.


## Benchmark Results

The results for the corpora Repetitive Pizza-Chili and Manzini follows attached.

Machine configuration:
- Processor: 2x Intel(R) Xeon(R) CPU E5-2620 v3 @ 2.40GHz (12 processores + 12 Threads)
- Ram Memory: 160GB  
- Disks: 4x 1TB 7200 RPM (Raid 5)
- Operating Systems: Ubuntu 18.04