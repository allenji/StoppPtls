#!/usr/bin/env python
intLumi = 19800

###################
# 'color' options #
###################
## 'black'
## 'red'  
## 'green'
## 'purple'
## 'blue'  
## 'yellow'
## default: cycle through list


####################
# 'marker' options #
####################
## 'circle'
## 'square'
## 'triangle'
## default: 'circle'

####################
#  'fill' options  #
####################
## 'solid'
## 'hollow'
## default: 'solid'


input_sources = [
    { 
        'condor_dir' : 'TriggerPurity2016_2016ReReco_mchamp600',
        #'dataset' : 'NoBPTX_2016BCDEFGH_23Sep2016_Ntuple',
        'dataset' : 'mchamp600_NtupleSeparateEvents_2016',
        'channel' : 'TriggerSelection',
        'legend_entry' : 'Pass L2Mu40',
        'marker' : 'circle',
        'color' : 'black',
        #'fill' : 'hollow',
        },
    { 
        'condor_dir' : 'TriggerPurity2016_2016ReReco_mchamp600',
        #'dataset' : 'NoBPTX_2016BCDEFGH_23Sep2016_Ntuple',
        'dataset' : 'mchamp600_NtupleSeparateEvents_2016',
        'channel' : 'TriggerPuritySelection',
        'legend_entry' : 'Pass L2Mu40 and Preselection',
        'marker' : 'square',
        'color' : 'red',
        #'fill' : 'hollow',
        },
]

