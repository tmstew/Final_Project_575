import numpy as np
import pandas as pd
f_23andme=pd.read_table("23andme_v5_hg19_ref.txt",names=["CHR", "POS", "dbSNP_ID", "ALLELE"])
var_drug_ann=pd.read_table("var_drug_ann.tsv",sep="\\t",engine="python")

# Two step merging

## Merging

all_merge=pd.DataFrame.merge(f_23andme,var_drug_ann,left_on="dbSNP_ID",right_on="Variant")

new_merge=all_merge.drop(axis=1,labels=["CHR","POS","Annotation ID","Variant","StudyParameters","Chromosome"])

new_merge=new_merge.iloc[:,[0,2,3,4,5,6,7,8,9,1]]
new_merge.columns=["dbSNP_ID","GENE_SYMBOL","DRUG_NAME","PMID","PHENOTYPE_CATEGORY","SIGNIFICANCE","NOTES","SENTENCE","ALLELE_PharmGKB","ALLELE_23andme"]

## Filter
final_csv=new_merge[new_merge["SIGNIFICANCE"]=="yes"][new_merge["PHENOTYPE_CATEGORY"]=="efficacy"]

final_csv

# ALternative method: one step merging

new_merge=pd.DataFrame.merge(f_23andme,var_drug_ann[var_drug_ann["Significance"]=="yes"][var_drug_ann["Phenotype Category"]=="efficacy"],left_on="dbSNP_ID",right_on="Variant")

new_merge=new_merge.drop(axis=1,labels=["CHR","POS","Annotation ID","Variant","StudyParameters","Chromosome"])

new_merge=new_merge.iloc[:,[0,2,3,4,5,6,7,8,9,1]]
new_merge.columns=["dbSNP_ID","GENE_SYMBOL","DRUG_NAME","PMID","PHENOTYPE_CATEGORY","SIGNIFICANCE","NOTES","SENTENCE","ALLELE_PharmGKB","ALLELE_23andme"]

final_csv=new_merge

final_csv

# Data cleaning

## Missing value
for i in range(0,10):
    if True in np.array(final_csv[final_csv.columns[i]].isnull()):
        final_csv[final_csv.columns[i]]=final_csv[final_csv.columns[i]].fillna("")
        
        
# Extra Credit

## I Second the method from Ying Yang. I cannot think about a better way to achieve this.

# Save file
final_csv.to_csv("23andme_PharmGKB_map.tsv",sep="\t")