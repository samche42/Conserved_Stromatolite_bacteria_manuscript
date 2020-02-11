# Conserved_Stromatolite_bacteria_manuscript
A collection of raw data, Python script and R scripts used to create data and images for manuscript entitled "Conserved bacterial genomes from two geographically distinct peritidal stromatolite formations shed light on potential functional guilds"

Heatmaps in the manuscript were created in iTol. Data was prepared in the following manner:

1. ORFs were called in all genomes using prokka 1.14.5.
2. ORFs were assigned KO annotations using kofamscan 1.0.0
3. KO annotations for each bin (in Kofamscan output folder) were parsed using kegg_parser.py to obtained counts of all KO entries listed in Phosphate_query. Phosphate_query was created manually.
4. KO counts were normalized to bin coverage i.e KO abundance = KO count*(bin_coverage/sum_of_all_Bins_coverage_in_sample)*100
See Raw_KO_counts_with_metadata.xlsx for clarification
