#!/usr/bin/env python

import os
import sys
import argparse
import subprocess


def _parse_arguments(desc, args):
    """
    Parses command line arguments
    :param desc:
    :param args:
    :return:
    """
    help_fm = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(description=desc,
                                     formatter_class=help_fm)
    parser.add_argument('input',
                        help='Edge file in tab delimited format')
    parser.add_argument('--directed', dest='directed', action='store_true',
                        help='If set, then treat input as a directed graph')
    parser.set_defaults(directed=False)
    parser.add_argument('--nosinglet', dest='nosinglet', action='store_true',
                        help='If set, then merge singlet with existing modules')
    parser.set_defaults(nosinglet=False)
    parser.add_argument('--seed', default=-1, type=int,
                        help='Seed for random generator')
    parser.add_argument('--p_val', default=0.1, type=float,
                        help='p-value: increase to get more module')
    parser.add_argument('--cp', default=0.5, type=float,
                        help='coverage parameter:  gigger value leads to bigger clusters')
    return parser.parse_args(args)


def run_oslom_cmd(directed, args):
    """
    Runs docker

    :param cmd_to_run: command to run as list
    :return:
    """
    if directed == True:
        cmd = ['OSLOM2/oslom_dir']
    else:
        cmd = ['OSLOM2/oslom_undir']
    cmd.extend(args)

    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    out, err = p.communicate()

    return p.returncode, out, err


def run_oslom(graph, directed=False, nosinglet=False, seed=-1, p_val=0.1, cp=0.5):
    """
    :param outdir: the output directory to comprehend the output link file
    :param graph: input file
    :param directed: whether to treat input file as directed
    :param nosinglet: whether to merge singlets
    :param seed: int
    :param p_val: greater for more clusters
    :param_cp: greater for larger communities
    :return
    """
    cmdargs = ['-f', graph]
    weight = ''
    with open(graph, 'r') as file:
        lines = file.read().splitlines()
        while lines[0][0] == '#':
            lines.pop(0)
        if len(lines[0].split()) >= 3:
            weight = '-w'
        else:
            weight = '-uw'
        cmdargs.append(weight)
    if nosinglet == False:
        cmdargs.append('-singlet')
    if isinstance(seed, int) and seed>=1:
        cmdargs.append('-seed')
        cmdargs.append(str(seed))
    cmdargs = cmdargs + ['-t', str(p_val), '-cp', str(cp)]
    cmdecode, cmdout, cmderr = run_oslom_cmd(directed, cmdargs)
    
    if cmdecode != 0:
        sys.stderr.write('Command failed with non-zero exit code: ' +
                         str(cmdecode) + ' : ' + str(cmderr) + '\n')
        return 1
    
    outfolder = graph + '_oslo_files'
    clusts_layers = []
    clusts_layers.append([])
    with open(os.path.join(outfolder, 'tp'), 'r') as cfile:
        lines = cfile.read().splitlines()
        for i in range(len(lines)//2):
            clusts_layers[0].append([])
            members = lines[2*i+1].split()
            for m in members:
                clusts_layers[0][i].append(m)
    cfile.close()
    i = 1
    while os.path.isfile(os.path.join(outfolder, 'tp'+str(i))):
        with open(os.path.join(outfolder, 'tp'+str(i)), 'r') as cfile:
            clusts_layers.append([])
            lines = cfile.read().splitlines()
            for j in range(len(lines)//2):
                clusts_layers[i].append([])
                members = lines[2*i+1].split()
                for m in members:
                    clusts_layers[i][j].append(m)
        cfile.close()
        i = i+1
    
    maxNode = 0
    for clust in clusts_layers[0]:
        maxNode = max(maxNode, max(clust))
    for i in range(len(clusts_layers[0])):
        for n in clusts_layers[0][i]:
            sys.stdout.write(str(maxNode+i+1) + ',' + str(n) + ',' + 'c-m' + ';')
    maxNode = maxNode + len(clusts_layers[0])
    for i in range(1, len(clusts_layers)):
        for j in range(len(clusts_layers[i-1])):
            for k in range(len(clusts_layers[i])):
                if all(x in clusts_layers[i][k] for x in clusts_layers[i-1][j]):
                    sys.stdout.write(str(maxNode+k+1) + ',' + str(maxNode-len(clusts_layers[i-1])+j+1) + ',' + 'c-c' + ';')
                    break
        maxNode = maxNode + len(clusts_layers[i])
    for i in range(len(clusts_layers[-1])):
        sys.stdout.write(str(maxNode+1) + ',' + str(maxNode-len(clusts_layers[-1])+i+1) + ',' + 'c-c' + ';')

    sys.stdout.flush()
    return 0


def main(args):
    """
    Main entry point for program

    :param args: command line arguments usually :py:const:`sys.argv`
    :return: 0 for success otherwise failure
    :rtype: int
    """
    desc = """
    Runs oslom on command line, sending output to standard out 
    """

    theargs = _parse_arguments(desc, args[1:])

    try:
        inputfile = os.path.abspath(theargs.input)
        
        return run_oslom(inputfile, directed=theargs.directed, nosinglet=theargs.nosinglet, seed=theargs.seed, p_val=theargs.p_val, cp=theargs.cp)
        
    except Exception as e:
        sys.stderr.write('Caught exception: ' + str(e))
        return 2


if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))
