import sys
#import gzip
#import shlex
#import subprocess
import glob
import os
import csv

#import matplotlib.pyplot as plt
#import pandas as pd
#import numpy as np
#from matplotlib.pyplot import figure
#from numpy.random import seed, rand
import re

sys.path.append(r"/usr/intel/pkgs/python3/3.6.3/modules/r1/lib/python3.6/site-packages")


def printD(outputfile, extracted_values, extracted_knob_values):
    #,outputtitle
    with open(outputfile,'a') as fileTmp:
        divider=1     # to convert to ns
        print(extracted_values)
    
        
        fileTmp.write("\n")
        fileTmp.write("\n")
        fileTmp.write("\n")
        fileTmp.write("INFO PULL FROM emurun.dut_cfg: \n")
        fileTmp.write("tlm_dut                    ,%s\n" % str(extracted_values.get('emu::model::tlm_dut', 'N/A')))
        fileTmp.write("EMU Model path             ,%s\n" % str(round(0)))
        fileTmp.write("real_cores                 ,%s\n" % str(extracted_values.get('emu::model::real_cores', 'N/A')))
        fileTmp.write("num_chs_per_mcs            ,%s\n" % str(extracted_values.get('emu::model::num_chs_per_mcs', 'N/A')))
        fileTmp.write("num_mcs                    ,%s\n" % str(extracted_values.get('emu::model::num_mcs', 'N/A')))
        fileTmp.write("num_sockets                ,%s\n" % str(extracted_values.get('emu::model::num_sockets', 'N/A')))
        fileTmp.write("num_threads_per_core       ,%s\n" % str(extracted_values.get('emu::model::num_threads_per_core', 'N/A')))
        
        fileTmp.write("bios_bin       ,%s\n" % str(extracted_values.get('emu::bios::tools::bios_bin', 'N/A')))
        
        fileTmp.write("XMPMode       ,%s\n" % str(extracted_values.get('emu::bios::knobs::XMPMode = Manual', 'N/A')))
        fileTmp.write("PpdEn       ,%s\n" % str(extracted_values.get('emu::bios::knobs::PpdEn', 'N/A')))
        fileTmp.write("RefreshMode       ,%s\n" % str(extracted_values.get('emu::bios::knobs::RefreshMode', 'N/A')))
        fileTmp.write("HostDdrFreqLimit       ,%s\n" % str(extracted_values.get('emu::bios::knobs::HostDdrFreqLimit', 'N/A')))
        fileTmp.write("DramRaplPwrLimitLockCsr       ,%s\n" % str(extracted_values.get('emu::bios::knobs::DramRaplPwrLimitLockCsr', 'N/A')))
        fileTmp.write("CkeProgramming       ,%s\n" % str(extracted_values.get('emu::bios::knobs::CkeProgramming', 'N/A')))
        fileTmp.write("mc_mode       ,%s\n" % str(extracted_values.get('emu::preload::tools::preloader::mc_mode', 'N/A')))
        fileTmp.write("preloader path       ,%s\n" % str(extracted_values.get('emu::preload::tools::preloader::path', 'N/A')))
        fileTmp.write("preloader_version       ,%s\n" % str(extracted_values.get('emu::preload::tools::preloader::version', 'N/A')))
        




        #fileTmp.write("#Cores/CHA                 ,%s\n" % str("< WIP >"))
        #fileTmp.write("EMU Model path             ,%s\n" % str("< WIP >"))
        #fileTmp.write("PLATFORM CONFIGURATION \n")
        #fileTmp.write("SOC RTL version            ,%s\n" % str("< WIP >"))
        #fileTmp.write("MCP RTL version            ,%s\n" % str("< WIP >"))
        #fileTmp.write("MC version                 ,%s\n" % str("< WIP >"))
        #fileTmp.write("SCF version                ,%s\n" % str("< WIP >"))
        #fileTmp.write("MCI/B2CMI PERF SETTING \n")
        #fileTmp.write("Memory configuration       ,%s\n" % str("< WIP >"))
        #fileTmp.write("SCF Performance setting    ,%s\n" % str("< WIP >"))
        #fileTmp.write("SISTEM CONFIGURATION \n")
        #fileTmp.write("Fuse recipe override       ,%s\n" % str("< WIP >"))
        #fileTmp.write("Register override          ,%s\n" % str("< WIP >"))
        #fileTmp.write("Buffer size                ,%s\n" % str("< WIP >"))
        #fileTmp.write("Refresh policy             ,%s\n" % str("< WIP >"))
        #fileTmp.write("Pcode version              ,%s\n" % str("< WIP >"))
        fileTmp.write("\n")

        fileTmp.write("INFO PULL FROM ubios.asm \n")
        fileTmp.write("CMD_Timing C00|C01      ,%s|%s\n" % (str(extracted_values.get('N0.C00: CMD Timing', 'N/A')), str(extracted_values.get('N0.C01: CMD Timing', 'N/A'))))
        fileTmp.write("XptPrefetchEn       ,%s\n" % str(extracted_values.get(' XptPrefetchEn', 'N/A')))
        fileTmp.write("xptprefetchdisable       ,%s\n" % str(extracted_values.get('xptprefetchdisable', 'N/A')))
        fileTmp.write("DfxD2cEn       ,%s\n" % str(extracted_values.get('DfxD2cEn', 'N/A')))
        fileTmp.write("ClockModulationEn       ,%s\n" % str(extracted_values.get('ClockModulationEn', 'N/A')))
        fileTmp.write("DfxBankXorEn       ,%s\n" % str(extracted_values.get('DfxBankXorEn', 'N/A')))
        fileTmp.write("QCLK Ratio       ,%s\n" % str(extracted_values.get('QCLK Ratio', 'N/A')))
        fileTmp.write("Clustering mode       ,%s\n" % str(extracted_values.get('clustering mode', 'N/A')))
        fileTmp.write("Paging Policy       ,%s\n" % str(extracted_values.get('Paging Policy', 'N/A')))
        fileTmp.write("DIMM config Dnsty|Width|Rank_cnt|      ,%s%s %s\n" % (str(extracted_values.get('dimmmtr_0.dnsty', 'N/A')), str(extracted_values.get('dimmmtr_0.width', 'N/A')), str(extracted_values.get('dimmmtr_0.rank_cnt', 'N/A'))))
        fileTmp.write("\n")

        fileTmp.write("INFO PULL FROM testbench.log \n")
        fileTmp.write("Core Clock Freq [MHz]       ,%s\n" % str(extracted_values.get('freq core', 'N/A')))
        fileTmp.write("Uncore Clock Freq [MHz]      ,%s\n" % str(extracted_values.get('freq uclk', 'N/A')))
        fileTmp.write("DDR Clock Freq [MHz]       ,%s\n" % str(extracted_values.get('freq ddr', 'N/A')))
        fileTmp.write("\n")

        fileTmp.write("CONFIGS OVERRIDES ON THIS TEST: \n")
        fileTmp.write("Knob Name,DefVal,CurVal\n")
        
        for key, value in extracted_knob_values.items():
            fileTmp.write("%s,%s,%s\n" % (str(key),str(value[0]),str(value[1]) ))
        
        fileTmp.write("\n")
        fileTmp.write("Fuse Name\n")


