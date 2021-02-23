
SIMPAR_PARALEL_DIRECTIVE = "#PARALLEL {"
OMP_PARALLEL_DIRECTIVE = "#pragma omp paralell"
OMP_SECTIONS_DIRECTIVE = "#pragma omp sections"
OMP_SECTION_DIRECTIVE = "#pragma omp section"
OPEN = "{"
CLOSE = "}"

with open('ex0_simpar.c') as src_file:
    lines = src_file.readlines()
    simpar_open = 0

    omp_par_open = 0
    omp_sections_open = 0
    omp_section_open = 0
    indent = ""
    for line in lines:
        line = line.strip()
        if (simpar_open):
            if (line == CLOSE):    # end of SIMPAR directive 
#                print(CLOSE)   # close the last section in sections 
#                omp_section_open = 0
                indent = indent[2:]
                print(indent + CLOSE)   # close sections
                omp_sections_open = 0
                indent = indent[2:]
                print(indent + CLOSE)   # close omp parallel 
                omp_par_open = 0
                simpar_open = 0
            else: 
                print(indent + OMP_SECTION_DIRECTIVE) 
                print(indent + line)
##                print(CLOSE)   # close this section  

        else:
            if (line == SIMPAR_PARALEL_DIRECTIVE):
                simpar_open = 1
                print(indent + OMP_PARALLEL_DIRECTIVE)
                print(indent + OPEN)
                indent = indent + "  "
                omp_par_open = 1
                print(indent + OMP_SECTIONS_DIRECTIVE)
                print(indent + OPEN)
                indent = indent + "  "
                omp_sections_open = 1
            else:     
                if (line == CLOSE):
                    print(line)
                else: 
                    print(indent + line)
        if (line.endswith('{') and line != SIMPAR_PARALEL_DIRECTIVE):
            indent = indent + "  "
        
