#!/usr/bin/python
"""
Requirements: msr-tools

Usage:
-Undervolt all parts of the cpu
undervolt -a [VALUE]
-Undervolt each piece at a different level
undervolt
"""

import sys
from subprocess import call

if len(sys.argv) < 2:
    print('Input the offset for each value.\ne.g. 50, 120, 150 = -50mV, -120mV, -150mV')
    cores = int(input('CPU Cores value:\n')) * -1
    gpu = int(input('GPU Cores value:\n'))* -1
    cache = int(input('CPU Cache value:\n'))* -1
    agent = int(input('System Agent value:\n'))* -1
    analog = int(input('Analog I/O value:\n'))* -1
    digital = int(input('Digital I/O value:\n'))* -1

    offset_cores = format(0xFFE00000&( (round(cores*1.024)&0xFFF) <<21), '08x')
    offset_gpu = format(0xFFE00000&( (round(gpu*1.024)&0xFFF) <<21), '08x')
    offset_cache= format(0xFFE00000&( (round(cache*1.024)&0xFFF) <<21), '08x')
    offset_agent = format(0xFFE00000&( (round(agent*1.024)&0xFFF) <<21), '08x')
    offset_analog = format(0xFFE00000&( (round(analog*1.024)&0xFFF) <<21), '08x')
    offset_digital = format(0xFFE00000&( (round(digital*1.024)&0xFFF) <<21), '08x')

    command_cpu =       "wrmsr 0x150 0x80000011" + offset_cores
    command_gpu =       "wrmsr 0x150 0x80000111" + offset_gpu
    command_cache =     "wrmsr 0x150 0x80000211" + offset_cache
    command_agent =     "wrmsr 0x150 0x80000311" + offset_agent
    command_analog =    "wrmsr 0x150 0x80000411" + offset_analog
    command_digital =   "wrmsr 0x150 0x80000511" + offset_digital

    commands = [command_cpu, command_gpu, command_cache, command_agent, command_analog, command_digital]

    for c in commands:
        call(c, shell=True)

elif sys.argv[1] == '-a':
    value = int(sys.argv[2])* -1
    offset_cores = format(0xFFE00000&( (round(value*1.024)&0xFFF) <<21), '08x')
    offset_gpu = format(0xFFE00000&( (round(value*1.024)&0xFFF) <<21), '08x')
    offset_cache= format(0xFFE00000&( (round(value*1.024)&0xFFF) <<21), '08x')
    offset_agent = format(0xFFE00000&( (round(value*1.024)&0xFFF) <<21), '08x')
    offset_analog = format(0xFFE00000&( (round(value*1.024)&0xFFF) <<21), '08x')
    offset_digital = format(0xFFE00000&( (round(value*1.024)&0xFFF) <<21), '08x')

    command_cpu =       "wrmsr 0x150 0x80000011" + offset_cores
    command_gpu =       "wrmsr 0x150 0x80000111" + offset_gpu
    command_cache =     "wrmsr 0x150 0x80000211" + offset_cache
    command_agent =     "wrmsr 0x150 0x80000311" + offset_agent
    command_analog =    "wrmsr 0x150 0x80000411" + offset_analog
    command_digital =   "wrmsr 0x150 0x80000511" + offset_digital
    
    commands = [command_cpu, command_gpu, command_cache, command_agent, command_analog, command_digital]

    for c in commands:
        call(c, shell=True)