def extract_value(pattern, line):
    match = re.search(r'=\s*([\w.-]+)', line)
    return match.group(1) if match else None

def extract_value_colon(pattern, line):
    #match = re.search(r':\s*([\w.-]+)', line)
    match = re.search(r':\s*(.+)$', line)
    return match.group(1) if match else None

def extract_value_arrow(pattern, line):
    match = re.search(r'>\s*([\w.-]+)', line)
    return match.group(1) if match else None

def extract_value_is(pattern, line):
    match = re.search(r'is\s+(.+)$', line)
    return match.group(1) if match else None

def extract_value_bars(pattern, line):
    match = re.search(r'\|\s*(.*?)\s*\|$', line)
    return match.group(1) if match else None

def extract_knob_names():
    readDATA_err = []
    extracted_knob_values = {}
    pattern = r'\|\s+\d+\|\s+\w+\|\s+([\w\s]+)\|\s+\d+\|\s+(\d+)\s+\|\s+(\d+)\s+\|'

    with open("ubios/flexconEmu/knobs_err.log", "rt", encoding="utf-8") as myline:
    
        readDATA_err = myline.readlines()
        for line in readDATA_err:
            # Extract the knob names, default values, and current values using regular expressions
            matches = re.findall(pattern, line)
            # Populate the dictionary with knob names as keys and corresponding values as a list
            for match in matches:
                knob_name = str(match[0])
                def_val = str(match[1])
                cur_val = str(match[2])
                extracted_knob_values[knob_name] = [def_val, cur_val]
                 
    return extracted_knob_values

