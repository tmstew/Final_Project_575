**Group member: Ying Yang**
- What was your biggest challenge in this project?

*When I tried to read the file 'annotations/var_drug_ann.tsv' by 'pd.read_csv', it takes me much time to fix the ParseError (Error tokenizing data. C error: Expected 12 fields in line 7290, saw 16). After googling and obtaining suggestions from Cristina, I decided to skip the line 7290 using 'error_bad_lines = False'.*

- What did you learn while working on this project?

*First, I learned to skip the unusable data when it is too hard to fix it.<br>
Second, I learned that we should try to avoid hardcode which may leads to brittleness.*

- If you had more time on the project what other question(s) would you like to answer?

*First, I would like to investigate which variants have significant associations with drug dosage. The study can be conducted by filtering the merged file by 'SIGNIFICANCE' is 'yes' and 'PHEONOTYPE CATEGORY' is 'dosage'.<br>
Second, I am also interested in comparing which variants possess different ALLELE_PharmGKB and ALLELE_23andme in the merged file.*

**Group member: Xueqing Wang**
- What was your biggest challenge in this project?

*I had a hard time finding the most appropriate function to use. It happened several times during the homework that after writing a complicated series of commands to get the desired result, I suddenly realized that there is a pandas function already written to do these things.*

- What did you learn while working on this project?

*1) always look for ready-to-use functions before starting coding from scratch; 2) care about the usability of the code: always think from the user's perspective, make the input easy and instructions clear, allow space for the user to customize the output; 3) care about the robustness of the code: add error handling methods at the place where 1) takes a user input; 2) the code may broke down because of changes in the file that the user feeds in.*

- If you had more time on the project what other question(s) would you like to answer?

*1) write the whole thing into a class; 2) add more error handling points; 3) What're the drugs that target each dbSNP_ID? 4) What's the most effective drug combination for each patient? That is, use the least kinds of drugs to target the most kinds of dbSNPs. 5) For the same gene, targeting at which or which combination of dbSNPs is the most effective and economic? (maybe current information is not enough)*

