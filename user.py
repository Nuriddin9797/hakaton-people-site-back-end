#!/usr/local/bin/python3
#import os re subprocess pandas
import os
import re
import subprocess
##############
#Let us begin!
##############
#Clear Screen
os.system('clear')
#Start!
print('Let us Start!')
##############################################################
#User will make a working directory whatever they want to name
##############################################################
#user enter directory name
while True:
 space=input("Please enter directory name: ")
#when nothing input, it will output "Empty input!"
 if not space:
  print('Empty input!')
  continue
 else:
#make directory and set it as workspace
  os.mkdir(space)
  os.chdir(space)
  break
#Output All result will be put into directory where user make
 print("All result will be put into "+space)


###########################################################
#Enter protein_family and taxonomic_group which user define
###########################################################
#Enter protein family
while True:
 protein_family=input("Enter protein_family:")
 if not protein_family:
  print('Empty input!')
  continue
 else:
  print("Protein family is "+protein_family)
  break
#Enter taxonomic group
while True:
 taxonomic_group=input("Enter taxonomic_group:")
 if not taxonomic_group:
  print('Empty input!')
  continue
 else:
  print("Taxonomic group is "+taxonomic_group)
  break
#Use esearch to search for protein sequences in NCBI database and use efetch to get fasta results
os.system('esearch -db protein -query \"'+protein_family +'[PROT] AND '+taxonomic_group+' [ORGN]\" | efetch -format fasta > protein.sequence.fa')
#Tell user that he have searched matched protein sequences in NCBI database
print("Having finished search matched protein sequences in NCBI database, the result file is protein.sequence.fa")
#Ask whether user want to check the result
NCBI_result=input("Do you want to check the result or just continue?\n\tIf you want,please type check\n\tIf not, you can type anything to continue\n\t")
#If user want, he will see the result
if NCBI_result == "check":
 check=open("protein.sequence.fa").read()
 print(check)
#If user want to continue
else:
 print("Ok! Let's continue to check its sequence number!")


##############################
#Check protein sequence number
##############################
#Open and read protein.sequence.fa
sequence_count=open("protein.sequence.fa").read()
#Count the number of protein sequences
sequence_number=len(list(re.finditer(r'>',sequence_count)))
#when you input wrong protein family name and taxonomic group name
if sequence_number != 0:
#Check if sequence number is more than 1000
 if sequence_number >= 1000 and sequence_number <=2:
#If the number is more than 1000 and less than 2, it would not be suitable to continue analyze
  print("The number of sequences is"+" "+str(sequence_number)+" "+"which is not suitable to continue analyze!")
 else:
#If the number is less than 1000 and more than 2, that is OK and it is suitable to continue analyze
  print("The number of sequences is"+" "+ str(sequence_number) +" "+"which is suitable to analyze!")
else:
#quit process to restart the process
 print("Please check your protein family name and taxonomic group name!!!It is wrong!")
 quit()


