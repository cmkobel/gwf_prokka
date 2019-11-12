"""
This workflow batches a job for prokka on each of files in the fasta directory

The output can be found in output/

"""


import gwf
import os

fasta_dir = 'fasta/'

gwf = gwf.Workflow()

def prokka(infile, infile_stem): #, outfile):
    #prefix  = os.path.basename(infile)#.replace('.gff', '')
    prefix = '.'.join(infile_stem.split('.')[:-1:]) 
    
    #outdir  = os.path.dirname(outfile)
    
    inputs  = [infile]
    outputs = ['output/' + prefix + '/completed.txt']
    options = {'nodes': 1, 'cores': 8, 'memory': '1g', 'walltime': '03:00:00', 'account': 'ClinicalMicrobio'} # initially 2 hours
    spec = """
prokka --cpu 8 --outdir output/{prefix} --prefix {prefix} {infile} && echo $(date) $SLURM_JOBID {infile} >> output/{prefix}/completed.txt

""".format(infile = infile,
           infile_stem = infile_stem,
           prefix = prefix)
    
    return (inputs, outputs , options, spec)





file_stems = os.listdir(fasta_dir)
print('number of files to consider:', len(file_stems))


for i, file_stem in enumerate(file_stems):
    input_file = fasta_dir + str(file_stem)
    
    gwf.target_from_template('prokka_' + str(i) + '_' + file_stem.replace('-', '_'), prokka(infile = input_file, infile_stem = file_stem))    




#for i, input_file in enumerate(file_stems):

