"""
desc:	get the tabbed format output from chatgpt raw output
author:	Yangzhe Peng
date:	2023/03/26
"""

import subprocess
import tqdm
import pdb

def get_line_num(filename):
    out = subprocess.getoutput(f'wc -l {filename}|cut -d " " -f1')
    return int(out)

if __name__=='__main__':
    raw_filename = 'raw_output.tsv'
    output_filename = 'processed.tsv'
    open(output_filename,'w').close()
    output_fp = open(output_filename,'a')

    sent = ''
    triples = []
    with open(raw_filename) as fp:
        for _ in tqdm.trange(get_line_num(raw_filename),desc='processing'):
            line = fp.readline().strip('\n')
            if line == '':
                if sent!='':
                    for triple in triples:
                        triple = triple.split('\t')
                        for t in triple:
                            t = t.lstrip('(')
                            t = t.rstrip(')')
                        while len(triple)<3:
                            triple.append('')
                        rht = f'{triple[1]}\t{triple[0]}\t{triple[2]}' # convert hrt to rht format
                        output_fp.write(f'{sent}\t1\t{rht}\n') # 1 is the confidence
                    triples = []
                continue

            if '\t' in line or '\\t'in line or '|' in line:
                if '\\t' in line:
                    line = line.replace('\\t','\t')
                if '|' in line:
                    line = line.replace('|','\t')
                line = line.replace('TAIL_ENTITY','')
                line = line.replace('HEAD_ENTITY','')
                line = line.replace('RELATION','')
                line = line.replace('Relation','')
                triples.append(line)
            else:
                sent = line