def extract_fuses_settings():
    readDATA_fuses = []
    extracted_fuses_values = {}
    
    with open("report.rpt", "rt", encoding="utf-8") as myline:
        readDATA_fuses = myline.readlines()

        for line in readDATA_fuses:
            if "CMDLINE" in line:
                extracted_cmdline = extract_value_colon('CMDLINE', line)
                cmdline_string = str(extracted_cmdline)
                splitted_cmdline_list = cmdline_string.split(' -')

            if "TESTED MODEL" in line:
                extracted_testmodel = extract_value_colon('TESTED MODEL', line)
                testmodel_string = str(extracted_testmodel)
                print(testmodel_string)

    my_dict = {}
    for item in splitted_cmdline_list:
        parts = item.split(' ', 1)
        key = parts[0]
        value = parts[1] if len(parts) > 1 else ''
        my_dict[key] = value


    #print(my_dict)

    filtered_dict = {key: value for key, value in my_dict.items() if key.startswith('fuse.fuse_string_file')}

    print(filtered_dict)

    new_dict = {}
    for key, value in filtered_dict.items():
        if key.startswith('fuse.fuse_string_file'):
            with open(value, 'r') as file:
                contents = file.read()
                matches = re.findall(r'([\w/]+)\s=\s(0x[0-9a-fA-F]+)', contents)
                fuses_dict = {match[0]: [int(match[1], 16), 0] for match in matches}
                new_dict[key] = fuses_dict
    print(new_dict)


    new_testmodel_string = testmodel_string + "/zse4/input_dir/fuses"

    project = 'gnr'

    if project == 'gnr':
        if 'fuse.fuse_string_file_gnrio_north' in new_dict:
            file_path = os.path.join(new_testmodel_string, 'por_fuses_ici_gnrio_north.txt')

            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()

                    #fuse_name, value = line.split('=')
                    #fuse_name = fuse_name.strip()

                    print(line)
                
                    #value = int(value.strip())
                    #if fuse_name in new_dict['fuse.fuse_string_file_gnrio_north']:
                    #    new_dict['fuse.fuse_string_file_gnrio_north'][fuse_name][1] = value
    #print(new_dict)

    
    

    

















def extract_emu_model_settings(dut_cfg, real_cores, num_mcs, tlm_dut, num_chs_per_mcs, num_sockets, num_threads_per_core, 
bios_bin, commandTiming, XMPMode, PpdEn, RefreshMode, HostDdrFreqLimit, DramRaplPwrLimitLockCsr, DfxBankXorEn, ClockModulationEn, 
CkeProgramming, mc_mode, preloader_path, preloader_version):
    readDATA_model = []
    extracted_values = {}

    with open(dut_cfg, "rt", encoding="utf-8") as myline:
        readDATA_model = myline.readlines()
        for line in readDATA_model:
            if real_cores in line:
                extracted_values[real_cores] = extract_value(real_cores, line)

            if num_mcs in line:
                extracted_values[num_mcs] = extract_value(num_mcs, line)

            if tlm_dut in line:
                extracted_values[tlm_dut] = extract_value(tlm_dut, line)

            if num_chs_per_mcs in line:
                extracted_values[num_chs_per_mcs] = extract_value(num_chs_per_mcs, line)
            
            if num_sockets in line:
                extracted_values[num_sockets] = extract_value(num_sockets, line)

            if num_threads_per_core in line:
                extracted_values[num_threads_per_core] = extract_value(num_threads_per_core, line)

            if bios_bin in line:
                extracted_values[bios_bin] = extract_value(bios_bin, line)

            if commandTiming in line:
                extracted_values[commandTiming] = extract_value(commandTiming, line)

            if XMPMode in line:
                extracted_values[XMPMode] = extract_value(XMPMode, line)

            if PpdEn in line:
                extracted_values[PpdEn] = extract_value(PpdEn, line)

            if RefreshMode in line:
                extracted_values[RefreshMode] = extract_value(RefreshMode, line)

            if HostDdrFreqLimit in line:
                extracted_values[HostDdrFreqLimit] = extract_value(HostDdrFreqLimit, line)

            if DramRaplPwrLimitLockCsr in line:
                extracted_values[DramRaplPwrLimitLockCsr] = extract_value(DramRaplPwrLimitLockCsr, line)

            if DfxBankXorEn in line:
                extracted_values[DfxBankXorEn] = extract_value(DfxBankXorEn, line)

            if ClockModulationEn in line:
                extracted_values[ClockModulationEn] = extract_value(ClockModulationEn, line)

            if CkeProgramming in line:
                extracted_values[CkeProgramming] = extract_value(CkeProgramming, line)

            if mc_mode in line:
                extracted_values[mc_mode] = extract_value(mc_mode, line)

            if preloader_path in line:
                extracted_values[preloader_path] = extract_value(preloader_path, line)

            if preloader_version in line:
                extracted_values[preloader_version] = extract_value(preloader_version, line)

    return extracted_values

