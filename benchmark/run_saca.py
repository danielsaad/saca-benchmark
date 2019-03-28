#!/usr/bin/python3

import subprocess
import matplotlib.pyplot as plt
import os
import csv
import time

yuta_bin = '../bin/sais_yuta_saca'
nong_bin = '../bin/sais_nong_saca'
divsufsort_bin = '../bin/divsufsort_saca'
test_bin = '../bin/sais_test'


def run_yuta(input_file):
    print('Running SAIS Yuta on', os.path.basename(input_file))
    start = time.perf_counter()
    subprocess.run([yuta_bin, input_file],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stop = time.perf_counter()
    return(stop-start)


def run_nong(input_file):
    print('Running SAIS Nong on', os.path.basename(input_file))
    start = time.perf_counter()
    subprocess.run([nong_bin, input_file],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stop = time.perf_counter()
    return(stop-start)


def run_divsufsort(input_file):
    print('Running Divsufsort on', os.path.basename(input_file))
    start = time.perf_counter()
    subprocess.run([divsufsort_bin, input_file],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stop = time.perf_counter()
    return(stop-start)


pizza_chili_corpus = os.path.join(*['..', 'corpora', 'pizza-chili-repetitive'])
manzini_corpus = os.path.join(*['..', 'corpora', 'manzini'])

pizza_chili_files = os.listdir(pizza_chili_corpus)
pizza_chili_files = [os.path.join(pizza_chili_corpus, f)
                     for f in pizza_chili_files if not f.endswith('.7z')]

manzini_files = os.listdir(manzini_corpus)
manzini_files = [os.path.join(manzini_corpus, f)
                 for f in manzini_files if not f.endswith('.bz2')]


pizza_chili_files.sort(key=lambda x: x.lower())
manzini_files.sort(key=lambda x: x.lower())

print(pizza_chili_files,manzini_files)

print("Running Pizza-Chili Repetitive Corpus")
with open('pizza-chili-corpus.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Experiment', 'SAIS Nong', 'SAIS Yuta', 'Divsufsort'])
    for f in pizza_chili_files:
        t = []
        t.append(run_nong(f))
        t.append(run_yuta(f))
        t.append(run_divsufsort(f))
        writer.writerow([os.path.basename(f), '{:.2f}'.format(
            t[0]), '{:.2f}'.format(t[1]), '{:.2f}'.format(t[2])])


print("Running Manzini Corpus")
with open('manzini.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Experiment', 'SAIS Nong', 'SAIS Yuta', 'Divsufsort'])
    for f in pizza_chili_files:
        t = []
        t.append(run_nong(f))
        t.append(run_yuta(f))
        t.append(run_divsufsort(f))
        writer.writerow([os.path.basename(f), '{:.2f}'.format(
            t[0]), '{:.2f}'.format(t[1]), '{:.2f}'.format(t[2])])
