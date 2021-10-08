#!/bin/bash

for f in *
do
  fLines=$(wc -l < $f)
  fWords=$(wc -w < $f)
  echo "$f $fLines $fWords"
  
done
