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
    { 'condor_dir' : 'MchampsGluinos2015_AcceptanceVsStoppingRegion',
      'dataset' : 'gluino2600_NtupleSeparateEvents',
      'channel' : 'NoCuts',
      'legend_entry' : 'Stop in Detector Only',
      'marker' : 'circle',
      'color' : 'black',
      #'fill' : 'hollow',
    },
    { 'condor_dir' : 'MchampsGluinos2015_AcceptanceVsStoppingRegion',
      'dataset' : 'gluino2600_NtupleSeparateEvents',
      'channel' : 'TriggerSelection',
      'legend_entry' : 'Trigger Applied',
      'marker' : 'square',
      'color' : 'red',
      #'fill' : 'hollow',
    },
    { 'condor_dir' : 'MchampsGluinos2015_AcceptanceVsStoppingRegion',
      'dataset' : 'gluino2600_NtupleSeparateEvents',
      'channel' : 'PreSelectionUpperLowerNoTrigger',
      'legend_entry' : 'Preselection Applied',
      'marker' : 'triangle',
      'color' : 'blue',
      #'fill' : 'hollow',
    },
    { 'condor_dir' : 'MchampsGluinos2015_AcceptanceVsStoppingRegion',
      'dataset' : 'gluino2600_NtupleSeparateEvents',
      'channel' : 'PreSelectionUpperLower',
      'legend_entry' : 'Trigger and Preselection Applied',
      'marker' : 'circle',
      'color' : 'green',
      #'fill' : 'hollow',
    },
    #{ 'condor_dir' : 'MchampsGluinos2015_AcceptanceVsStoppingRegion',
      #'dataset' : 'gluino2600_NtupleSeparateEvents',
      #'channel' : 'DelayedMuonsUpperLowerSelection',
      #'legend_entry' : 'Trigger and Full Selection Applied',
      #'marker' : 'square',
      #'color' : 'purple',
      #'fill' : 'hollow',
    #},
]

