The Mendelian Genetics Interpreter is a Python program designed to analyze a single-trait Mendelian cross between two parents. The user enters the genotypes of Parent 1 and Parent 2, and the program generates possible offspring genotypes and analyzes their genetic outcomes. 

Main functions of the program
1.Takes parent genotypes as input
The program asks the user to enter the genotypes of both parents, such as Aa.

2.Validates the genotype
It checks whether the entered genotypes have two characters. 

3.Extracts alleles
Each parent's two alleles are separated so that they can be used to generate gametes. 

4.Generates gametes
The program identifies the possible gametes produced by each parent. 

5.Creates a Punnett square
It combines the parental gametes to generate possible offspring genotypes. It also rearranges the genotype so that the uppercase allele comes first when appropriate. 

6.Counts offspring genotypes
It identifies the numbers of AA, Aa, and aa offspring and calculates their percentages. 

7.Determines phenotypes
The program classifies each offspring as Dominant or Recessive based on the genotype. 

8.Analyzes homozygous and heterozygous offspring
It separates offspring into homozygous and heterozygous groups. 

9.Identifies possible offspring genotypes
Finally, it uses a set to display the unique genotypes that can occur among the offspring.
