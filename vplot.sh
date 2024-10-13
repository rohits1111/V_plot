#!/bin/bash

#process_the_file
zless mapped.bed.gz | awk 'BEGIN{FS="\t"} {modified_mean = ((500+500)/($4-$3))*((($9+$10)/2)-$3)+(-500);print modified_mean,"\t",$12}' > modified_mean.bed
sort modified_mean.bed | uniq -c > freq.bed
cat freq.bed | awk '{print $1,$2,$3}' | tr -s ' ' '\t'> output.tsv | python scatter.py

