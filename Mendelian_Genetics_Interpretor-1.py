# MENDELIAN GENETICS INTERPRETOR

# Parent Genotypes
parent1 = input("Enter the genotype of Parent 1: ")
parent2 = input("Enter the genotype of Parent 2: ")

print("Parent 1: ", parent1)
print("Parent 2: ", parent2)

# Validation
if len(parent1) == 2 or len(parent2) == 2:
    print("Valid genotype entered.")
else:
    print("Invalid genotype entered. Program stopped.")
    quit()

# Allele Extraction
allele1_parent1 = parent1[0]
allele2_parent1 = parent1[1]
allele1_parent2 = parent2[0]
allele2_parent2 = parent2[1]

print("Allele 1 of Parent 1:", allele1_parent1)
print("Allele 2 of Parent 1:", allele2_parent1)
print("Allele 1 of Parent 2:", allele1_parent2)
print("Allele 2 of Parent 2:", allele2_parent2)

# Gamete Generation
gametes_parent1 = list(set([allele1_parent1, allele2_parent1]))
gametes_parent2 = list(set([allele1_parent2, allele2_parent2]))

print("Gametes of Parent 1:", gametes_parent1)
print("Gametes of Parent 2:", gametes_parent2)

# Punnett Square Generation
punnett_square = []
for gamete_parent1 in gametes_parent1:
    row = []
    for gamete_parent2 in gametes_parent2:
        offspring_genotype = gamete_parent1 + gamete_parent2
        if offspring_genotype[0].islower() and offspring_genotype[1].isupper():
            offspring_genotype = offspring_genotype[1] + offspring_genotype[0]

        row.append(offspring_genotype)
    punnett_square.append(row)

print("Punnett Square:")
for row in punnett_square:
    print(row)

# Offspring Genotype Generation
offspring = []
for row in punnett_square:
    for genotype in row:
        offspring.append(genotype)
print("Offspring Genotype: ", offspring)

# Genotype Counting
counts = {
    "AA" : 0,
    "Aa" : 0,
    "aa" : 0
}
for genotype in offspring:
    counts[genotype] = counts[genotype] + 1

print("AA =", counts["AA"])
print("Aa =", counts["Aa"])
print("aa =", counts["aa"])

# Genotype Percentage
total_offspring = len(offspring)
for genotype in counts:
    percentage = counts[genotype]/ total_offspring * 100
    print("Percentage of ", genotype,":", percentage)

# Phenotype Determination
phenotypes = []
for genotype in offspring:
    phenotypes.append("Dominant" if genotype[0].isupper() else "Recessive")

print("Phenotypes of offsprings: ", phenotypes)

# Phenotype Counting
phenotype_counts = {
    "Dominant": phenotypes.count("Dominant"),
    "Recessive": phenotypes.count("Recessive")
}

print("Dominant phenotype =", phenotype_counts["Dominant"])
print("Recessive phenotype =", phenotype_counts["Recessive"])

# Phenotype Percentage
phenotype_percentage_dominant = phenotype_counts["Dominant"]/total_offspring * 100
phenotype_percentage_recessive = phenotype_counts["Recessive"]/total_offspring * 100


print("Precentage of Dominant: ", phenotype_percentage_dominant)
print("Percentage of Recessive: ", phenotype_percentage_recessive)

# Genotypic Ratio
counts = {}

for genotype in offspring:

    if genotype not in counts:
        counts[genotype] = 1
    else:
        counts[genotype] = counts[genotype] + 1

print("Genotype Counts: ", counts)

# Phenotypic Ratio
phenotypic_counts = {}

for phenotype in offspring:

    if phenotype not in phenotypic_counts:
        phenotypic_counts[phenotype] = 1
    else:
        phenotypic_counts[phenotype] = phenotypic_counts[phenotype] + 1

print("Phenotypic Counts: ", phenotypic_counts)

print("Offspring list: ", offspring)

# Homozygous and Heterozygous Analysis
homozygous = []
heterozygous = []

for genotype in offspring:
    print("Checking:", genotype, "First:", genotype[0], "Second:", genotype[1])

    if genotype[0] == genotype[1]:
        print("Homozygous: ", genotype)
        homozygous.append(genotype)
    else:
        print("Heterozygous: ", genotype)
        heterozygous.append(genotype)

print("Homozygous offspring: ", homozygous)
print("Heterozygous offspring: ", heterozygous)

# Possible offspring analysis
possible_offspring = set()

for genotype in offspring:
    possible_offspring.add(genotype)

print("Possible offspring genotypes: ", possible_offspring)