#####################
#Check species number
#####################
#Ask the user if they want to continue
problem1=input("Ok so, do you want to check the number of species or not?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem1 == "yes":
 print("Ok, let's check!")
#Splitting the result with a line break
 sequence_lines = sequence_count.split('\n')
 species= []
 for line in sequence_lines:
#If the brackets are in the sequence
  if '[' in line:
#Splitting sequences via brackets
   species_name = line.split('[')[1].split(']')[0]
#Accumulate the split sequence
   species.append(species_name)
#Calculating the number of species
   species_count=len(set(species))
#Output the number of species
 print("The number of species is"+" "+str(species_count))

#######################################
#Check how many sequences are predicted
#######################################
#Ask the user if they want to continue
problem2=input("Ok so, do you want to check how many sequences are predicted or not?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem2 == "yes":
 print("Ok, let's check!")
#check how many sequences are predicted
 predicted_number=len(list(re.finditer(r'PREDICTED',sequence_count)))
 print("The number of predicted sequences is"+" "+str(predicted_number))

#######################################
#Check how many sequences are partial
#######################################
#Ask the user if they want to continue
question2=input("Ok so, do you want to check how many sequences are partial or not?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if question2 == "yes":
 print("Ok, let's check!")
#check how many sequences are partial
 partial_number=len(list(re.finditer(r'partial',sequence_count)))
 print("The number of partial sequences is"+" "+str(partial_number))


############################################################################
#Frist Part: analyse the level of conservation between the protein sequences
############################################################################
#Ask the user whether want to continue to analyse the level of conservation between the protein sequences
problem3=input("Now, do you want to analyse the level of conservation between the protein sequences or not?\n\tIf you want,please type yes\n\tIf not, you have to type anything to quit because this step is necessary!\n\t")
if problem3 == "yes":
 print("Ok, let's analyse the level of conservation!")
#Performing multiple sequence comparisons
 subprocess.call('clustalo -i protein.sequence.fa -o clustalo_result.fa --full --force --threads=30',shell=True)
 a=input("First is clustalo result. Do you want to see the clustalo result?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
 if a == "yes":
  a1=open("clustalo_result.fa").read()
  print(a1)
#Integration of sequence alignment results to generate consensus sequences
 os.system('cons clustalo_result.fa clustalo_result.cons')
 b=input("Then is consensus sequences. Do you want to see the consensus sequences?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
 if b == "yes":
  b1=open("clustalo_result.cons").read()
  print(b1)
#Building a protein database
 os.system('makeblastdb -in protein.sequence.fa -dbtype prot -parse_seqids -out protein_database')
 print("Now!You can see that we have created the protein database as above.")
#Performing BLASTP
 os.system('blastp -db protein_database -query clustalo_result.cons > blastp_result.out')
 while True:
  c=input("Next is BLASTP result. You need to see the BLASTP result and decide how many sequences you want whose bit score is higher\n\tPlease type yes\n\t")
  if c == "yes":
   print("Please read the results above and you can choose any number of sequence whose bit score is higher than other")
   c1=open("blastp_result.out").read()
   print(c1)
   break
  else:
   continue
#Let user choose how many sequences he might want to use for the conservation analysis
 chosen_sequence=[]
 counter=0
 while True:
  number=input("How many sequences you might want to use for the conservation analysis? \nPlease enter number which no more than the number of sequences! ")
  if number.isdigit():
   if int(number) <= sequence_number and  int(number) >= 2:
#From blastp_result.out to find the chosen sequences which the user want
    for line in open("blastp_result.out"):
     counter+=1
     if counter>=30 and counter<=(29+int(number)):
      chosen_sequence.append(line)
    print("Ok, the number of sequences you choose is "+number)
    break
   else:
    print("Your input are wrong!Please enter correct number ")
    continue
  else:
   print("Your input are wrong!Please enter correct number ")
   continue

#Obtain gene ID from the chosen sequence
 ID= []
 for line in chosen_sequence:
#By '>' and space to split the sequence
  ID_line= line.split(' ')
  ID.append(ID_line[0])

#Line break for gene ID
 ID='\n'.join(ID)
#Writing the gene ID into a file which named chosen_sequence.txt
 chosen=open('chosen_sequence.txt','w')
 chosen.write(ID)
 chosen.close()
#Using pullseq to match gene ID with protein sequence
 os.system('/localdisk/data/BPSM/Assignment2/pullseq -i protein.sequence.fa -n chosen_sequence.txt > chosen_sequence.fa')
 d=input("Finally they are chosen sequences. Do you want to see the chosen sequence?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
 if d == "yes":
  d1=open("chosen_sequence.fa").read()
  print(d1)
#Using plotcon to get Similarity Plot of Aligned Sequences
 os.system('plotcon -winsize 4 -sformat fasta chosen_sequence.fa -graph svg')
 print("The plot which stand the level of conservation between the protein sequences have been save in file which named plotcon.svg!!!!")
 os.system('firefox plotcon.svg')

else:
 quit()
########################################################################################
#Second Part: scan protein sequence(s) of interest with motifs from the PROSITE database
########################################################################################
#Ask the user wether to scan protein sequence(s) of interest with motifs from the PROSITE database
problem4=input("Now we haved finished analyse the level of conservation. Do you want to scan protein sequence of interest with motifs from the PROSITE database?\n\tPlease type yes because it also necessary\n\tIf you really don't want to continue you can type anything to quit\n\t")
if problem4 == "yes":
 print("Ok, let us scan protein sequence of your choice!")
#From protein.sequence.fa to get all the gene id
 gene_ID= []
 for line in open("chosen_sequence.fa"):
  if '>' in line:
   gene_ID_line= line.split('>')[1].split(' ')[0]
   gene_ID.append(gene_ID_line)
 f=input("Having get the gene names which you choose from previous BLASTP result.Do you want to see the chosen gene_ID?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
 if f == "yes":
  print(gene_ID)
#Open and read protein.sequence.fa
 single_sequence=open("chosen_sequence.fa").read()
#Use '$' to replace '\n' and use '$>' to replace '\n>'
 single_sequence=single_sequence.replace("\n","$").replace("$>","\n>")
#Splitting a sequence with a line break
 single_sequence=single_sequence.split('\n')
 for i in range(len(gene_ID)):
#Use '$' to replace ' ' and use ']' to ']\n'
   test=open(gene_ID[i], "w")
   test.write(str(single_sequence[i].replace("$","").replace("]","]\n")))
   test.close()

#Make a directory whcih called patmatmotifs where user want to put their patmatmotifs results
 os.mkdir("patmatmotifs")
#Using patmatmotifs to scan motifs from the PROSITE database
 for i in range(len(gene_ID)):
  os.system('patmatmotifs -sequence '+gene_ID[i]+' -outfile patmatmotifs/'+gene_ID[i]+'_motif_result')

 Motif_name=[]
 for i in range(len(gene_ID)):
  for line in open('patmatmotifs/'+gene_ID[i]+'_motif_result'):
   if 'Motif =' in line:
     Motif_name_line= line.split('Motif = ')[1].split('\n')[0]
     Motif_name.append(Motif_name_line)
 print("The following are the Motif name which you want!")
 print(Motif_name)
 print("And all the patmatmotifs results have been put into the directory which named patmatmotifs!!!!")

else:
 quit()
########################################################
#Third Part:other appropriate EMBOSS (or other) analysis
########################################################
#Ask the user whether want to do EMBOSS analysis like helixturnhelix
problem9=input("If you want to check motif, so are you intereted with other EMBOSS analysis like helixturnhelix which is also about check motif?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem9 == "yes":
 print("Ok, let's check!")
 os.system('helixturnhelix -sequence chosen_sequence.fa -outfile helixturnhelix_result.fa')
 helixturnhelix=input('Do you want to see the result of helixturnhelix?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t')
 if helixturnhelix == "yes":
  helixturnhelix1=open("helixturnhelix_result.fa").read()
  print(helixturnhelix1)

#Ask the user whether want to do EMBOSS analysis like comseq
problem5=input("So do you want to do other EMBOSS analysis like comseq?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem5 == "yes":
 print("Ok, let's continue!")
#Make a directory whcih called compseq where user want to put their compseq results
 os.mkdir("compseq")
#using compseq to calculate the composition of words of a specified length (dimer, trimer etc) in the input sequence(s)
 for i in range(len(gene_ID)):
  os.system('compseq -sequence '+gene_ID[i]+' -nozero -word 3 -outfile compseq/'+gene_ID[i]+'_compseq_result')
 print("Great! All the compseq results have been put into the directory which named compseq")

#Ask the user whether want to do EMBOSS analysis like pepstars
problem8=input("Then whether want to other EMBOSS analysis like pepstars?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem8 =="yes":
 print("Ok, let's continue!")
 os.system('pepstats -sequence chosen_sequence.fa -outfile pepstars_result.fa')
 pepstars=input('Do you want to see the result of pepstars?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t')
 if pepstars == "yes":
  pepstar=open("pepstars_result.fa").read()
  print(pepstar)

#Ask the user whether want to do BLASTX
problem6=input("Do you have any DNA sequence want to BLASTX in the previous protein database?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem6 == "yes":
 print("Ok, let's continue!")
 #Enter DNA sequence and BLASTX
 blastx_sequence=input("Enter blastx_DNA_sequence:")
 blastx=open('blastx.fa','w')
 blastx.write(blastx_sequence)
 blastx.close()
 os.system('blastx -db protein_database -query blastx.fa > blastx_output.out')
 ask1=input("Do you want to see the BLASTX result?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
 if ask1 == "yes":
  as1=open("blastx_output.out").read()
  print(as1)

#Ask the user whether want to do BLASTP
problem7=input("Do you have any protein sequence want to BLASTP in the previous protein database?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
if problem7 == "yes":
 print("Ok, let's continue!")
#Enter DNA sequence and BLASTP
 blastp_sequence=input("Enter blastp_protein_sequence:")
 blastp=open('blastp.fa','w')
 blastp.write(blastp_sequence)
 blastp.close()
 os.system('blastp -db protein_database -query blastp.fa > blastp_output.out')
 ask2=input("Do you want to see the BLASTP result?\n\tIf you want,please type yes\n\tIf not, you can type anything to continue\n\t")
 if ask2 == "yes":
  as2=open("blastp_output.out").read()
  print(as2)

#Finished process
print("We have done all the things which you want to analysis and All the result will put into "+space+" \n I hope you have got the results you were looking for")
print("Thank you very much and I hope it will help you!")