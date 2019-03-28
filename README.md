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


|  Manzini Corpus |           |           |            |
|:---------------:|:---------:|:---------:|:----------:|
| Experiment      | SAIS Nong | SAIS Yuta | Divsufsort |
| chr22.dna       |   10.31   |    5.52   |    4.13    |
| etext99         |   52.81   |   23.99   |    15.98   |
| gcc-3.0.tar     |    0.07   |    0.07   |    0.07    |
| howto           |   11.49   |    5.75   |    4.09    |
| jdk13c          |   14.77   |    4.66   |    4.82    |
| linux-2.4.5.tar |    0.13   |    0.15   |    0.09    |
| rctail96        |   47.94   |   17.47   |    14.98   |
| rfc             |    0.17   |    0.12   |    0.10    |
| sprot34.dat     |   49.04   |   19.20   |    14.10   |
| w3c2            |   12.55   |    4.56   |    4.49    |


| Pizza-Chili Repetitive |           |           |            |
|:----------------------:|:---------:|:---------:|:----------:|
| Experiment             | SAIS Nong | SAIS Yuta | Divsufsort |
| cere                   |   261.88  |   69.36   |    78.44   |
| coreutils              |   78.56   |   25.07   |    24.50   |
| dblp.xml.00001.1       |   51.25   |   12.14   |    18.12   |
| dblp.xml.00001.2       |   50.57   |   12.14   |    13.26   |
| dblp.xml.0001.1        |   50.67   |   12.05   |    13.03   |
| dblp.xml.0001.2        |   50.99   |   12.29   |    13.12   |
| dna.001.1              |   47.32   |   12.68   |    13.75   |
| einstein.de.txt        |   44.18   |   11.41   |    11.92   |
| einstein.en.txt        |   289.22  |   64.29   |    77.65   |
| english.001.2          |   55.76   |   15.09   |    13.74   |
| Escherichia_Coli       |   50.65   |   16.75   |    16.37   |
| fib41                  |   145.73  |   25.12   |    79.34   |
| influenza              |   63.28   |   16.53   |    20.52   |
| kernel                 |   107.49  |   32.04   |    31.82   |
| para                   |   243.80  |   63.78   |    71.40   |
| proteins.001.1         |   57.48   |   15.39   |    13.96   |
| rs.13                  |   108.93  |   19.64   |    76.73   |
| sources.001.2          |   46.78   |   13.04   |    11.54   |
| tm29                   |   125.30  |   25.58   |    82.93   |
| world_leaders          |   15.01   |    3.72   |    2.88    |