def extract_ubios_settings(C00_CMD_Timing, C01_CMD_Timing, XptPrefetchEn, xptprefetchdisable, DfxD2cEn, ClockModulation, DfxBankXor, 
QCLK_Ratio, clustering, Paging_Policy, Rank_cnt, Dnsty, Width):
    readDATA_model = []
    extracted_ubios_values = {}

    with open("ubios.asm", "rt", encoding="utf-8") as myline:
        readDATA_model = myline.readlines()
        for line in readDATA_model:
            if C00_CMD_Timing in line:
                extracted_ubios_values[C00_CMD_Timing] = extract_value(C00_CMD_Timing, line)

            if C01_CMD_Timing in line:
                extracted_ubios_values[C01_CMD_Timing] = extract_value(C01_CMD_Timing, line)

            if XptPrefetchEn in line:
                extracted_ubios_values[XptPrefetchEn] = extract_value_colon(XptPrefetchEn, line)

            if xptprefetchdisable in line:
                extracted_ubios_values[xptprefetchdisable] = extract_value_arrow(xptprefetchdisable, line)

            if DfxD2cEn in line:
                extracted_ubios_values[DfxD2cEn] = extract_value_colon(DfxD2cEn, line)

            if ClockModulation in line:
                extracted_ubios_values[ClockModulation] = extract_value_colon(ClockModulation, line)

            if DfxBankXor in line:
                extracted_ubios_values[DfxBankXor] = extract_value(DfxBankXor, line)

            if QCLK_Ratio in line:
                extracted_ubios_values[QCLK_Ratio] = extract_value_colon(QCLK_Ratio, line)

            if clustering in line:
                extracted_ubios_values[clustering] = extract_value_is(clustering, line)

            if Paging_Policy in line:
                extracted_ubios_values[Paging_Policy] = extract_value_bars(Paging_Policy, line)

            if Rank_cnt in line:
                value = extract_value_arrow(Rank_cnt, line)

                if value == "0x0":
                    extracted_ubios_values[Rank_cnt] = "SR"
                elif value == "0x1":
                    extracted_ubios_values[Rank_cnt] = "DR"
                elif value == "0x2":
                    extracted_ubios_values[Rank_cnt] = "QR"
                else:
                    print("N/A")

            if Dnsty in line:
                value = extract_value_arrow(Dnsty, line)

                if value == "0x0":
                    extracted_ubios_values[Dnsty] = "Reserved"
                elif value == "0x1":
                    extracted_ubios_values[Dnsty] = "2Gb"
                elif value == "0x2":
                    extracted_ubios_values[Dnsty] = "4Gb"
                elif value == "0x3":
                    extracted_ubios_values[Dnsty] = "8Gb"
                elif value == "0x4":
                    extracted_ubios_values[Dnsty] = "16Gb"
                elif value == "0x5":
                    extracted_ubios_values[Dnsty] = "12Gb"
                elif value == "0x6":
                    extracted_ubios_values[Dnsty] = "24Gb"
                elif value == "0x7":
                    extracted_ubios_values[Dnsty] = "32Gb"
                else:
                    print("N/A")
            
            if Width in line:
                value = extract_value_arrow(Width, line)

                if value == "0x0":
                    extracted_ubios_values[Width] = "x4"
                elif value == "0x1":
                    extracted_ubios_values[Width] = "x8"
                elif value == "0x2":
                    extracted_ubios_values[Width] = "x16"
                elif value == "0x3":
                    extracted_ubios_values[Width] = "reserved"
                else:
                    print("N/A")

          
  
    return extracted_ubios_values


def extract_testbench_settings(Frequency, Freq_core, Freq_uclk, Freq_ddr):
    readDATA_model = []
    extracted_testbench_values = {}

    with open("testbench.log", "rt", encoding="utf-8") as myline:
        readDATA_model = myline.readlines()
        for line in readDATA_model:

            if Frequency in line:
                if "coretile" in line or "core"  in line:
                    if "changed to" in line:
                        match = re.search(r'(\d+(\.\d+)?) MHz', line)

                        if match:
                            frequency_core = float(match.group(1))
                            extracted_testbench_values[Freq_core] = frequency_core
                            
                        else: pass
                    else:pass
                else:pass
            else:pass

            if Frequency in line:
                if "uclk" in line:
                    if "changed to" in line:
                        match = re.search(r'(\d+(\.\d+)?) MHz', line)

                        if match:
                            frequency_uclk = float(match.group(1))
                            extracted_testbench_values[Freq_uclk] = frequency_uclk
                            
                        else: pass
                    else:pass
                else:pass
            else:pass

            if Frequency in line:
                if "ddr" in line:
                    if "changed to" in line:
                        match = re.search(r'(\d+(\.\d+)?) MHz', line)

                        if match:
                            frequency_ddr = float(match.group(1))
                            extracted_testbench_values[Freq_ddr] = frequency_ddr
                            
                        else: pass
                    else:pass
                else:pass
            else:pass

    return extracted_testbench_values
       

