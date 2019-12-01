### Think and Reflection: Yongkai

1. What was your biggest challenge in this project?
- The biggest challeng I met is how to read these two files into Python. When I tried to use "read_table" or "read_csv" for file "var_drug_ann.tsv", it gave me an error that there are more elements in one row than others. Somehow I solved this issue by using seperation "\\t".
2. What did you learn while working on this project? 
- I learned to use some functions that I didn't familiar with before. Especially, I learned from my teammate Ying Yang about how to use "groupby" and "apply". I used to stick to "for" loop and it could make my code long and messy. And our teammates really make me think about how to write cleaner codes.
3. I you had more time on the project what other question(s) would you like to answer?
- I wish to answer is there a general way to filter the merged 23andme file and the variant-drug annotation file. My idea is to create a function so that users could choose conditions (like ```SIGNIFICANCE == yes ```) to filter the merged file.