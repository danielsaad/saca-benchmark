# saca-benchmark
Benchmark for Suffix Array Construction Algorithms


## Pre-requisites 

It is necessary to have
- CMake >= 2.8
- aria2 
- Python3 with csv module installed
- g++ >= 4.9
  
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



Machine configuration:
- Processor: 2x Intel(R) Xeon(R) CPU E5-2640 v3 @ 2.60GHzv (16 cores + 16 threads)
- Ram Memory: 60GB DDR4 2133 MhZ  
- Operating System: CentOS 7




|  Manzini Corpus |           |           |            |
|:---------------:|:---------:|:---------:|:----------:|
| Experiment      | SAIS Nong | SAIS Yuta | Divsufsort |
| chr22.dna       | 4.61      | 2.96      | 3.36       |
| etext99         | 18.24     | 10.80     | 10.57      |
| gcc-3.0.tar     | 0.04      | 0.04      | 0.05       |
| howto           | 5.10      | 3.36      | 3.36       |
| jdk13c          | 5.26      | 3.60      | 3.57       |
| linux-2.4.5.tar | 0.06      | 0.05      | 0.06       |
| rctail96        | 14.40     | 10.13     | 10.27      |
| rfc             | 0.10      | 0.08      | 0.08       |
| sprot34.dat     | 14.51     | 10.10     | 9.59       |
| w3c2            | 5.26      | 3.19      | 3.79       |



| Pizza-Chili Repetitive |           |           |            |
|:----------------------:|:---------:|:---------:|:----------:|
| Experiment       | SAIS Nong | SAIS Yuta | Divsufsort |
| cere             | 69.50     | 36.56     | 45.99      |
| coreutils        | 25.34     | 15.61     | 18.18      |
| dblp.xml.00001.1 | 12.31     | 7.54      | 8.99       |
| dblp.xml.00001.2 | 12.32     | 7.73      | 8.99       |
| dblp.xml.0001.1  | 13.33     | 7.72      | 9.47       |
| dblp.xml.0001.2  | 12.99     | 7.82      | 9.69       |
| dna.001.1        | 12.83     | 8.01      | 10.39      |
| einstein.de.txt  | 11.68     | 7.34      | 8.07       |
| einstein.en.txt  | 71.56     | 38.72     | 45.84      |
| english.001.2    | 15.36     | 8.77      | 10.69      |
| Escherichia_Coli | 14.70     | 11.01     | 11.90      |
| fib41            | 26.61     | 15.52     | 37.78      |
| influenza        | 18.89     | 12.07     | 14.32      |
| kernel           | 33.55     | 20.38     | 24.13      |
| para             | 59.66     | 35.45     | 43.98      |
| proteins.001.1   | 15.95     | 8.96      | 10.77      |
| rs.13            | 21.75     | 12.34     | 34.07      |
| sources.001.2    | 12.80     | 8.34      | 8.54       |
| tm29             | 24.59     | 15.47     | 46.74      |
| world_leaders    | 3.87      | 2.53      | 2.11       |