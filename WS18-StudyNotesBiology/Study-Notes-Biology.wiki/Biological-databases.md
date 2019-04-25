# Biological databases lecture notes 

## 30.10.2018
* Annotation
    * Add useful information
    * Links to use resources (URIs)
    * Provenance
    * Gene Annotation (what does it do? where does it start / end?, where is it expressed?)
* Curation
    * Human checking of the information in a database
    * Aggregation of similar data (Same classification)
* Gene Ontology
    * DAG
    * three sources: : mouse people, worm people, fly people
    * Three different views (hierarchical trees)
        * **[cellular componen**t](https://en.wikipedia.org/wiki/Cellular_component): the parts of a [cell](https://en.wikipedia.org/wiki/Cell_(biology)) or its [extracellular](https://en.wikipedia.org/wiki/Extracellular) environment;
        * **molecular function**: the elemental activities of a gene product at the molecular level
        * **[biological proces**s](https://en.wikipedia.org/wiki/Biological_process), operations or sets of molecular events with a defined beginning and end, pertinent to the functioning of integrated living units: cells, [tissues](https://en.wikipedia.org/wiki/Tissue_(biology)), [organs](https://en.wikipedia.org/wiki/Organ_(anatomy)), and [organisms](https://en.wikipedia.org/wiki/Organism).
* MGI Database guided tour
    * Mouse DNA
    * Different query options
        * Anatomy (order by spatial region)
        * Temporal (order by development stage)
        * Classical (DNA numbering)
=> Example for multi model (more than 1 dimension)
    * Submit data (Genes, Pheno data, Knock-in mouse data, …)
    * Analysis tools (Multiple genome viewer -> compare different mouse genomes)
    * Human-Mouse Disease Connection
    * Compatibility Mouse-Human (inbred strains)
* Ensembl Database
    * Look and compare genomes of different species (Human, Mouse & Zebrafish)
    * Similar to NCI
    * Hybrid database: Some data is queried from external sources, others from intertal
    * Provenance: Version control, where does the data come from, evolution of the database
* Swiss Prot Database
    * Highly curated protein database
* Useful info
    * mRNA average length: 1500 - 2000
    * gene average length: 150.000
    * Micro RNA (miRNA): Short non-coding RNAs that regulate gene expression post-transcriptionally. 
    * DBs are sorted by chemical properties/parts
    * Knock-In: Substitution instead of deactivation
    * The human leukocyte antigen (**HLA**)
    * Syntenic regions: Conservation of blocks of order within two sets of chromosomes that are being compared with each other.
    * A **transgene** is a gene that has been transferred from one organism to another. The introduction of a transgene (called "transgenesis") has the potential to change the phenotype of an organism.
    * A **quantitative trait locus** (QTL) is a region of DNA which is associated with a particular phenotypic trait, which varies in degree and which can be attributed to polygenic effects, i.e., the product of two or more genes, and their environment.
    * In biochemistry, a metabolic **pathway** is a linked series of chemical reactions occurring within a cell. The reactants, products, and intermediates of an enzymatic reaction are known as metabolites, which are modified by a sequence of chemical reactions catalyzed by enzymes.
    * Fugu fish has no introns
    * De-novo sequencing is much more work intensive
    * single nucleotide polymorphisms (SNP): Small differences between organisms of a species
    * Variations in genome: deletions, copy number variations (CNV), SNPs, different repeat 
    * Contec: A region of ample evidence that a gene sequence has a certain sequence 
* Takeaways:
    * Provenance: Backtracking of annotations
    * Ensemble is not **one** database it gets data from multiple sources 
    * Addression with **ENSG00000026508, **ENS: Ensemble, G: Gene
    * Persistence of identifiers
    * Gold Standard (highly curated data), "Havana project"
    * Variances in the genome

## 31.10.2018
* Ensemble CD44
    * small exon, long introns
    * 121 orthologues
    * Different views on the gene 
    * location of inflammation
    * makes tumor cells migrate
    * VEP (Variant effect predictor), Genetic variation may have functional impact
* SNP / SNV
    * SNP 1% and more 
    * SNV less
* Ensemble variation process: 
    * Variant import
    * Quality control
    * Linked data
    * Ensembl analysis (consequences, protein function prediction, Linkage disequilibrium data, variant conservation over species)
* Sequence ontology
    * Terms mapping to consequences
    * Rules for variations
6.11.2018
* Takeaways
    * SNPs have not to be in Genes (coding regions)
    * dbSNP (Humans only)
        * genetic variation
        * groups / haplotypes (shared variations)
        * reference is the consens of all examples
        * types / frequencies of diseases
        * good provenance tool
    * ClinVar
        * Association with disease
    * Not all SNPs are informative

## 7.11.2018
* General:
    * monogenic diseases: one gene implies a disease
    * complex diseases: combination of multiple gene variations 
    * Quantitative trait: A quantitative trait shows continued variation.
    * Etiology: Science of the of causality / origin of effects
    * MAPT: Gene responsible for tau protein 
    * An allele is a variant form of a given [gene](https://en.wikipedia.org/wiki/Gene). Sometimes, different alleles can result in different observable phenotypic traits
    * **Chromatin immunoprecipitation** (ChIP) is a type of immunoprecipitation experimental technique used to investigate the interaction between proteins and DNA in the cell.
* Regulome DB ([http://www.regulomedb.org/](http://www.regulomedb.org/)) 
    * Best db for impact genetic variation
    * rule based or scoring function 
    * biggest collection of human SNPs (invoked by ensemble)
    * function impact assesment 
    * important for exam
* GWAS Catalog
    * Genome Wide Association studies
    * Looking for SNPs specific for certain traits that are researched
    * Curated data from SNPs studies to link genotype to phenotype
* Review:
    * ClinVar
        * Gene -> Condition
        * Generalization (no isolation of incidents)
        * How often stuff is reviewed
    * RegulomeDB
        * RegulomeDB is a database that annotates SNPs with known and predicted regulatory elements in the intergenic regions of the H. sapiens genome

## 13.11.2018
* Gene Expression Databases
* General knowledge
    * rRNA: Important for protein synthesis
    * tRNA: Helps decode a mRNA into a protein
    * mRNA: convey information from DNA to ribosome
    * micro arrays: A DNA microarray is a collection of microscopic DNA spots attached to a solid surface. (does not give the best results)
    * RNAseq: Next-gen sequencing technique
    * Oligonucleotides are short [DNA](https://en.wikipedia.org/wiki/DNA) or [RNA](https://en.wikipedia.org/wiki/RNA) molecules
    * Abundancy: Copies of a gene per cell. 
    * Housekeeping genes: genes that are required for the maintenance of basic cellular function, and are expressed in all cells of an organism under normal conditions.
    * Enrich mRNA: 
    * **Sample over distribution with RNA-SEQ**
    * Most diverse organs (gene expressions): Brain & testicles
    * Single cell sequencing: Possible to get gene expressions with only ~10 cells
* Gene Expression
    * Total RNA: rRNA (90%), tRNA, non-coding (miRNA, …), mRNA 
    * outside influences can trigger gene expression
    * cFos gets poured out , after stimulus, with high #count / cell
    * housekeeping genes are always in abundance
    * next-gen sequencing makes it possible to notice gene expressions that are not in abundance (low #count/cell)
    * Most common state comparison: healthy vs diseased
* Array Express ([https://www.ebi.ac.uk/arrayexpress/](https://www.ebi.ac.uk/arrayexpress/))
* Expression Atlas ([https://www.ebi.ac.uk/gxa/home](https://www.ebi.ac.uk/gxa/home))
* Gene Expression Omnibus - GEO ([https://www.ncbi.nlm.nih.gov/geo/](https://www.ncbi.nlm.nih.gov/geo/)) 
* MIAME: **M**inimal **I**nformation for the **A**nnotation of Gene **E**xpression (Minimum information about a microarray experiment)
* Summary
    * different RNA types
    * abundance of protein encoding mRNAs
    * Gene expression experiments have to be annotated carefully (MIAME)

## 14.11.2018
* General information
    * Discretization: Form discrete classes and assign experiments to them 
    * Metagenomics: genetic material recovered directly from environmental samples
    * Transcriptome: Full range of mRNA molecules expressed by an organism. Can also be used to describe the array of mRNA transcripts produced in a particular cell
* Dual channel / color experiments
    * Mix tumor and normal sample
    * different dyes for both samples (red & green)
    * can use resulting color to indicate increase / decrease of tumor cells
* GEO (Gene Expression Experiments) >= Array Express
    * platform data: summary description + data table
    * sample data: conditions and results for one sample (sample can reference one platform, multiple series)
    * series data: links together samples of a whole study
    * Bias towards experiments done in the US
    * one of the biggest collections
* Array Express >= Expression Atlas
    * **Tutorial -> 2 questions of exam**
* Expression Atlas 
    * Anatomic atlas for gene expressions

## 20.11.2018
* UniProt (https://www.uniprot.org)
    * Biggest resource for protein data
    * Consortium of SwissProt, EMBL-EBI, ... 
    * Components
        * Sources -> UniParc (sequence archive) -> UniProtKB (Annotation, manual & automatic) -> (Proteoms, UniRef)
    * Entries:
        * Sequence data
        * Bibliographical references
        * Biological source (Taxonomic data)
    * Annotations
        * Organism
        * Cell type
        * diseased vs. healthy state
        * technology and platform
        * datetime
    * Subunits
        * UniProtKB / TrEMBL: Automatic translation / annotation of CDS in EMBL/GenBank/DDBJ ~133.500.000 entries
        * UniProtKB/SwissProt: Good quality, non-reduandant, ~500.000 entries
    * Identifiers
        * Stable identifiers for each protein, id is increasing
        * Merge: One ID becomes primary, the other one secondary
        * Split: Old ID becomes secondary
        * Proteins can become also a general name: [azAz19]{5}_[SPECIES]

## 21.11.18
* Proteon: the entire complement of proteins that is or can be expressed by a cell, tissue, or organism.
* Isoform: two functionally similar proteins that have a similar amino acid sequence and are either encoded by different genes or by RNA transcripts from the same gene which have had different exons removed.
* Alignments: 90 already high, 50 is also pretty high for proteins

## 27.11.18
* General information
    * Triple: Relationship between two objects
    * co-localization: In fluorescence microscopy, it refers to observation of the spatial overlap between two fluorescent labels to see if the different "targets" are located in the same area of the cell 
    * GFP: green fluorescent protein, creates green light, used to track other proteins
    * Phosphor relations: Attatchment of phosphor to protein for signaling
    * Post-translational modification: Protein modification after translation (through cells, enzymes)
* UniProt
    * Checks links to other dbs are stable / not broken
    * Best data for proteins (Thanks to Swissprot)
* Protein/Protein interaction (PPI)
	* Most biological process depend on these
    * Example: blood clotting in wounds
    * Example: proteins form a 3D network in the nucleus -> organizing chromosomes
    * Measurements / Detection methods / Assays (https://www.youtube.com/watch?v=ehryxM07rkI)
    	* Can be done in vitro (controlled env), In vivo (living organism), In silico
        * Proximity (charge transfer, resonance)
        * Colocalization used to track movement
        * Co-immunoprecipitation: Remove known proteins (in a complex) with matching antibodies to later analyze the unknown parts
        * Pull-down Assay: Attach bait protein to an immobilzied affinity ligand -> capture other proteins that bind to the bait -> pull down the complex for analysis
        * Label Transfer Assay (Used to find phosphor relation): 
	* Mapping
		* Yeast 2 Hybrid (Binary)
			* Detects direct physical interactiont between two proteins by the reconstitution of a transcription factor that activates reportet gene expression and promotes yeast cell survival on appropriate selective media
			* TODO: lookup
* BioGRID 
	* Quality assessment of bio-chemical publications
	* interaction repository, created by comprehensive curation
	* post-translational modifications (only one)
	* part of IMEx (Curation rules)
* IntAct
	* Molecular interaction database
	* part of IMEx
	
## 28.11.18
* IntAct
	* Search for proteins -> get list of binary interactions
	* two kind of interactions
		* binary: two proteins
		* co-complexeses: more than two proteins
	* co-complexes get resolved to binary interactions (solved both)
* String
	* protein-protein interaction networks
	* not fully curated
	* merges data from IntAct & BioGRID & others
	* edges / nodes have meaning
* Exam
	* find something about drug / protein (which database, which are better curated...)