#main
def main():
    ## Search emu model settings in emurun.dut_cfg
    dut_cfg = "emurun.dut_cfg"
    real_cores = "emu::model::real_cores"
    num_mcs = "emu::model::num_mcs"
    tlm_dut = "emu::model::tlm_dut"
    num_chs_per_mcs = 'emu::model::num_chs_per_mcs'
    num_sockets = 'emu::model::num_sockets'
    num_threads_per_core ='emu::model::num_threads_per_core'

    ## Search emu bios settings in emurun.dut_cfg
    bios_bin ='emu::bios::tools::bios_bin'
    commandTiming = 'emu::bios::knobs::commandTiming'
    XMPMode ='emu::bios::knobs::XMPMode = Manual'
    PpdEn ='emu::bios::knobs::PpdEn'
    RefreshMode = 'emu::bios::knobs::RefreshMode'
    HostDdrFreqLimit = 'emu::bios::knobs::HostDdrFreqLimit'
    DramRaplPwrLimitLockCsr= 'emu::bios::knobs::DramRaplPwrLimitLockCsr'
    DfxBankXorEn = 'emu::bios::knobs::DfxBankXorEn'
    ClockModulationEn = 'emu::bios::knobs::ClockModulationEn'
    CkeProgramming ='emu::bios::knobs::CkeProgramming'

    ## Search emu preloader settings in emurun.dut_cfg
    mc_mode = 'emu::preload::tools::preloader::mc_mode'
    preloader_path = 'emu::preload::tools::preloader::path'
    preloader_version = 'emu::preload::tools::preloader::version' #to fiz; None;path expeted

    ## Search  in ubios.asm
    ubios = "ubios.asm"
    C00_CMD_Timing = "N0.C00: CMD Timing"
    C01_CMD_Timing = "N0.C01: CMD Timing"
    XptPrefetchEn = " XptPrefetchEn"
    xptprefetchdisable = "xptprefetchdisable" # to fix; None; 0x0 expeted
    DfxD2cEn = "DfxD2cEn"
    ClockModulation = "ClockModulationEn"
    DfxBankXor = "DfxBankXorEn"
    QCLK_Ratio = "QCLK Ratio"
    clustering = "clustering mode"
    Paging_Policy ="Paging Policy"
    Rank_cnt = "dimmmtr_0.rank_cnt" # Based on MC0_channel_0
    Dnsty = "dimmmtr_0.dnsty"       # Based on MC0_channel_0
    Width = "dimmmtr_0.width"       # Based on MC0_channel_0

    ## Search  in testbench.log
    Frequency = "frequency"
    Freq_core = "freq core"
    Freq_uclk = "freq uclk"
    Freq_ddr = "freq ddr"

   ## Search in report.rpt

    

    extracted_values = extract_emu_model_settings(dut_cfg, real_cores, num_mcs, tlm_dut, num_chs_per_mcs, num_sockets, 
    num_threads_per_core, bios_bin, commandTiming, XMPMode, PpdEn, RefreshMode, HostDdrFreqLimit, DramRaplPwrLimitLockCsr, 
    DfxBankXorEn, ClockModulationEn, CkeProgramming, mc_mode, preloader_path, preloader_version)


    extracted_values.update(extract_ubios_settings(C00_CMD_Timing, C01_CMD_Timing, XptPrefetchEn, xptprefetchdisable, DfxD2cEn, 
    ClockModulation, DfxBankXor, QCLK_Ratio, clustering, Paging_Policy, Rank_cnt, Dnsty, Width))

    extracted_values.update(extract_testbench_settings(Frequency, Freq_core, Freq_uclk, Freq_ddr))
    
    
    extracted_knob_values = extract_knob_names()

    #extracted_switch_values = extract_fuses_settings()
    
    

    for key, value in extracted_knob_values.items():
        print(key, ":", value)

    for key, value in extracted_values.items():
        print(key, ":", value)
    
   
    outputName="Breakdown_Rem_L3_Lat_GNR.csv"
    

    with open(outputName,'w', newline='') as fileT:
            
        writer = csv.writer(fileT)
        csvHeader=[]
    
        writer.writerow(csvHeader)
        
        printD(outputName, extracted_values, extracted_knob_values)

                           
if __name__=="__main__":
    main()

